"""SVG-Abbildungen auf die Typografie der Arbeit umstellen.

Die Diagramme entstehen in bess_dispatch_optimization mit
analysen/helpers/praesentation_plots.py. Dieses Skript ist auf Folien
ausgelegt: Arial, Grundschriftgroesse 14, fast quadratisches Format. In der
Arbeit steht daneben 11 pt Fliesstext, die Bildunterschrift ist \\small
(10 pt). Uebernimmt man die Folienfassung unveraendert, sind die
Achsenbeschriftungen groesser als der Fliesstext.

Dieses Skript setzt die SVG deshalb um:

  Schriftfamilie   Arial -> Helvetica, passend zu \\usepackage{helvet}.
                   Beide sind metrisch gleich; reportlab bildet Helvetica
                   auf die PDF-Standardschrift ab, pdflatex bettet
                   NimbusSans ein. Optisch identisch.

  Schriftgroesse   auf die Zielgroessen unten, gemessen in pt auf der
                   fertigen Seite. Die Geometrie bleibt unberuehrt, es
                   entsteht also etwas mehr Weissraum um die Beschriftung.

  Vorkompensation  Die Abbildungen werden mit width=\\textwidth eingebunden.
                   Ist die SVG nicht exakt \\textwidth breit, skaliert
                   LaTeX sie und damit auch die Schrift. Das Skript rechnet
                   diesen Faktor heraus, sodass die Zielgroessen auf der
                   Seite exakt erreicht werden.

Die Datei wird in place geaendert und mit einer Marke versehen; ein
zweiter Lauf laesst sie unangetastet. Die unveraenderten Originale liegen
weiterhin in bess_dispatch_optimization.

Aufruf:
    python tools/svg_thesis_style.py                     # alles unter figures/
    python tools/svg_thesis_style.py figures/chapter_1   # ein Verzeichnis

Danach tools/svg2pdf.py laufen lassen, das die PDF neu erzeugt.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# \textwidth des Dokuments in pt, abgelesen aus main.log:
#   "Requested size: 455.24411pt" fuer \includegraphics[width=1.0\textwidth]
# Ergibt sich aus a4paper mit 2,5 cm Rand links und rechts.
TEXTWIDTH_PT = 455.24411

# svglib rechnet font-size aus px nach pt mit dem CSS-Faktor 96 dpi zu 72 dpi
# um, die Geometrie dagegen 1:1. Ohne diesen Faktor landet die Schrift um ein
# Viertel zu klein auf der Seite. Empirisch geprueft: font-size 9.93px
# erscheint im erzeugten PDF als 7.45pt, das ist genau 0,75.
PX_TO_PT = 0.75

MARKER = "<!-- thesis-style: Schriftgroessen und Schriftfamilie angepasst -->"

FONT_FAMILY = "'Helvetica', 'Nimbus Sans', 'Arial', sans-serif"

# Quellgroesse in px (Folienfassung) -> Zielgroesse in pt auf der Seite.
# Bezug: Fliesstext 11 pt, Bildunterschrift 10 pt. Abbildungsbeschriftung
# soll die Bildunterschrift nicht ueberragen.
SIZE_MAP = {
    16.0: 10.0,  # Titel im Bild
    14.0: 9.0,   # Achsenticks, Achsenbeschriftung, Legende
    11.0: 8.0,   # Datenbeschriftung an den Balken
    10.0: 7.5,   # nachgeordnete Beschriftung
    9.0: 7.0,    # Quellenzeile
    8.0: 7.0,    # Fussnote unter der Grafik
}


def target_size(px: float, scale: float) -> float:
    """Zielgroesse in SVG-Einheiten, vorkompensiert um den LaTeX-Skalierfaktor."""
    if px in SIZE_MAP:
        pt = SIZE_MAP[px]
    else:
        # Nicht kartierte Groessen proportional zur naechstgelegenen abbilden.
        nearest = min(SIZE_MAP, key=lambda k: abs(k - px))
        pt = SIZE_MAP[nearest] * px / nearest
    return round(pt / (scale * PX_TO_PT), 3)


def restyle(svg: Path) -> bool:
    s = svg.read_text(encoding="utf-8")
    if MARKER in s:
        print(f"  bereits angepasst  {svg.relative_to(ROOT)}")
        return False

    m = re.search(r'<svg[^>]*\swidth="([0-9.]+)pt"', s)
    if not m:
        print(f"  FEHLER  {svg.relative_to(ROOT)} -- Breite nicht lesbar")
        return False
    width_pt = float(m.group(1))
    scale = TEXTWIDTH_PT / width_pt

    seen: dict[float, float] = {}

    def repl(mo: re.Match) -> str:
        px = float(mo.group(1))
        new = target_size(px, scale)
        seen[px] = new
        return f"font-size: {new}px"

    s, n_size = re.subn(r"font-size: ?([0-9.]+)px", repl, s)
    s, n_fam = re.subn(r"font-family: ?[^;\"]+", f"font-family: {FONT_FAMILY}", s)
    s = s.replace("</svg>", MARKER + "\n</svg>")
    svg.write_text(s, encoding="utf-8", newline="\n")

    print(f"  angepasst  {svg.relative_to(ROOT)}")
    print(f"     Breite {width_pt:.1f}pt, Skalierung auf \\textwidth {scale:.4f}")
    print(f"     {n_size} Schriftgroessen, {n_fam} Schriftfamilien")
    for px in sorted(seen, reverse=True):
        print(f"     {px:>5.1f}px -> {seen[px]:>5.2f}px "
              f"(= {seen[px] * scale * PX_TO_PT:.1f}pt auf der Seite)")
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
    print(f"\n{changed} von {len(svgs)} Dateien angepasst.")
    if changed:
        print("Jetzt: python tools/svg2pdf.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
