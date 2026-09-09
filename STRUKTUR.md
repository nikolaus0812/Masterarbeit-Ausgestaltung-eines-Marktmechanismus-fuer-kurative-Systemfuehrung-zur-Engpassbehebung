# Struktur und Zuordnung

Stand 08.09.2026. Arbeitsdokument zur Überlegung der Gliederung. Es ersetzt weder
CLAUDE.md noch das Entscheidungsprotokoll, sondern zeigt, was heute wo steht und
welche Zuordnungen offen sind.

Legende zum Stand. **F** heißt ausformulierter Fließtext, **S** heißt
Stichpunktgerüst, **T** heißt teilweise.

---

## Gesamtgliederung

| | Kapitel | Stand |
|---|---|---|
| 1 | Einleitung | F |
| 2 | Grundlagen und Stand der Technik | F |
| 3 | Marktmechanismus und Modellierung des Speicherbetriebs | T |
| 4 | Exemplarische Anwendung und Ergebnisse | S |
| 5 | Bewertung und Diskussion | S |
| 6 | Zusammenfassung und Ausblick | S |

---

## Kapitel 2, was dort steht und woran Kapitel 3 anknüpft

- 2.1 Kurative Systemführung
  - 2.1.1 Präventive und kurative Systemführung im Engpassmanagement
  - 2.1.2 Prozessablauf und Zeitanforderungen
  - 2.1.3 Technologien kurativer Akteure
  - 2.1.4 Herausforderungen der Umsetzung
  - 2.1.5 Rechtlicher Rahmen
- 2.2 Marktrahmen und Systemdienstleistungen
  - 2.2.1 Selbstdispatch und Zentraldispatch
  - 2.2.2 Marktzeithorizonte und Handelsgelegenheiten
  - 2.2.3 Systemdienstleistungen
- 2.3 Vergütungslogiken für Systemdienstleistungen
  - 2.3.1 Vergütung von Redispatch-Maßnahmen
  - 2.3.2 Bemessung entgangener Erlösmöglichkeiten
  - 2.3.3 Grenzen der Übertragbarkeit auf BESS
  - 2.3.4 Vergütung von FCR und aFRR
  - 2.3.5 Wettbewerb um Leistung und Ladezustand
- 2.4 Zwischenfazit

**Kapitel 2 verweist genau einmal nach vorn**, nämlich in 2.2.1 mit
`sec:market_design_comparison` auf den Abgleich der Marktdesignansätze mit den
Anforderungen. Diese Marke liegt derzeit auf Abschnitt 3.1.2.

---

## Kapitel 3, heutiger Stand

- **Kapiteleinleitung** — F, sechs Sätze, am 08.09.2026 geschrieben
- **3.1 Anforderungen an einen kurativen Marktmechanismus**
  - Abschnittseinleitung — F, **zweiter Satz zu berichtigen**, er kündigt noch die
    entfallene Prüfung der Marktdesignansätze an
  - 3.1.1 Anforderungskatalog — Liste A1 bis A8 F, **Ausführung fehlt**
  - 3.1.2 Ableitung des Forschungsbedarfs — F, **zu überarbeiten**
- **3.2 Der kurative Reservierungspreis als offene Größe** — S
- **3.3 Rahmen des kurativen Marktprodukts** — S
  - 3.3.1 Gegenstand der Verpflichtung
  - 3.3.2 Parameter des Modells
  - 3.3.3 Offene Fragen für die Auswertung
  - 3.3.4 Beschaffung und Durchsetzung
- **3.4 Modellierungsansatz und Systemgrenzen** — S
  - 3.4.1 Ansatz und Systemgrenzen
  - 3.4.2 Eingangsdaten
- **3.5 Mathematische Formulierung des Optimierungsproblems** — S
  - 3.5.1 Modellstruktur und Lösungsverfahren
  - 3.5.2 Zielfunktion und Variablen
  - 3.5.3 Nebenbedingungen
- **3.6 Abgrenzung gegenüber dem modifizierten Weber-Ansatz** — S
- **3.7 Validierung des Modells** — S
  - 3.7.1 Vergleichsmaßstab
  - 3.7.2 Unterschiede in Vorausschau und Marktumfang

### Der Anforderungskatalog, Stand

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

Technologieneutral gefasst. Die Verengung auf das BESS steht in 3.1.2.

---

## Kapitel 4 bis 6

- **4 Exemplarische Anwendung und Ergebnisse** — S
  - 4.1 Referenzfall ohne kurative Bindung
  - 4.2 Fahrplan- und Ladezustandsverläufe unter kurativer Bindung
  - 4.3 Erlöswirkung und Opportunitätskosten
  - 4.4 Sensitivitätsanalyse — **zu bereinigen**, führt noch Abrufhäufigkeit,
    Vergütungsniveau und Pönalehöhe, die nach den Entscheidungen 4, 5 und 6
    entfallen
  - 4.5 Ableitung des kurativen Reservierungspreises
