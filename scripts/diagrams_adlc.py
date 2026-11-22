# Generates assets/diagrams/adlc/*.svg from data/tech-jobs-history.json (python3 scripts/diagrams_tech_jobs.py)
import html, os
OUT='/home/user/Claude_Project_3_LLM/assets/diagrams/adlc/'
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
ANIM='<style>.gr{animation:gr 1.4s cubic-bezier(.2,.8,.2,1) both;transform-box:fill-box;transform-origin:left center}.gu{animation:gu 1.4s cubic-bezier(.2,.8,.2,1) both;transform-box:fill-box;transform-origin:center bottom}.fd{animation:fd 1s ease-out both}.dr{stroke-dasharray:1600;animation:dr 2.4s ease-out both}@keyframes gr{from{transform:scaleX(0)}}@keyframes gu{from{transform:scaleY(0)}}@keyframes fd{from{opacity:0}}@keyframes dr{from{stroke-dashoffset:1600}}@media (prefers-reduced-motion:reduce){*{animation:none!important}}</style>'
def hbars(n,title,sub,rows,mx,unit='%',W=1000,src=''):
    H=110+len(rows)*54+40; s=head(W,H,title,sub)+ANIM
    for i,(lab,v,c,extra) in enumerate(rows):
        y=90+i*54; w=(W-420)*v/mx
        s+=note(24,y+24,lab,'#0f172a',14,bold=True)
        s+=f'<rect class="gr" style="animation-delay:{i*.15}s" x="330" y="{y+6}" width="{w:.1f}" height="28" rx="6" fill="{c}"/>'
        s+=note(338+w,y+26,(f'{v:g}{unit}' if unit else '')+(' '+extra if extra else ''),'#0f172a',13,bold=True)
    s+=note(24,H-16,src,'#64748b',11.5); save(n,s)
# 1 timeline
W,H=1200,470; s=head(W,H,'Sixty years of the software lifecycle','How teams have organised building software, 1956 → 2026')+ANIM
s+='<line class="dr" x1="40" y1="250" x2="1160" y2="250" stroke="#334155" stroke-width="3"/>'
EV=[(1956,'Stagewise model','SAGE air defence (Benington)','#64748b',1),(1970,'Royce paper','later called "waterfall"','#2563eb',-1),(1986,'Spiral model','Boehm: risk-driven loops','#7c3aed',1),(2001,'Agile Manifesto','17 people, Snowbird','#16a34a',-1),(2009,'DevOps','DevOpsDays, Ghent','#0d9488',1),(2014,'DORA','State of DevOps','#0891b2',-1),(2018,'Accelerate','four key metrics','#ea580c',1),(2022,'AI coding','assistants spread','#db2777',-1),(2025,'90% use AI','DORA 2025 survey','#dc2626',1),(2026,'ADLC','agents build and ship','#b91c1c',-1)]
for i,(y,t,sub,c,up) in enumerate(EV):
    x=100+i*111; yy=250-up*20; ty=150 if up>0 else 330
    s+=f'<g class="fd" style="animation-delay:{.15*i}s"><circle cx="{x:.0f}" cy="250" r="9" fill="{c}"/><line x1="{x:.0f}" y1="{250-up*9}" x2="{x:.0f}" y2="{ty+ (20 if up>0 else -36)}" stroke="{c}" stroke-dasharray="3 3"/>'
    s+=note(x,ty-14 if up>0 else ty,str(y),c,13,'middle',True)+note(x,ty+4 if up>0 else ty+18,t,'#0f172a',13.5,'middle',True)+note(x,ty+20 if up>0 else ty+34,sub,'#475569',11.5,'middle')+'</g>'
