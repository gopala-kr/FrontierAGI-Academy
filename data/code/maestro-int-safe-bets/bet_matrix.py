"""bet_matrix.py — twelve positions Maestro could take, scored on five factors (our model).

Factors (1-5): lab entry risk (higher = labs likely to enter, bad), commoditisation (bad),
Maestro advantage (good), market size (good, our assumption) and customer pull (good,
from customer_needs.py in Interlude Part 4). Safety = advantage + size + pull - entry -
commoditisation. Standard library only.
"""
B = [  # position, lab entry, commoditisation, Maestro advantage, market size, customer pull
    ("Independent gate & verification API",       2, 2, 5, 3, 5),
    ("Environments as a product (for labs)",      3, 2, 5, 3, 4),
    ("Evaluation for regulators / safety insts.", 1, 2, 4, 2, 4),
    ("Regulated vertical agents (finance, health)",3, 2, 4, 4, 5),
    ("Sovereign / India deployments",             2, 2, 3, 3, 4),
    ("On-prem gated agent platform",              2, 3, 4, 3, 4),
    ("Post-trained open model (Maestro-2.5)",     4, 4, 3, 3, 3),
    ("Coding harness",                            5, 5, 2, 4, 3),
    ("General agent builder",                     4, 4, 1, 4, 2),
    ("Frontier model from scratch (Maestro-3)",   5, 3, 1, 5, 2),
    ("Agent-to-agent commerce rails",             3, 2, 2, 3, 2),
    ("Consumer assistant",                        5, 5, 1, 5, 1),
]
rows = sorted(((a + s + p - e - c, n, e, c, a, s, p) for n, e, c, a, s, p in B), reverse=True)
print(f"{'position':44} entry commod adv size pull  safety")
for sc, n, e, c, a, s, p in rows: print(f"{n:44} {e:5d} {c:6d} {a:3d} {s:4d} {p:4d}  {sc:+5d}")
print("safe and Maestro-advantaged (safety >= 6): " + "; ".join(n for sc, n, *_ in rows if sc >= 6))
