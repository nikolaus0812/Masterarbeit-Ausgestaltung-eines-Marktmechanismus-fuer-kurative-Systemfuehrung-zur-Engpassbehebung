# -*- coding: utf-8 -*-
"""Gemeinsamer Datenzugriff fuer die Auswertungen der Schriftfassung.

**Warum es diese Datei gibt.** Am 23.09.2026 haben alle Auswertungen
zunaechst `be_pos` und `be_neg` aus `jahr_slots_2025.parquet` als
kurativen Reservierungspreis genommen. Das ist die **erste** Iteration:
ihr Median betraegt 15,87 und 16,70 Euro je Megawatt und Stunde, ihr
Maximum 488,48, naemlich der Deckel der Bisektion.

Die Arbeit weist die **zweite** Iteration aus. Sie steht in
`heatmap_stunden_2025.parquet` als `be_full_pos` und `be_full_neg` mit
einem Median von 12,22 und 9,85 und einem Maximum von 1008,00 und
510,48, also genau den Werten aus ERGEBNISSE Abschnitt 7.1.

Diese Datei fuehrt beide Quellen zusammen, damit der Fehler sich nicht
wiederholt: die Marktpreise und die belegte Leistung je Markt aus
`jahr_slots`, den Reservierungspreis der zweiten Iteration aus
`heatmap_stunden`.
"""
import pandas as pd

SLOTS = (r"C:\GIT-HUB\bess_dispatch_optimization\analysen\03_breakeven"
         r"\heatmaps\jahr_slots_2025.parquet")
STUNDEN = (r"C:\GIT-HUB\bess_dispatch_optimization\results\sensitivitaet"
           r"\sensi7_afrr_modellierung\0_basis\heatmap_stunden_2025.parquet")


def viertelstunden():
    """Viertelstunden mit Marktdaten und dem Preis der zweiten Iteration."""
    a = pd.read_parquet(SLOTS)
    a = a[~a["gesperrt"]].copy()
    a["day"] = pd.to_datetime(a["day"]).dt.normalize()
    a = a.drop(columns=["be_pos", "be_neg"])

    b = pd.read_parquet(STUNDEN)
    b = b[~b["gesperrt"]].copy()
    b["day"] = pd.to_datetime(b["day"]).dt.normalize()
    b = b[["day", "stunde", "be_full_pos", "be_full_neg"]].rename(
        columns={"be_full_pos": "res_ent", "be_full_neg": "res_lad"})

    d = a.merge(b, on=["day", "stunde"], how="inner", validate="many_to_one")
    d["monat"] = d["day"].dt.month
    return d


def stunden():
    """Stundenwerte des Reservierungspreises der zweiten Iteration."""
    b = pd.read_parquet(STUNDEN)
    b = b[~b["gesperrt"]].copy()
    b["day"] = pd.to_datetime(b["day"]).dt.normalize()
    b = b[["day", "stunde", "be_full_pos", "be_full_neg"]].rename(
        columns={"be_full_pos": "res_ent", "be_full_neg": "res_lad"})
    b["summe"] = b["res_ent"] + b["res_lad"]
    b["monat"] = b["day"].dt.month
    return b