s+=note(24,450,'Sources in Part 1. "Waterfall" was a later label; Royce himself warned the simple sequence was risky.','#64748b',11.5)
save('1-timeline.svg',s)
# 2 lanes
W,H=1200,520; s=head(W,H,'From SDLC to ADLC: what each stage becomes','Same job, new artefacts. Parts 3–10 of this series take one stage each')+ANIM
ST=[('Requirements','Task specs|+ eval sets'),('Design','Agent|architecture'),('Code','Context,|tools, prompts'),('Test','Evaluation|(evals)'),('Secure','Guardrails|+ red-team'),('Release','Staged|model rollout'),('Operate','Traces,|cost, drift'),('Maintain','Continuous|improvement')]
s+=note(24,104,'SDLC','#2563eb',15,'start',True)+note(24,330,'ADLC','#c2410c',15,'start',True)
for i,(a,b) in enumerate(ST):
    x=90+i*137
    s+=f'<g class="fd" style="animation-delay:{i*.1}s">'+box(x,80,124,60,a,None,'#2563eb',fs=13.5)+'</g>'
    s+=f'<g class="fd" style="animation-delay:{.8+i*.1}s">'+box(x,300,124,74,b.split('|')[0],[b.split('|')[1]],'#ea580c',fs=13)+'</g>'
    s+=arr(x+62,146,x+62,292,None,'#94a3b8',True)
s+='<path class="dr" d="M 1110 378 C 1100 450, 160 450, 152 382" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#a)"/>'+note(600,475,'Production learning feeds the next spec: the ADLC is a loop, not a line','#c2410c',13,'middle',True)
save('2-lanes.svg',s)
# 3 determinism
W,H=1100,400; s=head(W,H,'Why the old cycle breaks: same input, different outputs','Ordinary code vs a model inside the software (illustrative)')+ANIM
s+=band(24,80,500,280,'ORDINARY CODE','#2563eb')+band(576,80,500,280,'SOFTWARE WITH A MODEL INSIDE','#c2410c')
s+=box(54,130,140,50,'Input',None,'#2563eb')+box(234,130,120,50,'Function',None,'#2563eb')+box(394,130,110,50,'Output',None,'#2563eb')+arr(194,155,232,155)+arr(354,155,392,155)
s+=note(54,230,'Same input → same output, every time.','#0f172a',14)+note(54,256,'A test passes or fails.','#0f172a',14)+note(54,282,'Ship once; it behaves the same.','#0f172a',14)
s+=box(600,150,110,50,'Input',None,'#c2410c')+box(740,150,110,50,'Model',None,'#c2410c')
for j,t in enumerate(['Answer A','Answer B','Answer C']):
    s+=f'<g class="fd" style="animation-delay:{.4+j*.3}s">'+box(900,100+j*60,150,44,t,None,'#c2410c')+'</g>'+arr(850,175,898,122+j*60)
s+=note(600,300,'Same input → a range of outputs. Quality is a rate,','#0f172a',14)+note(600,324,'measured with evals; models, prompts and data all change.','#0f172a',14)
save('3-determinism.svg',s)
# 4 spec: story -> eval set
W,H=1200,420; s=head(W,H,'From a user story to an eval set','Part 3: requirements become example tasks with a pass rule and a target rate')+ANIM
B=[('User story','"As a customer I want a refund"',['for a faulty order"'],'#2563eb'),('Task examples','200 real tickets',['(sampled from history)'],'#7c3aed'),('Grading rule','Correct decision?',['Policy kept? Tone ok?'],'#0d9488'),('Edge + attack cases','limits, missing data,',['prompt injection'],'#dc2626'),('Target','90% correct,',['0 policy breaks'],'#c2410c')]
for i,(t,a,b,c) in enumerate(B):
    x=24+i*236; s+=f'<g class="fd" style="animation-delay:{i*.2}s">'+box(x,110,210,110,t,[a]+b,c,fs=16)+'</g>'
    if i: s+=arr(x-24,165,x-2,165)
