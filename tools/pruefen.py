"""Pruefsuite der Schriftfassung. Sie berichtet und aendert nichts.

Umgesetzt sind die zehn Pruefungen aus Abschnitt 3 des Uebergabepapiers und aus
Abschnitt 7 von WORKFLOW.md, naemlich

   1  Zeilenenden und Kodierung, CRLF und UTF-8
   2  Stil im Fliesstext, keine Doppelpunkte, Gedankenstriche, Semikola
   3  Klammerbilanz und Dollarparitaet
   4  Umgebungen, jedes \\begin hat sein \\end
   5  doppelte Leerzeilen
   6  gesperrte Begriffe
   7  Akronyme
   8  Marken, keine doppelt, jeder Verweis loest auf
   9  Zitatschluessel gegen literature.bib
  10  Floats mit Marke und Verweis

Aufruf:

    python tools/pruefen.py chapter_3.tex
    python tools/pruefen.py --bib literature.bib "chapter_*.tex" attachment.tex
    python tools/pruefen.py --alle

Dateinamen duerfen bloss stehen, also ohne Verzeichnis. Gesucht wird dann in
chapters/, in extras/ und im Wurzelverzeichnis. Muster in Anfuehrungszeichen
loest das Skript selbst auf, weil die Windows-Eingabeaufforderung das nicht tut.

Wichtig fuer die Pruefungen 8 bis 10. Marken, Verweise und Zitate greifen ueber
Dateigrenzen hinweg. Das Skript liest deshalb immer alle Textdateien als
Zusammenhang ein und meldet Befunde nur fuer die benannten Prueflinge. Sonst
gaelte jeder Verweis aus chapter_3.tex auf eine Marke in chapter_2.tex als
Fehler.

Eine Zeile, die den Kommentar "% pruefen: ok" traegt, bleibt bei den
inhaltlichen Pruefungen 2, 6 und 7 ausser Betracht. Das ist fuer die Stellen
gedacht, an denen ein Befund bewusst stehen bleibt, etwa die Einfuehrung eines
Akronyms in seiner Langform.

Rueckgabewert 1, sobald ein Befund vorliegt, sonst 0.
"""

import argparse
import fnmatch
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Reihenfolge wie in main.tex, sie bestimmt die Erstnennung der Akronyme.
KONTEXT = ([ROOT / "chapters" / "chapter_{}.tex".format(i) for i in range(1, 7)]
           + [ROOT / "extras" / "attachment.tex"])
SUCHORTE = (ROOT / "chapters", ROOT / "extras", ROOT)
STANDARD_BIB = ROOT / "literature" / "literature.bib"
ABKUERZUNGEN = ROOT / "extras" / "abbreviations.tex"

FREIGABE = "% pruefen: ok"

# Nach CLAUDE.md Abschnitt 5, Stand 08.09.2026. Basispreis ist dort nicht mehr
# gesperrt, sondern offen, weshalb er hier nicht mehr gemeldet wird. Die
# Fundstellen lassen sich mit --offen sichtbar machen.
GESPERRT = ("Mindestvergütung", "Vergütungsbereich", "Untergrenze der Vergütung",
            "Erlösdifferenz", "Schwellenpreis")
OFFENE_BEGRIFFE = ("Basispreis", "Strikepreis", "Ausspeiseseite", "Einspeiseseite",
                   "Ausspeicherseite", "Einspeicherseite", "BK8-22-0001-A")
AUSGESCHRIEBEN = ("Batteriespeicher", "Pumpspeicherkraftwerk")

# Befehle, deren geschweiftes Argument kein Fliesstext ist.
ARGUMENT_BEFEHLE = ("cite", "parencite", "textcite", "footcite", "citeauthor",
                    "citeyear", "autocite", "label", "ref", "autoref", "nameref",
                    "pageref", "eqref", "cref", "Cref", "includegraphics", "input",
                    "include", "url", "href", "si", "SI", "usepackage",
                    "bibliography", "acro", "DeclareAcronym")
TABELLEN = ("tabular", "tabularx", "tabulary", "longtable", "array")
FLOATS = ("figure", "table")

_BEFEHL = re.compile(r"\\(?:" + "|".join(ARGUMENT_BEFEHLE) + r")\*?"
                     r"(?:\[[^\]]*\])*(?:\{[^{}]*\})+")
