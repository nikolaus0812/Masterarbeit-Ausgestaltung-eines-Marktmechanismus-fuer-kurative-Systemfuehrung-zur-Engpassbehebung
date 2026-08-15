"""Verstoesse gegen die Stilvorgabe im Fliesstext finden.

Die Arbeit haelt die Regel ein, dass im Fliesstext keine Doppelpunkte, keine
Gedankenstriche und keine Semikola vorkommen (siehe Kopfkommentar von
chapters/chapter_1.tex). Dieses Skript prueft die Kapiteldateien darauf und
BERICHTET nur. Es aendert nichts.

Nicht geprueft wird, was kein Fliesstext ist:

  - Kommentarzeilen und angehaengte Kommentare. Ein "%" beendet die Zeile,
    "\\%" ist ein gesetztes Prozentzeichen und beendet sie nicht.
  - Die Argumente von \\cite, \\label, \\ref, \\autoref, \\includegraphics,
    \\input, \\url und \\si. Ein Doppelpunkt in "sec:market_horizons" ist
    Teil eines Schluessels und keine Interpunktion.
  - URLs, also alles ab "http://" oder "https://".
  - Zeitangaben der Form 14:30.
  - Mathe zwischen Dollarzeichen.
  - Zahlenbereiche wie 2020--2025. Der Halbgeviertstrich zwischen zwei Zahlen
    ist ein Bis-Strich und kein Gedankenstrich.
  - Der Befehl "\\;" (Abstand im Mathesatz).
  - Der Inhalt von tabular-Umgebungen. Eine Tabellenzelle ist kein Fliesstext,
    und "--" steht dort als Zeichen fuer "nicht erfuellt".
  - Die eckige Marke von \\item[...]. Sie ist eine Beschriftung, kein Satz.

Gemeldet werden danach:

  Doppelpunkt      :
  Semikolon        ;
  Gedankenstrich   --  ---  sowie die Zeichen U+2013 und U+2014

Aufruf:
    python tools/pruefe_stil.py                 # chapters/*.tex
    python tools/pruefe_stil.py datei.tex ...   # bestimmte Dateien

Rueckgabewert 1, wenn Verstoesse gefunden wurden, sonst 0.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Befehle, deren Argument in geschweiften Klammern kein Fliesstext ist.
ARGUMENT_BEFEHLE = ("cite", "parencite", "textcite", "footcite", "citeauthor",
                    "citeyear", "label", "ref", "autoref", "nameref", "pageref",
                    "eqref", "includegraphics", "input", "include", "url",
                    "href", "si", "SI", "usepackage", "bibliography")

_BEFEHL = re.compile(
    r"\\(?:" + "|".join(ARGUMENT_BEFEHLE) + r")\*?"
    r"(?:\[[^\]]*\])*"          # optionale Argumente, etwa \cite[S.\,12]{...}
    r"(?:\{[^{}]*\})+"          # ein oder mehrere Pflichtargumente
)
_URL = re.compile(r"https?://\S+")
_UHRZEIT = re.compile(r"\d{1,2}:\d{2}")
_MATHE = re.compile(r"(?<!\\)\$[^$]*\$")
_ZAHLBEREICH = re.compile(r"\d\s*-{2,3}\s*\d")
_ABSTAND = re.compile(r"\\;")
_ITEM_MARKE = re.compile(r"\\item\s*\[[^\]]*\]")

# Umgebungen, deren Inhalt kein Fliesstext ist.
TABELLEN = ("tabular", "tabularx", "tabulary", "longtable", "array")
_UMG_AUF = re.compile(r"\\begin\{(" + "|".join(TABELLEN) + r")\*?\}")
_UMG_ZU = re.compile(r"\\end\{(" + "|".join(TABELLEN) + r")\*?\}")

FUNDE = (
    (re.compile(r":"), "Doppelpunkt"),
    (re.compile(r";"), "Semikolon"),
    (re.compile(r"-{2,3}|–|—"), "Gedankenstrich"),
)


def ohne_kommentar(zeile: str) -> str:
    """Alles ab dem ersten nicht maskierten Prozentzeichen entfernen."""
    i = 0
    while i < len(zeile):
        if zeile[i] == "\\":
            i += 2                      # \% und jedes andere maskierte Zeichen
            continue
        if zeile[i] == "%":
            return zeile[:i]
        i += 1
    return zeile


def maskiere(zeile: str) -> str:
    """Bekannte Ausnahmen durch Punkte ersetzen.

    Ersetzt wird zeichenweise, damit die Spaltennummern der verbleibenden
    Fundstellen weiterhin auf die Originalzeile passen.
    """
    for muster in (_BEFEHL, _URL, _UHRZEIT, _MATHE, _ZAHLBEREICH, _ABSTAND,
                   _ITEM_MARKE):
        zeile = muster.sub(lambda m: "." * len(m.group(0)), zeile)
    return zeile


def ausschnitt(zeile: str, spalte: int, breite: int = 34) -> str:
    """Fundstelle mit etwas Text davor und danach, Fundzeichen in >< gesetzt."""
    a = max(0, spalte - breite)
    b = min(len(zeile), spalte + breite)
    vor = ("..." if a > 0 else "") + zeile[a:spalte]
    nach = zeile[spalte + 1:b] + ("..." if b < len(zeile) else "")
    return f"{vor}>{zeile[spalte]}<{nach}".replace("\t", " ")


def pruefe(pfad: Path) -> list[tuple[int, str, str]]:
    treffer = []
    text = pfad.read_text(encoding="utf-8")
    in_tabelle = 0
    for nr, zeile in enumerate(text.splitlines(), start=1):
        roh = ohne_kommentar(zeile)
        if not roh.strip():
            continue
        in_tabelle += len(_UMG_AUF.findall(roh))
        zu = len(_UMG_ZU.findall(roh))
        ueberspringen = in_tabelle > 0
        in_tabelle = max(0, in_tabelle - zu)
        if ueberspringen:
            continue
        pruefbar = maskiere(roh)
        for muster, art in FUNDE:
            for m in muster.finditer(pruefbar):
                treffer.append((nr, art, ausschnitt(roh, m.start())))
    return treffer


def main(argv: list[str]) -> int:
    if argv:
        dateien = [Path(a) for a in argv]
    else:
        dateien = sorted((ROOT / "chapters").glob("*.tex"))
    if not dateien:
        print("Keine Dateien gefunden.")
        return 0

    gesamt = 0
    for pfad in dateien:
        if not pfad.exists():
            print(f"{pfad}: nicht gefunden, uebersprungen.")
            continue
        treffer = pruefe(pfad)
        rel = pfad.relative_to(ROOT) if ROOT in pfad.resolve().parents else pfad
        print(f"\n{rel}: {len(treffer)} Verstoesse")
        for nr, art, stelle in treffer:
            print(f"  {rel}:{nr}  {art:14s} {stelle}")
        gesamt += len(treffer)

    print(f"\n{gesamt} Verstoesse insgesamt in {len(dateien)} Dateien.")
    return 1 if gesamt else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
