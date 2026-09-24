# Befund: der Leistungspreis der aFRR im Herbst 2025

Stand 24.09.2026. Vorgehen und Quellen in `README.md`. Alle Preise in Euro je
Megawatt und Stunde, alle Mengen in Megawatt, jeweils arithmetisches Mittel
über die Vier-Stunden-Zeitscheiben.

---

## 0 Abgleich der eigenen Monatswerte

Die Monatswerte der Anfrage sind reproduziert. Die Jahresdatei liefert für die
positive aFRR 12,6 / 13,5 / 12,1 / 15,5 / 20,6 / 19,5 / 14,4 / 14,4 / 34,2 /
31,2 / 16,8 / 10,6. Die Anfrage nennt für den März 12,2 statt 12,1, weil sie
über Viertelstunden mittelt und acht ungültige Viertelstunden ausschließt,
während hier über Zeitscheiben gemittelt wird. Die Abweichung beträgt 0,1 und
betrifft keinen Befund. **Die Eingangsdaten des Optimierungsmodells sind damit
gegen die Quelldatei bestätigt.**

---

## 1 Die Preisverdopplung ist ein Angebotsereignis

| Größe | 2024 Sep/Okt | 2024 übrige | 2025 Sep/Okt | 2025 übrige |
|---|---|---|---|---|
| Leistungspreis positiv | 14,7 | 12,8 | **32,7** | **15,0** |
| Grenzpreis positiv | 18,3 | 18,1 | **59,1** | 21,5 |
| angebotene Menge positiv | 4591 | 4338 | **3849** | 4337 |
| Leistungspreis negativ | 13,1 | 10,4 | 21,8 | 14,4 |
| angebotene Menge negativ | 3510 | 3584 | **3254** | 3701 |

Drei Befunde stehen fest.

1. **Der Herbst 2025 ist kein wiederkehrendes Muster.** Im Jahr 2024 liegt der
   September bei 14,9 und der Oktober bei 14,5 gegen ein Jahresmittel von 13,1.
   Ein Herbstaufschlag von 15 Prozent ist etwas anderes als das 2,2-Fache.
2. **Die angebotene Menge erreicht im September und Oktober 2025 ihr
   Jahresminimum**, nämlich 3804 und 3893 gegen 4337 in den übrigen zehn
   Monaten, also 11 Prozent weniger. Im Jahr 2024 war es umgekehrt: dort lag
   das Angebot im Herbst mit 4591 über dem Jahreswert.
3. **Die beschaffte Menge ist unverändert.** Die Spalte
   `GERMANY_ALLOCATED_VOLUME` wird erst ab dem 03.09.2025 geführt und liegt von
   September bis Dezember konstant zwischen 1986 und 2024 MW. Eine Anpassung
   der dimensionierten Regelleistungsmenge im Herbst ist damit für den Zeitraum,
   für den Daten vorliegen, ausgeschlossen.

## 2 Der Preis folgt 2025 der Angebotsmenge und nicht der Marktlage

Tageskorrelation des Leistungspreises der positiven aFRR, n = 365 beziehungsweise 366.

| Gegengröße | 2024 | 2025 |
|---|---|---|
| angebotene Menge | +0,00 | **−0,61** |
| Intradaypreis, Tagesmittel | +0,48 | +0,18 |
| Tagesspanne des Intradaypreises | +0,35 | +0,26 |
| Residuallast, Tagesmittel | +0,28 | +0,12 |

Im Jahr 2024 folgt der Leistungspreis dem Energiepreis, und die Angebotsmenge
ist ohne Einfluss. Im Jahr 2025 kehrt sich das um. **Die Erklärung über die
Energiepreise trägt für 2025 nicht.**

Die Preis-Mengen-Beziehung je Zeitscheibe bestätigt das.

| angebotene Menge | 2024 Preis | 2025 Preis | 2025 Sep/Okt | 2025 übrige |
|---|---|---|---|---|
| unter 3400 | 33,9 | 57,1 | 65,8 | 36,5 |
| 3400 bis 3700 | 12,3 | 33,8 | 38,7 | 29,0 |
| 3700 bis 4000 | 12,6 | 23,5 | 27,3 | 21,9 |
| 4000 bis 4300 | 13,0 | 16,2 | 24,2 | 14,9 |
| 4300 bis 4600 | 13,1 | 12,8 | 20,3 | 12,2 |
| über 4600 | 13,2 | 11,1 | 21,6 | 10,9 |

Im Jahr 2024 ist der Preis über alle Mengenklassen flach, nämlich 12 bis 13.
Im Jahr 2025 steigt er von 11,1 auf 57,1, sobald das Angebot knapp wird.
**Die Angebotskurve ist 2025 steil, 2024 war sie flach.**

