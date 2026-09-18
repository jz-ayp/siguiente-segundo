"""
Generar autograding tests para ejercicio de siguiente segundo (versión Classroom 50).
"""

import json
import random

FILENAME = "./solution/classroom50.json"
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

for case in cases:
    inp = f"{case[0]}\r\n{case[1]}\r\n{case[2]}"
    outp = siguiente_segundo(*case)
    #outp = f"{outp[0]}\r\n{outp[1]}\r\n{outp[2]}"
    outp = "(\n|.)*".join(str(i) for i in outp)
    name = f"{case[0]:02d}:{case[1]:02d}:{case[2]:02d}"
    entry = {
        "name": name,
        "type": "io",
        "run": "python3 " + PROG_FILE,
        "points": 10,
        "comparison": "regex",
        "input": inp,
        "expected": outp,
    }
    tests.append(entry)
#tests = {"tests": tests}
clsrm50 = {"assignments": [{"tests": tests}]}

with open(FILENAME, "w") as f:
    json.dump(clsrm50, f, indent=2, ensure_ascii=False)
