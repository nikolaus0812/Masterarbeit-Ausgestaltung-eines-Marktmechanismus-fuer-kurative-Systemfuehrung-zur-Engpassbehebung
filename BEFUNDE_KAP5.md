# Befunde der Kontrollprüfung von Kapitel 5

**Angelegt am 26.09.2026, Register geschlossen am 26.09.2026.** Grundlage war
die Kontrollprüfung nach `archiv/UEBERGABE_KAP5_PRUEFUNG.md`. Alle Befunde
B1 bis B35 sind auf Vorgabe des Verfassers umgesetzt oder mit Begründung
hingenommen. **Nichts ist offen.**

Die Entscheidungen stehen im Entscheidungsprotokoll unter `## chapter_5.tex`
in den fünf Einträgen vom 26.09.2026. Der ersetzte Wortlaut steht je Stelle
als Kommentar mit Datum und Befund in `chapters/chapter_5.tex`. Die
ausführliche Fassung dieser Datei mit Wortlaut und Begründung je Befund liegt
in der Git-Historie unter `af07967`.

Stellenangaben nennen Abschnitt und Absatz, denn Zeilennummern haben sich mit
dem Umbau mehrfach verschoben.

---

## Prüfstand nach dem letzten Durchgang

| Prüfung | Ergebnis |
|---|---|
| `python tools/pruefen.py --alle` | ohne Befund, 15 Dateien |
| `python tools/pruefe_stil.py` | Kapitel 4 und 5 ohne Verstoß, Kapitel 1 bis 3 nur Altbefunde Doppelpunkt |
| `python tools/absatzlaengen.py chapters/chapter_5.tex` | alle Absätze bei 8 Sätzen, Einleitung eingeschlossen |
| Build | 124 Seiten, Biber ohne Warnung, allein `ch:conc` undefiniert, weil Kapitel 6 auskommentiert ist |

Umfang: Einleitung 8 Sätze, 5.1 zwölf Absätze, 5.2 sieben, 5.3 sechs, 5.4
fünf, 5.5 sechs. Zwei Zitate im Kapitel, nämlich Weber und Mahgoub in 5.2 und
Consentec in 5.4; alle übrigen Quellen sind über die Kapitel 1 bis 4 im
Verzeichnis.

---

## Register

| Nr | Befund | Stelle | Erledigung |
|---|---|---|---|
| B1 | *des Mechanismus* ohne Adjektiv | 5.5 Aufwand | Absatz gestrichen, Nachweis nach 5.1 verschoben |
| B2 | absolute Feststellung zu § 13c ohne Beleg | 5.5 A1 | Absatz neu, § 13c wird nicht mehr gebraucht |
| B3 | *eine solche Beschaffung* ohne Bezugswort | 5.1 A4 | Satz neu |
| B4 | Numerusfehler *jede … sie* | 5.4 A4 | behoben |
| B5 | Pronomen über die Satzgrenze | 5.2 A6, 5.3 A3 zweimal, 5.4 A3 | drei ausgeschrieben, eine Stelle gestrichen |
| B6 | Präqualifikation doppelt | 5.4 A1, 5.5 | 5.4 A1 gestrichen |
| B7 | Zuschlag als Netzauskunft doppelt | 5.1 A6, 5.4 A3 | **hingenommen**, Prämisse gegen Folge |
| B8 | aFRR-Erlösanteil doppelt | 5.1 A9, 5.2 A3 | Nebensatz in 5.1 gestrichen |
| B9 | Liefertag doppelt | 5.2 A1, A7 | A1 kündigt nur an |
| B10 | einzelne Anlage doppelt | 5.2 A7, 5.5 A6 | 5.5 greift zurück |
| B11 | Abrufwahrscheinlichkeit und Pönale dreimal | 5.1 A7, 5.2 A7, 5.5 A6 | Nebensatz in 5.1 gestrichen |
| B12 | Lage der Ausschreibung dreimal | 5.1 A5, A9, 5.2 A3 | 5.1 A9 verkürzt |
| B13 | Ablösung doppelt | 5.3 A5, 5.5 A3 | **hingenommen**, Kostensicht gegen Betriebssicht |
| B14 | fast wörtlich aus Kapitel 2 | 5.4 A1 | gestrichen |
| B15 | fast wörtlich aus Kapitel 3 | 5.1 A2 | **hingenommen**, Nennung der Anforderung |
| B16 | fast wörtlich aus Kapitel 4 | 5.3 A4 | Eröffnung trägt jetzt eine These |
| B17 | *halbe Stunde* statt Megawattstunde je Megawatt | 5.3 A5 | Einheit gesetzt |
| B18 | Handelsschluss verallgemeinert | 5.4 A1 | *innerhalb der Regelzone* |
| B19 | *gemessene Spanne* | 5.2 A2 | *der vorsichtigere Wert* |
| B20 | Aufschlag nur relativ gelesen | 5.4 A5 | relativ steigt, absolut sinkt |
| B21 | *das ganze Jahr über* gegen 362 von 365 | Kapitel 4, Zeile 863 | *fast das ganze Jahr über* |
| B22 | *damit* ohne Begründung | 5.1 A2 | Satz neu |
| B23 | *wenig Regulierung* unbelegt | 5.1 A4 | Satz neu |
| B24 | *Anschließend* doppelt | Einleitung | *Danach* |
| B25 | Ankündigung von 5.4 nur halb | Einleitung | neu, mit Engpassmanagement |
| B26 | drei überholte Ableitungsmarken | Quelltext | datierte ERLEDIGT-Zeile davor, nichts gelöscht |
| B27 | Kopfkommentar mit erledigten Punkten | Quelltext | datierte ERLEDIGT-Zeile |
| B28 | *Abrufdauer* in Kapitel 4 | Kapitel 4 | bleibt zulässig, Entscheidung des Verfassers |
| B29 | § 13c ohne Beleg | Kapitel 2, Zeile 1295 | Beleg gesetzt |
| B30 | Binnenmarktverordnung fast wörtlich aus Kapitel 2 | 5.5 A2 | gestrichen |
| B31 | *Lieferfähigkeit* gegen *Verfügbarkeit* | 5.1 A7, A10, A11 | Verfügbarkeit bei der Einplanung, Lieferfähigkeit im Fehlerfall |
| B32 | acht Anforderungen *der Reihe nach* versprochen, sieben geliefert | 5.1 A1, A12 | *der Reihe nach* gestrichen, Zwischenfazit nennt die Umsetzbarkeit als achte |
| B33 | A1 kündigt die stärkste Annahme nicht an | 5.2 A1 | Sätze 4 bis 7 in Absatzreihenfolge, Preiskenntnis aufgenommen |
| B34 | Zahlen über die Vorgabe hinaus | 5.1 A5, 5.4 A2, Kopfkommentar | 23.30 Uhr und § 17 in 5.4 gestrichen, drei behalten mit Grund, Kopfkommentar datiert nachgezogen |
| B35 | *Zeitscheibe von einem Tag* war eine Deutung | 5.3 A5 | zwei Sätze erklären den einheitlichen Preis je Tag nach Kapitel 4, Füllsatz zur vorgehaltenen Energie gefallen |

**Eigenständige Ableitungen der Übergabe.** Nummer 1 bis 4 vom Verfasser am
26.09.2026 bestätigt, die Marken tragen eine datierte Zeile. Nummer 5 ist
erledigt, weil der Satz zum Preisniveau der Zone zurückgenommen ist.

---
