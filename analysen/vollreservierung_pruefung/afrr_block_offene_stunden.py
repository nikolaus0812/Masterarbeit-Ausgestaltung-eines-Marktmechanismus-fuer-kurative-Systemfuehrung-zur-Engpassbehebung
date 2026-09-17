# -*- coding: utf-8 -*-
"""
Warum bleibt aFRR-Leistung in Stunden, die bei den Preisen der ersten
Iteration nicht voll reserviert sind?

Frage des Verfassers vom 17.09.2026: "warum nutzt er noch aFRR? Ist aFRR
Energie oder was ist das? Ansonsten ergibt das keinen Sinn, da die aFRR
4h-Reservierungsfenster eigentlich relativ gut verdraengt werden koennen durch
die feinere Aufloesung des kurativen Marktes, nur die Viertelstunden-
Lieferprodukte machen Probleme."

Im Modell ist afrr_leistung die Vorhaltung, ueber den Vier-Stunden-Block
konstant; die aFRR-Arbeit haengt fest anteilig daran. Vermutung, die hier
geprueft wird: die Vorhaltung bleibt, weil sie fuer den GANZEN Block gilt und
im selben Block Stunden mit niedrigem kurativem Preis liegen. Dann haelt der
Speicher die aFRR fuer alle vier Stunden, und auch die teure Stunde des Blocks
wird nicht voll.

Fuer jede offene Stunde mit aFRR-Vorhaltung werden die Preise der ersten
Iteration aller vier Stunden des Blocks und deren Reservierung ausgegeben.
"""
import os
import sys

import numpy as np
import pandas as pd

LAUF = ("C:/GIT-HUB/bess_dispatch_optimization/results/einzellauf/"
        + (sys.argv[1] if len(sys.argv) > 1 else "run_20260917_141256"))
P = 100.0
VOLL = P - 0.01


def h_min(x):
    return np.asarray(x, dtype=float).reshape(-1, 4).min(axis=1)


def h_erst(x):
    return np.asarray(x, dtype=float).reshape(-1, 4)[:, 0]


def main():
    tage = sorted(d for d in os.listdir(LAUF) if d.startswith("2025-"))
    faelle = 0
    block_billiger = 0
    for tag in tage:
        basis = f"{LAUF}/{tag}/curative_breakeven"
        val = f"{basis}/validierung/{tag}_breakeven.csv"
        be = f"{basis}/curative_breakeven_{tag}.csv"
        if not (os.path.exists(val) and os.path.exists(be)):
            continue
        v = pd.read_csv(val)
        b = pd.read_csv(be)
        for richtung, kur, afrr, preis in (
                ("POS", "kur_leistung_ent", "afrr_leistung_pos", "be_pos"),
                ("NEG", "kur_leistung_lad", "afrr_leistung_neg", "be_neg")):
            k = h_min(v[kur])
            a = h_min(v[afrr])
            p = h_erst(b[preis])
            for h in range(24):
                if k[h] >= VOLL or a[h] <= 0.01:
                    continue
                faelle += 1
                blk = h // 4
                stunden = range(4 * blk, 4 * blk + 4)
                preise = [p[s] for s in stunden]
                kurs = [k[s] for s in stunden]
                if min(preise) < p[h]:
                    block_billiger += 1
                print(f"{tag} {richtung} Stunde {h:2d}  Block {4*blk:2d}-{4*blk+3:2d}  "
                      f"aFRR {a[h]:5.1f} MW  kurativ {k[h]:5.1f} MW  "
                      f"Preise im Block {[round(x, 1) for x in preise]}  "
                      f"kurativ im Block {[round(x, 0) for x in kurs]}")
    print()
    print(f"offene Stunden mit aFRR-Vorhaltung: {faelle}")
    print(f"davon mit einer billigeren Stunde im selben Block: {block_billiger}")


if __name__ == "__main__":
    main()
