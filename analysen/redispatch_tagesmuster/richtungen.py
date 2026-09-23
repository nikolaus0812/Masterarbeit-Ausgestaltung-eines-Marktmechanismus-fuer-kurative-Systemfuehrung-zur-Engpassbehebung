# -*- coding: utf-8 -*-
"""Tagesmuster des Redispatch je Richtung, 23.09.2026.

Die beiden Richtungen des Redispatch entsprechen den beiden Richtungen
der kurativen Reservierung. Soll die Einspeisung **reduziert** werden, so
kann ein Speicher statt einer Abregelung laden; das ist die
Ladereservierung. Soll sie **erhoeht** werden, so kann er entladen; das
ist die Entladereservierung.

Geprueft wird, ob der Bedarf je Richtung zu derselben Tageszeit auftritt
wie der hohe Preis derselben Richtung.

Eigene Auswertung der Schriftfassung vom 23.09.2026, nur lesend.
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

rd = pd.DataFrame({"zeit": raster, "reduzieren": runter, "erhoehen": hoch})
rd["stunde"] = rd["zeit"].dt.hour
rd_tag = rd.groupby("stunde")[["reduzieren", "erhoehen"]].mean()

h = laden.stunden()
p_tag = h.groupby("stunde")[["res_ent", "res_lad"]].median()

sag("# Tagesmuster des Redispatch je Richtung")
sag()
sag("Eigene Auswertung vom 23.09.2026 aus 19.369 Einzelmassnahmen von")
sag("netztransparenz.net. Jede Massnahme ist mit ihrer mittleren Leistung")
sag("anteilig auf die beruehrten Stunden verteilt. Der Reservierungspreis")
sag("ist der Median der zweiten Iteration.")
sag()
sag("**Die Zuordnung der Richtungen.** Soll die Einspeisung reduziert werden,")
sag("so kann ein Speicher statt einer Abregelung laden; das entspricht der")
sag("Ladereservierung. Soll sie erhoeht werden, so kann er entladen; das")
sag("entspricht der Entladereservierung.")
sag()
sag("| Stunde | Redispatch reduzieren | Ladereservierung | Redispatch erhoehen | Entladereservierung |")
sag("|---|---|---|---|---|")
for x in range(24):
    sag("| %02d | %.0f | %.1f | %.0f | %.1f |"
        % (x, rd_tag.loc[x, "reduzieren"], p_tag.loc[x, "res_lad"],
           rd_tag.loc[x, "erhoehen"], p_tag.loc[x, "res_ent"]))
sag()

sag("## 1 Wann der Bedarf am groessten ist")
sag()
sag("| Richtung | Maximum | Minimum | Verhaeltnis |")
sag("|---|---|---|---|")
for name, s in (("Reduzieren", "reduzieren"), ("Erhoehen", "erhoehen")):
    z = rd_tag[s]
    sag("| %s | %.0f MW um %d Uhr | %.0f MW um %d Uhr | %.2f |"
        % (name, z.max(), z.idxmax(), z.min(), z.idxmin(), z.max() / z.min()))
g = rd_tag["reduzieren"] + rd_tag["erhoehen"]
sag("| beide zusammen | %.0f MW um %d Uhr | %.0f MW um %d Uhr | %.2f |"
    % (g.max(), g.idxmax(), g.min(), g.idxmin(), g.max() / g.min()))
sag()

sag("## 2 Faellt der Bedarf mit dem hohen Preis zusammen?")
sag()
sag("| Paarung | Rangkorrelation ueber die 24 Tagesstunden |")
sag("|---|---|")
sag("| Reduzieren gegen Ladereservierung | %+.2f |"
    % rd_tag["reduzieren"].corr(p_tag["res_lad"], method="spearman"))
sag("| Erhoehen gegen Entladereservierung | %+.2f |"
    % rd_tag["erhoehen"].corr(p_tag["res_ent"], method="spearman"))
sag("| Reduzieren gegen Entladereservierung | %+.2f |"
    % rd_tag["reduzieren"].corr(p_tag["res_ent"], method="spearman"))
sag("| Erhoehen gegen Ladereservierung | %+.2f |"
    % rd_tag["erhoehen"].corr(p_tag["res_lad"], method="spearman"))
sag()

sag("## 3 Die sechs teuersten Stunden je Richtung")
sag()
for name, ps, rs in (("Ladereservierung", "res_lad", "reduzieren"),
                     ("Entladereservierung", "res_ent", "erhoehen")):
    teuer = p_tag[ps].nlargest(6).index.sort_values()
    anteil = rd_tag.loc[teuer, rs].sum() / rd_tag[rs].sum() * 100
    sag("**%s**, teuerste Stunden %s."
        % (name, ", ".join("%d" % x for x in teuer)))
    sag()
    sag("In diesen sechs Stunden faellt %.0f Prozent des Bedarfs der Richtung"
        % anteil)
    sag("an, gegenueber 25 Prozent bei gleichmaessiger Verteilung.")
    sag()

ZIEL = os.path.join(HIER, "BEFUND_RICHTUNGEN.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
