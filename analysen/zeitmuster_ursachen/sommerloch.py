# -*- coding: utf-8 -*-
"""Woran liegt der Preisrueckgang im Juli und August.

Der Verfasser vermutet die deutsche Ferienzeit, also geringere Last.
Geringere Last bei gleicher Solareinspeisung muesste den Mittagspreis
weiter druecken und mehr negative Viertelstunden erzeugen. Geprueft wird,
ob die Daten das hergeben.

Als Mass fuer den Solarueberschuss dient die Tiefe der Mittagsdelle,
also der Abstand des mittleren Preises von 11 bis 15 Uhr zum Tagesmittel.
Je tiefer, desto mehr Solareinspeisung drueckt den Mittagspreis.

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
d["monat"] = d["day"].dt.month

tagesmittel = d.groupby("day")["preis_da"].mean()
d["tagesmittel"] = d["day"].map(tagesmittel)
mittag = d[d["stunde"].isin(range(11, 16))].copy()
mittag["delle"] = mittag["preis_da"] - mittag["tagesmittel"]

bericht = []


def sag(z=""):
    bericht.append(z)
    sys.stdout.write(z + "\n")


sag("# Der Preisrueckgang im Juli und August")
sag()
sag("Eigene Auswertung vom 23.09.2026. Preise in Euro je Megawattstunde,")
sag("Reservierungspreise in Euro je Megawatt und Stunde.")
sag()
sag("| Monat | DA-Tagesmittel | Mittagsdelle | negative Viertelstunden | "
    "aFRR neg | Summe Res. Median |")
sag("|---|---|---|---|---|---|")
for mo in range(1, 13):
    z = d[d["monat"] == mo]
    zm = mittag[mittag["monat"] == mo]
    stunden = z.groupby(["day", "stunde"])[["be_pos", "be_neg"]].first()
    summe = (stunden["be_pos"] + stunden["be_neg"]).median()
    sag("| %02d | %.1f | %+.1f | %.0f %% | %.1f | %.1f |"
        % (mo, z["preis_da"].mean(), zm["delle"].mean(),
           (z["preis_idc"] < 0).mean() * 100, z["afrr_cap_neg"].mean(), summe))
sag()
sag("## Was die Zahlen sagen")
sag()
jun = mittag[mittag["monat"] == 6]["delle"].mean()
jul = mittag[mittag["monat"] == 7]["delle"].mean()
aug = mittag[mittag["monat"] == 8]["delle"].mean()
sep = mittag[mittag["monat"] == 9]["delle"].mean()
sag("Die Mittagsdelle betraegt im Juni %+.1f, im Juli %+.1f, im August %+.1f"
    % (jun, jul, aug))
sag("und im September %+.1f Euro je Megawattstunde." % sep)
sag()
sag("Geringere Last bei unveraenderter Solareinspeisung muesste die Delle")
sag("**vertiefen** und mehr negative Viertelstunden erzeugen. Beobachtet ist")
sag("das Gegenteil, also spricht die Ferienzeit als Erklaerung nicht fuer")
sag("sich. Die Daten der Arbeit enthalten keine Erzeugungs- oder Lastreihen,")
sag("mit denen sich die Ursache entscheiden liesse.")
sag()

ZIEL = os.path.join(HIER, "BEFUND_SOMMERLOCH.md")
io.open(ZIEL, "w", encoding="utf-8", newline="\n").write("\n".join(bericht) + "\n")
sys.stdout.write("\ngeschrieben: %s\n" % ZIEL)
