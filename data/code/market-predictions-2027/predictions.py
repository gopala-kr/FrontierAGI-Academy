"""predictions.py — the Interlude's ten predictions for 2027, ready to be scored later.

Reads data/predictions-2027.json. Prints each claim with its confidence and check date,
the expected number that come true if the confidences are honest, and how they will be
scored (Brier score = mean of (confidence - outcome)^2 once outcomes are known).
Standard library only.
"""
import json, os
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "predictions-2027.json")))
for p in sorted(d["items"], key=lambda p: (p["check"], -p["conf"])):
    print(f"#{p['id']:2d} {p['conf']:.0%} by {p['check']}  {p['claim'][:78]}")
exp = sum(p["conf"] for p in d["items"])
print(f"expected to come true if calibrated: {exp:.1f} of {len(d['items'])}")
done = [p for p in d["items"] if p["outcome"] is not None]
print(f"scored so far: {len(done)}" + (f", Brier {sum((p['conf'] - p['outcome']) ** 2 for p in done) / len(done):.3f}" if done else " (first checks due 2027-06)"))