_URL = re.compile(r"https?://\S+")
_UHRZEIT = re.compile(r"\d{1,2}:\d{2}")
_MATHE = re.compile(r"(?<!\\)\$[^$]*\$")
_ZAHLBEREICH = re.compile(r"\d\s*-{2,3}\s*\d")
_ABSTAND = re.compile(r"\\;")
_ITEM_MARKE = re.compile(r"\\item\s*\[[^\]]*\]")
_TAB_AUF = re.compile(r"\\begin\{(?:" + "|".join(TABELLEN) + r")\*?\}")
_TAB_ZU = re.compile(r"\\end\{(?:" + "|".join(TABELLEN) + r")\*?\}")
_ITEM = re.compile(r"^\s*\\item\b")
_CAPTION = re.compile(r"\\caption\*?\s*\{")
_BEGIN = re.compile(r"\\begin\{([^}]*)\}")
_END = re.compile(r"\\end\{([^}]*)\}")
_LABEL = re.compile(r"\\label\{([^}]*)\}")
_VERWEIS = re.compile(r"\\(?:ref|autoref|eqref|nameref|pageref|cref|Cref)\{([^}]*)\}")
_ZITAT = re.compile(r"\\(?:cite|parencite|textcite|footcite|citeauthor|citeyear"
                    r"|autocite)\*?(?:\[[^\]]*\])*\{([^}]*)\}")
_AC = re.compile(r"\\(ac|acs|acl|acf|acp)\*?\{([^}]*)\}")
_BIB_EINTRAG = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,")

STIL = ((re.compile(r":"), "Doppelpunkt"),
        (re.compile(r";"), "Semikolon"),
        (re.compile(r"-{2,3}|–|—"), "Gedankenstrich"))


class Befunde:
    """Sammelt die Meldungen und haelt sie nach Pruefung getrennt."""

    def __init__(self):
        self.liste = []

    def melde(self, nummer, datei, zeile, text):
        self.liste.append((nummer, datei, zeile, text))

    def zaehlung(self):
        return Counter(n for n, _, _, _ in self.liste)

    def __len__(self):
        return len(self.liste)


def ohne_kommentar(zeile):
    """Alles ab dem ersten nicht maskierten Prozentzeichen entfernen."""
    i = 0
    while i < len(zeile):
        if zeile[i] == "\\":
            i += 2
            continue
        if zeile[i] == "%":
            return zeile[:i]
        i += 1
    return zeile


def maskiere(zeile):
    """Bekannte Ausnahmen zeichenweise durch Punkte ersetzen.

    Zeichenweise, damit die Spaltennummern der Fundstellen weiterhin auf die
    Originalzeile passen.
    """
    for muster in (_BEFEHL, _URL, _UHRZEIT, _MATHE, _ZAHLBEREICH, _ABSTAND,
                   _ITEM_MARKE):
        zeile = muster.sub(lambda m: "." * len(m.group(0)), zeile)
    return zeile


def ausschnitt(zeile, spalte, breite=34):
    a = max(0, spalte - breite)
    b = min(len(zeile), spalte + breite)
    vor = ("..." if a > 0 else "") + zeile[a:spalte]
    nach = zeile[spalte + 1:b] + ("..." if b < len(zeile) else "")
    return "{}>{}<{}".format(vor, zeile[spalte], nach).replace("\t", " ")


class Datei:
    """Eine eingelesene Textdatei mit den fuer die Pruefungen noetigen Sichten."""

    def __init__(self, pfad):
        self.pfad = pfad
        self.name = pfad.name
        try:
            self.rel = pfad.relative_to(ROOT).as_posix()
        except ValueError:
            self.rel = str(pfad)
        self.bytes = pfad.read_bytes()
        try:
            self.text = self.bytes.decode("utf-8")
            self.kodierung = None
        except UnicodeDecodeError as fehler:
            self.text = self.bytes.decode("utf-8", "replace")
            self.kodierung = str(fehler)
        self.zeilen = self.text.split("\n")
        self.freigegeben = {n for n, z in enumerate(self.zeilen, 1) if FREIGABE in z}
        self.rein = [(n, ohne_kommentar(z)) for n, z in enumerate(self.zeilen, 1)]
        self._lagen = None

    def lagen(self):
        """Je Zeilennummer merken, ob sie in Tabelle oder Gleitumgebung liegt."""
        if self._lagen is not None:
            return self._lagen
        self._lagen = {}
        tabelle = 0
        float_tiefe = 0
        for n, z in self.rein:
            auf_tab = len(_TAB_AUF.findall(z))
            zu_tab = len(_TAB_ZU.findall(z))
            auf_fl = sum(len(re.findall(r"\\begin\{" + f + r"\*?\}", z)) for f in FLOATS)
            zu_fl = sum(len(re.findall(r"\\end\{" + f + r"\*?\}", z)) for f in FLOATS)
            tabelle += auf_tab
            float_tiefe += auf_fl
            self._lagen[n] = (tabelle > 0, float_tiefe > 0)
            tabelle = max(0, tabelle - zu_tab)
            float_tiefe = max(0, float_tiefe - zu_fl)
        return self._lagen


