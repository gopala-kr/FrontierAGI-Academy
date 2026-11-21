# Generates assets/diagrams/compare-agent/*.svg for blog/agentic-blueprint-compared.html (python3 scripts/diagrams_compare_agent.py)
import html, os
OUT='/home/user/Claude_Project_3_LLM/assets/diagrams/compare-agent/'
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
CC={'GCP':'#2563eb','AWS':'#ea580c','Azure':'#0284c7','OSS':'#16a34a'}
# 1 matrix
W,H=1280,900
s=head(W,H,'Four blueprints, one stack: what fills each layer','Same refund-ticket system in every column. ⚠️ = preview or unconfirmed name in that part')
rows=[('L1 Entry + identity',['API Gateway · IAM','API Gateway · Cognito','API Mgmt · Entra ID','Kong · Keycloak']),
('L2–3 Agent SDK',['ADK','Strands Agents','Agent Framework','LangGraph']),
('L2 Agent hosting',['Agent Engine ⚠️','AgentCore Runtime','Foundry Agent Svc','Kubernetes pods']),
('L2 Async work',['Pub/Sub','EventBridge + SQS','Service Bus + Event Grid','Temporal · NATS']),
('L8 Models',['Gemini · Model Garden','Bedrock','Foundry Models','vLLM + LiteLLM']),
('L4 Agent memory',['Sessions · Memory Bank','AgentCore Memory','Threads · Memory ⚠️','Postgres · Mem0']),
('L4 Records',['Firestore · AlloyDB','DynamoDB · Aurora','Cosmos DB','PostgreSQL']),
('L5 Tool door',['Agent Gateway ⚠️ · MCP','AgentCore Gateway','Toolboxes ⚠️ · APIM','MCP gateway + OPA']),
('RAG',['Vertex AI Search','Knowledge Bases','Azure AI Search','Qdrant / pgvector']),
('L6 Content filters',['Model Armor','Bedrock Guardrails','Prompt Shields','Llama Guard · Presidio']),
('L6 Secrets',['Secret Manager','Secrets Mgr · KMS','Key Vault','Vault']),
('L8 Traces + evals',['Cloud Trace · evals','CloudWatch · X-Ray','App Insights · evals','Langfuse · Tempo']),
('Delivery',['Cloud Build · Deploy','CodePipeline · ECR','GitHub Actions · ACR','Argo CD · Harbor'])]
cols=['Google Cloud','AWS','Azure','Open-source']
for j,c in enumerate(cols):
    s+=f'<rect x="{250+j*255}" y="76" width="245" height="34" rx="8" fill="{list(CC.values())[j]}"/><text x="{250+j*255+122}" y="98" text-anchor="middle" font-size="14" font-weight="800" fill="#fff">{c}</text>'
for i,(r,v) in enumerate(rows):
    y=120+i*59
    s+=f'<rect x="20" y="{y}" width="222" height="52" rx="8" fill="#f1f5f9" stroke="#cbd5e1"/>'+note(32,y+31,r,'#0f172a',13,bold=True)
    for j,t in enumerate(v):
        c=list(CC.values())[j]
        s+=f'<rect x="{250+j*255}" y="{y}" width="245" height="52" rx="8" fill="{c}12" stroke="{c}" stroke-width="1.2"/>'+note(250+j*255+122,y+31,t,'#0f172a',13,'middle')
save('1-layer-matrix.svg',s)
# 2 chooser
W,H=1280,560
s=head(W,H,'Which blueprint? A four-question chooser','Our rule of thumb, not a law: start at the top, stop at the first yes')
q=[('Must data stay on hardware you control (air-gap, strict residency)?','Open-source, self-hosted (Part 4)','OSS'),
('Do your users sign in with Entra ID and work in Microsoft 365?','Azure (Part 3)','Azure'),
('Are your data and security tooling already mostly on AWS?','AWS (Part 2)','AWS'),
('Is your data in BigQuery / Workspace, or do you want Gemini first?','Google Cloud (Part 1)','GCP')]
for i,(t,a,k) in enumerate(q):
    y=90+i*100
    s+=box(40,y,700,70,t,None,'#475569',fs=14)+arr(740,y+35,860,y+35,'yes')+box(862,y,380,70,a,None,CC[k],fs=15)
    if i<3: s+=arr(390,y+70,390,y+100,'no',lx=410,ly=y+90)
