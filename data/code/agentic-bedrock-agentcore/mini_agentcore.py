"""mini_agentcore.py — the AgentCore pattern in plain Python (illustrative).

Separate services around your agent: a runtime that gives every session its own
isolated worker, a gateway that turns APIs into tools and checks the caller, an
identity service that hands out per-tenant credentials, a memory service, and
usage metering. The agent itself is any framework; here a stub. Stdlib only.
"""
TICKETS = [("acme", "s1", "T1", 40), ("acme", "s2", "T2", 250), ("globex", "s3", "T3", 90), ("globex", "s3", "T3b", 30)]
SECRETS = {"acme": "acme-crm-token", "globex": "globex-crm-token"}

class Identity:                                   # hands out a credential only for the caller's own tenant
    def token(self, tenant, workload): return SECRETS[tenant] if workload == "triage-agent" else None
class Gateway:                                    # APIs as tools; checks the token belongs to the tenant
    def __init__(self): self.calls = 0
    def call(self, tool, tenant, token, **a):
        self.calls += 1
        if token != SECRETS[tenant]: return "403 wrong tenant"
        return {"lookup": f"{tenant}-tier-gold", "refund": f"refunded ${a.get('amount')}"}[tool]
class Memory:
    def __init__(self): self.short = {}
    def add(self, session, event): self.short.setdefault(session, []).append(event)
class Runtime:                                    # one isolated worker per session; metered by active seconds
    def __init__(self): self.workers, self.cpu_s = {}, 0.0
    def invoke(self, tenant, session, fn):
        w = self.workers.setdefault(session, {"tenant": tenant, "scratch": []})
        if w["tenant"] != tenant: return "session belongs to another tenant"
        self.cpu_s += 1.5; return fn(w)

ident, gw, mem, rt = Identity(), Gateway(), Memory(), Runtime()
def agent(tenant, session, tid, amount):
    def body(worker):
        tok = ident.token(tenant, "triage-agent")
        tier = gw.call("lookup", tenant, tok); mem.add(session, f"{tid}:{tier}")
        worker["scratch"].append(tid)
        res = "held for approval" if amount > 100 else gw.call("refund", tenant, tok, amount=amount)
        return f"{tier} -> {res}"
    return rt.invoke(tenant, session, body)
for t, s, tid, amt in TICKETS: print(f"{t:7} {s} {tid:4}: {agent(t, s, tid, amt)}")
print("cross-tenant call:", gw.call("lookup", "acme", SECRETS["globex"]))
print(f"sessions isolated: {len(rt.workers)} workers; session s3 scratch: {rt.workers['s3']['scratch']}")
print(f"metered: {rt.cpu_s} vCPU-seconds, {gw.calls} gateway calls, {sum(len(v) for v in mem.short.values())} memory events")
