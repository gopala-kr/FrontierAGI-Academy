"""crash_test.py — a worker dies in the middle of a refund. What happens on retry? (illustrative)

The triage agent decides to refund ticket T2 ($250), calls the payments API, and the
worker crashes before it records that the call succeeded. Three runtime models retry:
  naive      : re-run the whole task from the start
  checkpoint : resume from the last saved step (saved before the side effect)
  durable    : resume from an event history that records each completed activity,
               and call payments with an idempotency key
Standard library only; the payments API is a stub that counts real money movements.
"""
class Payments:
    def __init__(self): self.moves, self.seen = [], set()
    def refund(self, ticket, amount, key=None):
        if key and key in self.seen: return "duplicate ignored"
        if key: self.seen.add(key)
        self.moves.append((ticket, amount)); return "ok"

STEPS = ["classify", "lookup", "approve", "refund", "reply"]

def run(model, crash_at="refund"):
    pay, saved, history, crashed = Payments(), None, [], False
    def attempt(start):
        nonlocal crashed
        for i in range(start, len(STEPS)):
            s = STEPS[i]
            if model == "durable" and s in history: continue        # replay: completed activities are skipped
            if s == "refund":
                pay.refund("T2", 250, key="T2-refund" if model == "durable" else None)
                if not crashed: crashed = True; return "crash"      # dies before recording success
            if model == "checkpoint": saved_step[0] = i + 1
            history.append(s)
        return "done"
    saved_step = [0]
    attempt(0)
    start = saved_step[0] if model == "checkpoint" else 0
    attempt(start)
    return len(pay.moves), sum(a for _, a in pay.moves)

for m in ("naive", "checkpoint", "durable"):
    n, total = run(m)
    print(f"{m:10} refunds sent: {n}  money moved: ${total}  {'OK' if n == 1 else 'DOUBLE REFUND'}")
print("only history + an idempotency key make the side effect happen exactly once")
