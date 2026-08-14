"""Werkzeugkasten fuer die draw.io-Abbildungen.

Die SVG in figures/chapter_2 sind editierbare draw.io-Exporte: im Attribut
content des svg-Elements steckt die Diagrammquelle als mxfile-XML. Dieses
Modul liest sie heraus, laesst sie veraendern und exportiert danach ueber
draw.io Desktop sowohl PDF als auch SVG neu, sodass beide Fassungen
zusammenpassen.

Als Bibliothek gedacht, nicht als eigenstaendiges Skript. Die eigentlichen
Aenderungen stehen in tools/drawio_restyle.py.

WARUM DIE SCHRIFT UEBER DIE GEOMETRIE MITWACHSEN MUSS: Auf der Seite
erscheint die Beschriftung in

    Groesse auf der Seite = fontSize * k * (\\textwidth / Diagrammbreite)

Vergroessert man nur die Schrift, laeuft der Text aus den Kaesten. Skaliert
man nur die Geometrie herunter, ebenfalls. Die Breite muss deshalb
konstant bleiben, waehrend Schrift und Hoehen gemeinsam wachsen: die
Beschriftung bricht dann in mehr Zeilen um, fuer die die hoeheren Kaesten
Platz bieten.
"""

import html
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAWIO = Path(os.environ.get("DRAWIO", r"C:\Program Files\draw.io\draw.io.exe"))

# Aus dem fertigen main.pdf zurueckgerechnet: eine Beschriftung mit
# fontSize 12 erscheint in der exportierten PDF mit 8,02 pt.
PT_PER_FONTSIZE = 8.02 / 12
TEXTWIDTH_PT = 455.24411


def read_mxfile(svg: Path) -> str:
    m = re.search(r'\scontent="([^"]*)"', svg.read_text(encoding="utf-8"))
    if not m:
        raise ValueError(f"{svg} enthaelt keine mxfile-Quelle")
    return html.unescape(m.group(1))


def svg_size(svg: Path) -> tuple[int, int]:
    m = re.search(r'width="(\d+)px" height="(\d+)px"',
                  svg.read_text(encoding="utf-8"))
    return int(m.group(1)), int(m.group(2))


def page_pt(font_size: float, diagram_width_px: float) -> float:
    """Schriftgroesse in pt, wie sie auf der Seite ankommt."""
    pdf_pt = font_size * PT_PER_FONTSIZE
    # Die PDF ist etwa so breit wie die SVG in px, LaTeX skaliert auf \textwidth.
    return pdf_pt * (TEXTWIDTH_PT / diagram_width_px) * (diagram_width_px / diagram_width_px)


def scale_geometry(xml: str, *, fy: float = 1.0, fx: float = 1.0,
                   font: float = 1.0) -> str:
    """Geometrie und Schriftgroesse skalieren.

    fx und fy wirken auf x/width beziehungsweise y/height, font auf jedes
    fontSize in den Formatangaben. mxPoint-Elemente, mit denen draw.io die
    Stuetzpunkte von Verbindungen ablegt, werden mitgezogen.
    """
    def geo(m: re.Match) -> str:
        attr, val = m.group(1), float(m.group(2))
        f = fx if attr in ("x", "width") else fy
        return f'{attr}="{round(val * f, 2):g}"'

    xml = re.sub(r'\b(x|y|width|height)="([-\d.]+)"', geo, xml)
    xml = re.sub(r'fontSize=(\d+(?:\.\d+)?)',
                 lambda m: f"fontSize={round(float(m.group(1)) * font, 1):g}", xml)
    return xml


def write_and_export(svg: Path, xml: str) -> None:
    """mxfile als .drawio ablegen und PDF sowie SVG neu exportieren."""
    # Bewusst NICHT svg.with_suffix(".drawio"): unter diesem Namen liegt die
    # unveraenderte Quelle. Das finally unten wuerde sie loeschen.
    tmp = svg.with_name(svg.stem + ".export.tmp.drawio")
    tmp.write_text(xml, encoding="utf-8", newline="\n")
    try:
        for fmt, out in (("pdf", svg.with_suffix(".pdf")), ("svg", svg)):
            cmd = [str(DRAWIO), "--export", "--format", fmt, "--crop",
                   "--output", str(out), str(tmp)]
            if fmt == "svg":
                cmd.insert(-1, "--embed-diagram")
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            if res.returncode != 0 or not out.exists():
                raise RuntimeError((res.stderr or res.stdout).strip()[:400])
            print(f"    {out.name}")
    finally:
        tmp.unlink(missing_ok=True)
