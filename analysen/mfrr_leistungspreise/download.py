"""Laedt die Ergebnisuebersicht des mFRR-Leistungsmarkts je Tag 2025 von regelleistung.net."""
import datetime
import os
import time
import urllib.request

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs("mfrr_2025", exist_ok=True)
URL = ("https://www.regelleistung.net/apps/cpp-publisher/api/v1/download/tenders/resultsoverview"
       "?date={d}&exportFormat=xlsx&market=CAPACITY&productTypes=mFRR")
tag = datetime.date(2025, 1, 1)
fehler = []
while tag.year == 2025:
    ziel = f"mfrr_2025/{tag.isoformat()}.xlsx"
    if not os.path.exists(ziel):
        try:
            req = urllib.request.Request(URL.format(d=tag.isoformat()), headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=120) as r:
                daten = r.read()
            if daten[:2] == b"PK":
                open(ziel, "wb").write(daten)
            else:
                fehler.append(tag.isoformat())
        except Exception as e:
            fehler.append(f"{tag.isoformat()} {e}")
        time.sleep(0.5)
    tag += datetime.timedelta(days=1)
print("fertig, Fehler:", fehler)
