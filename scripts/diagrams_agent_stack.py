# Generates assets/diagrams/agent-stack, agent-ui and agent-prod SVGs (python3 scripts/diagrams_agent_stack.py)
import html, os
OUT='/home/user/Claude_Project_3_LLM/assets/diagrams/agent-stack/'
E=lambda s: html.escape(s)
DA64=' stroke-dasharray="6 4"'; DA54=' stroke-dasharray="5 4"'; MS=' marker-start="url(#%s)"'; FW=' font-weight="700"'
LC={'L1':'#2563eb','L2':'#7c3aed','L3':'#9333ea','L4':'#0d9488','L5':'#0891b2','L6':'#dc2626','L7':'#475569','L8':'#d97706','CD':'#be185d'}
def head(w,h,title,sub=''):
    s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="Inter, Segoe UI, Helvetica, Arial, sans-serif">'
    s+='<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#334155"/></marker>'
    s+='<marker id="r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#dc2626"/></marker></defs>'
    s+=f'<rect width="{w}" height="{h}" fill="#ffffff"/><text x="24" y="34" font-size="20" font-weight="800" fill="#0f172a">{E(title)}</text>'
    if sub: s+=f'<text x="24" y="56" font-size="13" fill="#475569">{E(sub)}</text>'
    return s
def box(x,y,w,h,t,sub=None,c='#334155',fill=None,dash=False,fs=14):
    f=fill or c+'14'
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{f}" stroke="{c}" stroke-width="1.6"{DA64 if dash else ""}/>'
    s+=f'<text x="{x+w/2}" y="{y+ (h/2 if not sub else 22)+ (5 if not sub else 0)}" text-anchor="middle" font-size="{fs}" font-weight="700" fill="#0f172a">{E(t)}</text>'
    if sub:
        for i,l in enumerate(sub if isinstance(sub,list) else [sub]):
            s+=f'<text x="{x+w/2}" y="{y+42+i*16}" text-anchor="middle" font-size="12" fill="#334155">{E(l)}</text>'
    return s
def band(x,y,w,h,label,c):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{c}0d" stroke="{c}" stroke-width="1.2"/><text x="{x+12}" y="{y+20}" font-size="12" font-weight="800" fill="{c}" letter-spacing=".5">{E(label)}</text>'
def arr(x1,y1,x2,y2,lab=None,c='#334155',dash=False,both=False,lx=None,ly=None,m='a'):
    s=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="1.7"{DA54 if dash else ""} marker-end="url(#{m})"{(MS%m) if both else ""}/>'
    if lab:
        X=lx if lx is not None else (x1+x2)/2; Y=ly if ly is not None else (y1+y2)/2-6
        s+=f'<rect x="{X-len(lab)*3.4-4}" y="{Y-12}" width="{len(lab)*6.8+8}" height="16" rx="4" fill="#ffffff" opacity=".92"/><text x="{X}" y="{Y}" text-anchor="middle" font-size="11.5" fill="#1e293b" font-style="italic">{E(lab)}</text>'
    return s
def note(x,y,t,c='#475569',fs=12,anchor='start',bold=False):
    return f'<text x="{x}" y="{y}" font-size="{fs}" fill="{c}" text-anchor="{anchor}"{FW if bold else ""}>{E(t)}</text>'
def save(n,s): open(OUT+n,'w').write(s+'</svg>')
# 1 stack map
W,H=1280,880
s=head(W,H,'The modern AI agent tech stack: six layers, one production layer, one loop','Layers after a third-party infographic by Denis Panjuta, redrawn; ✓ = covered in depth on this site · ~ = only mentioned · ✗ = not yet')
L=[('06 Interface & UI','#2563eb',[('Vercel AI SDK','◐'),('CopilotKit','○'),('assistant-ui','○'),('Streamlit','○'),('Gradio','○'),('AG-UI protocol','○')]),
('05 Runtime & hosting','#7c3aed',[('AgentCore','✓'),('Foundry','✓'),('Gemini Ent. ⚠️','✓'),('LangSmith Dep.','✓'),('Temporal','✓'),('Modal · Docker · K8s','◐')]),
('04 Memory & knowledge','#0d9488',[('Mem0 · Zep · Letta','✓'),('pgvector · Qdrant','✓'),('Pinecone · Weaviate','◐'),('Redis','✓'),('Neo4j (graph)','◐')]),
('03 Tools & protocols','#0891b2',[('MCP','✓'),('A2A','✓'),('Function calling','✓'),('E2B · Browserbase','✓'),('Composio','○'),('Tavily · Firecrawl','○')]),
('02 Agent frameworks','#15803d',[('LangGraph','✓'),('OpenAI Agents SDK','✓'),('Google ADK','✓'),('Claude SDK · MS AF','✓'),('CrewAI · Strands','✓'),('LlamaIndex · Mastra','◐')]),
('01 Foundation models','#d97706',[('Claude · GPT · Gemini','✓'),('Llama · Mistral · Qwen','✓'),('DeepSeek','✓'),('Grok','◐')])]
for i,(n,c,ts) in enumerate(L):
    y=80+i*92
    s+=f'<rect x="20" y="{y}" width="250" height="80" rx="10" fill="{c}"/><text x="34" y="{y+46}" font-size="16" font-weight="800" fill="#fff">{E(n)}</text>'
    for j,(t,m) in enumerate(ts):
        x=285+j*162
        col={'✓':'#16a34a','◐':'#d97706','○':'#dc2626'}[m]
        s+=f'<rect x="{x}" y="{y+10}" width="154" height="60" rx="8" fill="{c}10" stroke="{c}"/>'+note(x+77,y+38,t,'#0f172a',12,'middle',True)+note(x+77,y+58,{'✓':'✓ covered','◐':'~ mentioned','○':'✗ not yet'}[m],col,12,'middle',True)
