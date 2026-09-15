import json, csv, time, urllib.request, urllib.parse, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://www.marktstammdatenregister.de/MaStR/Einheit/EinheitJson/GetErweiterteOeffentlicheEinheitStromerzeugung"
# Speicher (2496), Nettonennleistung > 1000 kW, absteigend nach Leistung
filt = "Energieträger~eq~'2496'~and~Nettonennleistung~gt~'1000'"
felder = ["MaStRNummer", "EinheitName", "BetriebsStatusName", "Bundesland", "InbetriebnahmeDatum",
          "StromspeichertechnologieBezeichnung", "Stromspeichertechnologie", "Batterietechnologie",
          "Bruttoleistung", "Nettonennleistung", "NutzbareSpeicherkapazitaet", "SpeicherEinheitMastrNummer"]
rows = []
page = 1
while True:
    q = urllib.parse.urlencode({"sort": "Nettonennleistung-desc", "page": page, "pageSize": 2000, "group": "", "filter": filt})
    req = urllib.request.Request(BASE + "?" + q, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        d = json.load(r)
    data = d.get("Data", [])
    if not data:
        break
    for x in data:
        rows.append({k: x.get(k) for k in felder})
    print("Seite", page, "Zeilen", len(data), "kleinste Leistung kW", data[-1]["Nettonennleistung"])
    if len(data) < 2000 or data[-1]["Nettonennleistung"] <= 1000:
        break
    page += 1
    time.sleep(1)
with open("mastr_speicher_ab_1MW.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=felder)
    w.writeheader()
    w.writerows(rows)
print("gesamt", len(rows))
from collections import Counter
print(Counter((r["StromspeichertechnologieBezeichnung"], r["BetriebsStatusName"]) for r in rows).most_common(20))
