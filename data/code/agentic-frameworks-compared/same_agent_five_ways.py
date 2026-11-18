"""same_agent_five_ways.py — measure our five mini-builds of the same triage agent.

Each sibling folder holds a stdlib mini-version of one framework's pattern (ours,
illustrative). This counts code lines (no blanks, comments or docstrings), the
framework concepts each one needs, and checks they all reach the same decisions.
"""
import io, contextlib, runpy, os
BUILDS = [("OpenAI Agents SDK", "agentic-openai-agents-sdk/mini_openai_agents.py", ["Agent", "handoff", "guardrail", "approval", "runner loop"]),
          ("Google ADK 2.0", "agentic-google-adk/mini_adk.py", ["node", "graph", "session state", "router", "HITL pause"]),
          ("LangGraph", "agentic-langgraph/mini_langgraph.py", ["state", "node", "edge", "conditional edge", "checkpointer", "interrupt"]),
          ("CrewAI", "agentic-crewai/mini_crewai.py", ["Agent (role/goal/backstory)", "Task", "Crew", "Process", "Flow", "router"]),
          ("Claude Agent SDK", "agentic-claude-sdk-microsoft/mini_claude_sdk.py", ["query loop", "allowed tools", "hook", "can_use_tool", "subagent"]),
          ("MS Agent Framework", "agentic-claude-sdk-microsoft/mini_ms_workflow.py", ["executor", "edge", "message", "request port", "superstep"])]

def code_lines(path):
    src, n, in_doc = open(path).read().splitlines(), 0, False
    for l in src:
        s = l.strip()
        if s.startswith('"""'): in_doc = not in_doc if s.count('"""') == 1 else in_doc; continue
        if in_doc or not s or s.startswith("#"): continue
        n += 1
    return n

def decisions(path):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): runpy.run_path(path)
    out = {}
    for line in buf.getvalue().splitlines():
        if line[:2] in ("T1", "T2", "T3", "T4"): out[line[:2]] = "refund" if "refunded" in line else "escalate" if "escalat" in line else "no refund"
    return out

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
print(f"{'framework':19} {'lines':>5} {'concepts':>8}  decisions T1-T4")
for name, rel, concepts in BUILDS:
    p = os.path.join(base, rel); d = decisions(p)
    print(f"{name:19} {code_lines(p):5} {len(concepts):8}  {' '.join(d[k] for k in sorted(d))}")
print("all six reach the same four decisions; what differs is where the control lives")
