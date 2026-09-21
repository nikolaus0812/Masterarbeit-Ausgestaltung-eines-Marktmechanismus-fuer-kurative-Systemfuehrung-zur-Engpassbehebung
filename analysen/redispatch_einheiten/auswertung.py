"""Redispatch-Massnahmen der UeNB im Jahr 2025 je Einheit.

Beleg fuer den Satz in Abschnitt 1.1, dass sich der Redispatch bisher auf
wenige grosse Anlagen stuetzt. Stand 21.09.2026.

Quelle: Netztransparenz, Liste der Redispatch-Massnahmen 2025, Eintrag
netztransparenz_regelenergie_2026. Die Rohdaten liegen im Modellrepository
unter data/processed/Redispatch_netztransparnez.net/2025_Redispatchmassnahmen.parquet
und nicht in diesem Repository.

Aufruf mit dem Interpreter des Modellrepositorys:
  C:/ProgramData/anaconda3/envs/venv_mode/python.exe auswertung.py
"""
import sys
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")
QUELLE = (r"C:\GIT-HUB\bess_dispatch_optimization\data\processed"
          r"\Redispatch_netztransparnez.net\2025_Redispatchmaßnahmen.parquet")

df = pd.read_parquet(QUELLE)
for c in ["MITTLERE_LEISTUNG_MW", "MAXIMALE_LEISTUNG_MW", "GESAMTE_ARBEIT_MWH"]:
    df[c] = pd.to_numeric(df[c].astype(str).str.replace(".", "", regex=False)
                          .str.replace(",", ".", regex=False), errors="coerce")

# Nur Redispatch: ohne Countertrading (Boerse, Countertrade DE-DK), Probe- und Testfahrten
rd = df[df.GRUND_DER_MASSNAHME.str.contains("Redispatch") & ~df.BETROFFENE_ANLAGE.eq("Börse")]
g = (rd.groupby("BETROFFENE_ANLAGE")
       .agg(massnahmen=("GESAMTE_ARBEIT_MWH", "size"),
            arbeit_mwh=("GESAMTE_ARBEIT_MWH", "sum"),
            pmax_mw=("MAXIMALE_LEISTUNG_MW", "max"),
            primaerenergie=("PRIMAERENERGIEART", "first"))
       .sort_values("arbeit_mwh", ascending=False))
tot = g.arbeit_mwh.sum()

zeilen = []
zeilen.append(f"Massnahmen gesamt: {len(df)}, Einheiten gesamt: {df.BETROFFENE_ANLAGE.nunique()}")
zeilen.append(f"Nur Redispatch: {len(rd)} Massnahmen, {tot/1000:.1f} GWh, {len(g)} Einheiten")
richt = rd.groupby("RICHTUNG").GESAMTE_ARBEIT_MWH.sum() / 1000
zeilen.append("Richtung GWh: " + ", ".join(f"{k}: {v:.1f}" for k, v in richt.items()))
art = rd.groupby("PRIMAERENERGIEART").GESAMTE_ARBEIT_MWH.sum() / 1000
zeilen.append("Primaerenergie GWh: " + ", ".join(f"{k}: {v:.1f}" for k, v in art.items()))
for s in (100, 300, 500):
    sel = g[g.pmax_mw >= s]
    zeilen.append(f"Einheiten mit Pmax >= {s} MW: {len(sel)}, Anteil an der Arbeit {sel.arbeit_mwh.sum()/tot*100:.1f} %")
g["kumuliert"] = g.arbeit_mwh.cumsum() / tot
for q in (0.5, 0.8, 0.9):
    zeilen.append(f"{int(q*100)} % der Arbeit: groesste {int((g.kumuliert <= q).sum()) + 1} Einheiten")
print("\n".join(zeilen))
g.to_csv("redispatch_einheiten_2025.csv", sep=";", decimal=",", encoding="utf-8")
with open("ergebnis.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(zeilen) + "\n")
