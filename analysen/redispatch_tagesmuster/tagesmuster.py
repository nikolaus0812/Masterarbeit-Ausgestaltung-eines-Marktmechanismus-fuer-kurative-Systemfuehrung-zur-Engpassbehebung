# -*- coding: utf-8 -*-
"""Hat der Redispatch ein Tagesmuster?

Abschnitt 4.5 haelt den kurativen Reservierungspreis gegen den
Engpassmanagementbedarf. Der Preis hat ein ausgepraegtes Tagesmuster. Ob
der Redispatch eines hat, war bisher offen, weil die zitierte Mitteilung
der Bundesnetzagentur nur Jahressummen fuehrt.

`2025_Redispatchmassnahmen.parquet` von netztransparenz.net fuehrt jede
einzelne Massnahme des Jahres 2025 mit Beginn, Ende, Richtung und
mittlerer Leistung. Daraus laesst sich ein Stundenprofil bilden.

Verfahren: jede Massnahme wird mit ihrer mittleren Leistung auf die
Stunden verteilt, die sie beruehrt, anteilig nach der Ueberlappung. Die
Zeiten stehen in lokaler Zeit und damit in derselben Zeitrechnung wie die
Reservierungspreise.

Eigene Auswertung der Schriftfassung vom 23.09.2026, nur lesend.
"""
import io
import os
import sys

import numpy as np
import pandas as pd

QUELLE = (r"C:\GIT-HUB\bess_dispatch_optimization\data\processed"
          "\\Redispatch_netztransparnez.net\\2025_Redispatchma\u00dfnahmen.parquet")
PREISE = (r"C:\GIT-HUB\bess_dispatch_optimization\analysen\03_breakeven"
          r"\heatmaps\jahr_slots_2025.parquet")
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
d["arbeit"] = zahl(d["GESAMTE_ARBEIT_MWH"])
d["von"] = pd.to_datetime(d["BEGINN_DATUM"] + " " + d["BEGINN_UHRZEIT"],
                          format="%d.%m.%Y %H:%M", errors="coerce")
d["bis"] = pd.to_datetime(d["ENDE_DATUM"] + " " + d["ENDE_UHRZEIT"],
                          format="%d.%m.%Y %H:%M", errors="coerce")

sag("# Tagesmuster des Redispatch 2025")
sag()
sag("Eigene Auswertung vom 23.09.2026 aus den Einzelmassnahmen von")
sag("netztransparenz.net. Jede Massnahme ist mit ihrer mittleren Leistung")
sag("anteilig auf die beruehrten Stunden verteilt.")
sag()
sag("## 1 Die Grundgesamtheit")
sag()
sag("| Groesse | Wert |")
sag("|---|---|")
sag("| Massnahmen insgesamt | %d |" % len(d))
sag("| davon mit vollstaendigem Zeitstempel | %d |"
    % int((d["von"].notna() & d["bis"].notna()).sum()))
sag("| davon mit Leistungsangabe | %d |" % int(d["leistung"].notna().sum()))
sag()
sag("Gruende der Massnahme:")
sag()
sag("| Grund | Anzahl | Anteil |")
sag("|---|---|---|")
for grund, n in d["GRUND_DER_MASSNAHME"].value_counts().items():
    sag("| %s | %d | %.1f Prozent |" % (grund, n, n / len(d) * 100))
sag()
sag("Richtungen:")
sag()
sag("| Richtung | Anzahl |")
sag("|---|---|")
for r, n in d["RICHTUNG"].value_counts().items():
    sag("| %s | %d |" % (r, n))
sag()

gut = d[d["von"].notna() & d["bis"].notna() & d["leistung"].notna()
        & (d["bis"] > d["von"])].copy()
sag("Ausgewertet werden die %d Massnahmen mit vollstaendigen Angaben und"
    % len(gut))
sag("positiver Dauer, also %.1f Prozent aller Eintraege."
    % (len(gut) / len(d) * 100))
sag()

# ----------------------------------------------------------------------
# Stundenraster aufbauen
# ----------------------------------------------------------------------
raster = pd.date_range("2025-01-01", "2026-01-01", freq="h", inclusive="left")
index = {t: i for i, t in enumerate(raster)}
runter = np.zeros(len(raster))
hoch = np.zeros(len(raster))

