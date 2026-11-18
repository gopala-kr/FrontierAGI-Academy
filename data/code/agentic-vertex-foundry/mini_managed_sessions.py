"""mini_managed_sessions.py — the managed-sessions pattern of Vertex AI Agent Engine and
Azure AI Foundry Agent Service, in plain Python (illustrative).

You deploy the agent once; the platform keeps per-user sessions (events + state),
a memory bank that extracts facts across sessions, and scopes every call to a
tenant identity. The two clouds name things differently: sessions/events vs
threads/runs. Stub agent. Standard library only.
"""
class ManagedAgent:
    def __init__(self, cloud): self.cloud, self.sessions, self.memory = cloud, {}, {}
    def session(self, tenant, user):
        key = (tenant, user); return self.sessions.setdefault(key, {"events": [], "state": {}})
    def query(self, tenant, user, text):
        s = self.session(tenant, user); s["events"].append(("user", text))
        facts = self.memory.get((tenant, user), [])
        if "refund" in text: s["state"]["last_intent"] = "refund"
        if "my order" in text: self.memory.setdefault((tenant, user), []).append("prefers email replies")
        reply = f"[{self.cloud}] intent={s['state'].get('last_intent', '-')}, remembered={facts or '-'}"
        s["events"].append(("agent", reply)); return reply
for cloud, unit in (("vertex", "sessions/events"), ("foundry", "threads/runs")):
    a = ManagedAgent(cloud)
    print(cloud, unit)
    print("  ", a.query("acme", "ana", "refund my order, it broke"))
    a.sessions.pop(("acme", "ana"))                     # new session next week; memory survives
    print("  ", a.query("acme", "ana", "hello again"))
    print("  ", a.query("globex", "ana", "hello"))     # same user name, other tenant: nothing shared
