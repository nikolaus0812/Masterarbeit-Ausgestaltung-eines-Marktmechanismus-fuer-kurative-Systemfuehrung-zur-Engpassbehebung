# Struktur und Zuordnung

Stand 08.09.2026, nach dem Umbau von Kapitel 3 auf drei Abschnitte.
Arbeitsdokument. Es ersetzt weder CLAUDE.md noch das Entscheidungsprotokoll.

**F** heißt ausformulierter Fließtext, **S** heißt Stichpunktgerüst, **T** heißt
teilweise.

---

## Die bindende Randbedingung

Gemessen am Build vom 08.09.2026.

| | | |
|---|---|---|
| Kapitel 1 | S. 1 bis 5 | 5 Seiten |
| Kapitel 2 | S. 6 bis 34 | 29 Seiten, Zielwert war 25 |
| Kapitel 3 | ab S. 35 | derzeit 7, überwiegend Stichpunkte |

**Kapitel 3 beginnt auf Seite 35.** Damit die Ergebnisse vor Seite 50 anfangen,
darf Kapitel 3 höchstens **14 Seiten** umfassen. Der frühere Zielwert lag bei 19,
mit den Eingangsdaten bei 21.

Der zweite Hebel liegt in Kapitel 2, das seinen eigenen Zielwert um vier Seiten
überschreitet. Wird dort gekürzt, gewinnt Kapitel 3 dieselben vier Seiten.

Die Kapitel 4 bis 6 sind in `main.tex` Zeile 42 bis 44 auskommentiert. Der Build
umfasst deshalb nur die Kapitel 1 bis 3. Auf die Rechnung wirkt sich das nicht aus,
denn maßgeblich ist allein, wo Kapitel 3 endet.

---

## Kapitel 3, neue Gliederung mit Seitenzielen

| | | Seiten | Stand |
|---|---|---|---|
| | Kapiteleinleitung | 0,3 | F |
| **3.1** | **Anforderungen und Produkt** | **5** | |
| 3.1.1 | Anforderungskatalog A1 bis A8 mit Ausführung | 1,5 | T, Liste F, Ausführung fehlt |
| 3.1.2 | Gegenstand der Verpflichtung | 1 | S |
| 3.1.3 | Parameter des Produkts | 1 | S |
| 3.1.4 | Offene Fragen für die Auswertung | 0,5 | S |
| 3.1.5 | Beschaffung und Durchsetzung | 0,5 | S |
| 3.1.6 | Ableitung des Forschungsbedarfs | 0,5 | F, zu überarbeiten |
| **3.2** | **Optimierung des Speicherbetriebs** | **7** | |
| 3.2.1 | Ansatz und Lösungsverfahren | 1 | S |
| 3.2.2 | Eingangsdaten | 1 | S |
| 3.2.3 | Zielfunktion und Variablen | 1,5 | S |
| 3.2.4 | Nebenbedingungen | 2 | S |
| 3.2.5 | Systemgrenzen und Abgrenzungen | 1,5 | S |
| **3.3** | **Validierung des Modells** | **2** | |
| 3.3.1 | Vergleichsmaßstab | 1 | S |
| 3.3.2 | Unterschiede in Vorausschau und Marktumfang | 1 | S |

Der Forschungsbedarf steht jetzt **hinter** dem Produkt. Der Bogen lautet
Anforderungen, Produkt, Lücke, danach das Modell und zuletzt die Validierung.

In 3.2.1 sind drei frühere Teile aufgegangen, nämlich der Modellierungsansatz, der
Abschnitt zum kurativen Reservierungspreis als offener Größe und die
Methodendarstellung mit dem Lösungsverfahren.

In 3.2.5 sind die Systemgrenzen und die Abgrenzung gegenüber dem modifizierten
Weber-Ansatz zusammengeführt.

---

## Der Anforderungskatalog

| | Titel | trägt |
|---|---|---|
| A1 | Reaktionszeit | Differenzierung nach Aktivierungsgeschwindigkeit |
| A2 | Verbindlichkeit | binäre Erfüllung, deshalb Sanktion |
| A3 | Lokationalität | knotenscharfe Beschaffung |
| A4 | Bemessungsgegenstand | Vorhaltung nach Leistung und Bindungsdauer |
| A5 | Diskriminierungsfreiheit | Ansatz an Eigenschaften statt an Technologie |
| A6 | Teilnahme | freiwillig, Bedingungen dürfen den Vorteil nicht aufzehren |
| A7 | Verträglichkeit | bestehende Verpflichtungen und übrige Systemdienstleistungen |
| A8 | Umsetzbarkeit | integrierbar in bestehende Betriebsprozesse |

Technologieneutral gefasst, die Verengung auf das BESS steht in 3.1.6.

---

## Kapitel 4 bis 6

- **4 Exemplarische Anwendung und Ergebnisse** — S. 4.4 ist zu bereinigen, sie
  führt noch Abrufhäufigkeit, Vergütungsniveau und Pönalehöhe, die nach den
  Entscheidungen 4, 5 und 6 entfallen.
- **5 Bewertung und Diskussion** — S. Abschnitt 5.2 heißt bereits Bewertung anhand
  des Anforderungskatalogs und ist damit der Ort für den vollständigen Abgleich.
- **6 Zusammenfassung und Ausblick** — S

---

## Geparkt, Ort noch zu bestimmen

**Die diskutierten Anpassungen des Marktdesigns.** Sechs Sätze, im Wortlaut als
Kommentar in chapter_3.tex vor dem Anforderungskatalog. Inhalt in Stichpunkten.

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

Bei 14 Seiten Gesamtumfang trägt Kapitel 3 diese sechs Sätze nicht mehr in voller
Länge. Vorschlag, ein bis zwei Sätze in 3.1.6, wo die Marke aus Kapitel 2 auflöst,
der Rest nach Abschnitt 5.2.

**Der Netzbooster.** Aus dem Kapitel entfallen, weil er kein Marktdesign ist. Mit
ihm entfiel der Satz, dass genau diese Abgrenzung den Gegenstand der Arbeit
markiert. CLAUDE.md §9 sieht ihn in der Ableitung des Forschungsbedarfs vor.

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

---

## Nächste Schritte

1. Zweiter Satz der Abschnittseinleitung von 3.1, er kündigt noch die entfallene
   Prüfung der Marktdesignansätze an
2. Doppelung zwischen der Einleitung von 3.1 und dem ersten Satz von 3.1.1
3. Ausführung der acht Anforderungen in 3.1.1, dorthin gehören die Gegenseite des
   bilanziellen Ausgleichs, der Vorbehalt zu A8 und die Kopplungen
4. In 3.2.1 sind die Stichpunkte zu den Systemgrenzen nach 3.2.5 zu verschieben,
   ein Kommentar an der Stelle hält das fest
5. Überarbeitung von 3.1.6, dort stehen die Behauptungsstärke bei der einzigen
   geeigneten Technologie und die Vorwegnahme im Schlusssatz
