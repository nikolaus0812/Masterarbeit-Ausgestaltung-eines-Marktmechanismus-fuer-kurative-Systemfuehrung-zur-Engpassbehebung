"""SVG-Abbildungen nach PDF konvertieren.

Hintergrund: pdflatex kann SVG nicht direkt einbinden. Die Diagramme dieser
Arbeit entstehen als SVG im Repository bess_dispatch_optimization; dieses
Skript erzeugt daraus die PDF-Dateien, die \\includegraphics laedt.

Warum svglib und nicht cairosvg oder Inkscape: svglib und reportlab sind
reine Python-Pakete ohne native Abhaengigkeiten und lassen sich unter
Windows ohne GTK- oder Cairo-Installation einrichten.

Einrichtung (einmalig):
    python -m pip install svglib reportlab

Aufruf:
    python tools/svg2pdf.py                     # alle SVG unter figures/
    python tools/svg2pdf.py figures/chapter_1   # nur ein Verzeichnis
    python tools/svg2pdf.py pfad/zur/datei.svg  # nur eine Datei

Bestehende PDF werden nur neu erzeugt, wenn das SVG neuer ist.
Die Beschriftungen bleiben echter Text, nicht in Pfade umgewandelt --
geprueft an redispatch_jahresbedarf_2020_2025 und engpassmanagement_nep.
"""

import sys
from pathlib import Path

from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg

ROOT = Path(__file__).resolve().parent.parent


def is_drawio(svg: Path) -> bool:
    """draw.io-SVG erkennen und diesem Skript entziehen.

    Ihr Text steckt in foreignObject-Elementen, die svglib nicht kennt. Das
    Ergebnis waere eine PDF mit abgeschnittenen oder fehlenden
    Beschriftungen. Diese Dateien gehoeren zu tools/drawio2pdf.py.
    """
    return "&lt;mxfile" in svg.read_text(encoding="utf-8", errors="ignore")[:4096]


def made_here(pdf: Path) -> bool:
    """Stammt diese PDF aus diesem Skript?

    Hintergrund: Nicht jede SVG im Repository soll ueber svglib laufen. Die
    Abbildungen in figures/chapter_2 sind draw.io-Exporte; deren Text steckt
    in foreignObject-Elementen, die svglib nicht kennt. Konvertiert man sie
    trotzdem, entsteht eine PDF mit abgeschnittenen Beschriftungen und der
    eingebrannten Meldung "Text is not SVG - cannot display". Genau das ist
    einmal passiert und hat die vom Autor exportierten PDF ueberschrieben.

    Deshalb wird nur ueberschrieben, was reportlab selbst erzeugt hat. Das
    steht im Feld /Producer der PDF.
    """
    try:
        head = pdf.read_bytes()[:4096]
    except OSError:
        return False
    return b"ReportLab" in head


def convert(svg: Path) -> bool:
    """Konvertiert eine SVG-Datei. Gibt True zurueck, wenn geschrieben wurde."""
    pdf = svg.with_suffix(".pdf")
    if is_drawio(svg):
        print(f"  draw.io   {svg.relative_to(ROOT)} -- fuer tools/drawio2pdf.py")
        return False
    if pdf.exists() and pdf.stat().st_mtime >= svg.stat().st_mtime:
        print(f"  aktuell   {svg.relative_to(ROOT)}")
        return False
    if pdf.exists() and not made_here(pdf):
        print(f"  UEBERSPRUNGEN  {pdf.relative_to(ROOT)}")
        print("      Diese PDF stammt nicht aus diesem Skript und wird nicht")
        print("      ueberschrieben. Sie wurde vermutlich direkt aus einem")
        print("      Zeichenprogramm exportiert und ist dann besser als alles,")
        print("      was svglib aus der SVG machen kann. Zum Ersetzen die PDF")
        print("      von Hand loeschen.")
        return False
    drawing = svg2rlg(str(svg))
    if drawing is None:
        print(f"  FEHLER    {svg.relative_to(ROOT)} -- nicht lesbar")
        return False
    renderPDF.drawToFile(drawing, str(pdf))
    print(f"  erzeugt   {pdf.relative_to(ROOT)}  "
          f"({drawing.width:.0f} x {drawing.height:.0f} pt)")
    return True


def collect(targets: list[str]) -> list[Path]:
    if not targets:
        return sorted((ROOT / "figures").rglob("*.svg"))
    found: list[Path] = []
    for t in targets:
        p = Path(t)
        if not p.is_absolute():
            p = ROOT / p
        if p.is_dir():
            found.extend(sorted(p.rglob("*.svg")))
        elif p.suffix.lower() == ".svg":
            found.append(p)
        else:
            print(f"  uebersprungen: {t}")
    return found


def main() -> int:
    svgs = collect(sys.argv[1:])
    if not svgs:
        print("Keine SVG-Dateien gefunden.")
        return 1
    written = sum(convert(s) for s in svgs)
    print(f"\n{written} von {len(svgs)} Dateien neu erzeugt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
