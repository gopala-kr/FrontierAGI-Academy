"""overlap_score.py — how much of Maestro's revenue a frontier lab's new agent puts at risk.

Scenario numbers (month 48). For each product feature: its share of revenue, how much the
lab's launch overlaps it (0-1), and how many months a lab would need to copy what is
different about Maestro's version. Revenue at risk = share x overlap x (1 - copy months / 24),
capped at 0. Standard library only.
"""
ARR = 24.0   # $M annualised revenue at month 48 (scenario)
FEATURES = [  # name, revenue share, overlap with the lab's launch, months for the lab to copy Maestro's edge
    ("Coding harness (CLI, IDE, PR bot)",  0.30, 0.90,  3),
    ("Agent memory and skills",            0.12, 0.80,  6),
    ("Agent platform (customer agents)",   0.20, 0.50, 12),
    ("Verified-skill gate and audit record", 0.18, 0.20, 24),
    ("Customer-specific environments",     0.12, 0.10, 30),
    ("On-prem / private deployment",       0.08, 0.30, 18),
]
print(f"{'feature':38} {'share':>5} {'overlap':>7} {'copy mo':>7} {'at risk $M':>10}")
total = 0.0
for name, share, ov, copy in FEATURES:
    risk = ARR * share * ov * max(0.0, 1 - copy / 24); total += risk
    print(f"{name:38} {share:5.0%} {ov:7.0%} {copy:7d} {risk:10.2f}")
print(f"revenue at risk: ${total:.2f}M of ${ARR:.1f}M ARR ({total / ARR:.0%})")
safe = sum(ARR * s for n, s, o, c in FEATURES if o <= 0.3)
print(f"revenue in features the lab barely touches (overlap <= 30%): ${safe:.2f}M ({safe / ARR:.0%})")