Zugleich liegt der September und Oktober 2025 in jeder Mengenklasse über den
übrigen Monaten, etwa 27,3 gegen 21,9 bei 3700 bis 4000 MW. Damit zerfällt die
Verdopplung in zwei etwa gleich große Teile: die geringere Angebotsmenge und
ein höheres Gebotsniveau bei gleicher Menge. Rechnerisch läge der September und
Oktober bei der Angebotsmenge der übrigen Monate bei rund 20 bis 24 statt bei
32,7, die übrigen Monate liegen bei dieser Menge bei rund 14.

## 3 Was die vier Vermutungen der Anfrage betrifft

**Kraftwerksrevisionen, nicht bestätigt.** Als Kennzahl für die verfügbare
konventionelle Leistung dient das 95-Prozent-Quantil und das Maximum der nicht
erneuerbaren Erzeugung je Monat. Beide liegen im September und Oktober 2025 mit
23,3 und 29,2 GW beziehungsweise 26,8 und 32,4 GW auf oder über dem Niveau von
2024, nämlich 22,3 und 28,1 GW beziehungsweise 25,3 und 31,6 GW. Eine
allgemeine Revisionswelle ist in dieser Kennzahl nicht zu sehen. Die Kennzahl
misst allerdings die Erzeugung und nicht die präqualifizierte Leistung, sodass
der Ausfall einzelner präqualifizierter Einheiten unentdeckt bleiben kann.

**Schwachwindphase, verworfen, mit einem Nebenbefund.** Die Residuallast liegt
im September mit 19,8 GW und im Oktober mit 20,9 GW unter dem Jahresmittel von
23,7 GW. Der Herbst 2025 war also nicht windarm, sondern windreich. Die zwölf
teuersten Tage der positiven aFRR verteilen sich über Residuallasten von 3,8
bis 40,6 GW, und der Zusammenhang über alle Tage ist schwach U-förmig, nämlich
19,4 unter 8 GW, 16,0 zwischen 20 und 26 GW und 21,6 über 32 GW. **Teuer wird
die positive aFRR an beiden Rändern**, denn bei sehr hoher erneuerbarer
Einspeisung stehen die thermischen Kraftwerke still und können nichts
hochfahren, und bei sehr hoher Residuallast fahren sie an der Obergrenze. Der
teuerste Tag des Jahres, der 16.09.2025 mit 101,3 im Mittel und 683,5 im
Grenzpreis, ist ein solcher Tag: die erneuerbare Einspeisung deckte mit 50,6 GW
fast die gesamte Last von 54,4 GW, und das Angebot fiel auf 3414 MW. Der
September und der Oktober 2025 zählen acht Tage mit einer Residuallast unter
8 GW gegen zwei in denselben Monaten des Jahres 2024. Das erklärt einzelne
Spitzen und nicht das Niveau beider Monate, denn der U-förmige Zusammenhang ist
mit 19,4 gegen 16,0 schwach.

**Änderung an Ausschreibung oder Bedarf, teilweise verworfen.** Die beschaffte
Menge bleibt bei rund 2000 MW, siehe Abschnitt 1. **Eine strukturelle Änderung
fällt jedoch genau in das Fenster:** die aFRR-Leistungskooperation ALPACA ist
seit September 2025 um den tschechischen ÜNB ČEPS erweitert. In der Jahresdatei
erscheinen die tschechischen Spalten erstmals am 04.09.2025 und die deutsche
Zuschlagsmenge erstmals am 03.09.2025. **Die Erweiterung erklärt den Anstieg
gleichwohl nicht**, und zwar aus zwei Gründen. Erstens setzt die Erhöhung schon
am 25.08.2025 ein, also zehn Tage vorher: der Tagespreis springt von 8,5 am
24.08. auf 31,9 am 25.08. Zweitens ist Deutschland im September und Oktober
Nettoimporteur von aFRR-Leistung, nämlich mit 76 und 63 MW gegen 36 MW im
August. Ein größerer gemeinsamer Angebotsraum senkt den Preis und hebt ihn
nicht.

**Ereignis im Netzbetrieb, nur für einzelne Tage.** Der Marktbericht von Next
Kraftwerke für den September 2025 nennt den 08.09.2025, an dem die
Windeinspeisung abrupt einbrach und konventionelle Leistung ungeplant ausfiel,
mit Intradaypreisen bis 993 Euro je Megawattstunde. Einzelne Tage tragen den
Befund nicht: das Preisniveau ist in beiden Monaten an **allen** Wochentagen
erhöht, nämlich montags 33,1 gegen 15,9, mittwochs 44,7 gegen 18,2 und sonntags
15,2 gegen 9,8.

