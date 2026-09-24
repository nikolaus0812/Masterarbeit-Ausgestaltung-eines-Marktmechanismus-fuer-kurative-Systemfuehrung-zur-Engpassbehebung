"""Monatswerte des aFRR-Leistungsmarkts 2024, 2025 und 2026 aus den
Jahresdateien von regelleistung.net.

Prueft, ob der hohe Leistungspreis der positiven aFRR im September und
Oktober 2025 mit der angebotenen Menge zusammenhaengt.
"""
import datetime as dt
import os
import statistics
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mfrr_leistungspreise"))
from xlsx_lesen import lies  # noqa: E402

BASIS = ("C:/GIT-HUB/bess_dispatch_optimization/data/"
         "Regelleistung_regelleistung.net/aFRR_Leistung")
DATEIEN = {
    2024: "RESULT_OVERVIEW_CAPACITY_MARKET_aFRR_2024-01-01_2024-12-31.xlsx",
    2025: "RESULT_OVERVIEW_CAPACITY_MARKET_aFRR_2025-01-01_2025-12-31.xlsx",
    2026: "RESULT_OVERVIEW_CAPACITY_MARKET_aFRR_2026-01-01_2026-05-01.xlsx",
}


def exceldatum(z):
    return dt.date(1899, 12, 30) + dt.timedelta(days=int(z))


def einlesen(pfad):
    zeilen = lies(pfad)
    kopf = zeilen[0]
    idx = {name: i for i, name in enumerate(kopf)}
    gesucht = {
        "avg": "GERMANY_AVERAGE_CAPACITY_PRICE_[(EUR/MW)/h]",
        "marg": "GERMANY_MARGINAL_CAPACITY_PRICE_[(EUR/MW)/h]",
        "min": "GERMANY_MIN_CAPACITY_PRICE_[(EUR/MW)/h]",
        "angebot": "GERMANY_SUM_OF_OFFERED_CAPACITY_[MW]",
        "zuschlag": "GERMANY_ALLOCATED_VOLUME_[MW]",
        "saldo": "GERMANY_IMPORT(-)_EXPORT(+)_[MW]",
        "cz_avg": "CZECH_REPUBLIC_AVERAGE_CAPACITY_PRICE_[(EUR/MW)/h]",
    }
    sp = {k: idx[v] for k, v in gesucht.items() if v in idx}
    saetze = []
    for z in zeilen[1:]:
        if not z or z[0] is None:
            continue
        datum = exceldatum(z[0])
        produkt = z[3]
        richtung = "pos" if str(produkt).startswith("POS") else "neg"
        satz = {"datum": datum, "produkt": produkt, "richtung": richtung}
        for k in gesucht:
            i = sp.get(k)
            satz[k] = z[i] if i is not None and i < len(z) else None
        saetze.append(satz)
    return saetze


def mittel(werte):
    werte = [w for w in werte if isinstance(w, (int, float))]
    return statistics.fmean(werte) if werte else float("nan")


def tabelle(saetze, jahr, richtung):
    print(f"\n### {jahr}, Richtung {richtung}")
    print("| Monat | Zeitscheiben | Leistungspreis Mittel | Median | Grenzpreis | "
          "angebotene Menge MW | Saldo MW |")
    print("|---|---|---|---|---|---|---|")
    for m in range(1, 13):
        teil = [s for s in saetze if s["datum"].month == m and s["richtung"] == richtung]
        if not teil:
            continue
        preise = [s["avg"] for s in teil if isinstance(s["avg"], (int, float))]
        print("| {} | {} | {:.1f} | {:.1f} | {:.1f} | {:.0f} | {:.0f} |".format(
            m, len(teil), mittel(preise), statistics.median(preise),
            mittel([s["marg"] for s in teil]),
            mittel([s["angebot"] for s in teil]),
            mittel([s["saldo"] for s in teil])))


def zeitscheiben(saetze, jahr, richtung):
    print(f"\n### {jahr}, {richtung}, Leistungspreis je Vier-Stunden-Produkt und Monat")
    produkte = sorted({s["produkt"] for s in saetze if s["richtung"] == richtung})
    print("| Monat | " + " | ".join(p.split("_", 1)[1] for p in produkte) + " |")
    print("|---" * (len(produkte) + 1) + "|")
    for m in range(1, 13):
        zeile = []
        for p in produkte:
            teil = [s["avg"] for s in saetze
                    if s["datum"].month == m and s["produkt"] == p]
            zeile.append("{:.1f}".format(mittel(teil)) if teil else "-")
        if any(z != "-" for z in zeile):
            print(f"| {m} | " + " | ".join(zeile) + " |")


if __name__ == "__main__":
    alle = {}
    for jahr, name in DATEIEN.items():
        pfad = os.path.join(BASIS, name)
        if not os.path.exists(pfad):
            continue
        alle[jahr] = einlesen(pfad)
        print(f"{jahr}: {len(alle[jahr])} Zeitscheiben gelesen")
    for jahr in sorted(alle):
        for richtung in ("pos", "neg"):
            tabelle(alle[jahr], jahr, richtung)
    for jahr in sorted(alle):
        for richtung in ("pos", "neg"):
            zeitscheiben(alle[jahr], jahr, richtung)
