"""Haelt den Leistungspreis der positiven aFRR gegen die Marktlage 2024 und 2025.

Quellen: regelleistung.net (aFRR-Leistungsmarkt) und energy-charts.de
(Day-Ahead-Preis, Last, erneuerbare Einspeisung, Gaspreis), beide aus dem
Datenbestand des Optimierungsmodells.
"""
import csv
import datetime as dt
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(__file__))
import auswertung as A  # noqa: E402

PREISE = ("C:/GIT-HUB/bess_dispatch_optimization/data/"
          "Strompreise_energy-charts.de/strom_preise_de_{}_15min.csv")


def zahl(s):
    if s in (None, "", "nan"):
        return None
    try:
        return float(s.replace(",", "."))
    except ValueError:
        return None


def markt(jahr):
    """Tagesmittel von Day-Ahead-Preis, Residuallast und Gaspreis."""
    tage = {}
    with open(PREISE.format(jahr), encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f, delimiter=";"):
            ts = r["timestamp_local"][:10]
            d = dt.date(int(ts[:4]), int(ts[5:7]), int(ts[8:10]))
            if d.year != jahr:
                continue
            da = zahl(r["Intraday kontinuierlich, 15 Minuten Durchschnittspreis (DE-LU)"])
            last = zahl(r["Last"])
            ern = zahl(r["Erneuerbar"])
            gas = zahl(r["Gas (NCG, THE)"])
            e = tage.setdefault(d, {"da": [], "rl": [], "gas": [], "spanne": []})
            if da is not None:
                e["da"].append(da)
                e["spanne"].append(da)
            if last is not None and ern is not None:
                e["rl"].append((last - ern) / 1000.0)
            if gas is not None:
                e["gas"].append(gas)
    aus = {}
    for d, e in tage.items():
        aus[d] = {k: (statistics.fmean(v) if v else None)
                  for k, v in e.items() if k != "spanne"}
        aus[d]["spanne"] = (max(e["spanne"]) - min(e["spanne"])) if e["spanne"] else None
    return aus


def korrelation(x, y):
    paare = [(a, b) for a, b in zip(x, y) if a is not None and b is not None]
    if len(paare) < 3:
        return float("nan")
    a = [p[0] for p in paare]
    b = [p[1] for p in paare]
    return statistics.correlation(a, b)


if __name__ == "__main__":
    for jahr in (2024, 2025):
        saetze = A.einlesen(os.path.join(A.BASIS, A.DATEIEN[jahr]))
        m = markt(jahr)
        print(f"\n### {jahr}: Monatswerte")
        print("| Monat | aFRR pos | Angebot MW | IDC-Preis EUR/MWh | Tagesspanne IDC | "
              "Residuallast GW | Gas EUR/MWh |")
        print("|---|---|---|---|---|---|---|")
        for mon in range(1, 13):
            t = [s for s in saetze if s["datum"].month == mon and s["richtung"] == "pos"]
            tage = [d for d in m if d.month == mon]
            if not t or not tage:
                continue
            print("| {} | {:.1f} | {:.0f} | {:.1f} | {:.1f} | {:.1f} | {:.1f} |".format(
                mon, A.mittel([s["avg"] for s in t]),
                A.mittel([s["angebot"] for s in t]),
                A.mittel([m[d]["da"] for d in tage]),
                A.mittel([m[d]["spanne"] for d in tage]),
                A.mittel([m[d]["rl"] for d in tage]),
                A.mittel([m[d]["gas"] for d in tage])))
        # Tageskorrelation
        tagespreis, da, rl, angebot, spanne = [], [], [], [], []
        for d in sorted(m):
            t = [s for s in saetze if s["datum"] == d and s["richtung"] == "pos"]
            if not t:
                continue
            tagespreis.append(A.mittel([s["avg"] for s in t]))
            angebot.append(A.mittel([s["angebot"] for s in t]))
            da.append(m[d]["da"])
            rl.append(m[d]["rl"])
            spanne.append(m[d]["spanne"])
        print(f"\nTageskorrelation {jahr}, n = {len(tagespreis)}")
        print("  aFRR pos gegen IDC-Preis        {:+.2f}".format(korrelation(tagespreis, da)))
        print("  aFRR pos gegen IDC-Tagesspanne  {:+.2f}".format(korrelation(tagespreis, spanne)))
        print("  aFRR pos gegen Residuallast     {:+.2f}".format(korrelation(tagespreis, rl)))
        print("  aFRR pos gegen Angebotsmenge    {:+.2f}".format(korrelation(tagespreis, angebot)))
        print("  Angebotsmenge gegen Residuallast {:+.2f}".format(korrelation(angebot, rl)))
