"""Die draw.io-Abbildungen in Kapitel 2 auf die Typografie der Arbeit bringen.

Ziel ist ein einheitliches Bild ueber alle vier Abbildungen der Arbeit. Die
beiden Diagramme in Kapitel 1 entstehen aus matplotlib und kommen im
fertigen main.pdf mit 9,95 pt Beschriftung und 13,93 pt Titel an. Genau
darauf werden diese beiden hier eingestellt.

DIE RECHNUNG: Auf der Seite erscheint die Beschriftung mit

    Groesse = fontSize * 0,668 * (455,24 pt / Breite der exportierten PDF)

Die Breite muss also konstant bleiben, waehrend die Schrift waechst. Beides
zusammen bedeutet: die Beschriftung bricht in mehr Zeilen um, wofuer die
Kaesten hoeher werden muessen.

Die senkrechte Skalierung ist eine affine Abbildung y' = a*y auf Position
UND Hoehe. Das ist wesentlich: Kaesten, die mehrere Zeilen ueberspannen
(die Spurbezeichner und "Redispatch"), behalten so genau ihre Ausdehnung.

DIE GRENZE: Ein unteilbares Wort kann draw.io nicht umbrechen. Bei
fontSize 17 ist "Netzsicherheitrechnung" breiter als sein Kasten. Die
Kaesten werden deshalb verbreitert -- die Spaltenabstaende geben das her --
und in dem einen Wort, das auch dann nicht passt, steht eine Trennung.

ZUR SCHRIFTART: Die Quelle setzt durchgehend TeX Gyre Heros. Eine Schrift
namens Helvetica gibt es auf diesem Rechner nicht, draw.io ersetzte sie
beim Export durch Arial. TeX Gyre Heros stammt aus der TeX-Live-
Installation und geht wie das NimbusSans des Fliesstextes auf die URW
Nimbus Sans zurueck; es ist damit dieselbe Schrift, die usepackage helvet
setzt. Installiert ist sie fuer das Benutzerkonto unter
LOCALAPPDATA/Microsoft/Windows/Fonts, eingetragen in der Registrierung
unter HKCU Software/Microsoft/Windows NT/CurrentVersion/Fonts. Fehlt sie,
faellt draw.io wieder auf Arial zurueck: metrisch gleich, im Schriftbild
aber anders.

Aufruf:
    python tools/drawio_restyle.py
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import drawio_edit as de  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "figures" / "chapter_2"

# Zielgroessen auf der Seite, abgeglichen mit den Kapitel-1-Abbildungen.
PT_TEXT, PT_TITLE = 9.95, 13.93

# pt je fontSize-Einheit, aus dem fertigen main.pdf zurueckgerechnet.
# Unterschiedlich, weil die Abbildungen verschieden breit sind und damit
# verschieden stark auf \textwidth verkleinert werden.
PT_PER_UNIT = {"curative_process": 10.70 / 18,
               "preventiv_vs._curative_redispatch": 9.69 / 17.2}
BASE_FONT = {"curative_process": 12, "preventiv_vs._curative_redispatch": 14}
VSCALE = {"curative_process": 1.85, "preventiv_vs._curative_redispatch": 1.2}

TITLE = {
    "curative_process": ("Prozesskette einer kurativen Maßnahme", 50, 780, -12),
    "preventiv_vs._curative_redispatch":
        ("Betriebsmittelbelastung im Fehlerfall", 8, 800, 0),
}

SANS = "TeX Gyre Heros"

BOX_FROM, BOX_TO = 130, 150
BREAKS = {
    "Netzsicherheitrechnung": "Netzsicherheits-&#10;rechnung",
    # Zweizeilig umbrochen reichte die Zeile bis an den Kastenrand.
    "Abruf = Anpassung Leistungspunkt": "Abruf =&#10;Anpassung&#10;Leistungspunkt",
}

# Die beiden Achsenbeschriftungen standen zweizeilig. Einzeilig gelesen sind
# sie ruhiger; der Platz ist da, sobald die Kaesten breit genug sind.
ONELINE = {
    'value="Zeit&#xa; in h"': 'value="Zeit in h"',
    'value="Belastung &#xa;in A"': 'value="Belastung in A"',
}


def font_factor(name: str) -> float:
    return PT_TEXT / PT_PER_UNIT[name] / BASE_FONT[name]


def normalize_fonts(xml: str) -> str:
    """Eine Schriftart, keine Auszeichnung.

    Die Quellen mischten Helvetica und Arial und setzten acht Beschriftungen
    fett oder kursiv. In einer technischen Abbildung traegt das keine
    Bedeutung und macht das Bild unruhig.
    """
    xml = re.sub(r"fontFamily=(Arial|Helvetica)", f"fontFamily={SANS}", xml)
    xml = re.sub(r"fontStyle=\d+", "fontStyle=0", xml)
    # Fett und kursiv stehen teils nicht in der Formatangabe, sondern als
    # HTML im Text selbst -- und dort doppelt maskiert, weil das mxfile-XML
    # seinerseits im Attribut content der SVG steckt. Beide Schreibweisen
    # muessen weg. <div> und <br> bleiben, sie tragen Zeilenumbrueche.
    xml = re.sub(r"</?[bi]>", "", xml)
    xml = re.sub(r"&lt;/?[bi]&gt;", "", xml)
    # Formatangaben ohne fontFamily bekommen sie ergaenzt.
    def add(m: re.Match) -> str:
        s = m.group(1)
        if "fontFamily=" in s or not s.strip():
            return m.group(0)
        return f'style="{s.rstrip(";")};fontFamily={SANS};"'
    return re.sub(r'style="([^"]*)"', add, xml)


def widen_boxes(xml: str) -> str:
    """Kaesten von BOX_FROM auf BOX_TO verbreitern, Mitte beibehalten."""
    shift = (BOX_TO - BOX_FROM) / 2

    def geo(m: re.Match) -> str:
        x, w = float(m.group(1)), float(m.group(2))
        if int(w) != BOX_FROM:
            return m.group(0)
        return (m.group(0).replace(f'x="{m.group(1)}"', f'x="{x - shift:g}"')
                          .replace(f'width="{m.group(2)}"', f'width="{BOX_TO}"'))

    return re.sub(r'x="([-\d.]+)" y="[-\d.]+" width="([-\d.]+)"', geo, xml)


# Umbau im Belastungsdiagramm, Angaben im Koordinatensystem der Quelle.
# Die Zeitachse liegt bei y = 220.
LEGEND = {
    # Rahmen um die Legende entfernen: der Kasten bleibt als Zelle stehen,
    # zeichnet aber weder Flaeche noch Linie.
    'x="625" y="40" width="175" height="50"':
        'x="185" y="248" width="480" height="42"',
    'x="625" y="32" width="150" height="40"':
        'x="230" y="248" width="180" height="42"',
    'x="615" y="58" width="160" height="40"':
        'x="450" y="248" width="200" height="42"',
    # Linienmuster. Das helle hat neben Anfang und Ende einen Stuetzpunkt.
    # Bleibt der stehen, laeuft die Linie von der neuen Position zum alten
    # Ort und zurueck -- im Bild zwei Diagonalen quer durch das Diagramm.
    '<mxPoint x="787" y="51.63" />': '<mxPoint x="212" y="269" />',
    '<mxPoint x="797" y="51.63" as="sourcePoint" />':
        '<mxPoint x="200" y="269" as="sourcePoint" />',
    '<mxPoint x="777" y="51.63" as="targetPoint" />':
        '<mxPoint x="224" y="269" as="targetPoint" />',
    '<mxPoint x="777" y="78" as="sourcePoint" />':
        '<mxPoint x="420" y="269" as="sourcePoint" />',
    '<mxPoint x="797" y="78" as="targetPoint" />':
        '<mxPoint x="444" y="269" as="targetPoint" />',
    # TATL und PATL standen bei x = 70 bis 130 und ragten damit ueber die
    # Hochachse bei x = 120. Jetzt enden sie deutlich davor.
    'x="70" y="80" width="60" height="40"': 'x="18" y="80" width="84" height="40"',
    'x="70" y="120" width="60" height="40"': 'x="18" y="120" width="84" height="40"',
    # "Zeit in h" einzeilig: der Kasten war mit 60 px zu schmal dafuer und
    # sass zudem direkt am Pfeilende der Zeitachse.
    'x="750" y="220" width="60" height="40"':
        'x="690" y="232" width="120" height="30"',
    # "Rückführung N-1" sass bei x = 570 bis 680 und wurde von der
    # Ereignislinie bei x = 610 durchschnitten. Jetzt rechts davon.
    'x="570" y="180" width="110" height="30"':
        'x="628" y="178" width="140" height="30"',
    # "Kurative Reaktionszeit": der Kasten war mit 20 Einheiten nur eine
    # Zeile hoch, die Beschriftung bricht aber zweizeilig um und ragte oben
    # und unten heraus. Der weiss hinterlegte Kasten deckte die Ereignismarke
    # deshalb nur in der Mitte ab, und die Marke lief durch "Kurative"
    # hindurch. Jetzt so hoch wie der Text, Mitte bei y = 180 unveraendert.
    'x="350" y="170" width="150" height="20"':
        'x="349" y="157" width="152" height="46"',
}

# Die senkrechten Ereignislinien liefen bis y = 40 hinauf und schnitten
# dort durch die Beschriftungen, die sie erklaeren. Sie enden jetzt
# unterhalb davon; die Beschriftung steht frei darueber.
# Die Marken bei x = 290 und die gestrichelte TATL-Linie sind in draw.io an
# ihre Beschriftungen angebunden: die Linie endet an der Zelle, die
# Beschriftung unterbricht sie also. Diese Zellen duerfen weder verschoben
# noch ihre Endpunkte veraendert werden -- die Linie folgt sonst mit und
# laeuft quer durch das Bild. Nur die freien Marken werden gekuerzt.
MARKER_TOPS = [
    ('<mxPoint x="440" y="40" as="targetPoint" />',
     '<mxPoint x="440" y="102" as="targetPoint" />'),
    ('<mxPoint x="560" y="40" as="targetPoint" />',
     '<mxPoint x="560" y="124" as="targetPoint" />'),
    ('<mxPoint x="610" y="40" as="targetPoint" />',
     '<mxPoint x="610" y="124" as="targetPoint" />'),
]

# Die Achsenbeschriftung der Hochachse steht hochkant.
YLABEL_OLD = 'x="50" y="35" width="60" height="40"'
YLABEL_NEW = 'x="-88" y="116" width="180" height="28"'


def edit_belastung(xml: str) -> str:
    # "Kurative Reaktionszeit" ist die Beschriftung eines Massbandes und muss
    # zwischen seinen Pfeilen stehen. Dort kreuzt sie zwangslaeufig die
    # Ereignislinie. Ein weiss hinterlegter Kasten unterbricht die Linie --
    # so wird eine Masslinie ueblicherweise beschriftet.
    xml = xml.replace(
        'value="Kurative Reaktionszeit" style="text;whiteSpace=wrap;'
        'strokeColor=none;fillColor=default;',
        'value="Kurative Reaktionszeit" style="text;whiteSpace=wrap;'
        'strokeColor=none;fillColor=#FFFFFF;', 1)
    for old, new in MARKER_TOPS:
        xml = xml.replace(old, new)
    for old, new in ONELINE.items():
        if old not in xml:
            raise ValueError(f"Nicht gefunden: {old[:60]}")
        xml = xml.replace(old, new, 1)
    for old, new in LEGEND.items():
        if old not in xml:
            raise ValueError(f"Nicht gefunden: {old[:60]}")
        xml = xml.replace(old, new, 1)
    # Rahmenzelle unsichtbar schalten
    xml = re.sub(r'(<mxCell id="[^"]*xknEu-56"[^>]*style=")([^"]*)"',
                 r'\1fillColor=none;strokeColor=none;\2"', xml)
    # Hochachsenbeschriftung drehen und hochkant setzen
    i = xml.find(YLABEL_OLD)
    if i < 0:
        raise ValueError("Achsenbeschriftung nicht gefunden")
    xml = xml.replace(YLABEL_OLD, YLABEL_NEW, 1)
    j = xml.rfind("<mxCell", 0, i)
    head = xml[j:xml.find(">", j)]
    xml = xml.replace(head, re.sub(r'(style="[^"]*)"', r'\1rotation=-90;"', head), 1)
    return xml


def add_title(xml: str, name: str, size: float) -> str:
    """Titel oberhalb des Diagramms einfuegen.

    Wird nach der Skalierung aufgerufen, die Groessen sind daher bereits die
    endgueltigen.
    """
    text, x, w, y = TITLE[name]
    cell = (f'<mxCell id="thesis-title" value="{text}" '
            f'style="text;html=1;align=center;verticalAlign=middle;'
            f'fontFamily={SANS};fontSize={size:.1f};fontStyle=0;" '
            f'vertex="1" parent="1">'
            f'<mxGeometry x="{x}" y="{y}" width="{w}" height="34" as="geometry" />'
            f'</mxCell>')
    return xml.replace("</root>", cell + "</root>", 1)


def measure(pdf: Path) -> tuple[float, float]:
    """Groesste und haeufigste Schriftgroesse in pt, wie sie auf der Seite ankommt."""
    import pymupdf
    d = pymupdf.open(pdf)
    scale = de.TEXTWIDTH_PT / d[0].rect.width
    sizes: dict[float, int] = {}
    for b in d[0].get_text("dict")["blocks"]:
        for line in b.get("lines", []):
            for sp in line["spans"]:
                pt = round(sp["size"] * scale, 2)
                sizes[pt] = sizes.get(pt, 0) + len(sp["text"])
    d.close()
    body = max(sizes.items(), key=lambda kv: kv[1])[0]
    return body, max(sizes)


def restyle(name: str, *, widen: bool = False, belastung: bool = False) -> None:
    """Abbildung umbauen und die Schriftgroesse einregeln.

    Die Groesse auf der Seite haengt von der Breite der exportierten PDF ab,
    und die aendert sich mit dem Umbau. Statt auf einen vorab berechneten
    Faktor zu vertrauen, wird deshalb gemessen und nachgeregelt: exportieren,
    im PDF nachmessen, Faktor korrigieren, erneut exportieren.
    """
    svg = FIG / f"{name}.svg"
    # Quelle ist die unveraenderte .drawio-Datei. Frueher wurde aus der SVG
    # gelesen, die dieses Skript selbst schreibt -- ein zweiter Lauf haette
    # die Aenderungen dann ein zweites Mal angewandt.
    source = (FIG / f"{name}.drawio").read_text(encoding="utf-8")
    factor = font_factor(name)
    title_pt = PT_TITLE / PT_PER_UNIT[name]

    for it in range(4):
        xml = source
        if widen:
            xml = widen_boxes(xml)
        if belastung:
            xml = edit_belastung(xml)
        for old, new in BREAKS.items():
            xml = xml.replace(f'value="{old}"', f'value="{new}"')
        xml = normalize_fonts(xml)
        xml = de.scale_geometry(xml, fx=1.0, fy=VSCALE[name], font=factor)
        xml = add_title(xml, name, title_pt)
        de.write_and_export(svg, xml)

        body, title = measure(svg.with_suffix(".pdf"))
        if abs(body - PT_TEXT) < 0.08 and abs(title - PT_TITLE) < 0.12:
            print(f"  {name}: {body:.2f} pt Text, {title:.2f} pt Titel "
                  f"({it + 1} Durchlaeufe)")
            return
        factor *= PT_TEXT / body
        title_pt *= PT_TITLE / title
    print(f"  {name}: WARNUNG, nicht eingeregelt -- {body:.2f} / {title:.2f} pt")


def main() -> int:
    restyle("curative_process", widen=True)
    restyle("preventiv_vs._curative_redispatch", belastung=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
