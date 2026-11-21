# Generates assets/diagrams/azure-agent/*.svg for blog/agentic-blueprint-azure.html (python3 scripts/diagrams_azure_agent.py)
import html, os
OUT='/home/user/Claude_Project_3_LLM/assets/diagrams/azure-agent/'
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
A='#ff9900'
# 1 reference architecture
W,H=1280,860
s=head(W,H,'Production agent on Azure: the reference architecture, layer by layer','Each block of the blueprint mapped to the eight-layer agent stack used across this series (L1–L8) plus delivery (CI/CD)')
s+=band(20,80,230,250,'L1 · INTERFACES',LC['L1'])+box(36,110,198,90,'Users & apps',['web · mobile · chat/voice','enterprise systems, API clients'],LC['L1'],fs=13)+box(36,220,198,95,'API Mgmt + Entra ID',['authn · authz · rate limits','agent identities'],LC['L1'],fs=13)
s+=band(270,80,520,420,'L2–L3 · ORCHESTRATION (Agent Framework + Foundry Agent Service)',LC['L2'])
s+=box(430,112,200,70,'Supervisor / planner','plans & delegates',LC['L3'])
s+=box(290,250,150,74,'Research agent','search · RAG · APIs',LC['L3'])+box(455,250,150,74,'Analysis agent','reason over data',LC['L3'])+box(620,250,150,74,'Action agent','executes tools',LC['L3'])
s+=arr(500,182,370,248,'delegates')+arr(530,182,530,248)+arr(560,182,690,248,'delegates')
s+=box(300,385,470,90,'Multi-agent communication',['workflows (in process) · A2A (across services)','Service Bus + Event Grid (async messaging)'],LC['L2'])
s+=arr(365,324,365,388,both=True)+arr(530,324,530,388,both=True)+arr(695,324,695,388,both=True)
s+=arr(234,267,288,280,'request')
s+=band(810,80,450,170,'L8 · MODEL INFERENCE',LC['L8'])+box(826,108,130,120,'Foundry Models','OpenAI + more',LC['L8'])+box(966,108,130,120,'Azure ML','custom endpoints',LC['L8'])+box(1106,108,140,120,'AKS + vLLM','self-hosted open',LC['L8'])
s+=arr(790,150,824,150,both=True)
s+=band(810,265,450,235,'L4 · MEMORY & STATE',LC['L4'])+box(826,293,205,60,'Foundry Conversations','threads, history',LC['L4'])+box(1041,293,205,60,'Cosmos DB','app state, global',LC['L4'])+box(826,368,205,60,'Azure Managed Redis','fast, short-lived state',LC['L4'])+box(1041,368,205,60,'Foundry Memory ⚠️','long-term (preview)',LC['L4'])
s+=note(1035,470,'read before a turn, written after',LC['L4'],anchor='middle')+arr(790,330,824,330,both=True)
s+=band(20,345,230,330,'L5 · TOOLS',LC['L5'])+box(36,375,198,62,'Foundry Toolboxes','MCP servers ⚠️',LC['L5'])+box(36,447,198,62,'Azure Functions','custom tools',LC['L5'])+box(36,519,198,62,'API Management','enterprise APIs',LC['L5'])+box(36,591,198,62,'Logic Apps','workflow connectors',LC['L5'],fs=13)
s+=arr(250,470,298,440,'tool calls',both=True,lx=268,ly=418)
s+=band(810,515,450,210,'L6 · GUARDRAILS & SECURITY',LC['L6'])+box(826,543,200,72,'Foundry Guardrails ⚠️','prompt + response safety',LC['L6'],fs=13)+box(1036,543,210,72,'Entra ID / Agent ID','who acts, for whom',LC['L6'],fs=13)+box(826,627,135,72,'Content Safety','Prompt Shields',LC['L6'],fs=12)+box(971,627,130,72,'Azure RBAC','least privilege',LC['L6'],fs=13)+box(1111,627,135,72,'Key Vault','keys, secrets, certs',LC['L6'],fs=12)
s+=arr(770,470,824,560,'every call checked',c=LC['L6'],lx=760,ly=520)
s+=band(270,515,520,160,'L8 · OBSERVABILITY & EVALUATION',LC['L8'])+box(286,545,115,110,'Foundry Evals','quality, safety',LC['L8'],fs=12)+box(411,545,115,110,'Azure Monitor','logs · metrics',LC['L8'])+box(536,545,115,110,'App Insights','traces',LC['L8'])+box(661,545,115,110,'OpenTelemetry','agent + tool spans',LC['L8'])
s+=arr(530,470,530,543,'telemetry',dash=True,lx=560,ly=510)
s+=band(20,690,770,150,'CD · DELIVERY (CI/CD for agents)',LC['CD'])
for i,(t,sb) in enumerate([('GitHub','source'),('GitHub Actions','or Azure DevOps'),('Eval gate','tests + evals'),('ACR','container images'),('Deploy','Foundry / ACA / AKS')]):
    s+=box(36+i*150,720,130,100,t,sb,LC['CD'],fs=13)
    if i: s+=arr(36+i*150-20,770,36+i*150,770)
