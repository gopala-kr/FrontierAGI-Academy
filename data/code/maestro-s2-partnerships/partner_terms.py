"""partner_terms.py — score partnership offers by the options they take away (scenario).

Each clause gets a cost in "option value" points (0-10, our scale) and each offer a
benefit in points. Accept when benefit exceeds the total clause cost by a margin.
The scale is ours; the clause types are standard in commercial agreements.
Standard library only.
"""
CLAUSE_COST = {"exclusivity": 9, "right of first refusal on a sale": 7, "information rights on roadmap": 5,
               "most-favoured pricing": 3, "minimum volume commitment": 2, "co-marketing": 0}
OFFERS = [  # name, benefit points, clauses
    ("Cloud marketplace listing", 8, ["co-marketing", "minimum volume commitment"]),
    ("Systems integrator (white-label)", 9, ["most-favoured pricing", "exclusivity"]),
    ("Systems integrator (renegotiated, non-exclusive)", 7, ["most-favoured pricing"]),
    ("Frontier lab: model credits for exclusivity", 10, ["exclusivity", "information rights on roadmap", "right of first refusal on a sale"]),
]
for name, ben, cl in OFFERS:
    cost = sum(CLAUSE_COST[c] for c in cl); net = ben - cost
    verdict = "ACCEPT" if net >= 2 else "negotiate" if net >= -2 else "DECLINE"
    print(f"{verdict:9} {name:48} benefit {ben:2d}  clause cost {cost:2d}  net {net:+d}")
print("rule: a clause that limits who you can sell to, or who can buy you, costs more than most benefits")