y=640
s+=f'<rect x="20" y="{y}" width="1240" height="220" rx="12" fill="#f8fafc" stroke="#475569" stroke-dasharray="6 4"/>'+note(36,y+26,'PRODUCTION LAYER — runs under every agent','#334155',14,bold=True)
P=[('Observability',['LangSmith · Langfuse ✓','Arize Phoenix  ~','OpenTelemetry ✓']),('Evaluation',['promptfoo · Ragas ✓','DeepEval  ~','Braintrust  ~']),('Guardrails',['Llama Guard · NeMo ✓','Guardrails AI  ~','cloud filters ✓']),('Agent identity',['Entra Agent ID ⚠️ ✓','Auth0 for AI Agents  ~','Okta  ~']),('LLM gateway',['LiteLLM ✓','OpenRouter  ~','Portkey  ~'])]
for j,(t,ls) in enumerate(P):
    x=36+j*246
    s+=box(x,y+40,232,160,t,ls,'#475569',fs=15)
save('1-stack-map.svg',s)
# 2 loop
W,H=1280,420
s=head(W,H,'The agent loop the stack serves','User → interface → framework → model → tools → memory, repeated until done; the runtime keeps long tasks durable')
st=[('User','asks or triggers','#64748b'),('Interface (06)','chat, app, workspace','#2563eb'),('Framework (02)','plans next step','#15803d'),('Model (01)','reasons, picks a tool','#d97706'),('Tools via MCP (03)','acts in real systems','#0891b2'),('Memory (04)','stores, recalls','#0d9488'),('Result','answer or finished task','#64748b')]
for i,(t,d,c) in enumerate(st):
    x=24+i*178
    s+=box(x,120,160,96,t,d,c,fs=13)
    if i: s+=arr(x-18,168,x-2,168)
s+=f'<path d="M 1000 216 C 1000 330 470 330 470 218" fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#a)"/>'+note(735,330,'loop until done — runtime (05) checkpoints each turn','#7c3aed',13,'middle',True)
save('2-agent-loop.svg',s)
OUT='/home/user/Claude_Project_3_LLM/assets/diagrams/agent-ui/'
# UI 1 three protocols
W,H=1280,440
s=head(W,H,'Three protocols around one agent','MCP connects the agent to tools, A2A to other agents, AG-UI to the person on the screen')
s+=box(520,170,240,100,'Agent','framework + model','#15803d',fs=16)
s+=box(60,170,260,100,'User interface','chat · app · workspace','#2563eb',fs=15)+arr(320,220,518,220,'AG-UI (events)',both=True,lx=420,ly=208)
s+=box(960,90,260,90,'Tools & data','MCP servers','#0891b2',fs=15)+arr(760,195,958,140,'MCP',both=True)
s+=box(960,280,260,90,'Other agents','other teams / vendors','#7c3aed',fs=15)+arr(760,245,958,320,'A2A',both=True)
s+=note(640,410,'AG-UI is the newest of the three (2025) ⚠️; many apps still use a framework-specific stream instead.','#475569',13,'middle')
save('1-three-protocols.svg',s)
# UI 2 event stream
W,H=1280,560
s=head(W,H,'What the screen receives: one refund ticket as UI events','Agent → interface events in order (names generic, after AG-UI-style event types); red = waits for the human')
lanes=['Agent','Interface','Human']
X=[200,640,1080]
for i,l in enumerate(lanes):
    s+=f'<rect x="{X[i]-80}" y="74" width="160" height="30" rx="7" fill="#f1f5f9" stroke="#94a3b8"/><text x="{X[i]}" y="94" text-anchor="middle" font-size="13" font-weight="700">{l}</text><line x1="{X[i]}" y1="104" x2="{X[i]}" y2="540" stroke="#cbd5e1" stroke-dasharray="3 4"/>'
