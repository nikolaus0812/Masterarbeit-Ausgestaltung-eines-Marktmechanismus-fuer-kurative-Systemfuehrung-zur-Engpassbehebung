# -*- coding: utf-8 -*-
"""
Prueft, ob der Vollreservierungspreis aus der zweiten Iteration wirklich JEDE
Stunde und Richtung voll reserviert. Massstab ist das Kriterium des Verfahrens
selbst, naemlich hoechstens 0,01 MW Schlupf von 100 MW (_VOLL_TOL_MW).

Gelesen werden die gespeicherten Validierungslaeufe, keine neue Rechnung.
"""
import glob
import os

import pandas as pd

P = 100.0
TOL_MW = 0.01
SCHWELLE = P - TOL_MW

BASIS = "C:/GIT-HUB/bess_dispatch_optimization/results/einzellauf"


def auswerten(pfad):
    df = pd.read_csv(pfad)
    ent = df["kur_leistung_ent"].to_numpy(dtype=float)
    lad = df["kur_leistung_lad"].to_numpy(dtype=float)
    # 96 Viertelstunden auf 24 Stunden: die Reservierung ist je Stunde konstant,
    # das Minimum der vier Viertelstunden ist der Wert der Stunde.
    ent_h = ent.reshape(-1, 4).min(axis=1)
    lad_h = lad.reshape(-1, 4).min(axis=1)
    return ent_h, lad_h


def bericht(lauf, tag, methode):
    pfad = f"{BASIS}/{lauf}/{tag}/curative_breakeven/validierung/{tag}_{methode}.csv"
    if not os.path.exists(pfad):
        return
    ent_h, lad_h = auswerten(pfad)
    offen_p = [(h, round(float(ent_h[h]), 4)) for h in range(24) if ent_h[h] < SCHWELLE]
    offen_n = [(h, round(float(lad_h[h]), 4)) for h in range(24) if lad_h[h] < SCHWELLE]
    print(f"  {methode:10s} min POS {ent_h.min():8.4f} MW, min NEG {lad_h.min():8.4f} MW, "
          f"nicht voll: {len(offen_p)} POS / {len(offen_n)} NEG von je 24")
    if offen_p:
        print(f"             POS-Stunden {offen_p}")
    if offen_n:
        print(f"             NEG-Stunden {offen_n}")


def preise(lauf, tag):
    pfad = f"{BASIS}/{lauf}/{tag}/curative_breakeven/curative_breakeven_{tag}.csv"
    if not os.path.exists(pfad):
        return
    df = pd.read_csv(pfad)
    spalten = [s for s in df.columns if s.startswith("be_")]
    stuendlich = df.iloc[::4]
    for s in ("be_full_pos", "be_full_neg"):
        if s not in df.columns:
            continue
        w = stuendlich[s]
        print(f"  {s:14s} min {w.min():9.2f}  max {w.max():9.2f}  "
              f"Summe {w.sum():10.2f}  NaN {int(w.isna().sum())}  "
              f"gleich null {int((w == 0).sum())}")
    offen = [s for s in spalten if s.endswith("_offen")]
    for s in offen:
        n = int(stuendlich[s].astype(str).str.lower().isin(["true", "1"]).sum())
        print(f"  {s:14s} wahr in {n} Stunden")


if __name__ == "__main__":
    for lauf in sorted(os.listdir(BASIS)):
        if not lauf.startswith("run_"):
            continue
        tage = sorted(d for d in os.listdir(f"{BASIS}/{lauf}")
                      if d.startswith("2025-"))
        for tag in tage:
            pfad = f"{BASIS}/{lauf}/{tag}/curative_breakeven"
            if not os.path.isdir(pfad):
                continue
            print(f"\n{lauf}  {tag}")
            preise(lauf, tag)
            bericht(lauf, tag, "breakeven")
            bericht(lauf, tag, "vollverdr")
