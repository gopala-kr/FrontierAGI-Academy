"""kill_projects.py — focus by killing good projects (scenario, month 50).

Seven initiatives compete for 4,096 GPUs' worth of hours and 40 engineers. Each has an
expected value ($M over 24 months, our scenario estimate), GPU-hours (millions) and
engineers. Score = value / (share of GPU budget + share of engineering). Rule from the
owner's notes on Altman (focus by killing good projects): keep only scores of 60 or more. Standard library only.
"""
GPU_BUDGET, ENG_BUDGET = 14.0, 40          # million GPU-hours per year, engineers
INIT = [  # name, value $M, GPU-hours M, engineers
    ("Gate-as-a-service API",             38, 0.6,  6),
    ("Customer environments v2",          34, 2.0,  7),
    ("Post-train open model (Maestro-2.5)", 30, 3.5, 6),
    ("Regulated-industry edition",        26, 0.8,  6),
    ("Maestro-3 from scratch",            45, 11.0, 12),
    ("Consumer coding app",               12, 1.2,  8),
    ("Voice agent pilot",                  6, 0.9,  5),
]
scored = sorted(INIT, key=lambda x: -x[1] / (x[2] / GPU_BUDGET + x[3] / ENG_BUDGET))
g = e = 0; keep, kill = [], []
for name, v, gh, eng in scored:
    s = v / (gh / GPU_BUDGET + eng / ENG_BUDGET)
    if s >= 60: keep.append(name); g += gh; e += eng; tag = "KEEP"
    else: kill.append(name); tag = "kill"
    print(f"{tag:4} {name:38} value {v:3d}  score {s:6.1f}  GPU-h {gh:4.1f}M  eng {eng:2d}")
print(f"asked for: {sum(x[2] for x in INIT):.1f}M GPU-hours and {sum(x[3] for x in INIT)} engineers; budget {GPU_BUDGET}M and {ENG_BUDGET}")
print(f"kept {len(keep)} of {len(INIT)}: {g:.1f}M GPU-hours, {e} engineers (slack: {GPU_BUDGET - g:.1f}M, {ENG_BUDGET - e}); killed {len(kill)}: {', '.join(kill)}")
