"""entrant_map.py — where new AI companies cluster, and how exposed they are to the labs.

Reads data/ai-entrants-2026.json (a hand-curated, sourced sample, not a census) and
groups companies by layer: how many, how many valuations are reported, and the
average 'lab overlap' (our 0-3 judgement of how directly frontier labs compete).
Standard library only.
"""
import json, os
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "ai-entrants-2026.json")))
by = {}
for x in d["items"]: by.setdefault(x["layer"], []).append(x)
print(f"{'layer':11} {'companies':>9} {'avg lab overlap':>15}  examples")
for layer, xs in sorted(by.items(), key=lambda kv: -sum(x["overlap"] for x in kv[1]) / len(kv[1])):
    ov = sum(x["overlap"] for x in xs) / len(xs)
    print(f"{layer:11} {len(xs):9d} {ov:15.1f}  {', '.join(x['name'] for x in xs[:3])}")
hi = [x["name"] for x in d["items"] if x["overlap"] >= 3]; lo = [x["name"] for x in d["items"] if x["overlap"] == 0]
print(f"most exposed to the labs (3/3): {len(hi)}; least exposed (0/3): {len(lo)} -> {', '.join(lo)}")
