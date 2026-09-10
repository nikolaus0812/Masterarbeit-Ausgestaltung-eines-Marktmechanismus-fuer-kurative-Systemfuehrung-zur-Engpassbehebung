# Struktur und Zuordnung

Stand 09.09.2026, nach der Ausformulierung von 3.1.1.
Arbeitsdokument. Es ersetzt weder CLAUDE.md noch das Entscheidungsprotokoll.

**F** heißt ausformulierter Fließtext, **S** heißt Stichpunktgerüst, **T** heißt
teilweise.

---

## Die bindende Randbedingung

Gemessen am Build vom 09.09.2026, 68 Seiten, 0 Fehler.

| | | |
|---|---|---|
| Kapitel 1 | S. 1 bis 5 | 5 Seiten |
| Kapitel 2 | S. 6 bis 34 | 29 Seiten, Zielwert war 25 |
| Kapitel 3 | S. 35 bis 42 | 8 Seiten, Zielwert 14 |

**Kapitel 3 beginnt auf Seite 35.** Damit die Ergebnisse vor Seite 50 anfangen,
darf Kapitel 3 höchstens **14 Seiten** umfassen.

Hochgerechnet aus dem heutigen Stand landet das Kapitel bei etwa 14,5 Seiten. Der
Ausformulierungsfaktor liegt bei rund zwei, denn 3.1.1 ist von etwa einer Seite
Stichpunkt auf zwei Seiten Fließtext gewachsen.

Der zweite Hebel liegt in Kapitel 2, das seinen eigenen Zielwert um vier Seiten
überschreitet. Wird dort gekürzt, gewinnt Kapitel 3 dieselben vier Seiten.

Die Kapitel 4 bis 6 sind in `main.tex` Zeile 42 bis 44 auskommentiert.

---

## Kapitel 3, Gliederung mit Seitenzielen und Stand

| | | Ziel | heute | Stand |
|---|---|---|---|---|
| | Kapiteleinleitung | 0,3 | | F |
| **3.1** | **Anforderungen und Produkt** | **5** | **4** | |
| 3.1.1 | Anforderungskatalog A1 bis A8 mit Ausführung | 1,5 | 2 | **F** |
| 3.1.2 | Gegenstand der Verpflichtung | 1 | | S |
| 3.1.3 | Parameter des Produkts | 1 | | S |
| 3.1.4 | Offene Fragen für die Auswertung | 0,5 | | S |
| 3.1.5 | Beschaffung und Durchsetzung | 0,5 | | S |
| 3.1.6 | Ableitung des Forschungsbedarfs | 0,5 | | S |
| **3.2** | **Optimierung des Speicherbetriebs** | **7** | **3** | |
| 3.2.1 | Ansatz und Lösungsverfahren | 1 | | S |
| 3.2.2 | Eingangsdaten | 1 | | S |
| 3.2.3 | Zielfunktion und Variablen | 1,5 | | S |
| 3.2.4 | Nebenbedingungen | 2 | | S |
| 3.2.5 | Systemgrenzen und Abgrenzungen | 1,5 | | S |
| **3.3** | **Validierung des Modells** | **2** | **1** | |
| 3.3.1 | Vergleichsmaßstab | 1 | | S |
| 3.3.2 | Unterschiede in Vorausschau und Marktumfang | 1 | | S |

---

## Der Anforderungskatalog

| | Titel | trägt | Ausführung |
|---|---|---|---|
| A1 | Reaktionszeit | Differenzierung nach Aktivierungsgeschwindigkeit | 3 Sätze |
| A2 | Verbindlichkeit | binäre Erfüllung, deshalb Sanktion | 2 Sätze |
| A3 | Lokationalität | knotenscharfe Beschaffung | 2 Sätze |
| A4 | Bemessungsgegenstand | Vorhaltung nach Leistung und Bindungsdauer | 3 Sätze |
| A5 | Diskriminierungsfreiheit | Ansatz an Eigenschaften statt an Technologie | 2 Sätze |
| A6 | Teilnahme | freiwillig, Bedingungen dürfen den Vorteil nicht aufzehren | 2 Sätze |
| A7 | Verträglichkeit | bestehende Verpflichtungen und übrige Systemdienstleistungen | 2 Sätze |
| A8 | Umsetzbarkeit | integrierbar in bestehende Betriebsprozesse | 2 Sätze |

Technologieneutral gefasst.

---

## Anforderungsbezüge im Produktentwurf

Am 09.09.2026 eingetragen, jeder Stichpunkt in 3.1.2 bis 3.1.5 nennt seinen Bezug.

| Produktentscheidung | folgt aus |
|---|---|
| Vorhalteleistung statt Arbeit | A4 |
| Trennung von Vorhaltung und Abruf nach aFRR-Muster | A4 und A6 |
| Bindung statt Sperrung, Anlage darf weiterhandeln | A7 |
| Binäre Erfüllung | A2 |
| Vorgehaltene Leistung und Ladezustandsband | A4 und A7 |
| Bindungsdauer und Reaktionszeit | A1 und A4 |
| Vergütungsform | A4 |
| Beschaffungszeitpunkt | A1 und A6 |
| Ausschreibender, Turnus, Zuschlagsverfahren | A5 |
| Lokationalität der Beschaffung | A3 |
| Pönale | A2 |
| Vergütungslogik und Präqualifikation | A6 |
| Abgrenzung zum Netzbooster | A5 |
| Abgrenzung zum marktbasierten Redispatch | A4 |
| Einfügung in die Betriebsplanung | A8 |