def pruefung_1(d, b):
    if d.kodierung:
        b.melde(1, d.rel, 0, "keine gueltige UTF-8-Kodierung, {}".format(d.kodierung))
    lf = d.bytes.count(b"\n")
    crlf = d.bytes.count(b"\r\n")
    cr = d.bytes.count(b"\r") - crlf
    if crlf != lf or cr:
        b.melde(1, d.rel, 0, "Zeilenenden gemischt, {} Umbrueche gegen {} CRLF "
                             "und {} einzelne CR".format(lf, crlf, cr))
    return "{} Umbrueche, {} CRLF, UTF-8".format(lf, crlf)


def pruefung_2(d, b):
    lagen = d.lagen()
    for n, z in d.rein:
        if not z.strip() or n in d.freigegeben:
            continue
        in_tabelle, _ = lagen[n]
        if in_tabelle or _ITEM.match(z) or _CAPTION.search(z):
            continue
        pruefbar = maskiere(z)
        for muster, art in STIL:
            for m in muster.finditer(pruefbar):
                b.melde(2, d.rel, n, "{:14s} {}".format(art, ausschnitt(z, m.start())))


def pruefung_3(d, b):
    auf = zu = dollar = 0
    for _, z in d.rein:
        i = 0
        while i < len(z):
            c = z[i]
            if c == "\\":
                i += 2
                continue
            if c == "{":
                auf += 1
            elif c == "}":
                zu += 1
            elif c == "$":
                if z[i:i + 2] == "$$":
                    dollar += 2
                    i += 2
                    continue
                dollar += 1
            i += 1
    if auf != zu:
        b.melde(3, d.rel, 0, "Klammern unausgeglichen, {} geoeffnet gegen {} "
                             "geschlossen".format(auf, zu))
    if dollar % 2:
        b.melde(3, d.rel, 0, "ungerade Zahl von Dollarzeichen, {}".format(dollar))
    return "{} Klammerpaare, {} Dollarzeichen".format(auf, dollar)


def pruefung_4(d, b):
    stapel = []
    for n, z in d.rein:
        stellen = ([(m.start(), "auf", m.group(1)) for m in _BEGIN.finditer(z)]
                   + [(m.start(), "zu", m.group(1)) for m in _END.finditer(z)])
        for _, art, name in sorted(stellen):
            if art == "auf":
                stapel.append((name, n))
            elif not stapel:
                b.melde(4, d.rel, n, "\\end{{{}}} ohne offenes \\begin".format(name))
            elif stapel[-1][0] != name:
                offen, zeile = stapel.pop()
                b.melde(4, d.rel, n, "\\end{{{}}} schliesst \\begin{{{}}} aus Zeile "
                                     "{}".format(name, offen, zeile))
            else:
                stapel.pop()
    for name, n in stapel:
        b.melde(4, d.rel, n, "\\begin{{{}}} ohne \\end".format(name))


def pruefung_5(d, b):
    zeilen = [z.rstrip("\r") for z in d.zeilen]
    for i in range(len(zeilen) - 1):
        if zeilen[i] == "" and zeilen[i + 1] == "":
            b.melde(5, d.rel, i + 1, "zwei aufeinanderfolgende Leerzeilen")


def pruefung_6(d, b):
    for n, z in d.rein:
        if n in d.freigegeben:
            continue
        for wort in GESPERRT:
            for m in re.finditer(re.escape(wort), z, re.IGNORECASE):
                b.melde(6, d.rel, n, "gesperrter Begriff {}, {}".format(
                    wort, ausschnitt(z, m.start(), 42)))


