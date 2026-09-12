# -*- coding: utf-8 -*-
"""
quellencheck.py

Durchsucht die zu literature.bib gehoerenden PDF-Dateien nach Suchbegriffen und
schreibt einen kompakten Bericht mit Zitationsschluessel, Seitenzahl und
Fundstellenkontext. Der Bericht ist klein genug, um ihn hochzuladen, waehrend die
PDFs lokal bleiben.

VORAUSSETZUNG
    pypdf oder pymupdf. Eines von beiden genuegt, das Skript nimmt, was da ist.

AUFRUF, aus dem Wurzelverzeichnis des Repositories
    python tools/quellencheck.py "58,3"
    python tools/quellencheck.py "58,3" "Nettostromerzeugung" "Bruttostromverbrauch"
    python tools/quellencheck.py --key bundesnetzagentur_monitoringbericht_2026 "58,3"
    python tools/quellencheck.py --key bundesnetzagentur_anlage1_2024 --regex "13a\\s*Abs"
    python tools/quellencheck.py --liste
    python tools/quellencheck.py --map-vorschlag

OPTIONEN
    --bib PFAD        Pfad zur bib-Datei, Standard literature/literature.bib
    --pdfdir PFAD     Ordner mit den PDF, Standard literature/PDFs
    --map PFAD        Zuordnungstabelle, Standard tools/quellen_map.tsv
    --key SCHLUESSEL  Nur diesen Eintrag durchsuchen, mehrfach angebbar
    --regex           Suchbegriffe als regulaere Ausdruecke behandeln
    --kontext N       Zeichen vor und nach dem Treffer, Standard 220
    --max N           Hoechstzahl der Treffer je Datei und Begriff, Standard 8
    --out DATEI       Zieldatei, Standard quellencheck_bericht.md
    --liste           Nur auflisten, welche Eintraege eine auffindbare PDF haben
    --map-vorschlag   Entwurf der Zuordnungstabelle nach stdout schreiben

WIE EIN EINTRAG SEINE DATEI FINDET, in dieser Reihenfolge
    1. Das file-Feld des bib-Eintrags, falls der Pfad auf dieser Maschine existiert.
    2. Die Zuordnungstabelle, eine Zeile je Eintrag, Schluessel und Dateiname
       durch einen Tabulator getrennt, Zeilen mit # sind Kommentar.
    Ein automatischer Abgleich ueber Titel und Autor findet NICHT statt. Er lag
    bei einem Versuch nur bei zwei Dritteln und ordnete dabei mehrere Eintraege
    der falschen Datei zu, etwa der Festlegung eine ihrer Anlagen. Fuer
    Fundstellen in einer Abschlussarbeit ist das zu unsicher. --map-vorschlag
    erzeugt einen Entwurf, der von Hand zu bestaetigen ist.

HINWEISE
    Die Suche ist ohne Ruecksicht auf Gross- und Kleinschreibung. Zeilenumbrueche
    innerhalb des PDF-Textes werden vor der Suche zu Leerzeichen, damit ein ueber
    zwei Zeilen gebrochener Begriff gefunden wird. Trennstriche am Zeilenende
    werden entfernt.
    Findet das Skript keinen Text, ist die Datei vermutlich ein Scan ohne
    Textebene. Das wird im Bericht vermerkt.
"""

import argparse
import io
import os
import re
import sys
import unicodedata

BIB_STANDARD = os.path.join("literature", "literature.bib")
PDF_STANDARD = os.path.join("literature", "PDFs")
MAP_STANDARD = os.path.join("tools", "quellen_map.tsv")
OUT_STANDARD = "quellencheck_bericht.md"