Ohne Bezug bleiben die Tabelle der Produktparameter, weil sie eine
Darstellungsfrage ist, und die vier Stichpunkte in 3.1.4, weil sie Fragen sind.

---

## Zurückgestellt aus 3.1.1, Ort noch zu bestimmen

Alle drei stehen als Kommentar an ihrer Stelle in `chapter_3.tex`.

1. **Wachstum des BESS-Bestands gegen den Bedarf an Regelleistung.** Eigenes
   Argument des Verfassers. Kapitel 2 belegt allein den Stand 2024, nämlich
   810 MW präqualifizierte BESS in der FCR bei 564 MW deutschem Bedarf. Die
   Aussage über die Entwicklung geht darüber hinaus. Der Verfasser will sie beim
   Ausgestalten des Produkts führen, Vormerkung steht in 3.1.2.
2. **Die Paarbildung ist nicht beliebig**, weil eine Senke an einem anderen
   Netzknoten den ersten Engpass entlastet und einen zweiten verschärfen kann.
   Eigenes Argument des Verfassers, Vorschlag 3.1.5.
3. **Vorbehalt zu A8**, dass sich der Aufwand der Einfügung von außen nicht
   beurteilen lässt. CLAUDE.md §8 verlangt ihn, Vorschlag 3.1.5.

---

## Geparkt, Ort noch zu bestimmen

**Die diskutierten Anpassungen des Marktdesigns.** Sechs Sätze, im Wortlaut als
Kommentar in chapter_3.tex vor dem Anforderungskatalog.

- Die Anpassungen nehmen die Netzsituation früher in den Handel auf, verringern den
  Eingriffsbedarf und beschränken zugleich die Vermarktung
- Räumliche Auflösung der Preisbildung, von der Teilung der Gebotszone über
  regionale Gebiete allein für den Kurzfristhandel bis zu knotenscharfen Preisen
- Jede feinere Stufe bildet den Engpass genauer ab und verkleinert den Kreis der
  Anbieter, aus dem sich eine knotenscharfe Beschaffung bedienen könnte
- Kapazitätsbasierter Redispatch, der die bereitgehaltene Kapazität statt des
  Eingriffs bemisst und im Kern dieselbe Größe beschafft wie eine kurative
  Vorhaltung, unterschieden allein in Auslöser und Reaktionszeit
- Knotenscharfe Grenzkosten, ausdrücklich keine Anpassung des Marktdesigns, sondern
  eine Erweiterung des kostenbasierten Redispatch
- Keine von ihnen ist umgesetzt

Vorschlag, ein bis zwei Sätze in 3.1.6, wo die Marke aus Kapitel 2 auflöst, der
Rest nach Abschnitt 5.2.

**Der Netzbooster.** Aus dem Kapitel entfallen, weil er kein Marktdesign ist.

**Tabelle mit den 36 Bewertungen.** Als Kommentar erhalten, vorgesehen für 5.2.

---

## Offene Punkte

1. Wohin die sechs Sätze zu den Marktdesignanpassungen gehen
2. Wohin der Netzbooster und die Abgrenzung des Untersuchungsgegenstands gehen
3. Ob die Tabelle in 5.2 wieder aufgenommen wird
4. Ob in Kapitel 2 gekürzt wird, um Kapitel 3 vier Seiten zu geben
5. Ob 4.4 nach den Entscheidungen 4, 5 und 6 bereinigt wird
6. Die Belege in Kapitel 3 sind nur auf Auflösbarkeit geprüft, nicht auf
   inhaltliche Deckung. Für `ehrhart_analysis_2025`, `horsch_role_2017` und
   `einsiedler_analysis_2025` liessen sich die Volltexte nicht öffnen.
7. Der Konflikt zwischen knotenscharfer Beschaffung nach A3 und
   Diskriminierungsfreiheit nach A5 ist in 3.1.1 gestreift, aber nicht benannt.
   Nach CLAUDE.md §8 sagt der Text ausdrücklich, dass die Arbeit ihn nicht
   entscheidet.
8. `chapter_5.tex:230` trägt den Kommentar F3 folgt aus A2 und A3, das ist die
   alte Nummerierung und heißt jetzt A3 und A4.
9. `\ref{sec:storage_model}` in 3.1.3 löst auf 3.2.4 Nebenbedingungen auf. Gemeint
   ist die Stelle, an der die Symbole eingeführt werden, also 3.2.3.

---

## Nächste Schritte

1. 3.1.2 Gegenstand der Verpflichtung ausformulieren, dabei die Vormerkung zum
   Wachstum des BESS-Bestands einlösen
2. 3.1.3 Parameter des Produkts, dort die Tabelle mit Größe, Basisfall und in
   Kapitel 5 zu prüfen
3. 3.1.4 Offene Fragen, vier Fragen ohne Antwort
4. 3.1.5 Beschaffung und Durchsetzung, dorthin gehören die drei zurückgestellten
   Aussagen aus 3.1.1
5. 3.1.6 Forschungsbedarf, das Stichpunktgerüst steht seit dem 08.09.2026
6. In 3.2.1 sind die Stichpunkte zu den Systemgrenzen nach 3.2.5 zu verschieben
