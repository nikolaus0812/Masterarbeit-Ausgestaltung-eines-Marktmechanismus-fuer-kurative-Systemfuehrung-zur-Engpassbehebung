# -*- coding: utf-8 -*-
"""Woran liegen die teuren Perioden im Zeitmuster des Jahres 2025.

Eigene Auswertung der Schriftfassung vom 23.09.2026. Anlass ist die
Beobachtung des Verfassers, dass die Ladereservierung mittags Anfang und
Ende April, Anfang und Mitte Mai sowie Ende Juni teuer wird und die
Entladereservierung im September und Oktober.

Quelle ist `jahr_slots_2025.parquet` aus dem Analyse-Repository, das je
Viertelstunde den kurativen Reservierungspreis beider Richtungen, die im
Referenzfall belegte Leistung je Markt und die Marktpreise fuehrt. Es
wird ausschliesslich gelesen, nichts dorthin geschrieben.

Aufruf mit dem Interpreter des Modellrepositorys:
    C:/ProgramData/anaconda3/envs/venv_mode/python.exe ursachen.py
"""
import io
import os
import sys

import numpy as np
import pandas as pd

QUELLE = (r"C:\GIT-HUB\bess_dispatch_optimization\analysen\03_breakeven"
          r"\heatmaps\jahr_slots_2025.parquet")
HIER = os.path.dirname(os.path.abspath(__file__))

# Fenster, in denen die jeweilige Richtung teuer ist. Aus dem Tagesgang
# nach ERGEBNISSE Abschnitt 7.2: Laden mittags, Entladen abends.
MITTAG = range(10, 16)      # 10 bis 15 Uhr
ABEND = range(17, 21)       # 17 bis 20 Uhr

d = pd.read_parquet(QUELLE)
d = d[~d["gesperrt"]].copy()
d["day"] = pd.to_datetime(d["day"])
d["monat"] = d["day"].dt.month

bericht = []


def sag(zeile=""):
    bericht.append(zeile)
    sys.stdout.write(zeile + "\n")


sag("# Ursachen der teuren Perioden im Zeitmuster 2025")
sag()
sag("Eigene Auswertung vom 23.09.2026, Quelle `jahr_slots_2025.parquet`.")
sag("Preise der Reservierung in Euro je Megawatt und Stunde, Marktpreise")
sag("des Day-Ahead und des Intraday in Euro je Megawattstunde, der")
sag("aFRR-Leistungspreis in Euro je Megawatt und Stunde.")
sag()

# ----------------------------------------------------------------------
# 1 Tageswerte je Richtung im jeweiligen Fenster
# ----------------------------------------------------------------------
lad = d[d["stunde"].isin(MITTAG)].groupby("day").agg(
    preis=("be_neg", "mean"),
    afrr_cap=("afrr_cap_neg", "mean"),
    afrr_ene=("afrr_ene_preis_neg", "mean"),
    idc=("preis_idc", "mean"),
    idc_min=("preis_idc", "min"),
    da=("preis_da", "mean"),
    afrr_mw=("afrr_neg_mw", "mean"),
    idc_mw=("idc_lad_mw", "mean"),
    da_mw=("da_lad_mw", "mean"),
)
lad["neg_anteil"] = (d[d["stunde"].isin(MITTAG)]
                     .assign(neg=lambda x: x["preis_idc"] < 0)
                     .groupby("day")["neg"].mean() * 100)

ent = d[d["stunde"].isin(ABEND)].groupby("day").agg(
    preis=("be_pos", "mean"),
    afrr_cap=("afrr_cap_pos", "mean"),
    afrr_ene=("afrr_ene_preis_pos", "mean"),
    idc=("preis_idc", "mean"),
    idc_max=("preis_idc", "max"),
    da=("preis_da", "mean"),
    afrr_mw=("afrr_pos_mw", "mean"),
    idc_mw=("idc_ent_mw", "mean"),
    da_mw=("da_ent_mw", "mean"),
)

# ----------------------------------------------------------------------
# 2 Die vom Verfasser benannten Fenster gegen das uebrige Jahr
# ----------------------------------------------------------------------
FENSTER_LAD = [("Anfang April", "2025-04-01", "2025-04-10"),
               ("Ende April", "2025-04-21", "2025-04-30"),
               ("Anfang Mai", "2025-05-01", "2025-05-10"),
               ("Mitte Mai", "2025-05-11", "2025-05-20"),
               ("Ende Juni", "2025-06-21", "2025-06-30")]
FENSTER_ENT = [("September", "2025-09-01", "2025-09-30"),
               ("Oktober", "2025-10-01", "2025-10-31")]