s+=box(40,490,1200,50,'No clear yes? Pick the cloud you already pay for, and keep the portable pieces (open SDK, MCP, OpenTelemetry) so you can move later.',None,'#64748b',fs=13)
save('2-chooser.svg',s)
# 3 lock-in
W,H=1280,500
s=head(W,H,'What moves with you, and what does not','Lock-in by layer: green pieces move between all four blueprints; red pieces are rewritten if you switch')
items=[('Agent logic (prompts, graphs)','portable SDKs: ADK, Strands, Agent Fwk, LangGraph all open',0),('Tools over MCP','same MCP servers work everywhere',0),('Traces (OpenTelemetry)','same instrumentation, new backend',0),('Evals (golden sets)','data is yours; runner swappable',0),('Records (Postgres-compatible)','AlloyDB / Aurora / Azure PG / Postgres',1),('Agent memory services','Memory Bank, AgentCore Memory, Foundry Memory differ',2),('Content filters','Model Armor / Guardrails / Prompt Shields configs differ',2),('Identity + policy','IAM, Cognito, Entra, OPA rules rewritten',2),('Managed agent runtime','Agent Engine / AgentCore / Foundry APIs differ',2)]
col=['#16a34a','#d97706','#dc2626']
for i,(t,d,l) in enumerate(items):
    y=80+i*44
    s+=f'<rect x="40" y="{y}" width="{300+l*150}" height="34" rx="8" fill="{col[l]}22" stroke="{col[l]}"/>'+note(54,y+22,t,'#0f172a',13,bold=True)+note(660,y+22,d,'#334155',12)
s+=note(40,486,'Bar length = rough effort to move (our judgement). Design tip: keep the green layers clean and the red ones thin.','#475569',12)
save('3-lock-in.svg',s)
# 4 cost crossover
W,H=1280,520
s=head(W,H,'Per-token cloud vs self-hosted: where the lines cross','Our model with the example inputs from Parts 1–4: cloud ≈ $0.0312 per task; self-hosted ≈ $93,633 per month fixed (4 GPUs, 4 engineers)')
X0,Y0,PW,PH=110,450,1100,340
mx=5e6; my=200000
def px(t): return X0+t/mx*PW
def py(c): return Y0-c/my*PH
s+=f'<line x1="{X0}" y1="{Y0}" x2="{X0+PW}" y2="{Y0}" stroke="#94a3b8"/><line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y0-PH}" stroke="#94a3b8"/>'
for t in range(0,6): s+=note(px(t*1e6),Y0+20,f'{t}M','#475569',12,'middle')
for c in range(0,201,50): s+=note(X0-8,py(c*1000)+4,f'${c}k','#475569',12,'end')
s+=note(X0+PW/2,Y0+44,'tasks per month','#334155',12,'middle')
s+=f'<line x1="{px(0)}" y1="{py(0)}" x2="{px(mx)}" y2="{py(mx*0.0312)}" stroke="#2563eb" stroke-width="3"/>'+note(px(4.4e6),py(4.4e6*0.0312)-10,'cloud, per token','#2563eb',13,'middle',True)
s+=f'<line x1="{px(0)}" y1="{py(93633)}" x2="{px(mx)}" y2="{py(93633)}" stroke="#16a34a" stroke-width="3"/>'+note(px(0.9e6),py(93633)-10,'self-hosted, fixed','#16a34a',13,'middle',True)
xc=93633/0.0312
s+=f'<circle cx="{px(xc)}" cy="{py(93633)}" r="7" fill="#dc2626"/>'+note(px(xc),py(93633)+28,f'cross ≈ {xc/1e6:.1f}M tasks / month','#dc2626',13,'middle',True)
s+=note(X0+10,Y0-PH+10,'Ignores GPU capacity limits and volume discounts; illustrative only.','#64748b',12)
save('4-cost-crossover.svg',s)
print(round(xc))
