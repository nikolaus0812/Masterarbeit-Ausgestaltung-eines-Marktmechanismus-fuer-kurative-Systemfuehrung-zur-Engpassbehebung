# -*- coding: utf-8 -*-
"""Wie viel aFRR-Arbeit wird tatsaechlich abgerufen, 23.09.2026.

Vorgabe des Verfassers fuer Abschnitt 4.6.1: der Absatz soll die Annahme
der freien Lieferung einordnen und dazu die durchschnittliche Abrufmenge
nennen. Die Sensitivitaetsstufe "bis zum Abruf" laesst der Bezugsanlage
den vollen deutschlandweiten Abruf offen (optimizer.py, Zeile 312:
afrr_ene_qde_anteil = 1,0 bedeutet "sie bedient ihn allein"), die Stufe
"bis 100 MW" hebt auch diese Grenze auf. Ob das plausibel ist,
entscheidet sich an der Groesse des Abrufs.

Gelesen wird nur, geschrieben wird allein in dieses Verzeichnis.

Quellen im Analyse-Repository, beide unveraendert gelesen:
  Aktivierte aFRR betrieblich [2026-06-11 12-02-31].parquet
      netztransparenz.net, viertelstuendlich, MW je Regelzone und
      Deutschland, beide Richtungen, ab 2020. Eintrag
      netztransparenz_regelenergie_2026.
  RESULT_OVERVIEW_CAPACITY_MARKET_aFRR_2025-01-01_2025-12-31.parquet
      regelleistung.net, je Vierstundenprodukt die bezuschlagte
      Leistung GERMANY_ALLOCATED_VOLUME_[MW]. Eintrag
      regelleistung_ausschreibungsdaten_2026.
"""
import io
import os
import sys

import pandas as pd

HIER = os.path.dirname(os.path.abspath(__file__))
BASIS = r"C:\GIT-HUB\bess_dispatch_optimization\data\processed"
AKTIV = os.path.join(BASIS, "SRA_Zuschlag_netztransparenz.net",
                     "Aktivierte aFRR betrieblich "
                     "[2026-06-11 12-02-31].parquet")
LEIST = os.path.join(BASIS, "Regelleistung_regelleistung.net", "aFRR_Leistung",
                     "RESULT_OVERVIEW_CAPACITY_MARKET_aFRR_"
                     "2025-01-01_2025-12-31.parquet")

bericht = []


def sag(z=""):
    bericht.append(z)
    sys.stdout.write(z + "\n")


def zahl(s):
    """Deutsche Dezimaltrennung in float, wie im Redispatch-Befund."""
    return pd.to_numeric(s.astype(str).str.replace(".", "", regex=False)
                         .str.replace(",", ".", regex=False), errors="coerce")


# --------------------------------------------------- bezuschlagte Leistung
t = pd.read_parquet(LEIST)
t["vol"] = pd.to_numeric(t["GERMANY_ALLOCATED_VOLUME_[MW]"], errors="coerce")
vorhalt = {}
for kuerzel in ("POS", "NEG"):
    v = t[t["PRODUCT"].astype(str).str.startswith(kuerzel)]["vol"]
    vorhalt[kuerzel] = (v.mean(), v.min(), v.max(), len(v))

# ------------------------------------------------------ abgerufene Arbeit
d = pd.read_parquet(AKTIV)
d["tag"] = pd.to_datetime(d["Datum"], format="%d.%m.%Y", errors="coerce")
a = d[d["tag"].dt.year == 2025]
if len(a) != 35040:
    sys.stderr.write("ABBRUCH: %d Viertelstunden statt 35040\n" % len(a))
    raise SystemExit(1)
if sorted(a["Einheit"].unique()) != ["MW"]:
    sys.stderr.write("ABBRUCH: unerwartete Einheit\n")
    raise SystemExit(1)

sag("# Abruf der aFRR-Arbeit in Deutschland 2025")
sag()
sag("Eigene Auswertung vom 23.09.2026 fuer Abschnitt 4.6.1. Die")
sag("bezuschlagte Leistung stammt aus der Ausschreibungsuebersicht von")
sag("regelleistung.net, der Abruf aus der viertelstuendlichen Reihe")
sag("Aktivierte aFRR von netztransparenz.net. Alle 35.040")
sag("Viertelstunden des Jahres 2025 liegen vor.")
sag()
sag("| Richtung | bezuschlagt Mittel | Minimum | Maximum | Vierstundenprodukte |")
sag("|---|---|---|---|---|")
for kuerzel, name in (("POS", "positiv"), ("NEG", "negativ")):
    m, lo, hi, n = vorhalt[kuerzel]
    sag("| %s | %.0f MW | %.0f MW | %.0f MW | %d |" % (name, m, lo, hi, n))
sag()
sag("| Richtung | Abruf Mittel | Anteil | Median | Anteil | 95-Prozent-Quantil | Maximum |")
sag("|---|---|---|---|---|---|---|")
werte = {}
for kuerzel, name, spalte in (("POS", "positiv", "Deutschland (Positiv)"),
                              ("NEG", "negativ", "Deutschland (Negativ)")):
    v = zahl(a[spalte])
    vor = vorhalt[kuerzel][0]
    werte[kuerzel] = (v.mean(), v.mean() / vor * 100, v.median(),
                      v.median() / vor * 100, v.quantile(0.95), v.max(),
                      (v < 0.1 * vor).mean() * 100, v.sum() * 0.25 / 1e6)
    sag("| %s | %.1f MW | %.1f %% | %.1f MW | %.1f %% | %.0f MW | %.0f MW |"
        % ((name,) + werte[kuerzel][:6]))
sag()
for kuerzel, name in (("POS", "positiv"), ("NEG", "negativ")):
    w = werte[kuerzel]
    sag("**%s.** In %.0f Prozent der Viertelstunden bleibt der Abruf unter "
        "einem Zehntel der vorgehaltenen Leistung. Die Jahresarbeit betraegt "
        "%.2f TWh." % (name, w[6], w[7]))
    sag()

sag("## Was daraus fuer die Sensitivitaet folgt")
sag()
sag("Die Bezugsanlage hat 100 MW Nennleistung. Der mittlere Abruf in")
sag("Deutschland liegt mit %.0f und %.0f MW in derselben Groessenordnung."
    % (werte["POS"][0], werte["NEG"][0]))
sag("Die Stufe *bis zum Abruf* laesst der Bezugsanlage den vollen")
sag("deutschlandweiten Abruf offen, unterstellt ihr also, dass sie ihn")
sag("allein bedient. Die Stufe *bis 100 MW* hebt auch diese Grenze auf.")
sag("Der Referenzfall *pro rata* liefert dagegen den Anteil der eigenen")
sag("Vorhaltung am Abruf, im Mittel also %.1f und %.1f Prozent der"
    % (werte["POS"][1], werte["NEG"][1]))
sag("vorgehaltenen Leistung. Nur der Referenzfall ist fuer eine einzelne")
sag("Anlage zu erwarten.")
sag()

ZIEL = os.path.join(HIER, "BEFUND.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
