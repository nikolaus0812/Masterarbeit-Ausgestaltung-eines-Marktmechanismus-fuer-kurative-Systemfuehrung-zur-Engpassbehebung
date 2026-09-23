# -*- coding: utf-8 -*-
"""Neuberechnung der Zahlen, die in Kapitel 4 stehen, 23.09.2026.

Alle frueheren Auswertungen dieses Ordners haben `be_pos` und `be_neg`
als Reservierungspreis genommen, also die **erste** Iteration. Die Arbeit
weist die zweite aus. Diese Datei rechnet die Zahlen neu, die in den Text
eingegangen sind, und zwar mit `be_full_pos` und `be_full_neg`.
"""
import io
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import laden

HIER = os.path.dirname(os.path.abspath(__file__))
MITTAG = range(10, 16)
ABEND = range(17, 21)

bericht = []


def sag(z=""):
    bericht.append(z)
    sys.stdout.write(z + "\n")


d = laden.viertelstunden()
h = laden.stunden()

sag("# Neuberechnung mit der zweiten Iteration")
sag()
sag("Eigene Auswertung vom 23.09.2026. Reservierungspreis aus")
sag("`be_full_pos` und `be_full_neg`, also der zweiten Iteration.")
sag()
sag("## 0 Gegenprobe gegen ERGEBNISSE Abschnitt 7.1")
sag()
sag("| Richtung | Median | Mittel | Maximum |")
sag("|---|---|---|---|")
for name, s in (("Entladen", "res_ent"), ("Laden", "res_lad")):
    sag("| %s | %.2f | %.2f | %.2f |"
        % (name, h[s].median(), h[s].mean(), h[s].max()))
sag()
sag("ERGEBNISSE nennt 12,22 / 23,64 / 1008,00 und 9,85 / 24,33 / 510,48.")
sag()

# ----------------------------------------------------------------------
sag("## 1 Struktur der teuren Stunden, fuer Abschnitt 4.4")
sag()
for name, s in (("Entladereservierung", "res_ent"),
                ("Ladereservierung", "res_lad")):
    schwelle = h[s].quantile(0.90)
    teuer = h[h[s] > schwelle]
    je_stunde = teuer.groupby("stunde").size().sort_values(ascending=False)
    sag("**%s**, 90-Prozent-Quantil %.1f Euro je Megawatt und Stunde"
        % (name, schwelle))
    sag()
    sag("| Groesse | Wert |")
    sag("|---|---|")
    sag("| teure Stunden | %d |" % len(teuer))
    sag("| Kalendertage | %d |" % teuer["day"].nunique())
    sag("| Stunden je betroffenem Tag | %.1f |"
        % (len(teuer) / teuer["day"].nunique()))
    sag("| Anteil in den sechs staerksten Tagesstunden | %.0f Prozent |"
        % (je_stunde.head(6).sum() / len(teuer) * 100))
    sag("| diese Tagesstunden | %s |"
        % ", ".join("%d" % x for x in sorted(je_stunde.head(6).index)))
    sag("| Anteil Maerz bis Oktober | %.0f Prozent |"
        % (teuer["monat"].between(3, 10).mean() * 100))
    sag()

# ----------------------------------------------------------------------
sag("## 2 Woran der Preis haengt, fuer Abschnitt 4.1")
sag()
lad = d[d["stunde"].isin(MITTAG)].groupby("day").agg(
    preis=("res_lad", "mean"), afrr=("afrr_cap_neg", "mean"),
    idc=("preis_idc", "mean"))
ent = d[d["stunde"].isin(ABEND)].groupby("day").agg(
    preis=("res_ent", "mean"), afrr=("afrr_cap_pos", "mean"),
    idc=("preis_idc", "mean"))
sag("| Fenster | Rangkorrelation mit dem aFRR-Leistungspreis |")
sag("|---|---|")
sag("| Ladereservierung 10 bis 15 Uhr | %+.2f |"
    % lad["preis"].corr(lad["afrr"], method="spearman"))
sag("| Entladereservierung 17 bis 20 Uhr | %+.2f |"
    % ent["preis"].corr(ent["afrr"], method="spearman"))
sag()
sag("Mittlerer aFRR-Leistungspreis der Mittagsstunden im Mai %.1f gegen %.1f"
    % (lad.loc["2025-05-01":"2025-05-31", "afrr"].mean(), lad["afrr"].mean()))
sag("im Jahresmittel derselben Stunden, also das %.1f-Fache."
    % (lad.loc["2025-05-01":"2025-05-31", "afrr"].mean() / lad["afrr"].mean()))
sag()

# ----------------------------------------------------------------------
sag("## 3 Tages- und Jahresgang der Summe")
sag()
tag = h.groupby("stunde")["summe"].median()
mon = h.groupby("monat")["summe"].median()
sag("| Groesse | Wert |")
sag("|---|---|")
sag("| Median der Summe, groesste Tagesstunde | %.1f um %d Uhr |"
    % (tag.max(), tag.idxmax()))
sag("| Median der Summe, kleinste Tagesstunde | %.1f um %d Uhr |"
    % (tag.min(), tag.idxmin()))
sag("| Verhaeltnis ueber den Tag | %.2f |" % (tag.max() / tag.min()))
sag("| Median der Summe, groesster Monat | %.1f im Monat %d |"
    % (mon.max(), mon.idxmax()))
sag("| Median der Summe, kleinster Monat | %.1f im Monat %d |"
    % (mon.min(), mon.idxmin()))
sag("| Verhaeltnis ueber das Jahr | %.2f |" % (mon.max() / mon.min()))
sag()
sag("Verhaeltnis der beiden Richtungen je Tagesstunde, Median:")
sag()
mt = h.groupby("stunde")[["res_ent", "res_lad"]].median()
sag("| Stunde | entladen | ladend | Verhaeltnis |")
sag("|---|---|---|---|")
for s in (7, 13, 14, 19):
    z = mt.loc[s]
    gr, kl = max(z["res_ent"], z["res_lad"]), min(z["res_ent"], z["res_lad"])
    sag("| %02d | %.1f | %.1f | %.1f-fach |" % (s, z["res_ent"], z["res_lad"],
                                                gr / kl if kl else float("nan")))
sag()

ZIEL = os.path.join(HIER, "BEFUND_NEUBERECHNUNG.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
