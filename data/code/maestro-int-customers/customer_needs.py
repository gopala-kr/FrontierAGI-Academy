"""customer_needs.py — which AI customers value verifiable trust most (our scoring).

Seven customer segments are scored 1-5 on five needs. Scores are OUR assumptions,
informed by the 2026 surveys cited in the article (governance and integration as top
barriers; quality as top blocker for agent teams). Maestro's fit = how much of each
segment's weighted need its assets (gate record, environments, on-prem) cover.
Standard library only.
"""
NEEDS = ["reliability", "compliance", "cost", "integration", "speed"]
MAESTRO = {"reliability": 0.9, "compliance": 0.9, "cost": 0.4, "integration": 0.7, "speed": 0.3}   # how well Maestro serves each need
SEG = {  # segment: scores per need
    "Consumers":                  [2, 1, 5, 1, 5],
    "Developers":                 [3, 1, 4, 3, 5],
    "SMBs":                       [3, 2, 5, 4, 3],
    "Enterprises (unregulated)":  [4, 3, 3, 5, 3],
    "Regulated enterprises":      [5, 5, 2, 4, 2],
    "Governments / sovereign":    [5, 5, 2, 3, 1],
    "AI labs (buying evals/envs)":[5, 4, 2, 2, 3],
}
res = []
for s, sc in SEG.items():
    fit = sum(v * MAESTRO[n] for v, n in zip(sc, NEEDS)) / sum(sc); res.append((fit, s, sc))
print(f"{'segment':28} " + " ".join(f"{n[:6]:>6}" for n in NEEDS) + "  fit")
for fit, s, sc in sorted(res, reverse=True): print(f"{s:28} " + " ".join(f"{v:6d}" for v in sc) + f"  {fit:.2f}")
print("top three for a trust-and-verification product: " + ", ".join(s for _, s, _ in sorted(res, reverse=True)[:3]))
