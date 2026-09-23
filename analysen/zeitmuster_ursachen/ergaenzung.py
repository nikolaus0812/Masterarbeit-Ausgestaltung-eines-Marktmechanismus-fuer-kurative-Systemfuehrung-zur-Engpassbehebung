# -*- coding: utf-8 -*-
"""Ergaenzung zu ursachen.py: sind die Auffaelligkeiten Marktereignisse?

Geprueft wird, ob der hohe aFRR-Leistungspreis im September und Oktober
ein Ereignis des ganzen Tages ist oder eine Eigenschaft des betrachteten
Abendfensters, und wie sich der Juli vom uebrigen Sommer unterscheidet.
"""
import io
import os
import sys

import pandas as pd

QUELLE = (r"C:\GIT-HUB\bess_dispatch_optimization\analysen\03_breakeven"
          r"\heatmaps\jahr_slots_2025.parquet")
HIER = os.path.dirname(os.path.abspath(__file__))

d = pd.read_parquet(QUELLE)
d = d[~d["gesperrt"]].copy()
d["day"] = pd.to_datetime(d["day"])
d["monat"] = d["day"].dt.month

bericht = []


def sag(zeile=""):
    bericht.append(zeile)
    sys.stdout.write(zeile + "\n")


sag("# Ergaenzung: sind es Marktereignisse?")
sag()
sag("## 1 aFRR-Leistungspreis je Monat ueber alle Stunden")
sag()
sag("Die Vier-Stunden-Zeitscheiben der aFRR gelten fuer den ganzen Tag.")
sag("Wenn der Preis im September und Oktober auch ueber alle Stunden")
sag("erhoeht ist, ist es ein Ereignis des Regelleistungsmarktes und keine")
sag("Eigenschaft des Abendfensters.")
sag()
m = d.groupby("monat").agg(
    afrr_pos=("afrr_cap_pos", "mean"),
    afrr_neg=("afrr_cap_neg", "mean"),
    idc=("preis_idc", "mean"),
    da=("preis_da", "mean"),
)
m["neg_anteil"] = (d.assign(neg=lambda x: x["preis_idc"] < 0)
                   .groupby("monat")["neg"].mean() * 100)
sag("| Monat | aFRR pos | aFRR neg | IDC | DA | Anteil negativer "
    "Viertelstunden |")
sag("|---|---|---|---|---|---|")
for i in range(1, 13):
    sag("| %02d | %.1f | %.1f | %.1f | %.1f | %.0f%% |"
        % (i, m.loc[i, "afrr_pos"], m.loc[i, "afrr_neg"], m.loc[i, "idc"],
           m.loc[i, "da"], m.loc[i, "neg_anteil"]))
sag()
jahr = d["afrr_cap_pos"].mean()
sep_okt = d[d["monat"].isin([9, 10])]["afrr_cap_pos"].mean()
uebrig = d[~d["monat"].isin([9, 10])]["afrr_cap_pos"].mean()
sag("Der aFRR-Leistungspreis der positiven Richtung betraegt im September")
sag("und Oktober im Mittel %.1f gegen %.1f Euro je Megawatt und Stunde in"
    % (sep_okt, uebrig))
sag("den uebrigen zehn Monaten, also das %.1f-Fache." % (sep_okt / uebrig))
sag()

sag("## 2 Der Juli faellt aus dem Sommer heraus")
sag()
sag("| Groesse | Mai bis Juni | Juli | August |")
sag("|---|---|---|---|")
mj = d[d["monat"].isin([5, 6])]
ju = d[d["monat"] == 7]
au = d[d["monat"] == 8]
for name, spalte in (("aFRR-Leistungspreis negativ", "afrr_cap_neg"),
                     ("IDC-Preis", "preis_idc"),
                     ("DA-Preis", "preis_da")):
    sag("| %s | %.1f | %.1f | %.1f |"
        % (name, mj[spalte].mean(), ju[spalte].mean(), au[spalte].mean()))
for name, rahmen in (("Anteil negativer Viertelstunden in Prozent", None),):
    sag("| %s | %.0f | %.0f | %.0f |"
        % (name, (mj["preis_idc"] < 0).mean() * 100,
           (ju["preis_idc"] < 0).mean() * 100,
           (au["preis_idc"] < 0).mean() * 100))
sag()

sag("## 3 Der teuerste Abend des Jahres, der 08.09.2025")
sag()
tag = d[d["day"] == "2025-09-08"]
sag("| Stunde | Reservierung entladen | IDC-Preis | DA-Preis | "
    "aFRR-Leistungspreis | aFRR MW | IDC MW |")
sag("|---|---|---|---|---|---|---|")
for h in range(24):
    z = tag[tag["stunde"] == h]
    if z.empty:
        continue
    sag("| %02d | %.1f | %.1f | %.1f | %.1f | %.1f | %.1f |"
        % (h, z["be_pos"].mean(), z["preis_idc"].mean(), z["preis_da"].mean(),
           z["afrr_cap_pos"].mean(), z["afrr_pos_mw"].mean(),
           z["idc_ent_mw"].mean()))
sag()

ZIEL = os.path.join(HIER, "BEFUND_ERGAENZUNG.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
