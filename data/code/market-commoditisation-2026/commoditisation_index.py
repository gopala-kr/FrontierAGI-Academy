"""commoditisation_index.py — how fast each layer is turning into a commodity (our index).

Part 1 uses the site's data: the share of LLM releases in data/model-releases.json that
were open-weight, per year. Part 2 scores eight layers 0-10 from three inputs (our
assumptions, explained in the article): open alternative quality, price decline per
year, and number of serious competitors. Higher = more commoditised. Stdlib only.
"""
import json, os
m = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "model-releases.json")))
CUTOFF = "2026-11-17"  # data as it stood when this brief was written (18 Nov)
for y in ("2023", "2024", "2025", "2026"):
    xs = [x for x in m["items"] if str(x["date"]).startswith(y) and str(x["date"]) <= CUTOFF and "llm" in x["mod"]]
    op = sum(1 for x in xs if x.get("open") in (1, 2))
    print(f"{y}: {len(xs):3d} LLM releases, {op / len(xs):.0%} open-weight")
L = [  # layer, open alternative (0-1), price decline per year (0-1), serious competitors
    ("Chips", 0.1, 0.2, 4), ("Frontier models", 0.6, 0.6, 6), ("Open-weight models", 1.0, 0.7, 10), ("Harnesses", 0.6, 0.5, 8),
    ("Frameworks", 1.0, 0.0, 10), ("Runtimes", 0.5, 0.3, 6), ("Builders", 0.4, 0.2, 8), ("Verification & environments", 0.2, 0.1, 3)]
print(f"{'layer':28} index (0 = scarce, 10 = commodity)")
for n, o, p, c in sorted(L, key=lambda r: -(r[1] * 4 + r[2] * 4 + min(r[3], 10) / 10 * 2)):
    idx = o * 4 + p * 4 + min(c, 10) / 10 * 2
    print(f"{n:28} {idx:4.1f} {'#' * round(idx)}")
