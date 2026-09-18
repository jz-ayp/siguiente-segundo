import json
from pathlib import Path

#base_dir = Path(__file__).resolve().parent.parent
base_dir = Path(".")
f_in = base_dir / ".github" / "classroom" / "autograding.json"
f_out = base_dir / ".github" / "classroom" / "classroom50.json"

with f_in.open("r", encoding="utf-8") as file:
    tests = json.load(file)

#print(tests)
#print(type(data))

clsrm50 = []
for test in tests["tests"]:
    #print(test)
    clsrm50.append(
        {
            "name": test["name"],
            "type": "io",
            "run": "python3" + test["run"].split("python3")[1],
            "points": 10,
            "comparison": test["comparison"],
            "input": test["input"],
            "expected": test["output"],
        }
    )
clsrm50 = {"assignments": [{"tests": clsrm50}]}

with f_out.open("w", encoding="utf-8") as file:
    json.dump(clsrm50, file, indent=2, ensure_ascii=False)
          