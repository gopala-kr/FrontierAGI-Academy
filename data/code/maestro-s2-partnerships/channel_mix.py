"""channel_mix.py — three ways to sell Maestro, and what a year of each brings (scenario).

Direct sales, a cloud marketplace listing, and a systems integrator (SI). For each: deals
per year, average contract value, partner's revenue share, cost of sale per deal and
sales cycle. Net = revenue after the partner's share minus cost of sale. Standard library only.
"""
CH = [  # channel, deals/yr, ACV $k, partner share, cost of sale per deal $k, cycle weeks
    ("Direct (enterprise team)", 22, 310, 0.00, 95, 30),
    ("Cloud marketplace",        40, 140, 0.03, 18, 9),
    ("Systems integrator",       14, 420, 0.20, 40, 24),
]
tot_rev = tot_net = 0
print(f"{'channel':26} {'deals':>5} {'revenue $M':>10} {'net $M':>7} {'net/deal $k':>11} {'cycle wk':>8}")
for n, d, acv, sh, cos, wk in CH:
    rev = d * acv / 1000; net = rev * (1 - sh) - d * cos / 1000; tot_rev += rev; tot_net += net
    print(f"{n:26} {d:5d} {rev:10.2f} {net:7.2f} {net * 1000 / d:11.0f} {wk:8d}")
print(f"all three: ${tot_rev:.2f}M new revenue, ${tot_net:.2f}M after partner shares and cost of sale ({tot_net / tot_rev:.0%})")
d = CH[0]; direct_only = d[1] * d[2] / 1000 - d[1] * d[4] / 1000
print(f"direct only: ${direct_only:.2f}M; partners add ${tot_net - direct_only:.2f}M net in year one")
