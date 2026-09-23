# -*- coding: utf-8 -*-
"""Monate auf der Ebene, die Abbildung 4.6 zeigt, 23.09.2026.

Vorgabe des Verfassers: der Satz zum Jahresgang soll den guenstigsten
**Monat** nennen und nicht die Jahreszeit. Dieselbe Kenngroesse wie in
jahreszeiten_tagesebene.py, naemlich je Monat der Median der
Tagesmittel des Reservierungspreises und die mittlere
Redispatchleistung, damit die Zahlen der beiden Befunde
zusammenpassen.
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
NAME = ["", "Januar", "Februar", "M\u00e4rz", "April", "Mai", "Juni", "Juli",
        "August", "September", "Oktober", "November", "Dezember"]

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

# ----------------------------------------------------------------- Bericht
sag("# Monate auf der Ebene der Abbildung 4.6")
sag()
sag("Eigene Auswertung vom 23.09.2026, Erweiterung von")
sag("BEFUND_JAHRESZEITEN_TAG.md auf die Monate. Dieselbe Kenngroesse,")
sag("naemlich je Monat der Median der Tagesmittel und die mittlere")
sag("Redispatchleistung. Die Jahreszeitenwerte sind damit reproduzierbar.")
sag()
sag("| Monat | Tagesmittel entladen | Tagesmittel ladend | "
    "Redispatch herauf | Redispatch herunter |")
sag("|---|---|---|---|---|")
w = {}
for m in range(1, 13):
    p = tag[tag["monat"] == m]
    r = rd_tag[rd_tag["monat"] == m]
    w[m] = (p["ent"].median(), p["lad"].median(),
            r["hoch"].mean(), r["runter"].mean())
    sag("| %s | %.1f | %.1f | %.0f | %.0f |" % ((NAME[m],) + w[m]))
sag()

for spalte, titel in ((1, "Ladereservierung"), (0, "Entladereservierung")):
    kleinst = min(range(1, 13), key=lambda m: w[m][spalte])
    groesst = max(range(1, 13), key=lambda m: w[m][spalte])
    sag("**%s.** Am guenstigsten im %s mit %.1f, am teuersten im %s mit "
        "%.1f Euro je Megawatt und Stunde, das ist das %.2f-Fache."
        % (titel, NAME[kleinst], w[kleinst][spalte], NAME[groesst],
           w[groesst][spalte], w[groesst][spalte] / w[kleinst][spalte]))
    sag()
    sag("Verhaeltnis jedes Monats zum %s:" % NAME[kleinst])
    sag()
    sag("| Monat | Vielfaches | Prozent mehr |")
    sag("|---|---|---|")
    for m in range(1, 13):
        v = w[m][spalte] / w[kleinst][spalte]
        sag("| %s | %.2f | %+.0f |" % (NAME[m], v, (v - 1) * 100))
    sag()

kleinst = min(range(1, 13), key=lambda m: w[m][2])
groesst = max(range(1, 13), key=lambda m: w[m][2])
sag("**Redispatch herauf.** Am groessten im %s mit %.0f, am kleinsten im %s "
    "mit %.0f Megawatt im Tagesmittel, das ist das %.2f-Fache."
    % (NAME[groesst], w[groesst][2], NAME[kleinst], w[kleinst][2],
       w[groesst][2] / w[kleinst][2]))
sag()
sag("Verhaeltnis jedes Monats zum %s:" % NAME[groesst])
sag()
sag("| Monat | Anteil am %s | Prozent darunter |" % NAME[groesst])
sag("|---|---|---|")
for m in range(1, 13):
    v = w[m][2] / w[groesst][2]
    sag("| %s | %.2f | %+.0f |" % (NAME[m], v, (v - 1) * 100))
sag()

# ------------------------------------------------- redispatchreichste Tage
# Vorgabe des Verfassers: nicht das Mittel je Jahreszeit nennen, sondern
# wie viele der redispatchreichsten Tage in den Winter fallen. Die
# Abbildung stellt oben die Entladereservierung neben die Erhoehung der
# Einspeisung und unten die Ladereservierung neben die Reduzierung.
JAHRESZEITEN = [("Winter", [12, 1, 2]), ("Frühjahr", [3, 4, 5]),
                ("Sommer", [6, 7, 8]), ("Herbst", [9, 10, 11])]
sag("## Wie viele der redispatchreichsten Tage in welche Jahreszeit fallen")
sag()
for spalte, titel in (("hoch", "Erhöhung der Einspeisung, oberes Feld"),
                      ("runter", "Reduzierung der Einspeisung, unteres Feld"),
                      (None, "Summe beider Richtungen")):
    if spalte is None:
        reihe = rd_tag["hoch"] + rd_tag["runter"]
    else:
        reihe = rd_tag[spalte]
    sag("**%s.**" % titel)
    sag()
    sag("| Anzahl der Tage | " + " | ".join(n for n, _ in JAHRESZEITEN) + " |")
    sag("|---|---|---|---|---|")
    for k in (10, 20, 30, 50, 90):
        oben = reihe.sort_values(ascending=False).head(k)
        monate = oben.index.month
        zeile = []
        for _, mm in JAHRESZEITEN:
            zeile.append("%d" % int(np.isin(monate, mm).sum()))
        sag("| die %d groessten | %s |" % (k, " | ".join(zeile)))
    sag()
    sag("Groesster Tageswert %.0f am %s, kleinster %.0f am %s Megawatt."
        % (reihe.max(), reihe.idxmax().strftime("%d.%m."),
           reihe.min(), reihe.idxmin().strftime("%d.%m.")))
    sag()

ZIEL = os.path.join(HIER, "BEFUND_MONATE_TAG.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
