# -*- coding: utf-8 -*-
"""Berichtigung fuer die Entladerichtung: die Arbitrage ist eine Spanne.

`fuehrender_markt.py` setzt fuer den Energiemarkt den Preis der Stunde
selbst an. Das ueberschaetzt die Entladerichtung, denn wer entladen will,
muss die Energie vorher kaufen. Der Wert einer Entladestunde ist die
Spanne zwischen ihrem Preis und dem guenstigsten Bezug desselben Tages.

Fuer die Laderichtung besteht das Problem nicht, denn eine Ladung zu
einem negativen Preis bringt unmittelbar Geld ein.

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
PMAX = 100.0
ABEND = range(17, 21)

d = pd.read_parquet(QUELLE)
d = d[~d["gesperrt"]].copy()
d["day"] = pd.to_datetime(d["day"])
d["monat"] = d["day"].dt.month

# Guenstigster Bezug des Tages, ueber beide Energiemaerkte.
tagesmin = d.groupby("day")[["preis_da", "preis_idc"]].min().min(axis=1)
d["tagesmin"] = d["day"].map(tagesmin)

d["ent_afrr"] = d["afrr_cap_pos"]
d["ent_spanne"] = (d[["preis_da", "preis_idc"]].max(axis=1)
                   - d["tagesmin"]).clip(lower=0.0)
d["ent_ene"] = (d["afrr_ene_preis_pos"].fillna(0.0)
                * d["afrr_ene_pos_mw"].fillna(0.0) / PMAX)

KAND = {"aFRR-Leistung": "ent_afrr", "Arbitragespanne": "ent_spanne",
        "aFRR-Arbeit": "ent_ene"}

teil = d[d["stunde"].isin(ABEND)].copy()
werte = teil[list(KAND.values())]
namen = list(KAND.keys())
teil["fuehrend"] = [namen[i] for i in werte.values.argmax(axis=1)]
teil["opp"] = werte.max(axis=1)

bericht = []


def sag(z=""):
    bericht.append(z)
    sys.stdout.write(z + "\n")


sag("# Entladereservierung, Energiemarkt als Spanne gerechnet")
sag()
sag("Der Wert einer Entladestunde ist die Spanne zwischen ihrem Preis und")
sag("dem guenstigsten Bezug desselben Tages, nicht der Preis selbst.")
sag("Betrachtet sind die Viertelstunden von 17 bis 20 Uhr.")
sag()
sag("| Markt | Anteil der Viertelstunden | mittlere Opportunitaet |")
sag("|---|---|---|")
for name in KAND:
    m = teil["fuehrend"] == name
    sag("| %s | %.0f %% | %.1f |"
        % (name, m.mean() * 100, teil.loc[m, "opp"].mean() if m.any() else 0.0))
sag()
sag("Mittlere Opportunitaet %.1f, mittlerer Reservierungspreis %.1f Euro je"
    % (teil["opp"].mean(), teil["be_pos"].mean()))
sag("Megawatt und Stunde.")
sag()
sag("| Monat | " + " | ".join(KAND) + " | Opportunitaet | Reservierung |")
sag("|---" * (len(KAND) + 3) + "|")
for mo in range(1, 13):
    z = teil[teil["monat"] == mo]
    anteile = ["%.0f %%" % ((z["fuehrend"] == n).mean() * 100) for n in KAND]
    sag("| %02d | %s | %.1f | %.1f |"
        % (mo, " | ".join(anteile), z["opp"].mean(), z["be_pos"].mean()))
sag()

sag("## Was September und Oktober auszeichnet")
sag()
so = teil[teil["monat"].isin([9, 10])]
rest = teil[~teil["monat"].isin([9, 10])]
sag("| Groesse | September und Oktober | uebrige Monate | Faktor |")
sag("|---|---|---|---|")
for name, spalte in (("Reservierungspreis", "be_pos"),
                     ("aFRR-Leistungspreis", "ent_afrr"),
                     ("Arbitragespanne", "ent_spanne"),
                     ("Opportunitaet insgesamt", "opp")):
    a, b = so[spalte].mean(), rest[spalte].mean()
    sag("| %s | %.1f | %.1f | %.2f |" % (name, a, b, a / b if b else float("nan")))
sag()

ZIEL = os.path.join(HIER, "BEFUND_ENTLADEN_SPANNE.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
