"""pulse.py — AI Market Pulse, monthly issue: counts the month from the site's own data.

Reads data/lab-updates.json, data/model-releases.json, data/ai-investments.json and
data/predictions-2027.json. Prints this month's lab announcements by lab, releases by
modality and open share, the latest reported funding quarter, and predictions due.
Change MONTH to produce the next issue. Standard library only.
"""
import json, os
MONTH = "2026-11"
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
lu = json.load(open(os.path.join(D, "lab-updates.json")))["items"]
mr = json.load(open(os.path.join(D, "model-releases.json")))["items"]
iv = json.load(open(os.path.join(D, "ai-investments.json")))
pr = json.load(open(os.path.join(D, "predictions-2027.json")))["items"]
items = [x for x in lu if str(x["date"]).startswith(MONTH)]
by = {}
for x in items: by[x["lab"]] = by.get(x["lab"], 0) + 1
print(f"{MONTH}: {len(items)} lab announcements, {sum(1 for x in items if x.get('flagship'))} flagship")
print("  by lab: " + ", ".join(f"{k} {v}" for k, v in sorted(by.items(), key=lambda kv: -kv[1])))
rel = [x for x in mr if str(x["date"]).startswith(MONTH)]
mods = {}
for x in rel:
    for m in x["mod"]: mods[m] = mods.get(m, 0) + 1
print(f"  model releases: {len(rel)} ({', '.join(f'{k} {v}' for k, v in sorted(mods.items(), key=lambda kv: -kv[1]))}); open-weight {sum(1 for x in rel if x.get('open') in (1, 2))}")
q = iv["quarters"][-1]
print(f"latest funding quarter reported: {q['q']} ${q['total']}B ({q['by']})")
due = [p for p in pr if p["check"] <= MONTH]
print(f"predictions due by {MONTH}: {len(due)} of {len(pr)}; next check {min(p['check'] for p in pr)}")
