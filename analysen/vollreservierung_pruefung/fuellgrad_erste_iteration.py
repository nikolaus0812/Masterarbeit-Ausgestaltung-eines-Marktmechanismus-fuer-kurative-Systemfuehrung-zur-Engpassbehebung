# -*- coding: utf-8 -*-
"""
Fuellgrad und belegte Maerkte, wenn die Preise der ersten Iteration gemeinsam
vorgegeben werden.

Frage des Verfassers vom 17.09.2026 zu 3.2.4: welchen Fuellgrad man im Schnitt
erhaelt, wenn die Stundenpreise der ersten Iteration zugleich vorgegeben
werden, und welche Maerkte in den nicht voll reservierten Stunden offen
bleiben.

Datengrundlage: die gespeicherten Validierungslaeufe "breakeven" des neuesten
Einzellaufs mit der Basiskonfiguration. Der Jahreslauf speichert diese Laeufe
nicht; die Auswertung gilt deshalb nur fuer die vorliegenden Tage.

Kriterium "voll" wie im Verfahren: hoechstens 0,01 MW Schlupf von 100 MW.
Ein Markt gilt in einer Stunde als belegt, wenn seine Leistung dort in
mindestens einer Viertelstunde 0,01 MW uebersteigt.
"""
import os
import sys

import numpy as np
import pandas as pd

LAUF = ("C:/GIT-HUB/bess_dispatch_optimization/results/einzellauf/"
        + (sys.argv[1] if len(sys.argv) > 1 else "run_20260917_141256"))
P = 100.0
VOLL = P - 0.01
SCHWELLE = 0.01

MAERKTE = {
    "DA": ["da_leistung_lad", "da_leistung_ent"],
    "IDC": ["idc_leistung_lad", "idc_leistung_ent"],
    "aFRR": ["afrr_leistung_pos", "afrr_leistung_neg"],
    "FCR": ["fcr_leistung"],
}


def stuendlich_min(reihe):
    return reihe.to_numpy(dtype=float).reshape(-1, 4).min(axis=1)


def stuendlich_max(reihe):
    return np.abs(reihe.to_numpy(dtype=float)).reshape(-1, 4).max(axis=1)


def main():
    tage = sorted(d for d in os.listdir(LAUF) if d.startswith("2025-"))
    zeilen = []
    for tag in tage:
        pfad = f"{LAUF}/{tag}/curative_breakeven/validierung/{tag}_breakeven.csv"
        if not os.path.exists(pfad):
            continue
        df = pd.read_csv(pfad)
        for richtung, spalte in (("POS", "kur_leistung_ent"),
                                 ("NEG", "kur_leistung_lad")):
            res = stuendlich_min(df[spalte])
            offen = res < VOLL
            eintrag = {"tag": tag, "richtung": richtung,
                       "fuellgrad_mittel": float(np.mean(res) / P),
                       "offene_stunden": int(offen.sum())}
            for markt, spalten in MAERKTE.items():
                belegt = np.zeros(24, dtype=bool)
                for s in spalten:
                    if s in df.columns:
                        belegt |= stuendlich_max(df[s]) > SCHWELLE
                eintrag[f"{markt}_in_offenen"] = int((belegt & offen).sum())
            zeilen.append(eintrag)

    tab = pd.DataFrame(zeilen)
    pd.set_option("display.width", 160)
    print(tab.to_string(index=False))
    print()
    for richtung in ("POS", "NEG"):
        t = tab[tab.richtung == richtung]
        offen = t.offene_stunden.sum()
        n = 24 * len(t)
        print(f"{richtung}: Fuellgrad im Mittel {100 * t.fuellgrad_mittel.mean():.1f} %, "
              f"offen {offen} von {n} Stunden ({100 * offen / n:.0f} %)")
        for markt in MAERKTE:
            k = t[f"{markt}_in_offenen"].sum()
            anteil = 100 * k / offen if offen else float("nan")
            print(f"   {markt:5s} belegt in {k:3d} der offenen Stunden ({anteil:.0f} %)")


if __name__ == "__main__":
    main()
