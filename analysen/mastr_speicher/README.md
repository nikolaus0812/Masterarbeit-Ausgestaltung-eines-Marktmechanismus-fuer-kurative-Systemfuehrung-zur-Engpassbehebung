# Energieinhalt je Leistung aus dem Marktstammdatenregister

Beleg für die Spalte *Energiebindung, Energieinhalt je Leistung* in Tabelle 2.1
und für den Satz zu den PSKW in Abschnitt 2.1.3. Stand 15.09.2026.

## Quelle

Bundesnetzagentur, Marktstammdatenregister, öffentliche Einheitenübersicht
Stromerzeugung, Energieträger Speicher. Abruf am 15.09.2026 über den
JSON-Endpunkt der Einheitenübersicht mit `download.py`. Der Auszug
`mastr_speicher_auszug_2026-09-15.csv` enthält die 2000 leistungsstärksten
Speichereinheiten, absteigend nach Nettonennleistung, bis 184 kW. Damit sind
alle Einheiten ab 1 MW enthalten. Leistungen in kW, Speicherkapazität in kWh.

## Verfahren

`auswertung.py` rechnet je Einheit den Energieinhalt je Leistung als nutzbare
Speicherkapazität durch Nettonennleistung.

PSKW: Das Register führt je Maschinensatz eine Einheit und trägt bei jeder
Einheit die nutzbare Speicherkapazität des ganzen Werks. Die Einheiten werden
über das Paar Bundesland und Speicherkapazität zu Werken zusammengefasst, die
Leistungen summiert. Aufgenommen sind deutsche Werke mit Tages- oder
Wochenspeicher, also mit gesetztem Bundesland und höchstens 24 Stunden
Energieinhalt je Leistung. Ausgeschlossen sind die österreichischen und
luxemburgischen Werke, die im Register ohne Bundesland stehen (illwerke vkw,
Vianden, Silz, Kühtai, Obervermuntwerk), und die Werke an Jahresspeichern
(Schluchseegruppe mit Häusern, Witznau und Waldshut, Bleiloch, Schwarzenbach).
Die Zuordnung steht in `pskw_werke.csv`, Spalte `aufgenommen`.

BESS: Einheiten mit Stromspeichertechnologie Batterie ab 1 MW
Nettonennleistung, getrennt nach Betriebsstatus und nach Jahr der
Inbetriebnahme.

## Ergebnis

| Gruppe | Anzahl | Leistung | Energieinhalt je Leistung |
|---|---|---|---|
| PSKW in Betrieb, deutsche Werke mit Tages- oder Wochenspeicher | 18 Werke | 5,7 GW | 3,0 bis 9,0 h, Median 5,4 h, leistungsgewichtet 5,7 h, Quartile 4,4 und 6,7 h |
| BESS in Betrieb ab 1 MW | 520 Einheiten | 4,2 GW | Median 2,0 h, Quartile 1,1 und 2,2 h, leistungsgewichtet 1,8 h |
| BESS in Betrieb, Inbetriebnahme 2022 | 53 | 0,5 GW | Median 1,0 h |
| BESS in Betrieb, Inbetriebnahme 2025 | 102 | 0,8 GW | Median 2,1 h |
| BESS in Betrieb, Inbetriebnahme 2026 | 165 | 1,6 GW | Median 2,0 h |
| BESS in Planung ab 1 MW | 685 | 11,6 GW | Median 2,0 h, Quartile 2,0 und 2,2 h, leistungsgewichtet 3,0 h |

Der leistungsgewichtete Wert der geplanten BESS liegt wegen weniger Vorhaben
mit vier Stunden Energieinhalt je Leistung über dem Median.

Für Tabelle 2.1 folgt daraus: PSKW 3 bis 9 h, BESS 1 bis 2 h mit steigender
Tendenz. Die Battery Charts weisen denselben Anstieg von einer auf zwei
Stunden aus.
