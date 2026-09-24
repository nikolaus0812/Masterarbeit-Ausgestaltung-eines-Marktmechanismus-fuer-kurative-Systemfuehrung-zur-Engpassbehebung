# Antwort auf `ANFRAGE_AFRR_HERBST_2025.md`

> **Ins Archiv verschoben am 24.09.2026.** Die Anfrage ist erledigt.
> Offen bleibt allein der Einbau des Belegs `ffe_regelreserve_2025` in
> Abschnitt 4.4, siehe `HANDOFF.md` Abschnitt 6. Die fertigen
> Bibliographieeintraege stehen unten in Abschnitt 6 dieser Datei.

**Stand 24.09.2026.** Die Anfrage vom 23.09.2026 ist nicht von einem getrennten
Chat beantwortet worden, sondern in der Schriftfassung selbst, nämlich aus den
Jahresdateien von regelleistung.net für 2024, 2025 und 2026 und aus zwei
belegbaren Veröffentlichungen. Die vollständige Auswertung mit allen Zahlen
steht in `analysen/afrr_herbst_2025/BEFUND.md`, die Skripte daneben.

---

## 1 Zuerst der Abgleich, den Abschnitt 5 der Anfrage verlangt

**Die Eingangsdaten des Modells sind bestätigt.** Die Monatswerte der Anfrage
lassen sich aus der Quelldatei reproduzieren. Die einzige Abweichung liegt im
März, nämlich 12,1 statt 12,2 Euro je Megawatt und Stunde, und sie folgt
allein daraus, dass die Anfrage über Viertelstunden und der Abgleich über
Zeitscheiben mittelt. Kein Befund von Kapitel 4 ist berührt.

## 2 Die Hauptfrage ist beantwortet, aber nicht vollständig

Der Preis der positiven aFRR verdoppelt sich im September und Oktober 2025,
**weil das Angebot in diesen beiden Monaten sein Jahresminimum erreicht**,
nämlich 3849 gegen 4337 Megawatt in den übrigen zehn Monaten. Die beschaffte
Menge bleibt dabei bei rund 2000 Megawatt.

Drei der vier Vermutungen der Anfrage sind damit erledigt.

| Vermutung der Anfrage | Ergebnis |
|---|---|
| Kraftwerksrevisionen | **nicht bestätigt.** Die verfügbare konventionelle Leistung liegt im Herbst 2025 auf dem Niveau von 2024 |
| Schwachwindphase | **verworfen.** Der Herbst 2025 war windreich, die Residuallast lag unter dem Jahresmittel |
| Änderung an Ausschreibung oder Bedarf | **verworfen für den Bedarf**, er bleibt konstant. Eine Änderung am Markt gibt es gleichwohl, siehe unten |
| Ereignis im Netzbetrieb | **trägt nur einzelne Tage**, das Niveau ist an allen Wochentagen erhöht |

Die Verdopplung zerfällt in zwei etwa gleich große Teile. Der eine ist die um
elf Prozent geringere Angebotsmenge, der andere ein höheres Gebotsniveau bei
gleicher Menge. **Für den zweiten Teil gibt es keine Quelle.** Beide Richtungen
verlieren gleichzeitig rund elf Prozent ihres Angebots, was dafür spricht, dass
präqualifizierte Einheiten in diesen zwei Monaten gar nicht am Markt waren.
Welche das sind, sagt keine öffentliche Veröffentlichung.

**Die eine Änderung am Markt, die in das Fenster fällt,** ist die Erweiterung
der aFRR-Leistungskooperation ALPACA um den tschechischen ÜNB ČEPS seit
September 2025. Sie erklärt den Anstieg nicht, denn die Erhöhung setzt schon am
25.08.2025 ein, und Deutschland ist in beiden Monaten Nettoimporteur von
aFRR-Leistung. Ein größerer gemeinsamer Angebotsraum senkt den Preis.

**Vorschlag für den Text.** Der Jahresgang wird beschrieben und die Ursache
insoweit benannt, wie sie trägt: der Preis folgt 2025 der angebotenen Menge und
nicht der Marktlage, im September und Oktober ist das Angebot am knappsten. Der
verbleibende Teil wird als offen gekennzeichnet. Ein Satz zu ALPACA ist
entbehrlich, weil die Kooperation den Befund nicht erklärt.

