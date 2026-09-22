# Auftrag an das Analyse-Repository: Analysetage neu wählen

**Stand 22.09.2026.** Der Abschnitt *Der Text zum Kopieren* ist zum
Hineinkopieren in den Chat des Analyse-Repositorys gedacht. Anlass ist die
Frage des Verfassers, wie die Auswahl der Analysetage in Abschnitt 4.1 zu
begründen ist. Die Prüfung hat ergeben, dass eine der vier Begründungen nicht
mehr gilt.

---

## Der Text zum Kopieren

Abschnitt 4.1 muss begründen, warum gerade diese Tage gerechnet sind. Beim
Nachprüfen der vier Kriterien aus `main.py` ist eines durchgefallen. Der
Verfasser hat daraufhin entschieden, den Satz der Analysetage zu ändern.

### 1 Drei Kriterien stimmen, eines gilt nicht mehr

Nachgerechnet gegen die Rohdaten im Repository, jeweils über alle 365 Tage
des Jahres 2025:

| Tag | Kriterium aus `main.py` | nachgerechnet | Rang |
|---|---|---|---|
| 11.02.2025 | höchster Redispatch | 20 457 MW im Tagesmittel, beide Richtungen | **1** |
| 15.05.2025 | höchste aFRR-Kapazitätspreise | 66,87 €/(MW·h) im Tagesmittel | **1** |
| 26.08.2025 | höchste IDC-Arbitrage | 1603,7 €/MWh Tagesspanne des ID1 | **1** |
| 22.02.2025 | einzige Stunden ohne endlichen Verdrängungspreis | **gilt nicht mehr** | — |

**Zum 22.02.** Das Kriterium wurde am 17.09.2026 eingetragen. Im Gesamtlauf
vom 17.–19.09.2026 gibt es diese Stunden nicht mehr: `be_full_pos_offen` und
`be_full_neg_offen` sind im ganzen Jahr durchweg falsch, und die beiden
fraglichen Stunden des 22.02. tragen jetzt 19,30 (POS, Stunde 21) und 22,01
(NEG, Stunde 6) €/(MW·h). Vermutlich hat die Korrektur der
Kausalitätsbedingung des aFRR-Rückkaufs das mit behoben.

Der Tag sticht auch sonst nirgends heraus: Redispatch Rang 99,
aFRR-Energiepreise Rang 164 (positiv) und 117 (negativ), Tagesspanne des ID1
Rang 120, FCR Rang 322. Eine tragfähige Begründung für ihn gibt es nicht.

### 2 Der neue Satz: fünf Tage

Jeder Tag steht für ein Extrem eines der geführten Märkte, dazu der Netzbezug
und ein Tag, der die beiden Regelleistungsmärkte trennt.

| Tag | steht für | Wert | Rang 2025 |
|---|---|---|---|
| **20.01.2025** | größter Spread am Day-Ahead | 469,0 €/MWh (583,4 gegen 114,4) | **1** von 273 |
| **11.02.2025** | größter Redispatchbedarf | 20 457 MW im Tagesmittel | **1** von 365 |
| **06.05.2025** | FCR hoch bei niedriger aFRR-Leistung | FCR 113,5 €/MW, aFRR 15,6 €/(MW·h) | 16 bzw. 163 |
| **15.05.2025** | FCR **und** aFRR-Leistung zugleich am höchsten | FCR 169,9 €/MW, aFRR 66,9 €/(MW·h) | **1** und **1** |
| **26.08.2025** | größte Tagesspanne des ID1 | 1603,7 €/MWh | **1** von 365 |

**Der 22.02.2025 entfällt.**

Zur Begründung der beiden neuen Tage:

**20.01.2025.** Abschnitt 4.1 behauptet, der Day-Ahead weiche zuerst, und zwar
schon zwischen 10 und 15 €/(MW·h). Das ist die zentrale Ordnungsaussage des
Abschnitts, bisher geprüft an Tagen mit mittlerem bis geringem DA-Spread
(11.02. Rang 197, 22.02. Rang 236, 15.05. Rang 99, 26.08. Rang 64). Der 20.01.
trägt den dreifachen Spread und prüft die Aussage dort, wo sie am ehesten
kippen könnte. Er ist zugleich ein billiger FCR-Tag (Rang 280) und isoliert
den Effekt damit sauber.

**06.05.2025.** Am 15.05. sind FCR und aFRR-Leistung beide Rang 1, dort lässt
sich nicht trennen, welcher der beiden Märkte die Verdrängung treibt. Am 06.05.
liegt die FCR bei zwei Dritteln ihres Jahresmaximums, die aFRR-Leistung aber
nur bei einem Viertel. Nah dran wäre auch der 13.04. (FCR Rang 13, aFRR Rang
145); der 06.05. zieht die beiden etwas weiter auseinander.

