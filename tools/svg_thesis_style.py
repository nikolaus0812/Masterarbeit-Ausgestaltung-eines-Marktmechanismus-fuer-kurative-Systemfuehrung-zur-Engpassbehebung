"""SVG-Abbildungen fuer die Arbeit aufbereiten: Schriftfamilie und Normalisierung.

Zwei Eingriffe, beide rein textuell, ohne Einfluss auf das Layout:

  Schriftfamilie   Arial -> Helvetica, passend zu \\usepackage{helvet} in
                   extras/header.tex. Beide sind metrisch gleich; reportlab
                   bildet Helvetica auf die PDF-Standardschrift ab,
                   pdflatex bettet NimbusSans ein. Optisch identisch.

  Normalisierung   matplotlib schreibt Schriftangaben je nach Version in
                   zwei Formen:
                       alt:  style="font-size: 14px; font-family: 'Arial', ..."
                       neu:  style="font: 14px 'Arial', ..."   (CSS-Kurzform)
                   svglib wertet den Groessenanteil der Kurzform nicht aus
                   und setzt statt dessen eine Vorgabegroesse, sodass alle
                   Beschriftungen gleich gross herauskommen. Dieses Skript
                   ueberfuehrt die Kurzform daher in die Langform.

DIE SCHRIFTGROESSEN WERDEN HIER NICHT MEHR ANGEFASST. Sie werden in
tools/replot_figures.py bereits bei der Erzeugung gesetzt, weil matplotlib
das Layout -- Achsenraender, Legendenspalten, Umbrueche -- anhand der
Schriftgroesse berechnet. Wurden die Groessen nachtraeglich hier geaendert,
blieb das Layout auf den alten Werten stehen: abgeschnittene
Achsenbeschriftungen, ueberlappende Legendeneintraege.

Die Datei wird in place geaendert und mit einer Marke versehen; ein
zweiter Lauf laesst sie unangetastet.

Aufruf:
    python tools/svg_thesis_style.py                     # alles unter figures/
    python tools/svg_thesis_style.py figures/chapter_1   # ein Verzeichnis

Danach tools/svg2pdf.py laufen lassen, das die PDF neu erzeugt.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MARKER = "<!-- thesis-style: Schriftfamilie gesetzt, Schriftangaben normalisiert -->"

FONT_FAMILY = "'Helvetica', 'Nimbus Sans', 'Arial', sans-serif"


def restyle(svg: Path) -> bool:
    s = svg.read_text(encoding="utf-8")
    if MARKER in s:
        print(f"  bereits aufbereitet  {svg.relative_to(ROOT)}")
        return False

    # Reihenfolge ist wesentlich: erst die vorhandene Langform behandeln, dann
    # die Kurzform aufloesen. Andernfalls trifft der Langform-Ausdruck genau
    # das, was gerade aus der Kurzform geschrieben wurde.
    s, n_fam = re.subn(r"font-family: ?[^;\"]+", f"font-family: {FONT_FAMILY}", s)
    n_long = len(re.findall(r"font-size: ?[0-9.]+px", s))
    s, n_short = re.subn(
        r"font: ?([0-9.]+)px [^;\"]+",
        lambda mo: f"font-size: {mo.group(1)}px; font-family: {FONT_FAMILY}", s)

    if not (n_short or n_long):
        print(f"  FEHLER  {svg.relative_to(ROOT)} -- keine Schriftangabe gefunden.")
        print("          Weder 'font-size:' noch die CSS-Kurzform 'font:'. Die")
        print("          Datei bleibt unveraendert und wird NICHT markiert.")
        return False

    s = s.replace("</svg>", MARKER + "\n</svg>")
    svg.write_text(s, encoding="utf-8", newline="\n")

    print(f"  aufbereitet  {svg.relative_to(ROOT)}")
    print(f"     {n_long} Angaben in Langform, {n_short} Kurzformen aufgeloest, "
          f"{n_fam + n_short} Schriftfamilien gesetzt")
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
    return found


def main() -> int:
    svgs = collect(sys.argv[1:])
    if not svgs:
        print("Keine SVG-Dateien gefunden.")
        return 1
    changed = sum(restyle(s) for s in svgs)
    print(f"\n{changed} von {len(svgs)} Dateien aufbereitet.")
    if changed:
        print("Jetzt: python tools/svg2pdf.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
