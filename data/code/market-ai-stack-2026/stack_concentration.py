"""stack_concentration.py — how crowded each model layer was in 2026, from the site's own data.

Reads data/model-releases.json (the Model Release Map) and counts, per modality, the
releases dated 2026, how many different labs released something, the top lab's share
and the share of open-weight releases. Standard library only.
"""
import json, os
m = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "model-releases.json")))
rows = {}
for x in m["items"]:
    if not str(x["date"]).startswith("2026"): continue
    for mod in x["mod"]:
        r = rows.setdefault(mod, {"n": 0, "labs": {}, "open": 0})
        r["n"] += 1; r["labs"][x["lab"]] = r["labs"].get(x["lab"], 0) + 1; r["open"] += 1 if x.get("open") in (1, 2) else 0
print(f"{'modality':8} {'releases':>8} {'labs':>5} {'top lab share':>14} {'open-weight':>11}")
for mod, r in sorted(rows.items(), key=lambda kv: -kv[1]["n"]):
    top, k = max(r["labs"].items(), key=lambda kv: kv[1])
    print(f"{mod:8} {r['n']:8d} {len(r['labs']):5d} {k / r['n']:13.0%} ({top}) {r['open'] / r['n']:10.0%}")
allr = sum(r["n"] for r in rows.values()); print(f"2026 releases in the map: {allr} across {len({l for r in rows.values() for l in r['labs']})} labs")
