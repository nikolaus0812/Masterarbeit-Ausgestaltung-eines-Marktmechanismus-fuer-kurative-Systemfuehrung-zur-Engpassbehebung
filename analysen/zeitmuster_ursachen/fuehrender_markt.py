# -*- coding: utf-8 -*-
"""Welcher Markt stellt je Stunde die groesste Opportunitaet.

Die Rangkorrelationen aus `ursachen.py` trennen die Treiber nicht, weil
hohe Solareinspeisung zugleich negative Preise und einen teuren Preis
negativer Regelleistung erzeugt. Hier wird deshalb je Stunde gerechnet,
welcher Markt der Bezugsanlage am meisten einbraechte, wenn sie die
Stunde nicht kurativ reservierte. Das Verfahren entspricht dem Test des
Analyse-Repositorys in ERGEBNISSE Abschnitt 7.11.

Alle Groessen sind auf ein Megawatt Nennleistung und eine Stunde
bezogen, damit sie vergleichbar sind:

 - aFRR-Leistung: der Leistungspreis unmittelbar, in Euro je MW und h.
 - Energiemarkt: der Betrag des Preises, denn eine Ladung zu einem
   negativen Preis bringt Geld ein. Bei einer Abrufdauer von einer
   Stunde entspricht ein MW Reservierung einer MWh, sodass Euro je MWh
   und Euro je MW und Stunde gleich gross sind.
 - aFRR-Arbeit: Arbeitspreis mal abgerufener Menge je Nennleistung.

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
PMAX = 100.0          # Nennleistung der Bezugsanlage in MW

d = pd.read_parquet(QUELLE)
d = d[~d["gesperrt"]].copy()
d["day"] = pd.to_datetime(d["day"])
d["monat"] = d["day"].dt.month

bericht = []


def sag(z=""):
    bericht.append(z)
    sys.stdout.write(z + "\n")


sag("# Welcher Markt stellt die Opportunitaet")
sag()
sag("Eigene Auswertung vom 23.09.2026. Je Viertelstunde wird bestimmt,")
sag("welcher Markt der Bezugsanlage am meisten einbraechte. Alles in Euro")
sag("je Megawatt und Stunde. Das Verfahren folgt ERGEBNISSE Abschnitt 7.11.")
sag()

# ----------------------------------------------------------------------
# Kandidaten je Richtung
# ----------------------------------------------------------------------
# Laden: negative Preise bringen Geld, positive kosten. Also zaehlt der
# Betrag nur, wenn der Preis negativ ist.
d["lad_afrr"] = d["afrr_cap_neg"]
d["lad_idc"] = np.where(d["preis_idc"] < 0, -d["preis_idc"], 0.0)
d["lad_da"] = np.where(d["preis_da"] < 0, -d["preis_da"], 0.0)
d["lad_ene"] = (d["afrr_ene_preis_neg"].fillna(0.0)
                * d["afrr_ene_neg_mw"].fillna(0.0) / PMAX)

# Entladen: positive Preise bringen Geld.
d["ent_afrr"] = d["afrr_cap_pos"]
d["ent_idc"] = d["preis_idc"].clip(lower=0.0)
d["ent_da"] = d["preis_da"].clip(lower=0.0)
d["ent_ene"] = (d["afrr_ene_preis_pos"].fillna(0.0)
                * d["afrr_ene_pos_mw"].fillna(0.0) / PMAX)

KAND_LAD = {"aFRR-Leistung": "lad_afrr", "Energiemarkt negativ": "lad_idc",
            "Day-Ahead negativ": "lad_da", "aFRR-Arbeit": "lad_ene"}
KAND_ENT = {"aFRR-Leistung": "ent_afrr", "Energiemarkt": "ent_idc",
            "Day-Ahead": "ent_da", "aFRR-Arbeit": "ent_ene"}


def fuehrend(rahmen, kandidaten):
    werte = rahmen[list(kandidaten.values())]
    namen = list(kandidaten.keys())
    return pd.Series([namen[i] for i in werte.values.argmax(axis=1)],
                     index=rahmen.index), werte.max(axis=1)


MITTAG = range(10, 16)
ABEND = range(17, 21)


def block(kopf, maske, kandidaten, preisspalte, fenstername):
    sag("## %s" % kopf)
    sag()
    teil = d[maske].copy()
    teil["fuehrend"], teil["opp"] = fuehrend(teil, kandidaten)
    sag("Betrachtet sind die %s. Anteil der Viertelstunden, in denen der"
        % fenstername)
    sag("jeweilige Markt die groesste Opportunitaet stellt, und die mittlere")
    sag("Hoehe dieser Opportunitaet.")
    sag()
    sag("| Markt | Anteil der Viertelstunden | mittlere Opportunitaet |")
    sag("|---|---|---|")
    for name in kandidaten:
        m = teil["fuehrend"] == name
        if not m.any():
            sag("| %s | 0 %% | -- |" % name)
            continue
        sag("| %s | %.0f %% | %.1f |"
            % (name, m.mean() * 100, teil.loc[m, "opp"].mean()))
    sag()
    sag("Mittlere Opportunitaet insgesamt %.1f, mittlerer Reservierungspreis"
        % teil["opp"].mean())
    sag("%.1f Euro je Megawatt und Stunde." % teil[preisspalte].mean())
    sag()
    # Monatsbild
    sag("Anteil der Viertelstunden je Monat, in denen der Markt fuehrt:")
    sag()
    sag("| Monat | " + " | ".join(kandidaten) + " | Opportunitaet |")
    sag("|---" * (len(kandidaten) + 2) + "|")
    for mo in range(1, 13):
        z = teil[teil["monat"] == mo]
        anteile = ["%.0f %%" % ((z["fuehrend"] == n).mean() * 100)
                   for n in kandidaten]
        sag("| %02d | %s | %.1f |" % (mo, " | ".join(anteile), z["opp"].mean()))
    sag()
    return teil


lad = block("1 Ladereservierung, 10 bis 15 Uhr",
            d["stunde"].isin(MITTAG), KAND_LAD, "be_neg",
            "Viertelstunden von 10 bis 15 Uhr")
ent = block("2 Entladereservierung, 17 bis 20 Uhr",
            d["stunde"].isin(ABEND), KAND_ENT, "be_pos",
            "Viertelstunden von 17 bis 20 Uhr")

# ----------------------------------------------------------------------
# Wie heftig sind die negativen Preise wirklich
# ----------------------------------------------------------------------
sag("## 3 Wie heftig die negativen Preise sind")
sag()
neg = d[d["preis_idc"] < 0]
sag("Von %d Viertelstunden des Jahres tragen %d einen negativen"
    % (len(d), len(neg)))
sag("Intradaypreis, also %.1f Prozent." % (len(neg) / len(d) * 100))
sag()
sag("| Groesse | Wert |")
sag("|---|---|")
sag("| Median der negativen Preise | %.1f |" % neg["preis_idc"].median())
sag("| arithmetisches Mittel | %.1f |" % neg["preis_idc"].mean())
sag("| 5-Prozent-Quantil | %.1f |" % neg["preis_idc"].quantile(0.05))
sag("| Minimum | %.1f |" % neg["preis_idc"].min())
sag()
sag("Zum Vergleich der Leistungspreis der negativen aFRR in denselben")
sag("Viertelstunden: Median %.1f, Mittel %.1f Euro je Megawatt und Stunde."
    % (neg["afrr_cap_neg"].median(), neg["afrr_cap_neg"].mean()))
sag()
sag("In wie vielen dieser Viertelstunden ist der Betrag des negativen")
sag("Preises groesser als der aFRR-Leistungspreis: %.0f Prozent."
    % ((-neg["preis_idc"] > neg["afrr_cap_neg"]).mean() * 100))
sag()

ZIEL = os.path.join(HIER, "BEFUND_FUEHRENDER_MARKT.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
