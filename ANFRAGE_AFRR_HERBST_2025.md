# Anfrage: warum steigt der aFRR-Leistungspreis im Herbst 2025

**Stand 23.09.2026.** Absender ist die Schriftfassung der Masterarbeit
*Ausgestaltung eines Marktmechanismus für kurative Systemführung zur
Engpassbehebung* am IAEW der RWTH Aachen.

Adressat ist ein getrennter Chat, der auf **SMARD** und die **öffentlichen
Quellen der Bundesnetzagentur** zugreift, dazu auf regelleistung.net, die
Übertragungsnetzbetreiber und energy-charts.

---

## 1 Worum es geht

Die Arbeit bestimmt den kurativen Reservierungspreis eines Batteriespeichers
aus seinen Opportunitätskosten an den Märkten. Kapitel 4 beschreibt, wie dieser
Preis über das Jahr 2025 schwankt. Zwei Auffälligkeiten sollen im Text nicht
nur beschrieben, sondern begründet werden.

Eine eigene Auswertung der Marktpreise des Jahres 2025 hat ergeben, dass der
Preis in beiden Richtungen dem **aFRR-Leistungspreis** folgt. Damit verlagert
sich die Frage auf den Regelleistungsmarkt, und dort endet, was die Daten der
Arbeit hergeben.

---

## 2 Die Hauptfrage

**Warum liegt der Leistungspreis der positiven aFRR im September und Oktober
2025 rund beim Doppelten des übrigen Jahres?**

Eigene Auswertung, arithmetisches Mittel über alle 35 032 ausgewerteten
Viertelstunden des Jahres 2025, in Euro je Megawatt und Stunde. Zugrunde liegt
die Spalte `GERMANY_AVERAGE_CAPACITY_PRICE` aus der Datei
`RESULT_OVERVIEW_CAPACITY_MARKET_aFRR_2025-01-01_2025-12-31.xlsx` von
regelleistung.net, je Vier-Stunden-Produkt auf die Viertelstunden gelegt:

| Monat | aFRR positiv | aFRR negativ |
|---|---|---|
| Januar | 12,6 | 4,9 |
| Februar | 13,5 | 3,0 |
| März | 12,2 | 11,2 |
| April | 15,5 | 19,7 |
| Mai | 20,6 | 32,2 |
| Juni | 19,5 | 27,3 |
| Juli | 14,4 | 15,8 |
| August | 14,4 | 19,0 |
| **September** | **34,2** | 27,4 |
| **Oktober** | **31,2** | 16,5 |
| November | 16,8 | 6,9 |
| Dezember | 10,6 | 3,4 |

September und Oktober zusammen liegen bei 32,7 gegen 15,0 in den übrigen zehn
Monaten, also beim 2,2-Fachen. Jeder andere Monat liegt zwischen 10,6 und 20,6.

**Gesucht sind Erklärungen, die sich belegen lassen.** In Betracht kommen aus
unserer Sicht, ohne Anspruch auf Vollständigkeit:

1. Kraftwerksrevisionen im Herbst, die präqualifizierte Leistung vom Markt
   nehmen.
2. Eine Schwachwindphase, die zugleich die Energiepreise hebt und Anbieter
   bindet.
3. Änderungen an der Ausschreibung oder am Bedarf, etwa eine Anpassung der
   dimensionierten Regelleistungsmenge oder der Zeitscheiben.
4. Ein Ereignis im Netzbetrieb, etwa eine Häufung von Fahrplanabweichungen.

Bitte prüfen, welche davon die Daten tragen, und die übrigen ausdrücklich
verwerfen. Falls keine Quelle die Höhe erklärt, ist auch das ein Ergebnis und
soll so gesagt werden.

---

## 3 Die Nebenfrage

**Warum steigt der Leistungspreis der negativen aFRR von Frühjahr bis Sommer?**

Von 3,0 Euro je Megawatt und Stunde im Februar auf 32,2 im Mai, danach wieder
zurück auf 3,4 im Dezember. Unsere eigene Deutung lautet, dass die
Photovoltaik-Einspeisung mittags die Preise ins Negative drückt und zugleich
die Anbieter negativer Regelleistung verknappt, weil weniger Erzeugung am Netz
ist, die sich herunterregeln lässt.

Diese Deutung steht bislang ohne Beleg im Raum. **Gesucht ist eine zitierfähige
Quelle**, die den Zusammenhang zwischen hoher Solareinspeisung und dem Preis
negativer Regelleistung beschreibt, etwa ein Monitoringbericht der
Bundesnetzagentur, eine Veröffentlichung der Übertragungsnetzbetreiber oder
eine begutachtete Arbeit.

Zur Einordnung: der Anteil der Viertelstunden mit negativem Intradaypreis
beträgt in unserer Auswertung 0 bis 2 Prozent im Winter und 17 bis 22 Prozent
im Mai und Juni.

---

## 4 Eine dritte Beobachtung, nachrangig

Der Juli fällt aus dem Sommer heraus: der Leistungspreis der negativen aFRR
sinkt von 29,8 im Mai und Juni auf 15,8, der Anteil negativer Viertelstunden
von 20 auf 6 Prozent, und die Energiepreise steigen von 69,8 auf 89,1 Euro je
Megawattstunde. Falls sich das mit einer bekannten Wetterlage oder einer
Revisionsphase deckt, wäre ein Hinweis nützlich. Ohne Beleg bleibt der Punkt
unerwähnt.

---

## 5 Was die Antwort tragen muss

Die Arbeit zitiert mit biblatex. Für jede Aussage, die in den Text soll, wird
gebraucht:

- die Fundstelle mit Seite oder Abschnitt,
- eine belastbare URL mit Abrufdatum, bei SMARD zusätzlich die gewählte
  Auswertung und der Zeitraum,
- Herausgeber, Titel und Jahr in einer Form, aus der sich ein
  `literature.bib`-Eintrag bilden lässt.

**Keine Schätzungen und keine Plausibilitätsargumente ohne Quelle.** Die Arbeit
führt unbelegte Aussagen als offene Punkte und nimmt sie nicht in den Text. Ein
begründetes „dazu gibt es keine öffentliche Quelle" ist brauchbarer als eine
plausible Vermutung.

Sollten die Zahlen aus Abschnitt 2 einer öffentlichen Reihe widersprechen, ist
das der wichtigste Teil der Antwort. Unsere Werte stammen aus den
Eingangsdaten des Optimierungsmodells, also aus der in Abschnitt 2 genannten
Datei. Ein Abgleich gegen die von regelleistung.net veröffentlichte Reihe wäre
für sich genommen schon wertvoll. Zu beachten ist, dass der Mittelwert über die
Viertelstunden ungewichtet gebildet ist und dass acht Viertelstunden des Jahres
als ungültig ausgeschlossen sind.

---

## 6 Was nicht gebraucht wird

Keine Einführung in den Regelleistungsmarkt, keine Erklärung der
Produktzuschnitte und keine Beschreibung des Gebotsverfahrens. Alles davon
steht in Kapitel 2 der Arbeit und ist belegt. Gesucht ist allein die Erklärung der
beiden Preisbewegungen des Jahres 2025.