**Ein Nebeneffekt.** `ERGEBNISSE…md` Abschnitt 8 führt als nicht belegt, dass
die FCR nie verdrängt werde — an vier Tagen sei das kein Beweis. Mit dem 15.05.
ist der Tag mit den höchsten FCR-Preisen des Jahres im Satz, und mit dem 06.05.
einer, an dem die FCR ohne teure aFRR danebensteht. Bleibt die FCR auch dort
bei null, trägt die Aussage deutlich weiter.

### 3 Was zu tun ist

1. **Preisgitter rechnen** für den **20.01.2025** und den **06.05.2025**, im
   Format der bestehenden Seiten, also zehn Kacheln über p_res von null bis
   200 €/(MW·h). Die Lieferung nach `kapitel_anhang`, wie die übrigen.
2. **`dispatch_preisgitter_2025-02-22.pdf` zurückziehen.**
3. **`main.py`, Liste `DAYS`** auf die fünf Tage setzen und die Kommentare mit
   den oben nachgerechneten Kriterien versehen. Das alte Kriterium des 22.02.
   bitte als überholt kennzeichnen und nicht stillschweigend löschen.
4. **`ERGEBNISSE…md` Abschnitt 2** um die beiden neuen Tage ergänzen, also die
   Tabellen der belegten Leistung je Markt, den Abschnitt 2.1 (bei welchem
   Preis jeder Markt weicht) und 2.2 (Bindungsgrad). Den 22.02. dort
   herausnehmen.
5. **Abschnitt 2.3 prüfen.** Die vier belegten Aussagen stützen sich auf die
   alten vier Tage. Vor allem ist zu prüfen, ob „der Day-Ahead weicht zuerst"
   am 20.01. hält und ob die FCR am 06.05. und am 15.05. wirklich bei null
   bleibt.
6. **`ERGEBNISSE…md` Abschnitt 5**, die gepaarte Tagestabelle zum aFRR-Liefermodus,
   führt den 22.02. mit +358 Prozent. Entweder auf die neuen Tage umstellen
   oder als historische Auswertung kennzeichnen.

Nicht betroffen ist die aFRR-Sensitivität selbst, denn sie rechnet seit dem
21.09.2026 Jahresläufe statt gepoolter Analysetage.

### 4 Was die Schriftfassung tut

Nichts, bis die neuen Preisgitter vorliegen. Anhang F führt weiter die vier
alten Seiten, und die Tagesliste in 4.1 bleibt unverändert. Sobald geliefert
ist, wächst Anhang F auf fünf Seiten, das Dokument also um eine Seite, und die
Tagesliste wird gegen die Tabelle aus Abschnitt 2 dieses Auftrags getauscht.

Die Einzelbefunde in 4.1 stützen sich auf den 11.02., den 15.05. und den
26.08. und bleiben davon unberührt.

### 5 Rückfrage

Falls fünf Tage zu viel sind: Der **06.05.** ist der am ehesten entbehrliche,
weil er kein Rang-1-Tag ist, sondern ein Trenntag. Ohne ihn bleibt aber offen,
ob die FCR oder die aFRR-Leistung die Verdrängung am 15.05. treibt.

---

## Wie geprüft wurde

Alles gegen die Rohdaten im Analyse-Repository, ohne Nachrechnen in der
Schriftfassung:

- Redispatch je Tag über `redispatch.redispatch_hourly_day`, Tagesmittel beider
  Richtungen, dieselbe Aggregation wie im Abbildungsskript.
- aFRR-Kapazitätspreis aus
  `Regelleistung_regelleistung.net/aFRR_Leistung/RESULT_OVERVIEW_CAPACITY_MARKET_aFRR_2025…`,
  Spalte `TOTAL_AVERAGE_CAPACITY_PRICE_[(EUR/MW)/h]`, Tagesmittel.
- FCR-Preis aus der entsprechenden FCR-Datei, Spalte
  `GERMANY_SETTLEMENTCAPACITY_PRICE_[EUR/MW]`, Tagesmittel.
- ID1-Spanne und Day-Ahead-Spread aus
  `Strompreise_energy-charts.de/strom_preise_de_2025_*.parquet`, Tagesmaximum
  minus Tagesminimum.
- aFRR-Energiepreise aus `afrr_ene_vwap.parquet`, Tagesmittel je Richtung.
- Offene Stunden aus `jahr_stunden_2025.parquet` des Gesamtlaufs.

**Ein Vorbehalt zum Day-Ahead-Spread.** Die Stundenreihe reicht nur bis zum
30.09.2025, weil der Day-Ahead ab dem 01.10.2025 in Viertelstunden gehandelt
wird; der Rang 1 von 273 bezieht sich auf diesen Zeitraum. Für Oktober bis
Dezember liegt die größte Viertelstundenspanne bei 422,2 €/MWh am 14.10. und
damit unter den 469,0 des 20.01. Eine Viertelstundenspanne ist nie kleiner als
die Stundenspanne desselben Tages, also bleibt der 20.01. auch im vollen Jahr
vorn.