def pruefung_7(d, b, definiert, erstnennung):
    if d.name != ABKUERZUNGEN.name:
        for n, z in d.rein:
            if n in d.freigegeben:
                continue
            for wort in AUSGESCHRIEBEN:
                for m in re.finditer(wort, z):
                    b.melde(7, d.rel, n, "{} ausgeschrieben statt als Akronym, "
                                         "{}".format(wort, ausschnitt(z, m.start(), 38)))
    for n, z in d.rein:
        for m in _AC.finditer(z):
            form, schluessel = m.group(1), m.group(2)
            if form == "acp":
                b.melde(7, d.rel, n, "\\acp verwendet, Pluralform ist nicht vorgesehen")
            if schluessel not in definiert:
                b.melde(7, d.rel, n, "Akronym {} ohne Eintrag in {}".format(
                    schluessel, ABKUERZUNGEN.name))
    for schluessel, (rel, n, form, im_float) in erstnennung.items():
        if rel == d.rel and im_float and form != "acs":
            b.melde(7, d.rel, n, "Erstnennung von {} liegt in einer Gleitumgebung, "
                                 "dort steht \\acs statt \\{}".format(schluessel, form))


def pruefung_8(d, b, marken, verweise):
    for schluessel, orte in marken.items():
        eigene = [o for o in orte if o[0] == d.rel]
        if len(orte) > 1 and eigene:
            b.melde(8, d.rel, eigene[0][1], "Marke {} ist {}fach vergeben, {}".format(
                schluessel, len(orte), ", ".join("{}:{}".format(*o) for o in orte)))
    for schluessel, orte in verweise.items():
        if schluessel in marken:
            continue
        for rel, n in orte:
            if rel == d.rel:
                b.melde(8, d.rel, n, "Verweis auf {} loest gegen keine Marke "
                                     "auf".format(schluessel))


def pruefung_9(d, b, eintraege, bibname):
    for n, z in d.rein:
        for m in _ZITAT.finditer(z):
            for schluessel in (s.strip() for s in m.group(1).split(",")):
                if schluessel and schluessel not in eintraege:
                    b.melde(9, d.rel, n, "Zitatschluessel {} fehlt in {}".format(
                        schluessel, bibname))


def pruefung_10(d, b, verweise):
    for umgebung, praefix in (("figure", "fig:"), ("table", "tab:")):
        tiefe, start, inhalt = 0, None, []
        for n, z in d.rein:
            if re.search(r"\\begin\{" + umgebung + r"\*?\}", z):
                if tiefe == 0:
                    start, inhalt = n, []
                tiefe += 1
            if tiefe > 0:
                inhalt.append(z)
            if re.search(r"\\end\{" + umgebung + r"\*?\}", z):
                tiefe -= 1
                if tiefe == 0:
                    marken = _LABEL.findall("\n".join(inhalt))
                    if not marken:
                        b.melde(10, d.rel, start, "{} ohne Marke".format(umgebung))
                    for marke in marken:
                        if not marke.startswith(praefix):
                            b.melde(10, d.rel, start, "Marke {} traegt nicht das "
                                    "Praefix {}".format(marke, praefix))
                        if marke not in verweise:
                            b.melde(10, d.rel, start, "Marke {} wird nirgends "
                                    "referenziert".format(marke))


def sammle_kontext(dateien):
    """Marken, Verweise und Erstnennungen ueber alle Textdateien hinweg."""
    marken, verweise, erstnennung = defaultdict(list), defaultdict(list), {}
    for d in dateien:
        lagen = d.lagen()
        for n, z in d.rein:
            for m in _LABEL.finditer(z):
                marken[m.group(1)].append((d.rel, n))
            for m in _VERWEIS.finditer(z):
                for teil in (t.strip() for t in m.group(1).split(",")):
                    if teil:
                        verweise[teil].append((d.rel, n))
            for m in _AC.finditer(z):
                schluessel = m.group(2)
                if schluessel not in erstnennung:
                    erstnennung[schluessel] = (d.rel, n, m.group(1), lagen[n][1])
    return marken, verweise, erstnennung


def finde(angabe):
    """Einen Dateinamen oder ein Muster auf vorhandene Pfade abbilden."""
    pfad = Path(angabe)
    if pfad.is_absolute() and pfad.exists():
        return [pfad]
    if any(zeichen in angabe for zeichen in "*?["):
        treffer = []
        for ort in SUCHORTE:
            if ort.is_dir():
                treffer += [p for p in sorted(ort.glob("*"))
                            if p.is_file() and fnmatch.fnmatch(p.name, Path(angabe).name)]
        return treffer
    if (ROOT / angabe).exists():
        return [ROOT / angabe]
    if pfad.exists():
        return [pfad.resolve()]
    for ort in SUCHORTE:
        if (ort / pfad.name).exists():
            return [ort / pfad.name]
    return []


