# Generates assets/diagrams/software-factory/1-factory.svg
import html, os
OUT='/home/user/Claude_Project_3_LLM/assets/diagrams/software-factory/'
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
W,H=1280,560
s=head(W,H,'The software factory: events in, measured value out','Our reference shape. Each workflow is a graph of loops inside harnesses; the factory routes, budgets and measures them')
ev=[('Issue opened','#2563eb'),('Build failed','#dc2626'),('Alert fired','#ea580c'),('Dependency update','#0891b2'),('Schedule','#64748b')]
for i,(t,c) in enumerate(ev): s+=box(30,90+i*80,170,56,t,None,c,fs=13)+arr(200,118+i*80,288,290)
s+=box(290,230,170,120,'Router',['which workflow?','budget · owner'],'#1e40af',fs=15)
wf=[('Bug fix','graph: reproduce → fix → test → review'),('Perf fix','graph: profile ∥ benchmark → fix → review'),('CI repair','graph: diagnose → patch → re-run'),('Dependency bump','graph: update → test → canary')]
for i,(t,d) in enumerate(wf): s+=box(530,80+i*105,330,80,t,[d],'#2563eb',fs=14)+arr(460,290,528,120+i*105)
s+=box(940,150,300,110,'Value out',['merged · deployed','incident closed'],'#16a34a',fs=15)
for i in range(4): s+=arr(860,120+i*105,938,205)
s+=box(940,320,300,150,'Measurement',['cost per merged change','defect / revert rate','lead time · human minutes','which workflows pay off'],'#7c3aed',fs=15)
s+=arr(1090,260,1090,318)
s+=f'<path d="M 940 440 C 700 540 420 520 375 352" fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#a)"/>'+note(640,525,'improve routing, budgets, prompts and evals from what is measured','#6d28d9',13,'middle',True)
save('1-factory.svg',s)
print('ok')
