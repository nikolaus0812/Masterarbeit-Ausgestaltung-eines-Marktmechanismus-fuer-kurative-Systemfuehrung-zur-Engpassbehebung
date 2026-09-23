# -*- coding: utf-8 -*-
"""Die zehn ertragreichsten Arbitragepaare je Tag und ihre Lage.

Vorgabe des Verfassers vom 23.09.2026: liegen die besten Spannen eines
Tages in denselben Stunden, in denen auch die kurative Reservierung teuer
ist, so treibt das den Preis, besonders fuer die zuletzt verdraengten
Stunden.

Ein Paar besteht aus einer Bezugs- und einer Absatzviertelstunde
desselben Tages. Paar 1 verbindet die guenstigste mit der teuersten
Viertelstunde, Paar 2 die zweitguenstigste mit der zweitteuersten und so
fort bis Paar 10. Als Bezugspreis gilt das Kleinere aus Day-Ahead und
Intraday, als Absatzpreis das Groessere, denn die Bezugsanlage waehlt je
Viertelstunde den besseren Markt. Eine zeitliche Reihenfolge von Bezug
und Absatz wird nicht erzwungen; die Kennzahl misst die Tiefe des
Angebots an Spannen und keinen fahrbaren Fahrplan.

Eigene Auswertung der Schriftfassung vom 23.09.2026, nur lesend.
"""
import io
import os
import sys

import numpy as np
import pandas as pd

QUELLE = (r"C:\GIT-HUB\bess_dispatch_optimization\analysen\03_breakeven"
          r"\heatmaps\jahr_slots_2025.parquet")
HIER = os.path.dirname(os.path.abspath(__file__))
PAARE = 10

d = pd.read_parquet(QUELLE)
d = d[~d["gesperrt"]].copy()
d["day"] = pd.to_datetime(d["day"])
d["p_kauf"] = d[["preis_da", "preis_idc"]].min(axis=1)
d["p_verkauf"] = d[["preis_da", "preis_idc"]].max(axis=1)

bericht = []


def sag(z=""):
    bericht.append(z)
    sys.stdout.write(z + "\n")


zeilen = []
for tag, z in d.groupby("day"):
    z = z.sort_values("slot")
    kauf = z.nsmallest(PAARE, "p_kauf")
    verkauf = z.nlargest(PAARE, "p_verkauf")
    spannen = (verkauf["p_verkauf"].values - kauf["p_kauf"].values)
    # Stunden, die zu den zehn Paaren gehoeren.
    stunden_paare = set(kauf["stunde"]) | set(verkauf["stunde"])
    in_paar = z["stunde"].isin(stunden_paare)
    # Die teuersten Reservierungsstunden des Tages, je Richtung.
    je_stunde = z.groupby("stunde")[["be_pos", "be_neg"]].mean()
    top_ent = set(je_stunde["be_pos"].nlargest(6).index)
    top_lad = set(je_stunde["be_neg"].nlargest(6).index)
    zeilen.append({
        "day": tag,
        "spanne_1": spannen[0],
        "spanne_10": spannen[-1],
        "abfall": spannen[-1] / spannen[0] if spannen[0] > 0 else np.nan,
        "res_ent": z["be_pos"].mean(),
        "res_lad": z["be_neg"].mean(),
        "res_in_paar_ent": z.loc[in_paar, "be_pos"].mean(),
        "res_ausser_ent": z.loc[~in_paar, "be_pos"].mean(),
        "res_in_paar_lad": z.loc[in_paar, "be_neg"].mean(),
        "res_ausser_lad": z.loc[~in_paar, "be_neg"].mean(),
        "deckung_ent": len(top_ent & set(verkauf["stunde"])) / len(top_ent),
        "deckung_lad": len(top_lad & set(kauf["stunde"])) / len(top_lad),
    })

t = pd.DataFrame(zeilen).set_index("day")
t["monat"] = t.index.month

sag("# Die zehn ertragreichsten Arbitragepaare je Tag")
sag()
sag("Eigene Auswertung vom 23.09.2026. Alle Preise in Euro je Megawattstunde,")
sag("die Reservierungspreise in Euro je Megawatt und Stunde.")
sag()

