"""response_options.py — four responses to a frontier lab shipping a competing agent.

Scenario numbers. Each option has outcomes over 24 months with probabilities; value is
company value in $M at month 72. Extra burn shortens runway from the current cash.
Prints expected value, runway, and how much the "win" probability of the chosen option
could fall before another option beats it. Standard library only.
"""
CASH, BURN = 38.8, 1.45   # $M cash at month 48 and monthly net burn (scenario)
OPTIONS = {   # name: (extra monthly burn $M, [(probability, value $M), ...])
    "Compete head-on (match every feature)":      (0.90, [(0.15, 900), (0.45, 260), (0.40, 60)]),
    "Go vertical (regulated industries only)":    (0.20, [(0.30, 420), (0.50, 230), (0.20, 90)]),
    "Become the gate layer for any model/harness": (0.35, [(0.35, 650), (0.45, 300), (0.20, 80)]),
    "Sell now (acqui-hire offer)":               (0.00, [(1.00, 210)]),
}
res = {}
for name, (extra, outs) in OPTIONS.items():
    ev = sum(p * v for p, v in outs); runway = CASH / (BURN + extra); res[name] = (ev, runway, outs)
    print(f"{name:45} EV ${ev:6.1f}M  runway {runway:5.1f} months")
best = max(res, key=lambda k: res[k][0]); second = sorted(res, key=lambda k: -res[k][0])[1]
print(f"best: {best}")
ev2 = res[second][0]; outs = res[best][2]
(p1, v1), (p2, v2), (p3, v3) = outs
for d in range(0, int(p1 * 1000) + 1):                        # move probability from the win to the middle outcome
    q = p1 - d / 1000
    if q < 0: break
    if q * v1 + (p2 + d / 1000) * v2 + p3 * v3 < ev2:
        print(f"it stays best unless the chance of the top outcome falls from {p1:.0%} to below {q:.1%} (then: {second})"); break
