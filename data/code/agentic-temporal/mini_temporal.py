"""mini_temporal.py — Temporal's durable-execution pattern in plain Python (illustrative).

A workflow is deterministic code; anything with side effects (model calls, CRM,
payments) runs as an activity whose result is written to an event history. After a
crash the workflow is REPLAYED: completed activities return their recorded result
instead of running again. Approvals arrive as signals, even days later. Stdlib only.
"""
class Crash(Exception): pass
history, real_calls = [], {"model": 0, "crm": 0, "payments": 0}
def activity(name, kind, fn):
    for ev in history:                                  # replay: reuse the recorded result
        if ev[0] == name: return ev[1]
    real_calls[kind] += 1; result = fn(); history.append((name, result)); return result
def triage_workflow(ticket, amount, signals, crash_after=None):
    intent = activity("classify", "model", lambda: "refund")
    tier = activity("lookup", "crm", lambda: "silver")
    if amount > 100:
        if "approve" not in signals: return "waiting for signal 'approve'"   # durable timer/wait, no process held
    res = activity("refund", "payments", lambda: f"refunded ${amount}")
    if crash_after == "refund" and not any(e[0] == "reply" for e in history) and real_calls["payments"] == 1 and not signals.get("replayed"):
        signals["replayed"] = True; raise Crash()
    reply = activity("reply", "model", lambda: "reply sent")
    return f"{intent}/{tier}: {res}, {reply}"
sig = {}
print("run 1:", triage_workflow("T2", 250, sig))
sig["approve"] = True                                    # 3 days later: signal arrives
try: triage_workflow("T2", 250, sig, crash_after="refund")
except Crash: print("run 2: worker crashed right after the refund activity")
print("run 3 (replay):", triage_workflow("T2", 250, sig))
print(f"event history: {[e[0] for e in history]}")
print(f"real calls: {real_calls}  -> payments called once despite the crash")
