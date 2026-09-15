"""xlsx ohne openpyxl lesen: erstes Blatt als Liste von Zeilen."""
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def col_index(ref):
    letters = re.match(r"[A-Z]+", ref).group(0)
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch) - 64)
    return n - 1


def lies(pfad):
    with zipfile.ZipFile(pfad) as z:
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            for si in root.findall("m:si", NS):
                shared.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
        blatt = sorted(n for n in z.namelist() if n.startswith("xl/worksheets/sheet"))[0]
        root = ET.fromstring(z.read(blatt))
        zeilen = []
        for row in root.iter("{%s}row" % NS["m"]):
            werte = {}
            for c in row.findall("m:c", NS):
                v = c.find("m:v", NS)
                if v is None:
                    is_ = c.find("m:is", NS)
                    val = "".join(t.text or "" for t in is_.iter("{%s}t" % NS["m"])) if is_ is not None else None
                else:
                    val = v.text
                    if c.get("t") == "s":
                        val = shared[int(val)]
                    elif c.get("t") not in ("str", "inlineStr", "b"):
                        try:
                            val = float(val)
                        except (TypeError, ValueError):
                            pass
                werte[col_index(c.get("r"))] = val
            n = max(werte) + 1 if werte else 0
            zeilen.append([werte.get(i) for i in range(n)])
        return zeilen


if __name__ == "__main__":
    for r in lies(sys.argv[1])[:int(sys.argv[2]) if len(sys.argv) > 2 else 6]:
        print(r)