sag("## 1 Wie schnell die Spannen abfallen")
sag()
sag("| Groesse | Median | unteres Quartil | oberes Quartil |")
sag("|---|---|---|---|")
for name, spalte in (("Spanne des ersten Paares", "spanne_1"),
                     ("Spanne des zehnten Paares", "spanne_10"),
                     ("Verhaeltnis zehntes zu erstem Paar", "abfall")):
    sag("| %s | %.2f | %.2f | %.2f |"
        % (name, t[spalte].median(), t[spalte].quantile(0.25),
           t[spalte].quantile(0.75)))
sag()
sag("Das zehnte Paar traegt im Median noch %.0f Prozent der Spanne des ersten."
    % (t["abfall"].median() * 100))
sag()

sag("## 2 Liegt die Reservierung teuer, wo die Paare liegen")
sag()
sag("Mittlerer Reservierungspreis in den Stunden, die zu den zehn Paaren")
sag("gehoeren, gegen die uebrigen Stunden desselben Tages.")
sag()
sag("| Richtung | in den Paarstunden | in den uebrigen Stunden | Faktor |")
sag("|---|---|---|---|")
for name, a, b in (("Entladereservierung", "res_in_paar_ent", "res_ausser_ent"),
                   ("Ladereservierung", "res_in_paar_lad", "res_ausser_lad")):
    x, y = t[a].mean(), t[b].mean()
    sag("| %s | %.1f | %.1f | %.2f |" % (name, x, y, x / y))
sag()
sag("Deckung: Anteil der sechs teuersten Reservierungsstunden eines Tages,")
sag("die zugleich zu den zehn Paaren gehoeren.")
sag()
sag("| Richtung | Median | Mittel |")
sag("|---|---|---|")
sag("| Entladen gegen Absatzstunden | %.0f %% | %.0f %% |"
    % (t["deckung_ent"].median() * 100, t["deckung_ent"].mean() * 100))
sag("| Laden gegen Bezugsstunden | %.0f %% | %.0f %% |"
    % (t["deckung_lad"].median() * 100, t["deckung_lad"].mean() * 100))
sag()

sag("## 3 Woran der Tagespreis haengt, erstes oder zehntes Paar")
sag()
sag("Rangkorrelation nach Spearman ueber alle 365 Tage.")
sag()
sag("| | Spanne des ersten Paares | Spanne des zehnten Paares | Abfall |")
sag("|---|---|---|---|")
for name, spalte in (("Entladereservierung", "res_ent"),
                     ("Ladereservierung", "res_lad")):
    sag("| %s | %+.2f | %+.2f | %+.2f |"
        % (name,
           t[spalte].corr(t["spanne_1"], method="spearman"),
           t[spalte].corr(t["spanne_10"], method="spearman"),
           t[spalte].corr(t["abfall"], method="spearman")))
sag()

sag("## 4 Monatsbild")
sag()
sag("| Monat | Spanne Paar 1 | Spanne Paar 10 | Abfall | Deckung entladen | "
    "Deckung laden |")
sag("|---|---|---|---|---|---|")
m = t.groupby("monat").mean(numeric_only=True)
for i in range(1, 13):
    sag("| %02d | %.1f | %.1f | %.0f %% | %.0f %% | %.0f %% |"
        % (i, m.loc[i, "spanne_1"], m.loc[i, "spanne_10"],
           m.loc[i, "abfall"] * 100, m.loc[i, "deckung_ent"] * 100,
           m.loc[i, "deckung_lad"] * 100))
sag()

sag("## 5 Die zehn Tage mit der flachsten und der steilsten Staffel")
sag()
for kopf, rahmen in (("Flachste Staffel, das zehnte Paar traegt fast so viel "
                      "wie das erste", t.nlargest(10, "abfall")),
                     ("Steilste Staffel, die Spanne bricht nach dem ersten "
                      "Paar ein", t.nsmallest(10, "abfall"))):
    sag("**%s**" % kopf)
    sag()
    sag("| Tag | Paar 1 | Paar 10 | Abfall | Reservierung entladen | "
        "Reservierung laden |")
    sag("|---|---|---|---|---|---|")
    for tag, z in rahmen.iterrows():
        sag("| %s | %.1f | %.1f | %.0f %% | %.1f | %.1f |"
            % (tag.strftime("%d.%m."), z["spanne_1"], z["spanne_10"],
               z["abfall"] * 100, z["res_ent"], z["res_lad"]))
    sag()

ZIEL = os.path.join(HIER, "BEFUND_ARBITRAGEPAARE.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