## 3 Die Nebenfrage ist vollständig beantwortet

Die Deutung über die Photovoltaik trägt, und zwar doppelt.

**Aus den eigenen Daten.** Der Anstieg von 3,0 im Februar auf 32,2 im Mai
findet vollständig in den beiden Mittagsscheiben statt, nämlich 08 bis 12 und
12 bis 16 Uhr. Die Nachtscheiben bleiben das ganze Jahr zwischen 1 und 11 Euro
je Megawatt und Stunde. Dasselbe Muster zeigen die Jahre 2024 und 2026.

**Aus einer zitierfähigen Quelle.** Ganz und Kern von der Forschungsstelle für
Energiewirtschaft schreiben für das Jahr 2024, dass die erhöhten
PV-Einspeisemengen von Mai bis August und die damit verringerte Verfügbarkeit
thermischer Kraftwerke sich insbesondere in den Mittagsstunden auf den Markt
für negative Sekundärreserve auswirken. Der Wortlaut steht in
`analysen/afrr_herbst_2025/BEFUND.md` Abschnitt 5.

## 4 Die dritte Beobachtung bleibt unerwähnt

Der Julieinbruch tritt 2024 und 2025 auf, 2025 stärker. Eine Quelle, die ihn
benennt, ist nicht gefunden. Nach der Vorgabe der Anfrage bleibt der Punkt
damit aus dem Text.

## 5 Ein Nebenbefund zur Datenhaltung

Die Stundendatei der Strompreise führt ab dem 01.10.2025 keinen Day-Ahead-Preis
mehr, weil der Day-Ahead-Markt an diesem Tag auf Viertelstundenprodukte
umgestellt wurde. Jahresauswertungen für 2025 sind auf die Viertelstundendatei
zu stützen. Das Optimierungsmodell rechnet ohnehin viertelstündlich, ist also
nicht betroffen.

---

## 6 Einträge für `literature.bib`

Einzutragen erst, wenn der zugehörige Satz im Text steht, damit keine
verwaisten Einträge entstehen.

```bibtex
@online{ffe_regelreserve_2025,
  title = {Die Regelreservemärkte in Deutschland im Überblick},
  author = {Ganz, Kirstin and Kern, Timo},
  organization = {Forschungsstelle für Energiewirtschaft (FfE)},
  location = {München},
  date = {2025-08-06},
  url = {https://www.ffe.de/veroeffentlichungen/die-regelreservemaerkte-in-deutschland-im-ueberblick/},
  urldate = {2026-09-24},
  langid = {ngerman}
}

@online{regelleistung_alpaca_2026,
  title = {ALPACA (aFRR Leistungsmarkt)},
  author = {{Übertragungsnetzbetreiber Deutschland}},
  date = {2026},
  url = {https://www.regelleistung.net/de-de/EU-Kooperationen/ALPACA-aFRR-Leistungsmarkt},
  urldate = {2026-09-24},
  langid = {ngerman}
}
```

Der Eintrag `regelleistung_ausschreibungsdaten_2026` deckt die Jahresdateien
des Leistungs- und des Arbeitsmarkts bereits ab, `energy_charts_strompreise_2026`
die Reihen von energy-charts.

## 7 Was die Anfrage nicht hergibt

Der Marktbericht von Next Kraftwerke für den September 2025 nennt für die
positive Sekundärregelleistung ein Plus von 129,77 Prozent und als Ursache den
08.09.2025 mit einem abrupten Einbruch der Windeinspeisung und ungeplanten
Ausfällen konventioneller Leistung. Der Bericht ist ein Marktbericht eines
Anbieters und trägt zudem nur einzelne Tage. **Er wird nicht zitiert.**

Als nächster Schritt läge die Gebotsliste ANONYMOUS_LIST_OF_BIDS von
regelleistung.net nahe, die die Einzelgebote führt. Sie liegt nicht im
Datenbestand und wäre nur zu holen, wenn der verbleibende offene Teil der
Hauptfrage im Text beantwortet werden soll.
