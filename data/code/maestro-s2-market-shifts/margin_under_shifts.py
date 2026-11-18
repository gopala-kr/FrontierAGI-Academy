"""margin_under_shifts.py — Maestro's gross margin when the market shifts (scenario).

Three shifts arrive together: token prices fall, an open-weight model reaches parity
(customers push prices down), and buyers move from seats to price per finished task.
Price per task and cost per task are scenario numbers; the cost falls with token prices
only for the part of cost that is model tokens. Standard library only.
"""
PRICE, COST, TOKEN_SHARE = 4.00, 1.32, 0.70     # $ per finished task, $ cost per task, share of cost that is tokens
def margin(token_cut, parity_cut, per_task_mix):
    cost = COST * (TOKEN_SHARE / token_cut + (1 - TOKEN_SHARE))
    price = PRICE * (1 - parity_cut)
    price = price * (1 - per_task_mix * 0.15)    # per-task deals are priced ~15% below seat-equivalent
    return price, cost, (price - cost) / price
print(f"{'token price cut':>15} {'parity price cut':>16} {'per-task mix':>12} {'price':>6} {'cost':>5} {'margin':>7}")
for tc in (1, 2, 5):
    for pc in (0.0, 0.3):
        for mix in (0.2, 0.8):
            p, c, m = margin(tc, pc, mix)
            print(f"{tc:>14}x {pc:16.0%} {mix:12.0%} {p:6.2f} {c:5.2f} {m:7.1%}")
p0, c0, m0 = margin(1, 0.0, 0.2); p1, c1, m1 = margin(5, 0.3, 0.8)
print(f"today {m0:.1%} -> all three shifts {m1:.1%}: cheaper tokens more than pay for lower prices")
p2, c2, m2 = margin(1, 0.3, 0.8)
print(f"but if Maestro does not pass on cheaper tokens to its own costs (no re-platforming): {m2:.1%}")
