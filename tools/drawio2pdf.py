"""draw.io-Abbildungen nach PDF exportieren.

Die Abbildungen in figures/chapter_2 sind mit draw.io gezeichnet. Ihre SVG
sind "editierbare SVG": im Attribut content des svg-Elements steckt die
vollstaendige Diagrammquelle als mxfile-XML. draw.io kann eine solche SVG
direkt wieder oeffnen und exportieren.

WARUM NICHT tools/svg2pdf.py: Der Text dieser SVG liegt in
foreignObject-Elementen, also in eingebettetem HTML. svglib kennt die
nicht. Es rendert statt dessen den Ersatztext, den draw.io fuer diesen Fall
hinterlegt -- teils abgeschnitten ("Abruf = Anpassung Lei..."), teils gar
nicht vorhanden, dazu die eingebrannte Meldung "Text is not SVG - cannot
display". Ausserdem gehen Farben verloren. Der Export ueber draw.io selbst
ist dem in jeder Hinsicht ueberlegen und mit dem urspruenglich vom Autor
exportierten PDF deckungsgleich.

Voraussetzung: draw.io Desktop. Der Pfad laesst sich ueber die
Umgebungsvariable DRAWIO setzen.

Aufruf:
    python tools/drawio2pdf.py                     # alle draw.io-SVG
    python tools/drawio2pdf.py figures/chapter_2   # nur ein Verzeichnis

Aenderungen am Text der Abbildung, etwa eine Umbenennung, lassen sich
direkt in der SVG vornehmen -- sowohl im mxfile-XML als auch im
gerenderten Teil -- und danach mit diesem Skript neu exportieren.
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAWIO = Path(os.environ.get("DRAWIO", r"C:\Program Files\draw.io\draw.io.exe"))


def is_drawio(svg: Path) -> bool:
    """Traegt die SVG eine eingebettete draw.io-Quelle?"""
    return "&lt;mxfile" in svg.read_text(encoding="utf-8", errors="ignore")[:4096]


def export(svg: Path) -> bool:
    pdf = svg.with_suffix(".pdf")
    if pdf.exists() and pdf.stat().st_mtime >= svg.stat().st_mtime:
        print(f"  aktuell   {svg.relative_to(ROOT)}")
        return False
    res = subprocess.run(
        [str(DRAWIO), "--export", "--format", "pdf", "--crop",
         "--output", str(pdf), str(svg)],
        capture_output=True, text=True, timeout=300)
    if res.returncode != 0 or not pdf.exists():
        print(f"  FEHLER    {svg.relative_to(ROOT)}")
        print("     " + (res.stderr or res.stdout).strip()[:400])
        return False
    print(f"  erzeugt   {pdf.relative_to(ROOT)}")
    return True


def collect(targets: list[str]) -> list[Path]:
    roots = [Path(t) if Path(t).is_absolute() else ROOT / t
             for t in targets] or [ROOT / "figures"]
    found: list[Path] = []
    for p in roots:
        if p.is_dir():
            found.extend(sorted(p.rglob("*.svg")))
        elif p.suffix.lower() == ".svg":
            found.append(p)
    return [f for f in found if is_drawio(f)]


def main() -> int:
    if not DRAWIO.exists():
        print(f"draw.io nicht gefunden: {DRAWIO}")
        print("Pfad ueber die Umgebungsvariable DRAWIO setzen.")
        return 1
    svgs = collect(sys.argv[1:])
    if not svgs:
        print("Keine draw.io-SVG gefunden.")
        return 1
    written = sum(export(s) for s in svgs)
    print(f"\n{written} von {len(svgs)} Dateien exportiert.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
