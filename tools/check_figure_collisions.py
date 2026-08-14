"""Beruehrungen zwischen Beschriftung und Linien in den Abbildungen finden.

Sucht in den erzeugten PDF nach Stellen, an denen ein Textkasten einer
gezeichneten Linie zu nahe kommt. Gepruefte Abstaende sind die auf der
fertigen Seite, also nach der Verkleinerung auf \\textwidth.

Rechtecke werden uebersprungen: Beschriftung IN einem Kasten ist gewollt,
und ein Rechteck laesst sich ueber seinen Umriss nicht sinnvoll gegen den
Text darin pruefen. Geprueft werden Linien und Kurven.

Aufruf:
    python tools/check_figure_collisions.py [minimaler Abstand in pt]
"""

import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
TEXTWIDTH_PT = 455.24411
DEFAULT_MIN = 1.5


def segments(page) -> list[tuple[float, float, float, float]]:
    """Alle gezeichneten Strecken, Rechtecke ausgenommen."""
    out = []
    for d in page.get_drawings():
        for item in d["items"]:
            if item[0] == "l":
                p, q = item[1], item[2]
                out.append((p.x, p.y, q.x, q.y))
            elif item[0] == "c":
                p, q = item[1], item[4]
                out.append((p.x, p.y, q.x, q.y))
    return out


def dist_box_seg(box, seg) -> float:
    """Kleinster Abstand zwischen Rechteck und Strecke, 0 bei Schnitt."""
    x0, y0, x1, y1 = box
    ax, ay, bx, by = seg

    def dist_point_seg(px, py, ax, ay, bx, by):
        dx, dy = bx - ax, by - ay
        if dx == dy == 0:
            return ((px - ax) ** 2 + (py - ay) ** 2) ** 0.5
        t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
        return ((px - (ax + t * dx)) ** 2 + (py - (ay + t * dy)) ** 2) ** 0.5

    # Liegt ein Endpunkt im Kasten oder schneidet die Strecke ihn, ist der
    # Abstand null. Sonst der kleinste Abstand der vier Kanten.
    if x0 <= ax <= x1 and y0 <= ay <= y1:
        return 0.0
    if x0 <= bx <= x1 and y0 <= by <= y1:
        return 0.0
    corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    d = min(dist_point_seg(cx, cy, ax, ay, bx, by) for cx, cy in corners)
    for px, py in ((ax, ay), (bx, by)):
        cx = min(max(px, x0), x1)
        cy = min(max(py, y0), y1)
        d = min(d, ((px - cx) ** 2 + (py - cy) ** 2) ** 0.5)
    return d


def covers(page) -> list:
    """Deckende Flaechen, etwa Balken eines Diagramms.

    Liegt eine Beschriftung darin, verdeckt die Flaeche jede Linie
    dahinter. Eine gemessene Naehe zu einer Gitterlinie ist dann keine
    sichtbare Beruehrung.
    """
    page_area = page.rect.width * page.rect.height
    out = []
    for d in page.get_drawings():
        if d["type"] not in ("f", "fs") or d["fill"] is None:
            continue
        r = d["rect"]
        if d["fill"] == (1.0, 1.0, 1.0):
            # Weiss ist zugleich die Seitenfarbe. Eine grossflaechige weisse
            # Flaeche ist der Hintergrund und verdeckt nichts; eine kleine ist
            # der Hinterlegungskasten einer Beschriftung und verdeckt sehr
            # wohl. Die Grenze liegt bei einem Achtel der Bildflaeche.
            if r.width * r.height > page_area / 8:
                continue
        out.append(r)
    return out


def check(pdf: Path, min_pt: float) -> int:
    doc = pymupdf.open(pdf)
    page = doc[0]
    scale = TEXTWIDTH_PT / page.rect.width
    segs = segments(page)
    filled = covers(page)
    hits = []
    for b in page.get_text("dict")["blocks"]:
        for line in b.get("lines", []):
            for sp in line["spans"]:
                txt = sp["text"].strip()
                if not txt:
                    continue
                box = sp["bbox"]
                # Mitte des Textes statt vollstaendiger Einschluss: die
                # Hinterlegungskaesten von draw.io sind etwas schmaler als
                # ihr Text, decken die Linie darunter aber vollstaendig ab.
                cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
                if any(r.x0 <= cx <= r.x1 and r.y0 <= cy <= r.y1 for r in filled):
                    continue
                d = min((dist_box_seg(box, s) for s in segs), default=99)
                if d * scale < min_pt:
                    hits.append((d * scale, txt))
    doc.close()
    print(f"  {pdf.name}: {len(segs)} Strecken, {len(hits)} Beruehrungen "
          f"unter {min_pt} pt")
    for d, t in sorted(hits)[:12]:
        print(f"     {d:5.2f} pt  {t[:46]!r}")
    return len(hits)


def main() -> int:
    min_pt = float(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MIN
    total = sum(check(p, min_pt)
                for p in sorted((ROOT / "figures").rglob("*.pdf")))
    print(f"\n{total} Beruehrungen insgesamt.")
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main())
