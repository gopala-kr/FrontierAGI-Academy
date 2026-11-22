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
print('adlc ok')
