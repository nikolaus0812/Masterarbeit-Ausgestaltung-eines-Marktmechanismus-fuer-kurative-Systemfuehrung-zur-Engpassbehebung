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


def convert(svg: Path) -> bool:
    """Konvertiert eine SVG-Datei. Gibt True zurueck, wenn geschrieben wurde."""
    pdf = svg.with_suffix(".pdf")
    if pdf.exists() and pdf.stat().st_mtime >= svg.stat().st_mtime:
        print(f"  aktuell   {svg.relative_to(ROOT)}")
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