def tabelle(rahmen, fenster, spalten, kopf):
    sag("## %s" % kopf)
    sag()
    sag("| Zeitraum | " + " | ".join(s[1] for s in spalten) + " |")
    sag("|---" * (len(spalten) + 1) + "|")
    for name, von, bis in fenster:
        teil = rahmen.loc[von:bis]
        werte = [("%.1f" % teil[s[0]].mean()) for s in spalten]
        sag("| %s | %s |" % (name, " | ".join(werte)))
    alle = rahmen
    werte = [("%.1f" % alle[s[0]].mean()) for s in spalten]
    sag("| **ganzes Jahr** | %s |" % " | ".join(werte))
    sag()


SPALTEN_LAD = [("preis", "Reservierung"), ("afrr_cap", "aFRR-Leistung"),
               ("idc", "IDC-Preis"), ("idc_min", "IDC-Minimum"),
               ("neg_anteil", "Anteil negativ in %"),
               ("afrr_mw", "aFRR MW"), ("idc_mw", "IDC MW")]
SPALTEN_ENT = [("preis", "Reservierung"), ("afrr_cap", "aFRR-Leistung"),
               ("idc", "IDC-Preis"), ("idc_max", "IDC-Maximum"),
               ("da", "DA-Preis"), ("afrr_mw", "aFRR MW"), ("idc_mw", "IDC MW")]

tabelle(lad, FENSTER_LAD, SPALTEN_LAD,
        "1 Ladereservierung mittags, 10 bis 15 Uhr")
tabelle(ent, FENSTER_ENT, SPALTEN_ENT,
        "2 Entladereservierung abends, 17 bis 20 Uhr")

# ----------------------------------------------------------------------
# 3 Was den Preis erklaert: Korrelation ueber alle Tage
# ----------------------------------------------------------------------
sag("## 3 Woran der Preis haengt, ueber alle 365 Tage")
sag()
sag("Rangkorrelation nach Spearman zwischen dem Reservierungspreis im")
sag("Fenster und den moeglichen Treibern.")
sag()
for kopf, rahmen, treiber in (
        ("Ladereservierung mittags", lad,
         ["afrr_cap", "afrr_ene", "idc", "idc_min", "neg_anteil", "da"]),
        ("Entladereservierung abends", ent,
         ["afrr_cap", "afrr_ene", "idc", "idc_max", "da"])):
    sag("**%s**" % kopf)
    sag()
    sag("| Treiber | Rangkorrelation |")
    sag("|---|---|")
    for t in treiber:
        r = rahmen["preis"].corr(rahmen[t], method="spearman")
        sag("| %s | %+.2f |" % (t, r))
    sag()

# ----------------------------------------------------------------------
# 4 Die zwanzig teuersten Tage je Richtung
# ----------------------------------------------------------------------
for kopf, rahmen, spalten in (
        ("4 Die 15 teuersten Mittage der Ladereservierung", lad,
         ["preis", "afrr_cap", "idc", "idc_min", "neg_anteil"]),
        ("5 Die 15 teuersten Abende der Entladereservierung", ent,
         ["preis", "afrr_cap", "idc", "idc_max", "da"])):
    sag("## %s" % kopf)
    sag()
    oben = rahmen.nlargest(15, "preis")
    sag("| Tag | " + " | ".join(spalten) + " |")
    sag("|---" * (len(spalten) + 1) + "|")
    for tag, z in oben.iterrows():
        sag("| %s | %s |" % (tag.strftime("%d.%m."),
                             " | ".join("%.1f" % z[s] for s in spalten)))
    sag()

# ----------------------------------------------------------------------
# 5 Monatsbild der Treiber
# ----------------------------------------------------------------------
sag("## 6 Monatsmittel der Treiber")
sag()
monat_lad = lad.groupby(lad.index.month).mean(numeric_only=True)
monat_ent = ent.groupby(ent.index.month).mean(numeric_only=True)
sag("| Monat | Lad-Res | aFRR neg | IDC mittags | neg. Anteil | "
    "Ent-Res | aFRR pos | IDC abends |")
sag("|---|---|---|---|---|---|---|---|")
for m in range(1, 13):
    sag("| %02d | %.1f | %.1f | %.1f | %.0f%% | %.1f | %.1f | %.1f |"
        % (m, monat_lad.loc[m, "preis"], monat_lad.loc[m, "afrr_cap"],
           monat_lad.loc[m, "idc"], monat_lad.loc[m, "neg_anteil"],
           monat_ent.loc[m, "preis"], monat_ent.loc[m, "afrr_cap"],
           monat_ent.loc[m, "idc"]))
sag()

ZIEL = os.path.join(HIER, "BEFUND.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