def main(argv):
    zerleger = argparse.ArgumentParser(
        description="Pruefsuite der Schriftfassung, berichtet und aendert nichts.")
    zerleger.add_argument("dateien", nargs="*", help="Dateien oder Muster")
    zerleger.add_argument("--bib", default=None, help="Literaturdatei")
    zerleger.add_argument("--alle", action="store_true",
                          help="alle Kapitel und den Anhang pruefen")
    zerleger.add_argument("--knapp", action="store_true",
                          help="nur die Zusammenfassung ausgeben")
    zerleger.add_argument("--offen", action="store_true",
                          help="Fundstellen der noch offenen Begriffe auflisten, "
                               "ohne sie als Befund zu zaehlen")
    einstellungen = zerleger.parse_args(argv)

    if einstellungen.alle or not einstellungen.dateien:
        prueflinge = [p for p in KONTEXT if p.exists()]
    else:
        prueflinge, fehlend = [], []
        for angabe in einstellungen.dateien:
            treffer = finde(angabe)
            if treffer:
                prueflinge += treffer
            else:
                fehlend.append(angabe)
        for angabe in fehlend:
            print("nicht gefunden, uebersprungen: {}".format(angabe))
        if not prueflinge:
            print("Keine Datei zu pruefen.")
            return 1

    gesehen, geordnet = set(), []
    for p in prueflinge:
        if p not in gesehen:
            gesehen.add(p)
            geordnet.append(p)
    prueflinge = geordnet

    bib = Path(einstellungen.bib) if einstellungen.bib else STANDARD_BIB
    if not bib.is_absolute():
        gefunden = finde(str(bib))
        bib = gefunden[0] if gefunden else STANDARD_BIB
    if bib.exists():
        eintraege = set(_BIB_EINTRAG.findall(
            bib.read_bytes().decode("utf-8", "replace")))
    else:
        eintraege = set()
        print("Literaturdatei nicht gefunden, Pruefung 9 entfaellt: {}".format(bib))

    if ABKUERZUNGEN.exists():
        definiert = set(re.findall(r"\\(?:acro|DeclareAcronym)\{([^}]*)\}",
                                   ABKUERZUNGEN.read_bytes().decode("utf-8", "replace")))
    else:
        definiert = set()
        print("Abkuerzungsverzeichnis nicht gefunden: {}".format(ABKUERZUNGEN))

    kontext = [Datei(p) for p in KONTEXT if p.exists()]
    nach_pfad = {d.pfad: d for d in kontext}
    dateien = [nach_pfad.get(p) or Datei(p) for p in prueflinge]
    marken, verweise, erstnennung = sammle_kontext(
        kontext + [d for d in dateien if d.pfad not in nach_pfad])

    b = Befunde()
    for d in dateien:
        kopfzeile = pruefung_1(d, b)
        pruefung_2(d, b)
        bilanz = pruefung_3(d, b)
        pruefung_4(d, b)
        pruefung_5(d, b)
        pruefung_6(d, b)
        pruefung_7(d, b, definiert, erstnennung)
        pruefung_8(d, b, marken, verweise)
        if eintraege:
            pruefung_9(d, b, eintraege, bib.name)
        pruefung_10(d, b, verweise)
        if not einstellungen.knapp:
            print("\n{}\n  {}, {}".format(d.rel, kopfzeile, bilanz))
            eigene = [e for e in b.liste if e[1] == d.rel]
            if not eigene:
                print("  ohne Befund")
            for nummer, _, zeile, text in eigene:
                ort = "{}:{}".format(d.rel, zeile) if zeile else d.rel
                print("  Pruefung {:<2d} {:<28s} {}".format(nummer, ort, text))

    if einstellungen.offen:
        print("\n{}\nOffene Begriffe nach CLAUDE.md Abschnitt 5, kein Befund\n{}".format(
            "-" * 70, "-" * 70))
        for wort in OFFENE_BEGRIFFE:
            stellen = ["{}:{}".format(d.rel, n)
                       for d in dateien for n, z in d.rein
                       if re.search(re.escape(wort), z)]
            print("  {:20s} {:3d}x  {}".format(
                wort, len(stellen), ", ".join(stellen[:6]) + (" ..." if len(stellen) > 6 else "")))

    zaehlung = b.zaehlung()
    print("\n{}".format("-" * 70))
    if not len(b):
        print("Ohne Befund in {} Datei(en).".format(len(dateien)))
        return 0
    for nummer in sorted(zaehlung):
        print("  Pruefung {:<2d} {} Befund(e)".format(nummer, zaehlung[nummer]))
    print("{} Befund(e) insgesamt in {} Datei(en).".format(len(b), len(dateien)))
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