ev=[(2,1,'1 message: "refund my order"'),(0,1,'2 run started'),(0,1,'3 text delta… "Looking up your order"'),(0,1,'4 tool call: crm.read (shown as a card)'),(0,1,'5 tool result: order #1042, $240'),(0,1,'6 state: refund proposed, needs approval'),(1,2,'7 approve / reject buttons'),(2,1,'8 approve'),(1,0,'9 resume with approval'),(0,1,'10 tool call: refund.issue → done'),(0,1,'11 text: "Refunded $240" · run finished')]
y=130
for a,b,l in ev:
    red=a==1 and b==2 or a==2 and 'approve' in l
    s+=arr(X[a],y,X[b]+(-8 if b>a else 8),y,l,c='#dc2626' if red else '#334155',m='r' if red else 'a',lx=(X[a]+X[b])/2,ly=y-5)
    y+=37
save('2-event-stream.svg',s)
# UI 3 choosing
W,H=1280,430
s=head(W,H,'Picking a UI toolkit','By who builds the screen and how much of it is the product')
o=[('Streamlit / Gradio','Python, minutes',['internal tools, demos','data and ML teams','limited custom UX'],'#d97706'),('Vercel AI SDK + assistant-ui','TypeScript / React',['your own chat product','streaming, tool cards','you own the design'],'#2563eb'),('CopilotKit (+ AG-UI)','React, agent-native',['agent inside an existing app','shared state, approvals','framework adapters'],'#7c3aed')]
for i,(t,sb,p,c) in enumerate(o):
    x=40+i*410
    s+=box(x,90,380,300,t,[' '],c,fs=16)+note(x+190,140,sb,'#334155',13,'middle')
    for k,q in enumerate(p): s+=note(x+24,185+k*28,'• '+q,'#1e293b',13)
save('3-choose-ui.svg',s)
OUT='/home/user/Claude_Project_3_LLM/assets/diagrams/agent-prod/'
# P1 production layer around request
W,H=1280,520
s=head(W,H,'The production layer: five services every agent call passes through','One model call from the action agent, with each production service it touches')
s+=box(40,200,200,90,'Agent','wants to call a model','#15803d',fs=15)
st=[('Identity','who is this agent, for whom?','#be185d'),('Guardrail (in)','is the input safe?','#dc2626'),('LLM gateway','route, budget, fallback','#0369a1'),('Model','answer','#d97706'),('Guardrail (out)','is the output safe?','#dc2626')]
for i,(t,d,c) in enumerate(st):
    x=280+i*196
    s+=box(x,200,176,90,t,d,c,fs=14)
    s+=arr(x-38 if i==0 else x-20,245,x-2,245)
s+=f'<rect x="40" y="360" width="1200" height="60" rx="10" fill="#d9770614" stroke="#d97706"/>'+note(640,396,'Observability: every box above emits a span (OpenTelemetry) → traces, cost, latency','#0f172a',14,'middle',True)
s+=f'<rect x="40" y="436" width="1200" height="60" rx="10" fill="#7c3aed14" stroke="#7c3aed"/>'+note(640,472,'Evaluation: offline before release, online on sampled traces → scores and alerts','#0f172a',14,'middle',True)
for i in range(5): s+=arr(368+i*196,292,368+i*196,358,dash=True)
save('1-production-layer.svg',s)
# P2 gateway
W,H=1280,470
s=head(W,H,'What an LLM gateway does','One endpoint for every model: keys, budgets, routing, fallbacks and logs in one place')
s+=box(40,90,220,70,'Research agent',None,'#15803d',fs=14)+box(40,190,220,70,'Action agent',None,'#15803d',fs=14)+box(40,290,220,70,'Eval runner',None,'#7c3aed',fs=14)
s+=box(470,120,300,220,'LLM gateway',['per-agent virtual keys','budgets + rate limits','routing by role','fallback on errors','caching','spend + request logs'],'#0369a1',fs=17)
for y in (125,225,325): s+=arr(260,y,468,y if y!=325 else 300)
for i,(t,d) in enumerate([('Cloud model A','primary'),('Cloud model B','fallback'),('Self-hosted vLLM','cheap steps')]):
    s+=box(990,90+i*100,250,70,t,d,'#d97706',fs=14)+arr(770,230,988,125+i*100)
s+=note(40,440,'Self-hosted: LiteLLM, Portkey (open-source gateway). Hosted: OpenRouter, Portkey cloud, cloud vendors\' own gateways.','#334155',13)
save('2-llm-gateway.svg',s)
