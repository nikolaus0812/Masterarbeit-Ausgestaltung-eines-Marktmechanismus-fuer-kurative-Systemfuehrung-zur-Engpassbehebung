# -*- coding: utf-8 -*-
"""Redispatchprofil gegen den kurativen Reservierungspreis, 23.09.2026.

Das Stundenprofil des Redispatch stammt aus `tagesmuster.py` und ist von
der Spaltenverwechslung nicht betroffen, denn es nutzt keine Preisdaten.
Der Vergleich wird hier mit der **zweiten** Iteration neu gerechnet,
also mit `be_full_pos` und `be_full_neg`.
"""
import io
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "zeitmuster_ursachen"))
import laden

QUELLE = (r"C:\GIT-HUB\bess_dispatch_optimization\data\processed"
          "\\Redispatch_netztransparnez.net\\2025_Redispatchma\u00dfnahmen.parquet")
HIER = os.path.dirname(os.path.abspath(__file__))

bericht = []


def sag(z=""):
    bericht.append(z)
    sys.stdout.write(z + "\n")


# ----------------------------------------------------------------------
d = pd.read_parquet(QUELLE)


def zahl(s):
    return pd.to_numeric(s.astype(str).str.replace(".", "", regex=False)
                         .str.replace(",", ".", regex=False), errors="coerce")


d["leistung"] = zahl(d["MITTLERE_LEISTUNG_MW"])
d["von"] = pd.to_datetime(d["BEGINN_DATUM"] + " " + d["BEGINN_UHRZEIT"],
                          format="%d.%m.%Y %H:%M", errors="coerce")
d["bis"] = pd.to_datetime(d["ENDE_DATUM"] + " " + d["ENDE_UHRZEIT"],
                          format="%d.%m.%Y %H:%M", errors="coerce")
gut = d[d["von"].notna() & d["bis"].notna() & d["leistung"].notna()
        & (d["bis"] > d["von"])]

raster = pd.date_range("2025-01-01", "2026-01-01", freq="h", inclusive="left")
index = {t: i for i, t in enumerate(raster)}
runter = np.zeros(len(raster))
hoch = np.zeros(len(raster))
for _, z in gut.iterrows():
    t = z["von"].floor("h")
    while t < z["bis"]:
        i = index.get(t)
        if i is not None:
            a = max(z["von"], t)
            e = min(z["bis"], t + pd.Timedelta(hours=1))
            anteil = (e - a).total_seconds() / 3600.0
            if "reduzieren" in str(z["RICHTUNG"]).lower():
                runter[i] += z["leistung"] * anteil
            else:
                hoch[i] += z["leistung"] * anteil
        t += pd.Timedelta(hours=1)

rd = pd.DataFrame({"zeit": raster, "gesamt": runter + hoch})
rd["stunde"] = rd["zeit"].dt.hour
rd["monat"] = rd["zeit"].dt.month
rd_tag = rd.groupby("stunde")["gesamt"].mean()
rd_mon = rd.groupby("monat")["gesamt"].mean()

# ----------------------------------------------------------------------
h = laden.stunden()
p_tag = h.groupby("stunde")["summe"].median()
p_mon = h.groupby("monat")["summe"].median()

sag("# Redispatchbedarf gegen den kurativen Reservierungspreis")
sag()
sag("Eigene Auswertung vom 23.09.2026. Der Redispatch stammt aus den")
sag("Einzelmassnahmen von netztransparenz.net, der Reservierungspreis aus")
sag("der zweiten Iteration. Verglichen wird der Median der Summe beider")
sag("Richtungen mit der mittleren Redispatchleistung.")
sag()
sag("## 1 Wie stark beide ueber den Tag und ueber das Jahr schwanken")
sag()
sag("| | Redispatch | Reservierungspreis |")
sag("|---|---|---|")
sag("| groesste zu kleinster Tagesstunde | %.2f | %.2f |"
    % (rd_tag.max() / rd_tag.min(), p_tag.max() / p_tag.min()))
sag("| groesster zu kleinstem Monat | %.2f | %.2f |"
    % (rd_mon.max() / rd_mon.min(), p_mon.max() / p_mon.min()))
sag()
sag("Der Redispatch schwankt ueber den Tag also kaum, der Preis dagegen")
sag("um ein Vielfaches. Ueber das Jahr schwanken beide aehnlich stark.")
sag()
sag("## 2 Laufen sie gleich oder gegenlaeufig?")
sag()
sag("| Ebene | Rangkorrelation |")
sag("|---|---|")
sag("| ueber die 24 Tagesstunden | %+.2f |"
    % rd_tag.corr(p_tag, method="spearman"))
sag("| ueber die zwoelf Monate | %+.2f |"
    % rd_mon.corr(p_mon, method="spearman"))
sag()
sag("## 3 Die Monate im Einzelnen")
sag()
sag("| Monat | Redispatch in MW | Preis in Euro je MW und h |")
sag("|---|---|---|")
for m in range(1, 13):
    sag("| %02d | %.0f | %.1f |" % (m, rd_mon.loc[m], p_mon.loc[m]))
sag()
w = [11, 12, 1, 2]
s = [5, 6, 7, 8]
sag("Winter von November bis Februar: Redispatch %.0f MW, Preis %.1f."
    % (rd_mon.loc[w].mean(), p_mon.loc[w].mean()))
sag("Sommer von Mai bis August: Redispatch %.0f MW, Preis %.1f."
    % (rd_mon.loc[s].mean(), p_mon.loc[s].mean()))
sag()
sag("## 4 Die Tagesstunden im Einzelnen")
sag()
sag("| Stunde | Redispatch in MW | Preis in Euro je MW und h |")
sag("|---|---|---|")
for x in range(24):
    sag("| %02d | %.0f | %.1f |" % (x, rd_tag.loc[x], p_tag.loc[x]))
sag()

ZIEL = os.path.join(HIER, "BEFUND_VERGLEICH.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
