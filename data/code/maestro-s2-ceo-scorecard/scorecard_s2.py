"""scorecard_s2.py — the Season 2 CEO scorecard at month 54 (scenario).

Each metric has a target set at the Series A (month 18) and the value reached, taken from
earlier Season 2 scripts where one exists. Green = met, amber = within 25% of target, red = missed. Standard library only.
"""
M = [  # metric, target, actual, higher is better, source
    ("Net revenue retention, platform (%)", 130, 165, True,  "S2 Part 19 cohort_retention.py"),
    ("Merge rate on customer tasks (%)",     55, 45.2, True, "S2 Part 19 metrics.py"),
    ("Platform gross margin (%)",            45, 27,  True,  "S2 Part 15 platform_economics.py"),
    ("Maestro-2 gain on held-out tasks (pts)", 4, 5.2, True, "S2 Part 15 eval_m2.py"),
    ("Training run goodput (%)",             90, 90.8, True, "S2 Part 14 run_sim.py"),
    ("Merged rate with harness (%)",         50, 59,  True,  "S2 Part 16 harness_ab.py"),
    ("Enterprise security reviews passed",    8, 6,   True,  "S2 Part 18 security_review.py"),
    ("Months of runway",                     24, 30.3, True, "runway_and_options.py"),
    ("Gate incidents (unsafe skill shipped)", 0, 0,   False, "gate log (scenario)"),
    ("Revenue at risk from lab launch (%)",  20, 36,  False, "S2 Part 20 overlap_score.py"),
]
tally = {"green": 0, "amber": 0, "red": 0}
for name, tgt, act, hib, src in M:
    ok = act >= tgt if hib else act <= tgt
    near = (act >= tgt * 0.75) if hib else (act <= tgt * 1.25 + 0.5)
    rag = "green" if ok else "amber" if near else "red"; tally[rag] += 1
    print(f"{rag:5} {name:40} target {tgt:>5} actual {act:>5}  ({src})")
print(f"{tally['green']} green, {tally['amber']} amber, {tally['red']} red")
