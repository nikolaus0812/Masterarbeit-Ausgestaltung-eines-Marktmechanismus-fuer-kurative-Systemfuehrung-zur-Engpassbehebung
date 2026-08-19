"""Diagramme fuer Kapitel 1 erzeugen: Querformat, Dokumenttypografie.

NICHT AUSFUEHREN. Dieses Skript wandert vollstaendig in das Repository
bess_dispatch_optimization, weil die Nachbearbeitung zur Erzeugung und nicht
zur Schriftfassung gehoert. Bis zum Umzug bleibt es unveraendert liegen.

Der Grund fuer die Sperre steht in TEXTWIDTH_PT weiter unten. Der Wert
455,24411 wird dort mit 72 statt mit 72,27 in Zoll umgerechnet, das Skript
zielt also auf big points statt auf TeX-Punkte. Ein Lauf schreibt die
Abbildungen mit diesem alten Punktmass neu und macht sie wieder 0,37 Prozent
zu breit. Die Zielbreite ist 6,29921 Zoll.

Nach dem Umzug ersetzt die dortige Loesung dieses Skript. Jedes Analyseskript
erhaelt eine standardmaessig leere Variable fuer ein optionales
Zielverzeichnis. Ist sie gesetzt, legt das Skript die Datei zusaetzlich im
Kapitelordner dieser Schriftfassung ab.

Die Diagramme entstehen in bess_dispatch_optimization mit
analysen/helpers/praesentation_plots.py. Dort sind sie auf Folien
ausgelegt: halbe Folienbreite, Grundschriftgroesse 14, Legende einspaltig
darunter, Spiegelbalken um die Nulllinie.

Zwei Wege:

  engpassmanagement_nep   ruft die Originalfunktion auf und korrigiert die
                          fertige Figur (Achsenbeschriftung, Quellenzeile,
                          Kopfhoehe).

  redispatch_jahresbedarf wird hier neu gezeichnet. Die Originalfassung ist
                          ein Spiegelbalkendiagramm mit Hochfahren ueber und
                          Runterfahren unter der Nulllinie; gewuenscht ist
                          ein gestapelter Balken ueber der Achse. Das laesst
                          sich an der fertigen Figur nicht mehr aendern. Die
                          Daten kommen unveraendert aus
                          _redispatch_jahresmengen, es wird nichts von Hand
                          abgetippt.

Am anderen Repository wird nichts geaendert. Alle Abweichungen werden zur
Laufzeit gesetzt und danach zurueckgenommen.

KEIN TITEL IM BILD: Die Abbildungen tragen keine Ueberschrift. Was sie
zeigen, steht in der Bildunterschrift; ein Titel im Bild wiederholte sie.

SCHRIFTGROESSEN: alles im Diagramm 11 pt wie der Fliesstext. Ausnahme ist
die Fussnote unter dem NEP-Diagramm mit 9 pt.

WIE DIE GROESSEN GETROFFEN WERDEN: Die Abbildung wird so erzeugt, dass sie
bereits \\textwidth breit ist; dann skaliert LaTeX sie nicht mehr. Die
Schriftgroessen sind fest auf Zielgroesse geteilt durch 0,75 gesetzt --
svglib rechnet font-size aus px nach pt mit dem CSS-Faktor 72/96 um, die
Geometrie dagegen 1:1. Nachgefuehrt wird die BILDGROESSE, nicht die
Schrift: fuehrt man die Schrift nach, waechst mit ihr die Legende, mit der
Legende die ueber bbox_inches="tight" bestimmte Ausgabebreite und damit der
Bedarf an noch groesserer Schrift -- das laeuft davon.

Voraussetzung: ein Python mit matplotlib, numpy und pandas:

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
# Die Hoehe wird nicht mehr erzwungen. Eine senkrechte Achsenbeschriftung
# braucht so viel Achsenhoehe, wie ihr Text lang ist; presst man die
# Abbildung auf eine Zielhoehe, wird sie wieder abgeschnitten. Nachgefuehrt
# wird daher nur die Breite, die Hoehe ergibt sich aus figsize.
MAX_HEIGHT_PT = 285.0      # Hinweis, wenn es zu hoch wird

# svglib rechnet px nach pt mit 72/96 um. Siehe tools/svg_thesis_style.py.
PX_TO_PT = 0.75

# Zielgroessen in pt auf der fertigen Seite.
# PT_TITLE wird nicht mehr gesetzt, seit die Abbildungen ohne Ueberschrift
# stehen. Der Eintrag bleibt, weil TARGETS die Groesse 16 der Folienfassung
# noch abbilden muss: pp.PP traegt sie als axes.titlesize, und target_pt
# soll dafuer keinen genaeherten Wert erfinden.
PT_TITLE = 14.0
# Im fertigen main.pdf gemessen: Fliesstext 10,91 pt, Bildunterschrift
# 9,96 pt. Die Beschriftung im Diagramm orientiert sich an der
# Bildunterschrift, die unmittelbar darunter steht -- gegen sie wirkte
# Fliesstextgroesse zu gross.
PT_TEXT = 10.0
PT_NOTE = 8.5      # Fussnote unter dem NEP-Diagramm

# Schriftgroesse der Folienfassung -> Zielgroesse. 16 traegt die
# Folienfassung als axes.titlesize, 8 ist die Fussnote, alles dazwischen ist
# Beschriftung im Diagramm. Ein Titel wird nicht mehr gesetzt.
TARGETS = {16.0: PT_TITLE, 14.0: PT_TEXT, 11.0: PT_TEXT,
           10.0: PT_TEXT, 9.0: PT_NOTE, 8.0: PT_NOTE}

# HOEHEN, seit die Abbildungen ohne Titel stehen: 4,3 statt 3,6 und 3,8
# statt 3,6. Die senkrechte Achsenbeschriftung ist laenger, als die Achse
# hoch ist; ueber ihr Ende hinaus ragte sie frueher in den Raum, den der
# Titel freihielt. Ohne Titel wurde sie am oberen Seitenrand beschnitten,
# beim NEP-Diagramm um 4,8 pt, beim Redispatch-Diagramm um 1,7 pt. Die
# Werte unten sind die kleinsten, bei denen nichts mehr uebersteht.
# ACHTUNG: Wer diese Hoehen senkt, muss danach nachsehen, ob die
# Achsenbeschriftung noch vollstaendig SICHTBAR ist. Eine Textsuche im PDF
# genuegt dafuer NICHT -- der abgeschnittene Teil steht weiterhin im
# Inhaltsstrom und wird gefunden. Zu pruefen ist die Textbegrenzung gegen
# das Seitenrechteck.
FIGURES = {
    "engpassmanagement_nep.svg": dict(
        mode="patch", fn="plot_engpassmanagement_nep",
        figsize=(6.3, 4.3), ncol=2, legend_y=-0.30,
        ylabel="Engpassmanagementbedarf in TWh",
    ),
    "redispatch_jahresbedarf_2020_2025.svg": dict(
        mode="own", figsize=(6.3, 3.8), ncol=2, legend_y=-0.20,
        ylabel="Engpassmanagementbedarf in TWh",
    ),
}


def target_pt(orig: float) -> float:
    if orig in TARGETS:
        return TARGETS[orig]
    nearest = min(TARGETS, key=lambda k: abs(k - orig))
    return TARGETS[nearest] * orig / nearest


def svg_size(path: Path) -> tuple[float, float]:
    m = re.search(r'width="([0-9.]+)pt" height="([0-9.]+)pt"',
                  path.read_text(encoding="utf-8"))
    return float(m.group(1)), float(m.group(2))


def strip_source(fig) -> None:
    """Quellenzeile entfernen, uebrige Fussnoten behalten.

    Beim NEP-Diagramm stehen Fussnote und Quelle in einem einzigen
    Textobjekt. Die Fussnote erklaert das Sternchen in der Legende und muss
    bleiben, die Quellenzeile soll weg.
    """
    for t in list(fig.texts):
        keep = [ln for ln in t.get_text().split("\n")
                if not ln.strip().startswith("Quelle")]
        if keep:
            t.set_text("\n".join(keep))
        else:
            t.remove()


def place_head(ax, ylabel: str, conv) -> None:
    """Achsenbeschriftung setzen.

    Die Achsenbeschriftung steht senkrecht neben der Achse. Sie ist lang,
    die Abbildung braucht deshalb genug Hoehe -- siehe figsize in FIGURES.

    KEIN TITEL IM BILD: Die Aussage der Abbildung steht in der
    Bildunterschrift. Ein Titel im Bild wiederholte sie und stuende zudem
    in einer anderen Schriftgroesse unmittelbar darueber.

    Der Titel wird ausdruecklich GELEERT und nicht nur nicht gesetzt. Die
    Folienfassung in bess_dispatch_optimization bringt einen eigenen mit
    ("Engpassmanagement-Bedarf 2032 bis 2045"); frueher hat ihn das hier
    gesetzte set_title ueberschrieben. Ohne das Leeren bliebe er stehen.
    """
    ax.set_title("")
    ax.set_ylabel(ylabel, fontsize=conv(14))


def tuck_notes(fig, ax) -> None:
    """Verbliebene Fussnoten direkt unter die Legende ruecken.

    Sie stehen in Figurkoordinaten und rutschen im flachen Format sonst weit
    nach unten, was die Abbildung unnoetig hoch macht.
    """
    fig.canvas.draw()
    legend = ax.get_legend()
    if legend is None or not fig.texts:
        return
    bottom = fig.transFigure.inverted().transform(legend.get_window_extent().p0)[1]
    for t in fig.texts:
        t.set_y(bottom - 0.04)
        t.set_va("top")


def polish_nep(fig, cfg, conv) -> None:
    ax = fig.axes[0]
    lo, hi = ax.get_ylim()
    ax.set_ylim(lo, hi * 1.05)
    place_head(ax, cfg["ylabel"], conv)
    strip_source(fig)
    tuck_notes(fig, ax)


def draw_redispatch(pp, plt, MaxNLocator, Line2D, cfg, conv, figsize, out_dir):
    """Jahresredispatch als gestapelter Balken ueber der Achse.

    Ein Balken je Jahr, von unten nach oben Hochfahren, Runterfahren
    Wind und Photovoltaik, Runterfahren konventionell und sonstige. Die
    Werte stehen einheitlich mittig im jeweiligen Abschnitt, die Summe
    ueber dem Balken. Ein Abschnitt bekommt nur dann eine Zahl, wenn er
    hoch genug dafuer ist.
    """
    d = pp._redispatch_jahresmengen(2020, 2025)
    years = list(d.index)
    x = range(len(years))
    # Der dritte Eintrag traegt kein "Runterfahren:" mehr. Beide Eintraege
    # stehen in derselben Legendenzeile, das Wort gilt damit fuer beide.
    # Gemessen: mit doppeltem Praefix ist die Legendenzeile 531 pt breit und
    # passt nicht in die Textbreite von 455 pt, ohne 434 pt.
    parts = [("hoch", pp.C_HOCH_B, "Hochfahren"),
             ("ee", pp.C_EE, "Runterfahren: Wind + Photovoltaik"),
             ("konv_runter", pp.C_RUNT_B, "konventionell / sonstige")]
    ges = d["gesamt"].to_numpy(float)

    with plt.rc_context(pp.PP):
        fig, ax = plt.subplots(figsize=figsize)
        bottom = [0.0] * len(years)
        for col, color, label in parts:
            v = d[col].to_numpy(float)
            ax.bar(list(x), v, bottom=bottom, width=0.64, color=color, zorder=3,
                   edgecolor="black", linewidth=0.7, label=label)
            bottom = [b + s for b, s in zip(bottom, v)]

        top = max(ges) * 1.18
        ax.set_ylim(0, top)

        # Zahlen einheitlich mittig im Abschnitt, aber nur wenn er Platz bietet.
        base = [0.0] * len(years)
        for col, _c, _l in parts:
            v = d[col].to_numpy(float)
            for i, val in enumerate(v):
                if val / top > 0.10:
                    ax.text(i, base[i] + val / 2, f"{val:.1f}", ha="center",
                            va="center", fontsize=conv(11), color="white",
                            zorder=5)
            base = [b + s for b, s in zip(base, v)]
        # Die Summenzeile steht ueber den Balken und damit vor den
        # Gitterlinien. Ein deckender Hintergrund verhindert, dass eine
        # Gitterlinie durch die Ziffern laeuft.
        for i, g in enumerate(ges):
            ax.annotate(f"{g:.1f}", xy=(i, g), xytext=(0, 4),
                        textcoords="offset points", ha="center", va="bottom",
                        fontsize=conv(11), color=pp.C_GES, zorder=6,
                        bbox=dict(facecolor="white", edgecolor="none",
                                  pad=0.8))

        # Bei flacher Achse setzt matplotlib sonst nur zwei Teilstriche.
        ax.yaxis.set_major_locator(MaxNLocator(nbins=4, integer=True))
        ax.set_xticks(list(x))
        ax.set_xticklabels([str(y) for y in years], fontsize=conv(14))
        ax.tick_params(axis="y", labelsize=conv(14))
        place_head(ax, cfg["ylabel"], conv)
        # Zwei Zeilen: oben Hochfahren allein, unten beide Runterfahren
        # nebeneinander. matplotlib fuellt SPALTENWEISE, nicht zeilenweise --
        # bei zwei Spalten landen die Eintraege 0 und 1 in der linken, 2 und 3
        # in der rechten Spalte. Der Leereintrag muss deshalb an dritter
        # Stelle stehen, damit er oben rechts zu liegen kommt.
        # Kompakte Symbole und enger Spaltenabstand sind noetig, damit die
        # beiden langen Beschriftungen nebeneinander in die Textbreite passen.
        h, l = ax.get_legend_handles_labels()
        blank = Line2D([], [], linestyle="none")
        ax.legend([h[0], h[1], blank, h[2]], [l[0], l[1], " ", l[2]],
                  loc="upper center", bbox_to_anchor=(0.5, cfg["legend_y"]),
                  ncol=2, fontsize=conv(14), framealpha=0.0,
                  columnspacing=0.6, handlelength=0.9, handletextpad=0.35,
                  borderpad=0.1)
        fig.tight_layout()
    return pp._save_pp(fig, Path(out_dir), "redispatch_jahresbedarf_2020_2025.png")


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
        from matplotlib.ticker import MaxNLocator
        from matplotlib.lines import Line2D
        from matplotlib.axes import Axes
        from matplotlib.figure import Figure
        # Die Plot-Bibliothek ist im Analyse-Repository umgezogen. Beide
        # Ablagen werden versucht, damit dieses Skript in beiden Staenden
        # laeuft.
        try:
            from analysen.code.helpers import praesentation_plots as pp
        except ImportError:
            from analysen.helpers import praesentation_plots as pp
    except ImportError as exc:
        print(f"Import fehlgeschlagen: {exc}")
        print('Mit einem Python aufrufen, das matplotlib hat, etwa '
              '"C:/ProgramData/anaconda3/python.exe".')
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    orig = dict(subplots=plt.subplots, legend=pp._legend_below,
                annotate=Axes.annotate, atext=Axes.text, ftext=Figure.text,
                save=pp._save_pp, PP=dict(pp.PP))
    problems = 0

    # Schriftgroesse, die matplotlib setzen muss, damit die Zielgroesse in pt
    # herauskommt. Fest, weil die Abbildung \textwidth breit ist.
    def conv(fs):
        return target_pt(float(fs)) / PX_TO_PT

    for name, cfg in FIGURES.items():
        svg = OUT_DIR / name
        fig_w, fig_h = cfg["figsize"]
        w = h = 0.0

        for it in range(6):
            pp.PP.update({k: conv(orig["PP"][k]) for k in
                          ("font.size", "axes.titlesize", "axes.labelsize",
                           "xtick.labelsize", "ytick.labelsize", "legend.fontsize")})
            try:
                if cfg["mode"] == "own":
                    draw_redispatch(pp, plt, MaxNLocator, Line2D, cfg, conv, (fig_w, fig_h), OUT_DIR)
                else:
                    plt.subplots = (lambda *a, _fs=(fig_w, fig_h), **k:
                                    orig["subplots"](*a, **{**k, "figsize": _fs}))
                    pp._legend_below = (lambda ax, _n=cfg["ncol"], _y=cfg["legend_y"],
                                        **k: orig["legend"](ax, **{
                                            **k, "ncol": _n, "y": _y,
                                            "fontsize": conv(k.get("fontsize", 14))}))
                    for cls, attr, key in ((Axes, "annotate", "annotate"),
                                           (Axes, "text", "atext"),
                                           (Figure, "text", "ftext")):
                        setattr(cls, attr, (lambda self, *a, _f=orig[key], **k: _f(
                            self, *a, **({**k, "fontsize": conv(k["fontsize"])}
                                         if "fontsize" in k else k))))
                    pp._save_pp = (lambda fig, *a, _c=cfg, **k: (
                        polish_nep(fig, _c, conv), orig["save"](fig, *a, **k))[1])
                    getattr(pp, cfg["fn"])(out_dir=OUT_DIR)
            finally:
                plt.subplots, pp._legend_below = orig["subplots"], orig["legend"]
                Axes.annotate, Axes.text = orig["annotate"], orig["atext"]
                Figure.text, pp._save_pp = orig["ftext"], orig["save"]
                pp.PP.clear(); pp.PP.update(orig["PP"])

            png = svg.with_suffix(".png")
            if png.exists():
                png.unlink()   # Vorschau-PNG wird nicht gebraucht
            if not svg.exists():
                print(f"  FEHLER  {name} wurde nicht erzeugt")
                problems += 1
                break

            w, h = svg_size(svg)
            # Bei fester Schrift sind die Raender konstant; die Differenz laesst
            # sich direkt auf die figsize addieren.
            dw = TEXTWIDTH_PT - w
            if abs(dw) < 1.0:
                break
            fig_w = fig_w + dw / 72.0
            if fig_w < 1.0:
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
