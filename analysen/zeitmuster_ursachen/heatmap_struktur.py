# -*- coding: utf-8 -*-
"""Wie liegen die teuren Stunden in der Heatmap.

Die Abbildung zeigt fuer die Ladereservierung ein zusammenhaengendes Band
ueber die Mitte des Tages und fuer die Entladereservierung eher einzelne
teure Tage. Dieser Eindruck wird hier gemessen, damit der Text ihn
belegen kann statt ihn zu behaupten.

Betrachtet sind die Stunden oberhalb des 90-Prozent-Quantils je Richtung.

Eigene Auswertung der Schriftfassung vom 23.09.2026, nur lesend.
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
stunden = d.groupby(["day", "stunde"])[["be_pos", "be_neg"]].first().reset_index()
stunden["monat"] = stunden["day"].dt.month

bericht = []


def sag(z=""):
    bericht.append(z)
    sys.stdout.write(z + "\n")


sag("# Struktur der teuren Stunden in der Heatmap")
sag()
sag("Eigene Auswertung vom 23.09.2026. Betrachtet sind die Stunden oberhalb")
sag("des 90-Prozent-Quantils je Richtung, also je 876 der 8758 Stunden.")
sag()

for name, spalte in (("Entladereservierung", "be_pos"),
                     ("Ladereservierung", "be_neg")):
    schwelle = stunden[spalte].quantile(0.90)
    teuer = stunden[stunden[spalte] > schwelle]
    tage = teuer["day"].nunique()
    je_tag = len(teuer) / tage
    sag("## %s" % name)
    sag()
    sag("| Groesse | Wert |")
    sag("|---|---|")
    sag("| 90-Prozent-Quantil | %.1f Euro je Megawatt und Stunde |" % schwelle)
    sag("| teure Stunden | %d |" % len(teuer))
    sag("| verteilt auf Kalendertage | %d von 365 |" % tage)
    sag("| teure Stunden je betroffenem Tag | %.1f |" % je_tag)
    # Konzentration ueber die Tagesstunden
    je_stunde = teuer.groupby("stunde").size().sort_values(ascending=False)
    sechs = je_stunde.head(6).sum() / len(teuer) * 100
    sag("| Anteil in den sechs staerksten Tagesstunden | %.0f Prozent |" % sechs)
    sag("| diese Tagesstunden | %s |"
        % ", ".join("%d" % h for h in sorted(je_stunde.head(6).index)))
    # Konzentration ueber die Monate
    je_monat = teuer.groupby("monat").size()
    sag("| Anteil von M\u00e4rz bis Oktober | %.0f Prozent |"
        % (je_monat.reindex(range(3, 11)).fillna(0).sum() / len(teuer) * 100))
    sag()

ZIEL = os.path.join(HIER, "BEFUND_HEATMAP.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
