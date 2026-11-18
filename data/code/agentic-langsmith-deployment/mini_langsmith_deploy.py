"""mini_langsmith_deploy.py — the LangSmith Deployment pattern in plain Python (illustrative).

Threads (one per ticket) hold checkpointed state; runs are queued and picked up by
workers; a run can stop at an interrupt and resume days later over the API; a new
message on a busy thread follows a "double-texting" policy (reject, enqueue,
interrupt or rollback). Stub agent. Standard library only.
"""
from collections import deque
threads, queue, log = {}, deque(), []
def create_run(tid, msg, policy="enqueue"):
    th = threads.setdefault(tid, {"state": {}, "busy": False, "checkpoints": 0})
    if th["busy"]:
        if policy == "reject": log.append(f"{tid}: new message rejected (run in progress)"); return
        if policy == "interrupt": log.append(f"{tid}: current run interrupted, new run queued")
    queue.append((tid, msg)); th["busy"] = True
def worker():
    while queue:
        tid, msg = queue.popleft(); th = threads[tid]; s = th["state"]
        s.setdefault("msgs", []).append(msg); th["checkpoints"] += 1
        if "refund $250" in msg and "approved" not in s:
            s["waiting"] = "approve $250?"; log.append(f"{tid}: interrupted, waiting for a human (checkpoint {th['checkpoints']})"); continue
        if msg == "resume: yes": s["approved"] = True; s.pop("waiting", None); s["result"] = "refunded $250"
        elif "refund $40" in msg: s["result"] = "refunded $40"
        th["checkpoints"] += 1; th["busy"] = False; log.append(f"{tid}: done -> {s.get('result', 'replied')} (checkpoints {th['checkpoints']})")
create_run("T1", "refund $40"); create_run("T2", "refund $250"); create_run("T2", "also my mug broke", policy="reject")
worker()
log.append("... 3 days later, the approver clicks yes (POST /threads/T2/runs with resume) ...")
threads["T2"]["busy"] = False; create_run("T2", "resume: yes"); worker()
print("\n".join(log))