s+=band(810,740,450,100,'L7 · KNOWLEDGE & INFRASTRUCTURE',LC['L7'])+note(826,785,'AI Search · Foundry IQ · Blob Storage',LC['L7'],13,bold=True)+note(826,808,'Container Apps · AKS · VMs · Virtual Network',LC['L7'],13,bold=True)
save('1-reference-architecture.svg',s)

# 2 request path
W,H=1280,620
lanes=['User','APIM + Entra','Guardrails','Supervisor','Research','Analysis','Action','Toolbox + APIM','Tools / data','Memory','Trace']
s=head(W,H,'One request, hop by hop','A refund ticket moving through the Azure blueprint (lanes = components; numbered arrows = calls in order; red = checked by a guardrail)')
X=[70+i*113 for i in range(len(lanes))]
for i,l in enumerate(lanes):
    s+=f'<rect x="{X[i]-54}" y="74" width="108" height="30" rx="7" fill="#f1f5f9" stroke="#94a3b8"/><text x="{X[i]}" y="94" text-anchor="middle" font-size="{11 if len(l)>14 else 12}" font-weight="700" fill="#0f172a">{E(l)}</text><line x1="{X[i]}" y1="104" x2="{X[i]}" y2="600" stroke="#cbd5e1" stroke-dasharray="3 4"/>'
steps=[(0,1,'1 ticket + Entra token'),(1,2,'2 screen input'),(2,3,'3 clean prompt'),(3,9,'4 load memory'),(3,4,'5 "find customer + policy"'),(4,7,'6 crm.read (research identity)'),(7,8,'7 allowed → Function'),(3,5,'8 decide refund?'),(5,6,'9 refund $64'),(6,7,'10 refund.issue (action identity)'),(7,8,'11 under $100 → execute'),(3,2,'12 screen answer'),(2,1,'13 reply'),(3,9,'14 write events + facts'),(1,10,'15 spans for every hop')]
y=130
for a,b,l in steps:
    red='screen' in l or 'allowed' in l or 'under' in l
    c='#dc2626' if red else '#334155'
    s+=arr(X[a],y,X[b]+(-8 if b>a else 8),y,l,c=c,dash=(b==10),m='r' if red else 'a',lx=(X[a]+X[b])/2,ly=y-5)
    y+=31
save('2-request-path.svg',s)

