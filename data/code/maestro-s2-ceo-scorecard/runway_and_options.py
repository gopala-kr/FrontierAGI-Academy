"""runway_and_options.py — cash, burn and three paths at month 54 (scenario).

Starts from cash at month 48 (S2 Part 20) after the Phase 9 decisions: kill three projects
(saves burn), add partner revenue. Then compares three paths with what each needs to be true.
Standard library only.
"""
cash48, burn48 = 38.8, 1.45          # $M, $M per month (S2 Part 20)
saving, partner_net = 0.28, 0.10     # monthly burn saved by kills (Part 21), monthly partner net (Part 22)
burn = burn48 - saving - partner_net
cash54 = cash48 - 6 * burn
print(f"month 54: cash ${cash54:.1f}M, net burn ${burn:.2f}M/month, runway {cash54 / burn:.1f} months")
PATHS = [
    ("Series B ($120M)", "ARR growth >= 2.5x a year and NRR >= 140% for two more quarters", 120.0, burn * 2.2),
    ("Default alive at current size", "gross margin >= 55% and ARR >= $40M", 0.0, 0.0),
    ("Strategic sale", "a buyer values the gate record, not just the team", None, None),
]
for name, needs, raise_, new_burn in PATHS:
    if raise_ is None: print(f"{name:32} needs: {needs}"); continue
    if new_burn == 0: print(f"{name:32} needs: {needs}  (break-even: burn falls to $0)"); continue
    print(f"{name:32} needs: {needs}  -> runway {(cash54 + raise_) / new_burn:.0f} months at ${new_burn:.2f}M/month")