for _, z in gut.iterrows():
    von, bis, p = z["von"], z["bis"], z["leistung"]
    if bis <= raster[0] or von >= raster[-1] + pd.Timedelta(hours=1):
        continue
    t = von.floor("h")
    while t < bis:
        i = index.get(t)
        if i is not None:
            anfang = max(von, t)
            ende = min(bis, t + pd.Timedelta(hours=1))
            anteil = (ende - anfang).total_seconds() / 3600.0
            if "reduzieren" in str(z["RICHTUNG"]).lower():
                runter[i] += p * anteil
            else:
                hoch[i] += p * anteil
        t += pd.Timedelta(hours=1)

prof = pd.DataFrame({"zeit": raster, "runter": runter, "hoch": hoch})
prof["gesamt"] = prof["runter"] + prof["hoch"]
prof["stunde"] = prof["zeit"].dt.hour
prof["monat"] = prof["zeit"].dt.month

# ----------------------------------------------------------------------
sag("## 2 Tagesgang")
sag()
sag("Mittlere Leistung je Tagesstunde ueber das ganze Jahr, in MW.")
sag()
sag("| Stunde | herunter | herauf | gesamt |")
sag("|---|---|---|---|")
tag = prof.groupby("stunde")[["runter", "hoch", "gesamt"]].mean()
for h in range(24):
    sag("| %02d | %.0f | %.0f | %.0f |"
        % (h, tag.loc[h, "runter"], tag.loc[h, "hoch"], tag.loc[h, "gesamt"]))
sag()
sag("Groesste Stunde %.0f MW um %d Uhr, kleinste %.0f MW um %d Uhr, also"
    % (tag["gesamt"].max(), tag["gesamt"].idxmax(),
       tag["gesamt"].min(), tag["gesamt"].idxmin()))
sag("ein Verhaeltnis von %.2f." % (tag["gesamt"].max() / tag["gesamt"].min()))
sag()

sag("## 3 Jahresgang")
sag()
sag("| Monat | herunter | herauf | gesamt |")
sag("|---|---|---|---|")
mon = prof.groupby("monat")[["runter", "hoch", "gesamt"]].mean()
for m in range(1, 13):
    sag("| %02d | %.0f | %.0f | %.0f |"
        % (m, mon.loc[m, "runter"], mon.loc[m, "hoch"], mon.loc[m, "gesamt"]))
sag()
sag("Groesster Monat %.0f MW im Monat %d, kleinster %.0f MW im Monat %d, also"
    % (mon["gesamt"].max(), mon["gesamt"].idxmax(),
       mon["gesamt"].min(), mon["gesamt"].idxmin()))
sag("ein Verhaeltnis von %.2f." % (mon["gesamt"].max() / mon["gesamt"].min()))
sag()

# ----------------------------------------------------------------------
sag("## 4 Vergleich mit dem kurativen Reservierungspreis")
sag()
p = pd.read_parquet(PREISE)
p = p[~p["gesperrt"]].copy()
p["day"] = pd.to_datetime(p["day"])
ps = p.groupby(["day", "stunde"])[["be_pos", "be_neg"]].first().reset_index()
ps["summe"] = ps["be_pos"] + ps["be_neg"]
preis_tag = ps.groupby("stunde")["summe"].median()
preis_monat = ps.groupby(ps["day"].dt.month)["summe"].median()

sag("| | Redispatch | Reservierungspreis, Median der Summe |")
sag("|---|---|---|")
sag("| Verhaeltnis groesste zu kleinster Tagesstunde | %.2f | %.2f |"
    % (tag["gesamt"].max() / tag["gesamt"].min(),
       preis_tag.max() / preis_tag.min()))
sag("| Verhaeltnis groesster zu kleinstem Monat | %.2f | %.2f |"
    % (mon["gesamt"].max() / mon["gesamt"].min(),
       preis_monat.max() / preis_monat.min()))
sag()
sag("Rangkorrelation ueber die 24 Tagesstunden: %+.2f."
    % tag["gesamt"].corr(preis_tag, method="spearman"))
sag("Rangkorrelation ueber die zwoelf Monate: %+.2f."
    % mon["gesamt"].corr(preis_monat, method="spearman"))
sag()

ZIEL = os.path.join(HIER, "BEFUND.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