# 3 channels
W,H=1280,520
s=head(W,H,'Three ways agents talk to each other on Azure','Same supervisor and specialists; the channel sets latency, coupling and failure handling')
cols=[('Agent Framework workflow','in one process',['supervisor routes to sub-agents in a graph','shared thread state','no network hop','one deploy, one failure domain']),('A2A protocol','agent ↔ agent over HTTP',['each agent its own Foundry agent','discovered by agent card','teams deploy independently','network hop + auth on every call']),('Service Bus + Event Grid','messages, asynchronous',['supervisor sends a message, moves on','Service Bus queues buffer the work','retries + dead-letter queues','no immediate answer; needs correlation'])]
for i,(t,sb,p) in enumerate(cols):
    x=30+i*415
    s+=band(x,80,395,420,t.upper(),[LC['L3'],LC['L2'],LC['L5']][i])+note(x+14,122,sb,'#334155',13)
    s+=box(x+125,140,145,52,'Supervisor',None,LC['L3'])
    if i==0:
        s+=f'<rect x="{x+20}" y="215" width="355" height="110" rx="10" fill="none" stroke="#94a3b8" stroke-dasharray="5 4"/>'+note(x+30,232,'one workflow run','#64748b',11)
        for j,n in enumerate(['Research','Analysis','Action']): s+=box(x+32+j*115,250,100,52,n,None,LC['L3'],fs=13)+arr(x+197,192,x+82+j*115,248)
        s+=note(x+300,165,'tool call',anchor='middle')
    if i==1:
        for j,n in enumerate(['Research svc','Analysis svc','Action svc']): s+=box(x+20+j*125,262,110,56,n,None,LC['L2'],fs=12)+arr(x+197,192,x+75+j*125,260,both=True)
        s+=note(x+197,350,'HTTPS + agent card + auth',anchor='middle')
    if i==2:
        s+=box(x+90,228,215,40,'Service Bus queue',None,LC['L5'],fs=13)+arr(x+197,192,x+197,226,'emit',lx=x+225,ly=212)
        for j,n in enumerate(['Worker A','Worker B','Worker C']): s+=box(x+32+j*115,300,100,44,n,None,LC['L5'],fs=12)+arr(x+197,268,x+82+j*115,298,dash=True)
        s+=note(x+197,362,'results → event "done" (or callback)',anchor='middle')
    for k,q in enumerate(p): s+=note(x+20,400+k*22,'• '+q,'#1e293b',13)
save('3-multi-agent-channels.svg',s)

# 4 memory
W,H=1280,520
s=head(W,H,'Where an Azure agent keeps what it knows','Four stores, chosen by how long a fact must live and how fast it must be read (indicative, not measured)')
tiers=[('Azure Managed Redis','seconds–minutes','scratch state, locks, rate counters','sub-ms reads',LC['L7']),('Foundry Conversations','one conversation','thread: turns, tool results','read every turn',LC['L4']),('Foundry Memory ⚠️','weeks–months','extracted facts, preferences, summaries','retrieved by relevance',LC['L4']),('Cosmos DB / SQL','years (system of record)','orders, customers, refunds','queried via tools',LC['L5'])]
for i,(t,life,what,read,c) in enumerate(tiers):
    x=40+i*305
    s+=box(x,110,280,250,t,[' '],c,fs=14)+note(x+140,170,'lives: '+life,'#0f172a',13,'middle',True)+note(x+140,195,what,'#334155',12,'middle')+note(x+140,222,read,'#334155',12,'middle')
s+=arr(60,400,1220,400,'longer life → slower, more durable, more governed',c='#475569',lx=640,ly=392)
s+=note(40,450,'Rule of thumb: the model sees recent events + the top few long-term records each turn; business truth is never "remembered" — it is re-read from Cosmos DB / SQL through a tool.','#1e293b',13)
s+=note(40,474,'Writes: the thread is appended every turn; long-term memory extracts facts after a conversation; the action agent writes the database only through the gateway.','#1e293b',13)
save('4-memory-tiers.svg',s)

