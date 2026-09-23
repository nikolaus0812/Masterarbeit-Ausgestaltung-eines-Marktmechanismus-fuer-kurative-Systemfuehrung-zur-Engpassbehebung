# -*- coding: utf-8 -*-
"""Jahreszeiten fuer Abschnitt 4.5, mit dem Median der Summe.

Der bisherige Text nennt je Jahreszeit die beiden Mediane und ihre
Summe. Das ist die Summe der Mediane und nicht der Median der Summe.
Hier stehen beide nebeneinander, damit der Unterschied sichtbar ist.
"""
import io
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import laden

HIER = os.path.dirname(os.path.abspath(__file__))
JAHRESZEITEN = {"Winter (Dez bis Feb)": [12, 1, 2],
                "Fruehjahr (Mrz bis Mai)": [3, 4, 5],
                "Sommer (Jun bis Aug)": [6, 7, 8],
                "Herbst (Sep bis Nov)": [9, 10, 11]}

bericht = []


def sag(z=""):
    bericht.append(z)
    sys.stdout.write(z + "\n")


h = laden.stunden()

sag("# Jahreszeiten des kurativen Reservierungspreises")
sag()
sag("Eigene Auswertung vom 23.09.2026, zweite Iteration. Preise in Euro je")
sag("Megawatt und Stunde.")
sag()
sag("| Jahreszeit | Median entladen | Median ladend | Summe der Mediane | "
    "Median der Summe |")
sag("|---|---|---|---|---|")
werte = {}
for name, monate in JAHRESZEITEN.items():
    z = h[h["monat"].isin(monate)]
    a, b = z["res_ent"].median(), z["res_lad"].median()
    m = z["summe"].median()
    werte[name] = m
    sag("| %s | %.2f | %.2f | %.2f | **%.2f** |" % (name, a, b, a + b, m))
sag()
guenstig = min(werte, key=werte.get)
sag("Guenstigste Jahreszeit: %s mit %.1f Euro je Megawatt und Stunde."
    % (guenstig, werte[guenstig]))
sag()
sag("| Jahreszeit | Median der Summe | gegen die guenstigste |")
sag("|---|---|---|")
for name, m in werte.items():
    sag("| %s | %.1f | %+.0f Prozent |"
        % (name, m, (m / werte[guenstig] - 1) * 100))
sag()

sag("## Monatsweise, zum Nachschlagen")
sag()
sag("| Monat | Median der Summe |")
sag("|---|---|")
for m in range(1, 13):
    sag("| %02d | %.1f |" % (m, h[h["monat"] == m]["summe"].median()))
sag()

ZIEL = os.path.join(HIER, "BEFUND_JAHRESZEITEN.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
