"""Diagramme im Querformat und in der Typografie der Arbeit neu erzeugen.

Die Diagramme entstehen in bess_dispatch_optimization mit
analysen/helpers/praesentation_plots.py. Dort sind sie auf Folien
ausgelegt: halbe Folienbreite, figsize (6.6, 5.45), Grundschriftgroesse 14,
Legende einspaltig darunter. In der Arbeit ergaebe das bei voller
Textbreite ein rund 14 cm hohes Bild mit Beschriftungen, die groesser sind
als der 11-pt-Fliesstext.

Dieses Skript ruft dieselben Funktionen mit flachem Seitenverhaeltnis,
mehrspaltiger Legende und angepassten Schriftgroessen auf. Am anderen
Repository wird nichts geaendert: alle Abweichungen werden zur Laufzeit
gesetzt und danach zurueckgenommen. Die Daten kommen aus derselben Quelle
wie fuer die Folien, es wird nichts von Hand abgetippt.

WARUM DIE SCHRIFTGROESSE HIER GESETZT WIRD UND NICHT NACHTRAEGLICH IN DER
SVG: matplotlib berechnet das Layout -- Achsenraender, Legendenspalten,
Zeilenumbrueche -- anhand der Schriftgroesse. Wird die Schrift erst in der
fertigen SVG geaendert, bleibt das Layout auf den alten Groessen stehen.
Die Folge waren abgeschnittene Achsenbeschriftungen und ueberlappende
Legendeneintraege.

WIE DIE ZIELGROESSEN GETROFFEN WERDEN: Die Abbildung wird so erzeugt, dass
sie bereits \\textwidth breit ist. Dann skaliert LaTeX sie nicht mehr, und
die Schriftgroessen kommen unveraendert auf der Seite an. Sie sind fest auf
Zielgroesse geteilt durch 0,75 gesetzt -- svglib rechnet font-size aus px
nach pt mit dem CSS-Faktor 72/96 um, die Geometrie dagegen 1:1.

Nachgefuehrt wird also die BILDGROESSE, nicht die Schrift. Das ist der
entscheidende Unterschied zu einem frueheren Ansatz: Fuehrt man die Schrift
nach, waechst mit ihr die Legende, mit der Legende die ueber
bbox_inches="tight" bestimmte Ausgabebreite und damit der Bedarf an noch
groesserer Schrift -- das laeuft davon. Bei fester Schrift sind die Raender
konstant, und die Korrektur der figsize konvergiert in ein bis zwei
Schritten.

Voraussetzung: ein Python mit matplotlib, numpy und pandas. Der
Systeminterpreter dieser Maschine hat das nicht, Anaconda schon:

    "C:/ProgramData/anaconda3/python.exe" tools/replot_figures.py

Danach:

    python tools/svg_thesis_style.py   # Schriftfamilie, Normalisierung
    python tools/svg2pdf.py            # SVG -> PDF

Der Pfad zum Analyse-Repository laesst sich ueber BESS_REPO setzen.
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BESS_REPO = Path(os.environ.get("BESS_REPO", r"C:\GIT-HUB\bess_dispatch_optimization"))
OUT_DIR = ROOT / "figures" / "chapter_1"

TEXTWIDTH_PT = 455.24411   # \textwidth, siehe main.log
TEXTHEIGHT_PT = 665.38307  # \textheight
TARGET_HEIGHT_PT = 195.0   # angestrebte Hoehe der Abbildung auf der Seite
MAX_HEIGHT_PT = 205.0      # knapp unter einem Drittel der Satzspiegelhoehe

# svglib rechnet px nach pt mit 72/96 um. Siehe tools/svg_thesis_style.py.
PX_TO_PT = 0.75

# Schriftgroesse der Folienfassung -> Zielgroesse in pt auf der Seite.
# Bezug: Fliesstext 11 pt, Bildunterschrift 10 pt. Die Beschriftung der
# Abbildung soll die Bildunterschrift nicht ueberragen.
TARGETS = {
    16.0: 10.0,  # Titel im Bild
    14.0: 9.0,   # Achsenticks, Achsenbeschriftung, Legende
    11.0: 8.0,   # Datenbeschriftung an den Balken
    10.0: 7.5,   # nachgeordnete Beschriftung
    9.0: 7.0,    # Quellenzeile
    8.0: 7.0,    # Fussnote unter der Grafik
}

# name der SVG -> (Funktionsname, figsize, Legendenspalten, Legendenabstand)
FIGURES = {
    "redispatch_jahresbedarf_2020_2025.svg": ("plot_redispatch_jahresbedarf",
                                              (6.3, 2.7), 2, -0.34),
    "engpassmanagement_nep.svg": ("plot_engpassmanagement_nep",
                                  (6.3, 2.7), 2, -0.34),
}


def polish(fig, conv) -> None:
    """Vertikales Layout auf das flache Format umstellen.

    Die Plotfunktionen sind fuer ein hohes Bild geschrieben. Bei rund 195 pt
    Hoehe treten drei Probleme auf, die sich nur an der fertigen Figur
    beheben lassen:

      1. Die Achsenbeschriftung laeuft senkrecht ueber die volle Bildhoehe und
         ist laenger, als das Bild hoch ist. Sie wird deshalb waagerecht ueber
         die Achse gesetzt. Der Wortlaut bleibt unveraendert.
      2. Der Titel im Bild wiederholt die \\caption und belegt genau den Platz,
         den die Achsenbeschriftung jetzt braucht. Er entfaellt.
      3. Die Zeile "Σ = Gesamt in TWh" sitzt oben links und wuerde mit der
         Achsenbeschriftung kollidieren. Sie wandert nach rechts.

    Alle drei Eingriffe sind Gestaltung, kein Inhalt: es verschwindet keine
    Angabe, nur der doppelte Titel.
    """
    ax = fig.axes[0]
    ax.set_title("")

    # "Σ = Gesamt in TWh" nach rechts. set_position() greift hier nicht: das
    # Textobjekt ist eine Annotation mit textcoords="offset points", die
    # Methode verschiebt also den Versatz, nicht den Ankerpunkt.
    for t in ax.texts:
        if t.get_text().startswith("Σ ="):
            t.xy = (1.0, 1.0)
            t.set_ha("right")

    # Mehr Kopfhoehe. Bei flachem Format ruecken die Zahlen ueber den Balken
    # und die Summenzeile darueber sonst ineinander.
    lo, hi = ax.get_ylim()
    ax.set_ylim(lo, hi * 1.14)

    # Die Summenzeile steht fest bei up_max * 1.15 und stoesst dort an die
    # Zahl ueber dem hoechsten Balken. Sie bekommt eine eigene Zeile knapp
    # unter dem oberen Achsenrand.
    row_y = ax.get_ylim()[1] * 0.87
    for t in ax.texts:
        txt = t.get_text()
        if txt.startswith("Σ ") and not txt.startswith("Σ ="):
            t.xy = (t.xy[0], row_y)
            t.set_position((t.xy[0], row_y))

    # Achsenbeschriftung waagerecht ueber die Achse. fontsize wird bewusst
    # unkonvertiert uebergeben -- Axes.annotate ist gepatcht und rechnet um.
    label = ax.get_ylabel()
    if label:
        ax.set_ylabel("")
        ax.annotate(label, xy=(0.0, 1.0), xycoords="axes fraction",
                    xytext=(0, 5), textcoords="offset points",
                    ha="left", va="bottom", fontsize=14)

    # Die Quellenzeile sitzt in Figurkoordinaten und rutscht bei flachem
    # Format weit unter die Legende. Sie wird direkt darunter gesetzt.
    fig.canvas.draw()
    legend = ax.get_legend()
    if legend is not None and fig.texts:
        inv = fig.transFigure.inverted()
        bottom = inv.transform(legend.get_window_extent().p0)[1]
        for t in fig.texts:
            t.set_y(bottom - 0.06)
            t.set_va("top")


def target_pt(orig: float) -> float:
    if orig in TARGETS:
        return TARGETS[orig]
    nearest = min(TARGETS, key=lambda k: abs(k - orig))
    return TARGETS[nearest] * orig / nearest


def svg_size(path: Path) -> tuple[float, float]:
    m = re.search(r'width="([0-9.]+)pt" height="([0-9.]+)pt"',
                  path.read_text(encoding="utf-8"))
    return float(m.group(1)), float(m.group(2))


def main() -> int:
    if not BESS_REPO.is_dir():
        print(f"Analyse-Repository nicht gefunden: {BESS_REPO}")
        print("Pfad ueber die Umgebungsvariable BESS_REPO setzen.")
        return 1
    sys.path.insert(0, str(BESS_REPO))

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.axes import Axes
        from matplotlib.figure import Figure
        from analysen.helpers import praesentation_plots as pp
    except ImportError as exc:
        print(f"Import fehlgeschlagen: {exc}")
        print('Mit einem Python aufrufen, das matplotlib hat, etwa '
              '"C:/ProgramData/anaconda3/python.exe".')
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    originals = dict(subplots=plt.subplots, legend=pp._legend_below,
                     annotate=Axes.annotate, atext=Axes.text, ftext=Figure.text,
                     save=pp._save_pp, PP=dict(pp.PP))
    problems = 0

    # Schriftgroesse, die matplotlib setzen muss, damit die Zielgroesse in pt
    # herauskommt. Fest, weil die Abbildung am Ende \textwidth breit ist und
    # LaTeX sie nicht mehr skaliert.
    comp = 1.0 / PX_TO_PT

    def conv(fs, _c=comp):
        return target_pt(float(fs)) * _c

    for name, (fn_name, figsize, ncol, legend_y) in FIGURES.items():
        fn = getattr(pp, fn_name)
        svg = OUT_DIR / name
        fig_w, fig_h = figsize
        w = h = 0.0

        for it in range(6):

            pp.PP.update({k: conv(originals["PP"][k]) for k in
                          ("font.size", "axes.titlesize", "axes.labelsize",
                           "xtick.labelsize", "ytick.labelsize", "legend.fontsize")})
            plt.subplots = (lambda *a, _fs=(fig_w, fig_h), **k:
                            originals["subplots"](*a, **{**k, "figsize": _fs}))
            pp._legend_below = (lambda ax, _n=ncol, _y=legend_y, **k:
                                originals["legend"](ax, **{
                                    **k, "ncol": _n, "y": _y,
                                    "fontsize": conv(k.get("fontsize", 14))}))
            # Die Plotfunktionen setzen fontsize teils direkt am Aufruf.
            Axes.annotate = (lambda self, *a, **k: originals["annotate"](
                self, *a, **({**k, "fontsize": conv(k["fontsize"])}
                             if "fontsize" in k else k)))
            Axes.text = (lambda self, *a, **k: originals["atext"](
                self, *a, **({**k, "fontsize": conv(k["fontsize"])}
                             if "fontsize" in k else k)))
            Figure.text = (lambda self, *a, **k: originals["ftext"](
                self, *a, **({**k, "fontsize": conv(k["fontsize"])}
                             if "fontsize" in k else k)))
            # _save_pp bekommt die fertige Figur unmittelbar vor dem Speichern.
            # Das ist der einzige Punkt, an dem sich das vertikale Layout noch
            # korrigieren laesst, ohne die Plotfunktionen zu aendern.
            pp._save_pp = (lambda fig, *a, **k:
                           (polish(fig, conv), originals["save"](fig, *a, **k))[1])
            try:
                fn(out_dir=OUT_DIR)
            finally:
                plt.subplots = originals["subplots"]
                pp._legend_below = originals["legend"]
                Axes.annotate, Axes.text = originals["annotate"], originals["atext"]
                Figure.text = originals["ftext"]
                pp._save_pp = originals["save"]
                pp.PP.clear(); pp.PP.update(originals["PP"])

            png = svg.with_suffix(".png")
            if png.exists():
                png.unlink()   # Vorschau-PNG wird nicht gebraucht
            if not svg.exists():
                print(f"  FEHLER  {name} wurde nicht erzeugt")
                problems += 1
                break

            w, h = svg_size(svg)
            # Bei fester Schrift sind die von bbox_inches="tight" erzeugten
            # Raender konstant. Die Differenz laesst sich daher direkt auf die
            # figsize addieren; das konvergiert in ein bis zwei Schritten.
            dw, dh = TEXTWIDTH_PT - w, TARGET_HEIGHT_PT - h
            if abs(dw) < 1.0 and abs(dh) < 1.0:
                break
            fig_w, fig_h = fig_w + dw / 72.0, fig_h + dh / 72.0
            if fig_w < 1.0 or fig_h < 0.8:
                # Die Ausgabebreite hat eine Untergrenze: Legende und
                # Achsenbeschriftung sind breiter als die Zeichenflaeche und
                # lassen sich ueber figsize nicht weiter verkleinern. Dann
                # hilft nur ein anderes Legendenlayout, nicht ein kleineres
                # Bild.
                print(f"  FEHLER  {name}: Breite laesst sich nicht auf "
                      f"{TEXTWIDTH_PT:.0f} pt bringen, gemessen {w:.0f} pt.")
                print("          Untergrenze durch Legende oder Achsen"
                      "beschriftung. Spaltenzahl in FIGURES aendern.")
                problems += 1
                break
        else:
            print(f"  WARNUNG  {name}: Bildgroesse nicht konvergiert")

        if not svg.exists():
            continue
        flag = "" if h <= MAX_HEIGHT_PT else "   ZU HOCH"
        print(f"  {name}")
        print(f"     {w:.1f} x {h:.1f} pt bei figsize ({fig_w:.2f}, {fig_h:.2f}), "
              f"{it + 1} Durchlaeufe")
        print(f"     Skalierung durch LaTeX {TEXTWIDTH_PT / w:.4f}, Hoehe "
              f"{h / TEXTHEIGHT_PT * 100:.0f} % der Satzspiegelhoehe{flag}")
        if h > MAX_HEIGHT_PT:
            problems += 1

    print("\nJetzt: python tools/svg_thesis_style.py && python tools/svg2pdf.py")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