# 5 tools
W,H=1280,560
s=head(W,H,'How the agent reaches the outside world on Azure','Every tool call leaves through Foundry tools (MCP) and API Management, then fans out to Functions, Logic Apps and enterprise APIs')
s+=box(40,200,200,90,'Agent (Agent Fwk)','tool decision',LC['L3'])
s+=box(300,200,190,90,'MCP client','lists tools · calls',LC['L5'])+arr(240,245,298,245,'call(name,args)',lx=270,ly=232)
s+=box(550,190,200,110,'Toolbox + APIM','identity · policy · limits',LC['L6'])+arr(490,245,548,245,'request',lx=519,ly=232)
s+=arr(750,215,880,120)+arr(750,235,880,230)+arr(750,255,880,340)+arr(750,275,880,450)
s+=box(882,80,360,80,'Azure Functions','your business logic as tools',LC['L5'])
s+=box(882,190,360,80,'API Management','existing internal + external APIs',LC['L5'])
s+=box(882,300,360,80,'Logic Apps','prebuilt workflow connectors',LC['L5'])
s+=box(882,410,360,80,'Other MCP servers','Microsoft + third-party tools',LC['L5'])
s+=box(550,360,200,80,'Denied','logged, agent told why',LC['L6'],dash=True)+arr(650,300,650,358,'policy says no',c=LC['L6'],m='r',lx=700,ly=332)
s+=note(40,520,'Why one door: identity, rate limits, policy and audit live in the gateway. Tools added later inherit the same checks without touching agent code.','#1e293b',13)
save('5-tools-mcp.svg',s)

# 6 guardrails
W,H=1280,500
s=head(W,H,'Guardrails in depth on Azure: five checks on one request','No single layer is trusted; each catches a different failure (red = can stop the request)')
chk=[('1 Prompt Shields (in)','prompt attacks,\nharmful content'),('2 Entra ID + Agent ID','which user, which\nagent, on whose behalf'),('3 Toolbox / APIM policy','is this tool call\nallowed, within limits?'),('4 RBAC / Key Vault','least privilege;\nno keys in prompts'),('5 Content Safety (out)','harmful or\nungrounded answers')]
for i,(t,d) in enumerate(chk):
    x=40+i*245
    s+=box(x,120,210,120,t,d.split('\n'),LC['L6'],fs=14)
    if i: s+=arr(x-35,180,x-2,180)
    s+=arr(x+105,240,x+105,300,'stop',c=LC['L6'],m='r',lx=x+130,ly=275)+box(x+30,302,150,44,'blocked + logged',None,LC['L6'],dash=True,fs=12)
s+=box(40,380,1200,70,'Azure Monitor and Entra sign-in logs sit beside all five: every allowed or blocked call leaves an audit record a reviewer can replay.',None,'#64748b',fs=13)
save('6-guardrails.svg',s)

# 7 cicd
W,H=1280,470
s=head(W,H,'Shipping an agent on Azure: CI/CD with an evaluation gate','Code, prompts and tool configs ship together; infrastructure is code too (Bicep / Terraform)')
st=[('Commit','code + prompts | + tool config','#475569'),('GitHub Actions','or Azure DevOps','#be185d'),('Eval gate','tests + | Foundry evals','#dc2626'),('ACR','container image','#be185d'),('Deploy','Foundry Agent Svc | ACA / AKS','#be185d'),('Production','traces + online evals','#d97706')]
for i,(t,d,c) in enumerate(st):
    x=30+i*208
    s+=box(x,120,185,110,t,d.split(' | '),c,fs=14)
    if i: s+=arr(x-21,175,x-2,175)
s+=arr(429,232,429,300,'eval fail → stop',c='#dc2626',m='r',lx=480,ly=272)+box(350,302,160,50,'back to commit',None,'#dc2626',dash=True,fs=12)
s+=f'<path d="M1158 232 C1158 430 900 430 900 232" fill="none" stroke="#d97706" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#a)"/>'+note(1030,420,'online regressions → roll back to the previous version','#b45309',12,'middle')
save('7-cicd.svg',s)

