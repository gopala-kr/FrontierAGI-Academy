"""billing_units.py — the same 2,000 tickets, billed in four builders' units (illustrative).

Runs our four mini-builds and reads the monthly unit count each prints. Units differ:
n8n executions, Zapier tasks (Zap) or activities (Agent), Copilot Studio credits,
Make credits. Plan sizes and prices are secondary-sourced list prices (Nov 2026,
check the vendors' pages); Copilot and Make per-event credits are our assumptions.
"""
import io, contextlib, runpy, os, re
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def last_numbers(rel):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): runpy.run_path(os.path.join(base, rel))
    return buf.getvalue().strip().splitlines()[-1]
rows = [("n8n (cloud)", "agentic-n8n/mini_n8n.py", r"(\d[\d,]*) executions", "Pro: 10,000 executions for ~EUR 50/month"),
        ("Zapier (Zap)", "agentic-zapier/mini_zapier.py", r"Zap (\d[\d,]*) tasks", "task plans scale with volume"),
        ("Copilot Studio", "agentic-copilot-studio/mini_copilot_studio.py", r"= ([\d,]+) credits", "PAYG $0.01 per credit"),
        ("Make", "agentic-make/mini_make.py", r"([\d,]+) credits a month", "plans sold by credits per month")]
for name, rel, pat, note in rows:
    m = re.search(pat, last_numbers(rel) if "zapier" not in rel else last_numbers(rel))
    print(f"{name:15} {m.group(1):>8} units/month   ({note})")
print("one ticket = 1 n8n execution, but ~5 Zapier tasks or ~9 Make credits: the unit decides the bill")