s+=note(24,280,'Illustrative numbers. The eval set is written before the agent is built, and grows every time production finds a new failure (Part 10).','#334155',13)
save('4-spec.svg',s)
# 5 autonomy spectrum
W,H=1200,380; s=head(W,H,'Design: how much does the system decide?','Part 4: from fixed workflows to autonomous agents (after Anthropic’s "workflows vs agents" distinction)')+ANIM
s+='<defs><linearGradient id="g5" x1="0" x2="1"><stop offset="0" stop-color="#2563eb"/><stop offset="1" stop-color="#dc2626"/></linearGradient></defs><rect class="gr" x="40" y="120" width="1120" height="18" rx="9" fill="url(#g5)"/>'
for i,(t,a,b) in enumerate([('Single call','one prompt, one answer','cheapest, most predictable'),('Workflow','fixed steps in code','prompt chain, router, parallel'),('Agent with gates','model picks tools','humans approve risky steps'),('Autonomous agent','model plans and acts','long tasks, least predictable')]):
    x=110+i*330; s+=f'<g class="fd" style="animation-delay:{.3+i*.2}s"><circle cx="{x}" cy="129" r="13" fill="#fff" stroke="#0f172a" stroke-width="2"/>'+note(x,180,t,'#0f172a',16,'middle',True)+note(x,204,a,'#334155',13,'middle')+note(x,224,b,'#64748b',12.5,'middle')+'</g>'
s+=note(40,300,'← more control, cost and reliability','#2563eb',13,'start',True)+note(1160,300,'more flexibility and capability →','#dc2626',13,'end',True)+note(600,350,'Rule of thumb: use the simplest option that meets the eval target.','#0f172a',14,'middle',True)
save('5-autonomy.svg',s)
# 6 context window stack
W,H=1100,460; s=head(W,H,'Code becomes context: what fills the window','Part 5: one agent turn, by share of tokens (illustrative)')+ANIM
L=[('System prompt and instructions',8,'#2563eb'),('Tool definitions',10,'#7c3aed'),('Context files and skills (e.g. CLAUDE.md)',12,'#0d9488'),('Retrieved documents',25,'#ca8a04'),('Conversation and tool results so far',35,'#ea580c'),('Room left for the answer',10,'#94a3b8')]
y=80
for i,(t,p,c) in enumerate(L):
    h=p*3.3; s+=f'<rect class="gr" style="animation-delay:{i*.15}s" x="60" y="{y}" width="420" height="{h-3}" rx="5" fill="{c}"/>'+note(500,y+h/2+5,f'{t}  ·  {p}%','#0f172a',13.5,'start',True); y+=h
s+=note(60,y+30,'Shares are an example, not a measurement. Long agent runs fill the window with tool results, which is why context engineering matters.','#475569',12.5)
save('6-context.svg',s)
# 7 eval gate pipeline
W,H=1200,380; s=head(W,H,'Test becomes evaluation: the release gate','Part 6: every change to model, prompt, tools or context runs the same eval set')+ANIM
P=[('Change','model, prompt, tool','#2563eb'),('Run eval set','200 tasks × 3 runs','#7c3aed'),('Grade','code checks, LLM judge,','#0d9488'),('Compare','vs last release','#ca8a04')]
for i,(t,a,c) in enumerate(P):
    x=24+i*230; s+=f'<g class="fd" style="animation-delay:{i*.2}s">'+box(x,120,200,90,t,[a]+(['human spot-checks'] if i==2 else []),c,fs=16)+'</g>'
    if i: s+=arr(x-30,165,x-2,165)
s+='<polygon points="1010,115 1080,165 1010,215 940,165" fill="#fff7ed" stroke="#c2410c" stroke-width="2"/>'+note(1010,162,'Pass','#0f172a',13,'middle',True)+note(1010,178,'threshold?','#0f172a',12,'middle')+arr(944,165,936,165)+arr(1080,165,1150,165)+note(1150,150,'Release','#16a34a',14,'end',True)
s+=arr(1010,215,1010,280,'no',"#dc2626",m='r')+note(1010,300,'Back to change; add the failures to the eval set','#dc2626',13,'middle',True)
s+=note(24,345,'Numbers are an example. Unlike a unit test, the result is a rate with uncertainty: see the calculator in Part 6.','#475569',12.5)
save('7-evalgate.svg',s)
print('adlc ok')
