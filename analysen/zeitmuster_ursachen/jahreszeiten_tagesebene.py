# -*- coding: utf-8 -*-
"""Jahreszeiten auf der Ebene, die Abbildung 4.6 zeigt, 23.09.2026.

Vorgabe des Verfassers: so nah wie moeglich an der Abbildung bleiben,
damit der Leser die Zahlen nachvollziehen kann. Abbildung 4.6 traegt je
Tag das **arithmetische Mittel** des kurativen Reservierungspreises und
die Redispatchleistung im Tagesmittel. Beide Groessen werden deshalb
hier je Jahreszeit zusammengefasst.
"""
import io
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import laden

HIER = os.path.dirname(os.path.abspath(__file__))
REDISPATCH = (r"C:\GIT-HUB\bess_dispatch_optimization\data\processed"
              "\\Redispatch_netztransparnez.net\\2025_Redispatchma\u00dfnahmen.parquet")
JAHRESZEITEN = [("Winter", [12, 1, 2]), ("Fr\u00fchjahr", [3, 4, 5]),
                ("Sommer", [6, 7, 8]), ("Herbst", [9, 10, 11])]
LINIE = 101.0

bericht = []


def sag(z=""):
    bericht.append(z)
    sys.stdout.write(z + "\n")


# ----------------------------------------------------------------- Preis
h = laden.stunden()
tag = h.groupby("day").agg(ent=("res_ent", "mean"), lad=("res_lad", "mean"))
tag["monat"] = tag.index.month

# ------------------------------------------------------------ Redispatch
d = pd.read_parquet(REDISPATCH)


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
rd = pd.DataFrame({"zeit": raster, "runter": runter, "hoch": hoch})
rd["day"] = rd["zeit"].dt.normalize()
rd_tag = rd.groupby("day")[["runter", "hoch"]].mean()
rd_tag["monat"] = rd_tag.index.month

sag("# Jahreszeiten auf der Ebene der Abbildung 4.6")
sag()
sag("Eigene Auswertung vom 23.09.2026. Abbildung 4.6 traegt je Tag das")
sag("arithmetische Mittel des Reservierungspreises und die")
sag("Redispatchleistung im Tagesmittel. Beide sind hier je Jahreszeit")
sag("zusammengefasst, damit der Text die Abbildung nachvollziehbar macht.")
sag()
sag("| Jahreszeit | Tagesmittel entladen | Tagesmittel ladend | "
    "Redispatch herauf | Redispatch herunter |")
sag("|---|---|---|---|---|")
werte = {}
for name, monate in JAHRESZEITEN:
    p = tag[tag["monat"].isin(monate)]
    r = rd_tag[rd_tag["monat"].isin(monate)]
    werte[name] = (p["ent"].median(), p["lad"].median(),
                   r["hoch"].mean(), r["runter"].mean())
    sag("| %s | %.1f | %.1f | %.0f | %.0f |" % ((name,) + werte[name]))
sag()
sag("Ausgewiesen ist je Jahreszeit der Median der Tagesmittel und die")
sag("mittlere Redispatchleistung.")
sag()

sag("## Verhaeltnisse, fuer den Text")
sag()
w = werte["Winter"]
sag("| Jahreszeit | Entladereservierung gegen Winter | Ladereservierung gegen Winter | Redispatch herauf gegen Winter |")
sag("|---|---|---|---|")
for name, _ in JAHRESZEITEN:
    z = werte[name]
    sag("| %s | %+.0f Prozent | %+.0f Prozent | %+.0f Prozent |"
        % (name, (z[0] / w[0] - 1) * 100, (z[1] / w[1] - 1) * 100,
           (z[2] / w[2] - 1) * 100))
sag()

sag("## Wie oft das Tagesmittel unter der Bezugslinie bleibt")
sag()
sag("| Jahreszeit | entladend | ladend |")
sag("|---|---|---|")
for name, monate in JAHRESZEITEN:
    p = tag[tag["monat"].isin(monate)]
    sag("| %s | %d von %d | %d von %d |"
        % (name, int((p["ent"] < LINIE).sum()), len(p),
           int((p["lad"] < LINIE).sum()), len(p)))
sag("| **ganzes Jahr** | %d von %d | %d von %d |"
    % (int((tag["ent"] < LINIE).sum()), len(tag),
       int((tag["lad"] < LINIE).sum()), len(tag)))
sag()
sag("Die Bezugslinie betraegt %.0f Euro je bewegter Megawattstunde." % LINIE)
sag()

ZIEL = os.path.join(HIER, "BEFUND_JAHRESZEITEN_TAG.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
