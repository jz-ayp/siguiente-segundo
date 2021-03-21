"""
Generar JSON para ejercicio de años bisiestos
"""

import json
import random

FILENAME = ".github/classroom/autograding.json"
PROG_FILE = "segundo_siguiente.py"


def siguiente_segundo(h, m, s):
    "Determinar la hora correspondiente al siguiente segundo."
    s += 1
    if s > 59:
        s = 0
        m += 1
        if m > 59:
            m = 0
            h += 1
            if h > 23:
                h = 0
    return (h, m, s)


cases = []
for hora in [0, -1, 23]:
    for minuto in [0, -1, 59]:
        for segundo in [0, -1, 59]:
            if hora == -1:
                hora = random.randint(1, 22)
            if minuto == -1:
                minuto = random.randint(1, 58)
            if segundo == -1:
                segundo = random.randint(1, 58)
            cases.append((hora, minuto, segundo))

output = {}
tests = []

for i, case in enumerate(cases, start=1):
    inp = f"{case[0]}\r\n{case[1]}\r\n{case[2]}"
    outp = siguiente_segundo(*case)
    #outp = f"{outp[0]}\r\n{outp[1]}\r\n{outp[2]}"
    outp = "(\n|.)*".join(str(i) for i in outp)
    name = f"Test{i:02d}"
    entry = {
        "name": name,
        "setup": "",
        "run": "LANG=en_US.utf8 timeout 3m python3 " + PROG_FILE,
        "input": inp,
        "output": outp,
        "comparison": "regex",
        "timeout": 1,
        "points": 1
        }
    tests.append(entry)
tests = {"tests": tests}

with open(FILENAME, "w") as f:
    json.dump(tests, f, indent=2)