- **5 Bewertung und Diskussion** — S
  - 5.1 Einordnung in den regulatorischen Rahmen
  - 5.2 **Bewertung anhand des Anforderungskatalogs**
  - 5.3 Übertragbarkeit auf Systemebene
  - 5.4 Kritische Würdigung der Modellannahmen
  - 5.5 Handlungsempfehlungen
- **6 Zusammenfassung und Ausblick** — S

---

## Geparkt, Ort noch zu bestimmen

### Die diskutierten Anpassungen des Marktdesigns

Sechs Sätze, am 08.09.2026 satzweise geschrieben und danach geparkt, weil ein
Vergleich mit dem Produkt dessen Definition voraussetzt. Der vollständige Wortlaut
steht als Kommentar in chapter_3.tex vor dem Anforderungskatalog.

Inhalt in Stichpunkten.

- Die Anpassungen nehmen die Netzsituation früher in den Handel auf, verringern
  den Eingriffsbedarf und beschränken zugleich die Vermarktung
- Räumliche Auflösung der Preisbildung, von der Teilung der Gebotszone über
  regionale Gebiete allein für den Kurzfristhandel bis zu knotenscharfen Preisen
- Jede feinere Stufe bildet den Engpass genauer ab und verkleinert den Kreis der
  Anbieter, aus dem sich eine knotenscharfe Beschaffung bedienen könnte
- Kapazitätsbasierter Redispatch, der die bereitgehaltene Kapazität statt des
  Eingriffs bemisst und im Kern dieselbe Größe beschafft wie eine kurative
  Vorhaltung, unterschieden allein in Auslöser und Reaktionszeit
- Knotenscharfe Grenzkosten, ausdrücklich **keine** Anpassung des Marktdesigns,
  sondern eine Erweiterung des kostenbasierten Redispatch
- Keine von ihnen ist umgesetzt

**Drei mögliche Orte.**

1. **3.1.2 Forschungsbedarf.** CLAUDE.md §9 sieht dort zwei Sätze zu den
   nächstliegenden Alternativen vor. Spricht dafür, dass die Marke aus Kapitel 2
   dort liegt. Spricht dagegen, dass 0,5 Seiten für sechs Sätze knapp sind.
2. **3.3.1 Gegenstand der Verpflichtung.** Dort wird das Produkt definiert, und
   die Abgrenzung im engeren Sinn gehört dorthin. Spricht dafür, dass der Satz zur
   Gleichheit mit dem kapazitätsbasierten Redispatch erst dort sagbar ist.
3. **5.2 Bewertung anhand des Anforderungskatalogs.** Der Abschnitt existiert
   bereits und trägt genau diese Aufgabe. CLAUDE.md §9 verweist den vollständigen
   Abgleich samt Matrix und den Einwand der adversen Selektion dorthin.

**Vorschlag.** Aufteilen. Ein bis zwei Sätze in 3.1.2, weil die Marke aus
Kapitel 2 dort auflöst und die Lücke den Abstand zu diesen Ansätzen braucht. Die
Abgrenzung des Produkts in 3.3.1. Der vollständige Abgleich in 5.2.

### Der Netzbooster

Aus 3.1.1 entfallen, weil er kein Marktdesign ist, sondern kurative Systemführung
mit einer regulierten Anlage. Mit ihm entfiel der Satz, dass genau diese Abgrenzung
den Gegenstand der Arbeit markiert. CLAUDE.md §9 sieht ihn als eine der beiden
nächstliegenden Alternativen in 3.1.2 vor.

### Tabelle 3.1 mit den 36 Bewertungen

Am 08.09.2026 entfallen und als Kommentar erhalten. CLAUDE.md §9 sieht sie in
Kapitel 5 vor, wo sie zugleich den Einwand der adversen Selektion trägt. Passt zu
Abschnitt 5.2.

---

## Offene Zuordnungsfragen

1. Wohin die sechs Sätze zu den Marktdesignanpassungen gehen, siehe oben
2. Wohin der Netzbooster und die Abgrenzung des Untersuchungsgegenstands gehen
3. Ob Tabelle 3.1 in 5.2 wieder aufgenommen wird
4. Ob der Überschriftenkonflikt in 3.4 bleibt, wo der Abschnitt und sein erster
   Unterabschnitt fast gleich heißen
5. Ob 4.4 nach den Entscheidungen 4, 5 und 6 bereinigt wird
6. Ob der Umfang von Kapitel 3 bei 19 Seiten bleibt oder auf 21 steigt, nachdem
   die Eingangsdaten in 3.4 aufgenommen sind

---

## Was als Nächstes ansteht, wenn die Struktur steht

1. Zweiter Satz der Abschnittseinleitung von 3.1, er kündigt noch die entfallene
   Prüfung an
2. Doppelung zwischen der Einleitung von 3.1 und dem ersten Satz von 3.1.1, beide
   leiten die Anforderungen her
3. Ausführung der acht Anforderungen in 3.1.1, dorthin gehören die Gegenseite des
   bilanziellen Ausgleichs, der Vorbehalt zu A8 und die Kopplungen
4. Überarbeitung von 3.1.2, dort stehen die Behauptungsstärke bei der einzigen
   geeigneten Technologie und die Vorwegnahme im Schlusssatz