def bib_lesen(pfad):
    """Liefert eine Liste aus (schluessel, titel, autor, datum, dateipfade)."""
    with io.open(pfad, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()

    eintraege = []
    for m in re.finditer(r"@\w+\{([^,\s]+)\s*,(.*?)(?=\n@\w+\{|\Z)", text, re.S):
        key = m.group(1).strip()
        body = m.group(2)

        def feld(name):
            g = re.search(r"\b" + name + r"\s*=\s*\{(.*?)\}\s*,?\s*\n", body, re.S)
            if not g:
                return ""
            return re.sub(r"\s+", " ", re.sub(r"[{}]", "", g.group(1))).strip()

        titel = feld("title")
        autor = feld("author")
        datum = feld("date")

        f_feld = re.search(r"\bfile\s*=\s*\{(.*?)\}\s*,?\s*\n", body, re.S)
        pfade = []
        if f_feld:
            roh = f_feld.group(1)
            # Zotero trennt mehrere Dateien mit ; und maskiert : und \ mit \
            for stueck in roh.split(";"):
                stueck = stueck.strip()
                if not stueck:
                    continue
                stueck = stueck.replace("\\:", ":").replace("\\\\", "\\")
                # Zotero-Form "Titel:PFAD:application/pdf" abfangen
                teile = stueck.split(":")
                if len(teile) >= 3 and teile[-1].lower().startswith("application"):
                    stueck = ":".join(teile[1:-1])
                if stueck.lower().endswith(".pdf"):
                    pfade.append(stueck)
        eintraege.append((key, titel, autor, datum, pfade))
    return eintraege


def jobs_lesen(pfad):
    """Auftragsdatei lesen. Liefert Liste aus (kennung, schluesselliste, begriffe).

    Drei Spalten, durch Tabulator getrennt. Mehrere Schluessel mit Komma,
    mehrere Begriffe mit Semikolon. Zeilen mit # sind Kommentar.
    """
    auftraege = []
    with io.open(pfad, "r", encoding="utf-8") as f:
        for nr, zeile in enumerate(f, start=1):
            zeile = zeile.rstrip("\n")
            if not zeile.strip() or zeile.lstrip().startswith("#"):
                continue
            teile = zeile.split("\t")
            if len(teile) < 3:
                print("Zeile %d hat weniger als drei Spalten, uebersprungen." % nr)
                continue
            kennung = teile[0].strip()
            keys = [k.strip() for k in teile[1].split(",") if k.strip()]
            begriffe = [b.strip() for b in teile[2].split(";") if b.strip()]
            if kennung and keys and begriffe:
                auftraege.append((kennung, keys, begriffe))
    return auftraege


def map_lesen(pfad):
    """Zuordnungstabelle lesen. Liefert ein Dictionary Schluessel zu Dateiname."""
    zuordnung = {}
    if not os.path.exists(pfad):
        return zuordnung
    with io.open(pfad, "r", encoding="utf-8") as f:
        for zeile in f:
            zeile = zeile.rstrip("\n")
            if not zeile.strip() or zeile.lstrip().startswith("#"):
                continue
            teile = zeile.split("\t")
            if len(teile) >= 2 and teile[1].strip():
                zuordnung[teile[0].strip()] = teile[1].strip()
    return zuordnung


def langpfad(p):
    """Windows begrenzt Pfade auf 260 Zeichen. Drei der Dateien in
    literature/PDFs liegen mit 266 bis 269 Zeichen darueber und sind ohne
    diesen Zusatz nicht zu oeffnen. Das Praefix hebt die Grenze auf."""
    if os.name != "nt":
        return p
    voll = os.path.abspath(p)
    if len(voll) < 250 or voll.startswith("\\\\?\\"):
        return voll
    return "\\\\?\\" + voll


def dateien_finden(key, pfade_aus_bib, zuordnung, pdfdir):
    """Liefert (liste_der_pfade, herkunft)."""
    da = [q for q in pfade_aus_bib if os.path.exists(langpfad(q))]
    if da:
        return da, "bib"
    name = zuordnung.get(key)
    if name:
        voll = name if os.path.isabs(name) else os.path.join(pdfdir, name)
        if os.path.exists(langpfad(voll)):
            return [voll], "map"
        return [], "map, Datei fehlt"
    return [], "keine Zuordnung"


def seitentexte(pdf_pfad):
    """Liefert (liste_der_seitentexte, fehlermeldung)."""
    try:
        from pypdf import PdfReader
    except ImportError:
        PdfReader = None
    if PdfReader is not None:
        try:
            reader = PdfReader(langpfad(pdf_pfad))
        except Exception as e:
            return None, "Datei nicht lesbar, %s" % e
        seiten = []
        for s in reader.pages:
            try:
                seiten.append(s.extract_text() or "")
            except Exception:
                seiten.append("")
        return seiten, None
    try:
        import pymupdf
    except ImportError:
        sys.exit("Weder pypdf noch pymupdf gefunden. Installieren mit  pip install pypdf")
    try:
        doc = pymupdf.open(langpfad(pdf_pfad))
    except Exception as e:
        return None, "Datei nicht lesbar, %s" % e
    seiten = []
    for s in doc:
        try:
            seiten.append(s.get_text() or "")
        except Exception:
            seiten.append("")
    doc.close()
    return seiten, None


def normieren(t):
    t = t.replace("\r", "\n")
    t = re.sub(r"-\n(?=\w)", "", t)      # Trennstrich am Zeilenende
    t = re.sub(r"\s*\n\s*", " ", t)      # Umbrueche zu Leerzeichen
    t = re.sub(r"[ \t]{2,}", " ", t)
    return t


def suchen(seiten, begriffe, als_regex, kontext, maxtreffer):
    ergebnis = []
    for begriff in begriffe:
        muster = begriff if als_regex else re.escape(begriff)
        rx = re.compile(muster, re.I)
        gefunden = 0
        for nr, roh in enumerate(seiten, start=1):
            if gefunden >= maxtreffer:
                break
            t = normieren(roh)
            for m in rx.finditer(t):
                a = max(0, m.start() - kontext)
                b = min(len(t), m.end() + kontext)
                auszug = t[a:b].strip()
                if a > 0:
                    auszug = "... " + auszug
                if b < len(t):
                    auszug = auszug + " ..."
                ergebnis.append((begriff, nr, auszug))
                gefunden += 1
                if gefunden >= maxtreffer:
                    break
    return ergebnis


# --- nur fuer --map-vorschlag ------------------------------------------------

STOPP = set("""der die das den dem des ein eine einer eines und oder von vom zur
zum fuer im in an auf mit bei als aus nach ueber the of and for with""".split())


def falten(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.replace("ß", "ss").lower()


def woerter(s):
    return {w for w in re.findall(r"[a-z0-9]{4,}", falten(s)) if w not in STOPP}


def map_vorschlag(eintraege, pdfdir):
    """Entwurf der Zuordnung. Jede Zeile ist von Hand zu pruefen."""
    if not os.path.isdir(pdfdir):
        sys.exit("PDF-Ordner nicht gefunden, %s" % pdfdir)
    dateien = sorted(f for f in os.listdir(pdfdir) if f.lower().endswith(".pdf"))
    index = [(f, woerter(os.path.splitext(f)[0])) for f in dateien]

    print("# Zuordnung bib-Schluessel zu Datei in %s" % pdfdir)
    print("# ENTWURF, jede Zeile ist gegen die Datei zu pruefen und dann das")
    print("# fuehrende Fragezeichen zu entfernen. Zeilen ohne Dateinamen sind offen.")
    print("#")
    for key, titel, autor, datum, _ in eintraege:
        nachnamen = set()
        for a in autor.split(" and "):
            a = a.strip()
            if a:
                nachnamen.add(falten(a.split(",")[0].strip().split()[-1]))
        nachnamen = {n for n in nachnamen if len(n) >= 4}
        tw = woerter(titel)
        jahr = datum[:4]
        bewertet = []
        for f, fw in index:
            s = len(tw & fw) / max(1, min(len(tw), 8))
            if nachnamen & fw:
                s += 0.5
            if jahr and jahr[2:] == f[:2]:
                s += 0.25
            if s > 0:
                bewertet.append((s, f))
        bewertet.sort(key=lambda x: (-x[0], x[1]))
        if not bewertet or bewertet[0][0] < 0.5:
            print("?%s\t" % key)
        else:
            print("?%s\t%s" % (key, bewertet[0][1]))


# --- Auftragsbetrieb ----------------------------------------------------------

def auftraege_abarbeiten(a, eintraege, zuordnung):
    """Auftragsdatei abarbeiten und einen Bericht je Kennung schreiben.

    Jede Datei wird nur einmal eingelesen, auch wenn mehrere Auftraege sie
    verwenden. Das spart bei 300-seitigen Berichten spuerbar Zeit.
    """
    auftraege = jobs_lesen(a.jobs)
    nach_key = {e[0]: e for e in eintraege}
    cache = {}

    def seiten_holen(key):
        if key in cache:
            return cache[key]
        e = nach_key.get(key)
        if e is None:
            cache[key] = (None, "Schluessel nicht in der bib")
            return cache[key]
        pfade, herkunft = dateien_finden(key, e[4], zuordnung, a.pdfdir)
        if not pfade:
            cache[key] = (None, herkunft)
            return cache[key]
        seiten, fehler = seitentexte(pfade[0])
        if seiten is None:
            cache[key] = (None, fehler)
        elif not any(s.strip() for s in seiten):
            cache[key] = (None, "kein Text extrahierbar, vermutlich Scan, %d Seiten"
                          % len(seiten))
        else:
            cache[key] = (seiten, os.path.basename(pfade[0]))
        return cache[key]

    zeilen = ["# Quellencheck", "",
              "Auftragsdatei %s, %d Auftraege." % (a.jobs, len(auftraege)), ""]
    ohne_treffer, probleme = [], []

    for kennung, keys, begriffe in auftraege:
        block = []
        for key in keys:
            seiten, info = seiten_holen(key)
            if seiten is None:
                probleme.append((kennung, key, info))
                block.append("- %s, nicht durchsuchbar, %s" % (key, info))
                block.append("")
                continue
            treffer = suchen(seiten, begriffe, a.regex, a.kontext, a.maxtreffer)
            if not treffer:
                continue
            block.append("### %s" % key)
            block.append("")
            block.append("Datei %s, %d Seiten" % (info, len(seiten)))
            block.append("")
            for begriff, nr, auszug in treffer:
                block.append("- %s, Seite %d" % (begriff, nr))
                block.append("")
                block.append("  > %s" % auszug)
                block.append("")
        zeilen.append("## %s" % kennung)
        zeilen.append("")
        zeilen.append("Begriffe %s" % ", ".join(begriffe))
        zeilen.append("")
        if any(z.startswith("###") for z in block):
            zeilen.extend(block)
        else:
            zeilen.extend(block)
            zeilen.append("Kein Treffer.")
            zeilen.append("")
            ohne_treffer.append(kennung)

    if probleme:
        zeilen.append("## Nicht durchsuchbare Quellen")
        zeilen.append("")
        for kennung, key, info in probleme:
            zeilen.append("- %s, %s, %s" % (kennung, key, info))
        zeilen.append("")

    with io.open(a.out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(zeilen))

    groesse = os.path.getsize(a.out)
    print("Auftraege %d, davon ohne Treffer %d. Quellen gelesen %d."
          % (len(auftraege), len(ohne_treffer),
             sum(1 for v in cache.values() if v[0] is not None)))
    if ohne_treffer:
        print("ohne Treffer, %s" % ", ".join(ohne_treffer))
    if probleme:
        print("nicht durchsuchbar, %s"
              % ", ".join(sorted(set(k for _, k, _ in probleme))))
    print("Bericht %s, %.0f kB" % (a.out, groesse / 1024.0))


# -----------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(add_help=True)
    p.add_argument("begriffe", nargs="*", help="Suchbegriffe")
    p.add_argument("--bib", default=BIB_STANDARD)
    p.add_argument("--pdfdir", default=PDF_STANDARD)
    p.add_argument("--map", default=MAP_STANDARD, dest="mappfad")
    p.add_argument("--key", action="append", default=[])
    p.add_argument("--regex", action="store_true")
    p.add_argument("--kontext", type=int, default=220)
    p.add_argument("--max", type=int, default=8, dest="maxtreffer")
    p.add_argument("--out", default=OUT_STANDARD)
    p.add_argument("--liste", action="store_true")
    p.add_argument("--map-vorschlag", action="store_true", dest="mapvorschlag")
    p.add_argument("--jobs", default=None)
    a = p.parse_args()

    if not os.path.exists(a.bib):
        sys.exit("bib-Datei nicht gefunden, %s" % a.bib)

    eintraege = bib_lesen(a.bib)
    if a.key:
        gewuenscht = set(a.key)
        eintraege = [e for e in eintraege if e[0] in gewuenscht]
        fehlend = gewuenscht - set(e[0] for e in eintraege)
        for k in sorted(fehlend):
            print("Schluessel nicht in der bib gefunden, %s" % k)

    if a.mapvorschlag:
        map_vorschlag(eintraege, a.pdfdir)
        return

    zuordnung = map_lesen(a.mappfad)

    if a.liste:
        offen = 0
        for key, titel, autor, datum, pfade in eintraege:
            da, herkunft = dateien_finden(key, pfade, zuordnung, a.pdfdir)
            status = "ok, %s" % herkunft if da else herkunft
            if not da:
                offen += 1
            print("%-52s %-22s %s" % (key[:52], status, titel[:60]))
        print()
        print("%d von %d Eintraegen ohne auffindbare Datei." % (offen, len(eintraege)))
        if not zuordnung:
            print("Zuordnungstabelle %s fehlt. Entwurf mit --map-vorschlag erzeugen."
                  % a.mappfad)
        return

    if a.jobs:
        auftraege_abarbeiten(a, eintraege, zuordnung)
        return

    if not a.begriffe:
        sys.exit("Keine Suchbegriffe angegeben.")

    zeilen = []
    zeilen.append("# Quellencheck")
    zeilen.append("")
    zeilen.append("Suchbegriffe, %s" % ", ".join(a.begriffe))
    zeilen.append("")
    getroffen = 0
    geprueft = 0
    ohne_datei = []

    for key, titel, autor, datum, pfade in eintraege:
        vorhandene, herkunft = dateien_finden(key, pfade, zuordnung, a.pdfdir)
        if not vorhandene:
            ohne_datei.append(key)
            continue
        for pdf in vorhandene:
            geprueft += 1
            seiten, fehler = seitentexte(pdf)
            if seiten is None:
                zeilen.append("## %s" % key)
                zeilen.append("")
                zeilen.append("%s" % fehler)
                zeilen.append("")
                continue
            if not any(s.strip() for s in seiten):
                zeilen.append("## %s" % key)
                zeilen.append("")
                zeilen.append("Kein Text extrahierbar, vermutlich ein Scan ohne Textebene. %d Seiten." % len(seiten))
                zeilen.append("")
                continue
            treffer = suchen(seiten, a.begriffe, a.regex, a.kontext, a.maxtreffer)
            if not treffer:
                continue
            getroffen += 1
            zeilen.append("## %s" % key)
            zeilen.append("")
            zeilen.append("%s" % titel)
            zeilen.append("")
            zeilen.append("Datei %s, %d Seiten" % (os.path.basename(pdf), len(seiten)))
            zeilen.append("")
            for begriff, nr, auszug in treffer:
                zeilen.append("- Begriff %s, Seite %d" % (begriff, nr))
                zeilen.append("")
                zeilen.append("  > %s" % auszug)
                zeilen.append("")

    if getroffen == 0:
        zeilen.append("Keine Treffer in %d geprueften Dateien." % geprueft)
    if ohne_datei:
        zeilen.append("")
        zeilen.append("## Nicht geprueft, keine Datei zugeordnet")
        zeilen.append("")
        for k in ohne_datei:
            zeilen.append("- %s" % k)

    with io.open(a.out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(zeilen))
    print("Geprueft %d Dateien, Treffer in %d, ohne Zuordnung %d. Bericht nach %s"
          % (geprueft, getroffen, len(ohne_datei), a.out))


if __name__ == "__main__":
    main()
