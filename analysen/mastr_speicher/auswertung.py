"""Energieinhalt je Leistung der Speicher am deutschen Netz aus dem Marktstammdatenregister.

Eingabe: mastr_speicher_auszug_2026-09-15.csv, erzeugt mit download.py am 15.09.2026.
Der Auszug enthaelt alle Einheiten mit Energietraeger Speicher, absteigend nach
Nettonennleistung, bis unter 1 MW (2000 Zeilen, kleinste Leistung 184 kW).
Leistungen in kW, Speicherkapazitaet in kWh, wie im Register.

Ausgabe: pskw_werke.csv (je Werk) und die Kennzahlen auf der Konsole.
"""
import csv
import datetime
import os
import re
import statistics
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))
rows = list(csv.DictReader(open("mastr_speicher_auszug_2026-09-15.csv", encoding="utf-8")))


def f(x):
    return float(x) if x not in ("", "None", None) else None


# ---------------------------------------------------------------- PSKW
# Das Register fuehrt je Maschinensatz eine Einheit und traegt bei jeder Einheit
# die nutzbare Speicherkapazitaet des ganzen Werks. Die Einheiten eines Werks
# werden deshalb ueber das Paar (Bundesland, Speicherkapazitaet) zusammengefasst
# und die Leistungen summiert.
ps = [r for r in rows if r["StromspeichertechnologieBezeichnung"] == "Pumpspeicher"
      and r["BetriebsStatusName"] == "In Betrieb"]
werke = defaultdict(lambda: {"P_kW": 0.0, "n": 0, "namen": set()})
for r in ps:
    key = (r["Bundesland"], f(r["NutzbareSpeicherkapazitaet"]))
    werke[key]["P_kW"] += f(r["Nettonennleistung"])
    werke[key]["n"] += 1
    werke[key]["namen"].add(re.split(r" (M|MS|PSS|F|Bl|Maschine|PSW|R|T|Pe|-)\b", r["EinheitName"])[0])

tab = []
for (bl, E), v in werke.items():
    ep = E / v["P_kW"]
    # Deutsche Werke mit Tages- oder Wochenspeicher: Bundesland gesetzt und
    # Energieinhalt je Leistung bis 24 h. Ausgeschlossen sind damit die
    # oesterreichischen und luxemburgischen Werke ohne Bundesland (illwerke vkw,
    # Vianden, Silz, Kuehtai, Obervermuntwerk) und die Werke an Jahresspeichern
    # (Schluchseegruppe Haeusern, Witznau, Waldshut; Bleiloch; Schwarzenbach).
    aufgenommen = bool(bl) and ep <= 24
    tab.append({"Bundesland": bl, "Werk": "; ".join(sorted(v["namen"])), "Einheiten": v["n"],
                "P_MW": round(v["P_kW"] / 1000, 1), "E_MWh": round(E / 1000, 1),
                "E_je_P_h": round(ep, 2), "aufgenommen": int(aufgenommen)})
tab.sort(key=lambda t: -t["P_MW"])
with open("pskw_werke.csv", "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(tab[0].keys()))
    w.writeheader()
    w.writerows(tab)

de = [t for t in tab if t["aufgenommen"]]
eps = sorted(t["E_je_P_h"] for t in de)
P = sum(t["P_MW"] for t in de)
E = sum(t["E_MWh"] for t in de)
print(f"PSKW in Betrieb: {len(ps)} Einheiten, {sum(f(r['Nettonennleistung']) for r in ps) / 1000:.0f} MW gesamt")
print(f"Deutsche Werke mit E/P <= 24 h: {len(de)} Werke, {P:.0f} MW, {E:.0f} MWh")
print(f"  E/P Spanne {eps[0]:.1f} bis {eps[-1]:.1f} h, Median {statistics.median(eps):.1f} h, "
      f"leistungsgewichtet {E / P:.1f} h, Quartile {eps[len(eps) // 4]:.1f} und {eps[3 * len(eps) // 4]:.1f} h")

# ---------------------------------------------------------------- BESS


def jahr(s):
    m = re.search(r"Date\((\d+)\)", s or "")
    return datetime.datetime.fromtimestamp(int(m.group(1)) / 1000, datetime.UTC).year if m else None


for status in ("In Betrieb", "In Planung"):
    b = [r for r in rows if r["StromspeichertechnologieBezeichnung"] == "Batterie"
         and r["BetriebsStatusName"] == status and f(r["Nettonennleistung"]) >= 1000
         and f(r["NutzbareSpeicherkapazitaet"])]
    ep = sorted(f(r["NutzbareSpeicherkapazitaet"]) / f(r["Nettonennleistung"]) for r in b)
    Pb = sum(f(r["Nettonennleistung"]) for r in b)
    Eb = sum(f(r["NutzbareSpeicherkapazitaet"]) for r in b)
    print(f"BESS {status} ab 1 MW: {len(b)} Einheiten, {Pb / 1000:.0f} MW, {Eb / 1000:.0f} MWh, "
          f"E/P leistungsgewichtet {Eb / Pb:.2f} h, Median {statistics.median(ep):.2f} h, "
          f"Quartile {ep[len(ep) // 4]:.2f} und {ep[3 * len(ep) // 4]:.2f} h")
    if status == "In Betrieb":
        byj = defaultdict(list)
        for r in b:
            byj[jahr(r["InbetriebnahmeDatum"])].append((f(r["NutzbareSpeicherkapazitaet"]), f(r["Nettonennleistung"])))
        for j in sorted(k for k in byj if k and k >= 2018):
            v = byj[j]
            print(f"  Inbetriebnahme {j}: {len(v)} Einheiten, {sum(p for e, p in v) / 1000:.0f} MW, "
                  f"E/P leistungsgewichtet {sum(e for e, p in v) / sum(p for e, p in v):.2f} h, "
                  f"Median {statistics.median(e / p for e, p in v):.2f} h")