# 8 trace
W,H=1280,450
s=head(W,H,'What the trace shows: one ticket as spans','Illustrative timings for one refund ticket; on Azure these spans land in Application Insights via OpenTelemetry')
sp=[('apim: auth + throttle',0,8,0),('prompt shields: pass',8,40,1),('supervisor: decompose (model call)',48,420,0),('research: crm.read + kb.retrieve',468,110,1),('analysis: decide (model call)',578,380,1),('action: refunded',958,60,1),('gateway: denied research write',1018,2,1),('content safety out: pass',1020,40,0),('thread + memory write',1060,15,0)]
sc=900/1075
for i,(n,st0,ms,ind) in enumerate(sp):
    y=90+i*34
    s+=note(30+ind*16,y+16,n,'#0f172a',12)
    c='#d97706' if 'model' in n else ('#dc2626' if 'denied' in n else '#2563eb')
    s+=f'<rect x="{340+st0*sc}" y="{y+3}" width="{max(3,ms*sc)}" height="18" rx="3" fill="{c}"/>'+note(min(1180,340+st0*sc+max(3,ms*sc)+6),y+16,f'{ms} ms','#475569',11)
s+=note(340,402,'0 ms','#64748b',11)+note(1240,402,'1,075 ms','#64748b',11,'end')+note(30,435,'orange = model calls (most of the time)   red = blocked call','#475569',12)
save('8-trace.svg',s)

# 9 hosting
W,H=1280,470
s=head(W,H,'Where the agent itself runs on Azure: three hosting choices','Same Agent Framework code; the difference is who operates the servers and how much you can tune')
opt=[('Foundry Agent Service','Microsoft runs it',['hosted agents, threads built in','identity, tools + evals wired in','least ops, least control'],LC['L2']),('Container Apps','serverless containers',['you ship an image','scale to zero, per-use billing','you wire sessions & memory'],LC['L1']),('AKS','Kubernetes',['you run the cluster','GPUs for vLLM self-hosting','most control, most ops'],LC['L7'])]
for i,(t,sb,p,c) in enumerate(opt):
    x=40+i*410
    s+=box(x,90,380,300,t,[' '],c,fs=16)+note(x+190,140,sb,'#334155',13,'middle')
    for k,q in enumerate(p): s+=note(x+24,185+k*28,'• '+q,'#1e293b',13)
    s+=f'<rect x="{x+24}" y="300" width="{332*(0.3+0.35*i)}" height="14" rx="7" fill="{c}"/>'+note(x+24,340,'ops you own','#475569',12)
save('9-hosting.svg',s)

# 10 RAG
W,H=1280,470
s=head(W,H,'Knowledge (RAG): grounding answers in your documents','Optional in the blueprint, used here for the refund policy: index once, retrieve on every relevant turn')
s+=band(20,80,600,330,'INDEXING (offline, when documents change)',LC['L7'])
for i,(t,sb) in enumerate([('Blob Storage','policy PDFs, FAQs'),('Chunk + embed','indexer / Foundry IQ'),('Azure AI Search','vector + hybrid')]):
    s+=box(40+i*195,150,175,90,t,sb,LC['L7'],fs=13)
    if i: s+=arr(40+i*195-20,195,40+i*195,195)
s+=note(40,300,'• re-sync when a document changes','#1e293b',13)+note(40,324,'• metadata (region, version) kept with each chunk','#1e293b',13)
s+=band(660,80,600,330,'RETRIEVAL (online, per question)',LC['L4'])
for i,(t,sb) in enumerate([('Research agent','"refund policy?"'),('Retrieve','top-k chunks'),('Answer','cites the chunk')]):
    s+=box(680+i*195,150,175,90,t,sb,LC['L4'],fs=13)
    if i: s+=arr(680+i*195-20,195,680+i*195,195)
s+=arr(620,195,698,195,'query',dash=True,lx=650,ly=180)
s+=note(680,300,'• groundedness detection (Content Safety) flags','#1e293b',13)+note(680,324,'  answers the chunks do not support','#1e293b',13)
s+=note(20,450,'Policies live in RAG; facts about this customer live in the database. Mixing them is how agents quote the wrong refund limit.','#1e293b',13)
save('10-rag.svg',s)
print(sorted(os.listdir(OUT)))