## 4 Was offen bleibt

Beide Richtungen verlieren gleichzeitig rund 11 Prozent ihres Angebots, nämlich
die positive von 4337 auf 3849 und die negative von 3701 auf 3254 MW. Ein
Opportunitätskosteneffekt würde die Richtungen gegenläufig bewegen, weil teure
Energie das Vorhalten in der einen Richtung verteuert und in der anderen
verbilligt. Der gleichgerichtete Rückgang spricht dafür, dass präqualifizierte
Einheiten in diesen zwei Monaten gar nicht am Markt waren. **Welche Einheiten
das sind, sagt keine öffentliche Quelle.** Die Gebotsliste
(ANONYMOUS_LIST_OF_BIDS) von regelleistung.net führt die Einzelgebote und läge
als nächster Schritt nahe, liegt aber nicht im Datenbestand.

---

## 5 Der Jahresgang der negativen aFRR ist ein Mittagsphänomen

Leistungspreis der negativen aFRR 2025 je Vier-Stunden-Produkt.

| Monat | 00–04 | 04–08 | 08–12 | 12–16 | 16–20 | 20–24 |
|---|---|---|---|---|---|---|
| Februar | 4,5 | 3,5 | 1,9 | 6,2 | 0,6 | 1,2 |
| Mai | 4,0 | 4,1 | **51,1** | **97,8** | 34,2 | 1,9 |
| Juni | 2,8 | 3,4 | 42,0 | 80,1 | 34,4 | 1,2 |
| Dezember | 7,3 | 5,5 | 2,9 | 2,4 | 0,6 | 1,8 |

Der Anstieg von 3,0 im Februar auf 32,2 im Mai findet vollständig in den beiden
Mittagsscheiben statt. Die Nachtscheiben bleiben das ganze Jahr zwischen 1 und
11. Dasselbe Muster zeigen die Jahre 2024 und 2026, im Mai 2026 sogar mit 146,7
in der Scheibe 12 bis 16. **Die Deutung über die Photovoltaik ist damit aus den
eigenen Daten gestützt**, denn die Preisspitze liegt genau in den Stunden der
Solareinspeisung und nirgends sonst.

Die positive aFRR verhält sich spiegelbildlich: ihre Tageshöchstwerte liegen in
den Scheiben 08 bis 12 und 16 bis 20, die Mittagsscheibe 12 bis 16 liegt
darunter.

### Zitierfähige Quelle

Ganz und Kern von der Forschungsstelle für Energiewirtschaft beschreiben den
Zusammenhang für das Jahr 2024 wörtlich:

> „In den sonnenreichen Monaten von Mai bis August führen die höhere solare
> Einstrahlung und die höheren Volllaststunden zur höchsten PV-Stromerzeugung
> im Jahresverlauf. Diese erhöhten Einspeisemengen und damit reduzierte
> Verfügbarkeit von thermischen Kraftwerken wirken sich insbesondere in den
> Mittagsstunden auf den Markt für negative Sekundärreserve aus."

Ganz, Kirstin und Kern, Timo: *Die Regelreservemärkte in Deutschland im
Überblick*, Forschungsstelle für Energiewirtschaft e. V., München, 06.08.2025,
Abschnitt *Regelleistungspreise im Überblick*, Datengrundlage 2010 bis 2024.
Die dort genannte Einheit „58 €/MWh" ist als Euro je Megawatt und Stunde zu
lesen, denn es geht um einen Leistungspreis.

---

## 6 Der Juli, nachrangig

Der Leistungspreis der negativen aFRR fällt im Juli 2025 auf 15,8 gegen 32,2 im
Mai und 27,3 im Juni. Im Jahr 2024 fällt er im Juli ebenfalls, nämlich auf 15,3
gegen 19,9 im Juni. Ein Julieinbruch tritt also in beiden Jahren auf, 2025
stärker. Eine Quelle, die ihn benennt, ist nicht gefunden. **Ohne Beleg bleibt
der Punkt unerwähnt**, wie in der Anfrage vorgesehen.

---

## 7 Nebenbefund zur Datenhaltung

Die Stundendatei `strom_preise_de_2025_60min.csv` führt ab dem 01.10.2025 keinen
Day-Ahead-Preis mehr, weil der Day-Ahead-Markt an diesem Tag auf
Viertelstundenprodukte umgestellt wurde. Auswertungen über das ganze Jahr 2025
sind deshalb auf die Viertelstundendatei zu stützen. Das Optimierungsmodell
rechnet ohnehin viertelstündlich.
