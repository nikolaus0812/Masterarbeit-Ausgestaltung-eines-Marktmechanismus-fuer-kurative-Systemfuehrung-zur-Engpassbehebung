"""Die draw.io-Abbildungen in Kapitel 2 auf die Typografie der Arbeit bringen.

AUSGANGSLAGE: Beide Abbildungen sind fuer den Bildschirm gezeichnet. Im
Dokument erscheinen ihre Beschriftungen mit 6,6 beziehungsweise 7,6 pt --
gegen 9,96 pt Bildunterschrift und 10,91 pt Fliesstext also deutlich zu
klein.

DIE RECHNUNG: Auf der Seite erscheint die Beschriftung mit

    Groesse = fontSize * 0,668 * (455,24 pt / Breite der exportierten PDF)

Die Breite muss also konstant bleiben, waehrend die Schrift waechst. Beides
zusammen bedeutet: die Beschriftung bricht in mehr Zeilen um, wofuer die
Kaesten hoeher werden muessen.

DIE GRENZE: Ein unteilbares Wort kann draw.io nicht umbrechen. Bei
fontSize 18 ist "Netzsicherheitrechnung" rund 190 px breit und laeuft aus
einem 130 px breiten Kasten heraus. Die Kaesten werden deshalb auf 150 px
verbreitert -- die Spaltenabstaende geben das her -- und in dem einen Wort,
das auch dann nicht passt, steht jetzt eine Trennung.

Die senkrechte Skalierung ist eine affine Abbildung y' = a*y auf Position
UND Hoehe. Das ist wesentlich: Kaesten, die mehrere Zeilen ueberspannen
(die Spurbezeichner und "Redispatch"), behalten so genau ihre Ausdehnung.
Skalierte man Positionen und Hoehen mit verschiedenen Faktoren, passten
diese Kaesten nicht mehr zu den Zeilen.

Aufruf:
    python tools/drawio_restyle.py

Danach steht in figures/chapter_2 je eine neue SVG und PDF.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import drawio_edit as de  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "figures" / "chapter_2"

# Je Abbildung, weil die Ausgangsgroessen verschieden sind: 12 im
# Prozessdiagramm, 14 im Belastungsdiagramm. Beide sollen bei rund 10 pt auf
# der Seite ankommen.
FONT = {"curative_process": 1.5,                      # 12 -> 18
        "preventiv_vs._curative_redispatch": 1.23}    # 14 -> 17,2
VSCALE = {"curative_process": 1.6,
          "preventiv_vs._curative_redispatch": 1.2}
BOX_FROM, BOX_TO = 130, 150   # Kaesten verbreitern, Spaltenraster bleibt

# Unteilbare Woerter, die auch im breiteren Kasten nicht passen.
BREAKS = {"Netzsicherheitrechnung": "Netzsicherheits-&#10;rechnung"}


def widen_boxes(xml: str) -> str:
    """Kaesten von BOX_FROM auf BOX_TO verbreitern, Mitte beibehalten."""
    shift = (BOX_TO - BOX_FROM) / 2

    def geo(m: re.Match) -> str:
        x, w = float(m.group(1)), float(m.group(2))
        if int(w) != BOX_FROM:
            return m.group(0)
        return m.group(0).replace(f'x="{m.group(1)}"', f'x="{x - shift:g}"') \
                         .replace(f'width="{m.group(2)}"', f'width="{BOX_TO}"')

    return re.sub(r'x="([-\d.]+)" y="[-\d.]+" width="([-\d.]+)"', geo, xml)


# Umbau der Legende im Belastungsdiagramm. Sie stand als Kasten oben rechts
# im Diagramm; sie gehoert unter das Diagramm. Angaben im Koordinatensystem
# der Quelle, also vor der senkrechten Streckung.
#
# Die Zeitachse liegt bei y = 220. Die Legende steht darunter auf einer
# Zeile: je ein Linienmuster links von seiner Beschriftung.
LEGEND = {
    # Rahmen
    'x="625" y="40" width="175" height="50"':
        'x="185" y="248" width="480" height="42"',
    # Beschriftung hell. Breite auf die groessere Schrift ausgelegt: fett
    # gesetzt braucht "kurative Belastung" bei fontSize 17,2 rund 175 px,
    # sonst bricht sie zweizeilig um.
    'x="625" y="32" width="150" height="40"':
        'x="230" y="248" width="180" height="42"',
    # Beschriftung dunkel, entsprechend rund 195 px
    'x="615" y="58" width="160" height="40"':
        'x="450" y="248" width="200" height="42"',
    # Linienmuster hell (Zelle xknEu-36) und dunkel (xknEu-37).
    # Das helle hat neben Anfang und Ende einen Stuetzpunkt. Bleibt der
    # stehen, laeuft die Linie von der neuen Position zum alten Ort und
    # wieder zurueck -- im Bild zwei lange Diagonalen quer durch das
    # Diagramm. Er muss mit auf die Mitte des Musters.
    '<mxPoint x="787" y="51.63" />': '<mxPoint x="212" y="269" />',
    '<mxPoint x="797" y="51.63" as="sourcePoint" />':
        '<mxPoint x="200" y="269" as="sourcePoint" />',
    '<mxPoint x="777" y="51.63" as="targetPoint" />':
        '<mxPoint x="224" y="269" as="targetPoint" />',
    '<mxPoint x="777" y="78" as="sourcePoint" />':
        '<mxPoint x="420" y="269" as="sourcePoint" />',
    '<mxPoint x="797" y="78" as="targetPoint" />':
        '<mxPoint x="444" y="269" as="targetPoint" />',
    # Achsenbeschriftung "Belastung in A": im Original 60 px breit und damit
    # schon vor der Vergroesserung zu schmal, sie stiess an die Hochachse.
    'x="50" y="35" width="60" height="40"':
        'x="8" y="28" width="104" height="48"',
}


def move_legend(xml: str) -> str:
    for old, new in LEGEND.items():
        if old not in xml:
            raise ValueError(f"Legendenteil nicht gefunden: {old[:60]}")
        xml = xml.replace(old, new, 1)
    return xml


def restyle(name: str, *, widen: bool = False, legend: bool = False) -> None:
    svg = FIG / f"{name}.svg"
    xml = de.read_mxfile(svg)
    if widen:
        xml = widen_boxes(xml)
    if legend:
        xml = move_legend(xml)
    for old, new in BREAKS.items():
        xml = xml.replace(f'value="{old}"', f'value="{new}"')
    xml = de.scale_geometry(xml, fx=1.0, fy=VSCALE[name], font=FONT[name])
    print(f"  {name}")
    de.write_and_export(svg, xml)


def main() -> int:
    restyle("curative_process", widen=True)
    restyle("preventiv_vs._curative_redispatch", legend=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
