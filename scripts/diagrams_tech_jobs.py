# Generates assets/diagrams/tech-jobs/*.svg from data/tech-jobs-history.json (python3 scripts/diagrams_tech_jobs.py)
import html, os
OUT='/home/user/Claude_Project_3_LLM/assets/diagrams/tech-jobs/'
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
import json
D=json.load(open('/home/user/Claude_Project_3_LLM/data/tech-jobs-history.json'))
CPI=D['cpi']; M=D['metrics']
def real(y,v):
    ys=str(int(y)); c=CPI.get(ys)
    return v*CPI['2024']/c if c else None
# 1 role lanes 2005-2026
W,H=1280,640
s=head(W,H,'Tech roles that emerged, changed, faded or disappeared, 2005–2026','Bars run from when a title took off to today (or to when it faded). Colour = what is happening to it now. Notes marked "our reading" are judgement, not data')
X0,X1=330,1240; Y0,Y1=2005,2026.9
def px(y): return X0+(max(y,Y0)-Y0)/(Y1-Y0)*(X1-X0)
for y in range(2005,2027,3): s+=f'<line x1="{px(y)}" y1="80" x2="{px(y)}" y2="{H-40}" stroke="#e2e8f0"/>'+note(px(y),H-20,str(y),'#64748b',12,'middle')
col={'rising':'#16a34a','changing':'#2563eb','faded':'#d97706','gone':'#dc2626','shrinking':'#9333ea'}
for i,r in enumerate(D['roles']):
    y=92+i*37; e=r['end'] or 2026.9; b=r['born']
    s+=note(20,y+16,r['name'],'#0f172a',13,bold=True)
    s+=f'<rect x="{px(b)}" y="{y+2}" width="{max(6,px(e)-px(b))}" height="20" rx="6" fill="{col[r["state"]]}" opacity=".85"/>'
    if r['peak'] and r['peak']>=Y0: s+=f'<circle cx="{px(r["peak"])}" cy="{y+12}" r="6" fill="#fff" stroke="#0f172a" stroke-width="2"/>'
    if b<Y0: s+=note(X0-6,y+16,'←','#64748b',13,'end')
lx=X0
for k,c in col.items(): s+=f'<rect x="{lx}" y="58" width="14" height="14" rx="3" fill="{c}"/>'+note(lx+20,70,k,'#334155',12); lx+=120
s+=f'<circle cx="{lx+10}" cy="65" r="6" fill="#fff" stroke="#0f172a" stroke-width="2"/>'+note(lx+22,70,'peak','#334155',12)
save('1-roles-2005-2026.svg',s)
# 2 pay real dollars
W,H=1280,520
s=head(W,H,'Pay for tech work, in 2024 dollars, 2005–2024','Reported figures converted with the US CPI-U annual average. Different surveys measure different things: compare lines with care')
X0,X1,Yb,Yt=110,1220,460,90; vmin,vmax=60000,170000
def py(v): return Yb-(v-vmin)/(vmax-vmin)*(Yb-Yt)
def pxx(y): return X0+(y-2005)/(2024-2005)*(X1-X0)
for v in range(60000,170001,20000): s+=f'<line x1="{X0}" y1="{py(v)}" x2="{X1}" y2="{py(v)}" stroke="#e2e8f0"/>'+note(X0-8,py(v)+4,f'${v//1000}k','#64748b',12,'end')
for y in range(2005,2025,3): s+=note(pxx(y),Yb+22,str(y),'#64748b',12,'middle')
series=[('us_swdev_median_wage','#2563eb','BLS software developer median'),('us_tech_avg_salary_dice','#16a34a','Dice average tech salary'),('data_scientist_glassdoor','#9333ea','Glassdoor data scientist median base')]
ly=110
for k,c,lab in series:
    pts=[(p[0],real(p[0],p[1]),p[1]) for p in M[k]['points'] if real(p[0],p[1])]
    seg=[q for q in pts if q[0]>=2016]
    if len(seg)>1: s+='<polyline fill="none" stroke="'+c+'" stroke-width="3" points="'+' '.join(f'{pxx(a)},{py(b)}' for a,b,_ in seg)+'"/>'
    for a,b,n in pts: s+=f'<circle cx="{pxx(a)}" cy="{py(b)}" r="5" fill="{c}"/>'+note(pxx(a)+6,py(b)+(18 if k=='data_scientist_glassdoor' and a==2019 else -8),f'${b/1000:.0f}k','#0f172a',11)
    s+=f'<rect x="{X0+10}" y="{ly-11}" width="14" height="14" rx="3" fill="{c}"/>'+note(X0+30,ly,lab,'#334155',12); ly+=20
s+=note(X0,500,'Points more than a decade apart are not joined. 2005 Dice $69.7k and 2016 BLS ($48.12/h × 2,080) are converted by us; BLS changed the software developer category between 2019 and 2020.','#64748b',12)
save('2-pay-real.svg',s)
# 3 demand: Indeed + layoffs
W,H=1280,520
s=head(W,H,'Demand fell after the 2022 peak: postings and layoffs','Left: US software development postings on Indeed (1 Feb 2020 = 100). Right: tech layoffs per year tracked by Layoffs.fyi')
X0,X1,Yb,Yt=90,600,450,100
def ix(y): return X0+(y-2020)/(2027-2020)*(X1-X0)
def iy(v): return Yb-(v-40)/(120-40)*(Yb-Yt)
for v in (40,60,80,100,120): s+=f'<line x1="{X0}" y1="{iy(v)}" x2="{X1}" y2="{iy(v)}" stroke="#e2e8f0"/>'+note(X0-8,iy(v)+4,str(v),'#64748b',12,'end')
for y in range(2020,2028): s+=note(ix(y),Yb+22,str(y),'#64748b',12,'middle')
P=M['indeed_swdev_postings']['points']
s+='<polyline fill="none" stroke="#2563eb" stroke-width="3" stroke-dasharray="6 5" points="'+' '.join(f'{ix(p[0])},{iy(p[1])}' for p in P)+'"/>'
for p in P: s+=f'<circle cx="{ix(p[0])}" cy="{iy(p[1])}" r="5" fill="#2563eb"/>'+note(ix(p[0])+6,iy(p[1])-8,str(p[1]),'#0f172a',11)
s+=note(ix(2021.2),iy(112),'2021–22: far above 100 (exact peak not in our sources)','#475569',12)
s+=note(X0,490,'Dashed = only the sourced points are joined; the line is not the full series.','#64748b',12)
L=[p for p in M['layoffs']['points'] if p[0]>=2022]; bx=700
for i,p in enumerate(L):
    h=p[1]/280000*300; x=bx+i*130
    s+=f'<rect x="{x}" y="{450-h}" width="90" height="{h}" rx="6" fill="{"#fca5a5" if len(p)>5 else "#dc2626"}"/>'+note(x+45,445-h,f'{p[1]/1000:.0f}k'+(' est.' if len(p)>5 else ''),'#0f172a',13,'middle',True)+note(x+45,472,str(p[0]),'#64748b',12,'middle')
s+=note(700,500,'Light bars = estimated or incomplete (2022 derived from "2023 was 59% higher"; 2025 partial).','#64748b',12)
save('3-demand.svg',s)
# 4 H-1B and India
W,H=1280,480
s=head(W,H,'The global thread: H-1B registrations and India\'s tech workforce','Left: H-1B cap registrations by fiscal year (USCIS, via secondary reports). Right: India tech industry headcount (NASSCOM)')
P=M['h1b_registrations']['points']
for i,p in enumerate(P):
    h=p[1]/800000*280; x=80+i*90
    s+=f'<rect x="{x}" y="{420-h}" width="64" height="{h}" rx="6" fill="#0891b2"/>'+note(x+32,414-h,f'{p[1]/1000:.0f}k','#0f172a',12,'middle',True)+note(x+32,442,'FY'+str(p[0]+1)[2:],'#64748b',12,'middle')
P=[p for p in M['india_tech_workforce']['points'] if p[0]>=2016]
for i,p in enumerate(P):
    h=p[1]/6.5*280; x=700+i*105
    s+=f'<rect x="{x}" y="{420-h}" width="74" height="{h}" rx="6" fill="#ea580c" opacity="{0.6 if p[0]==2026 else 1}"/>'+note(x+37,414-h,f'{p[1]}M','#0f172a',12,'middle',True)+note(x+37,442,('FY' if p[0]>2016 else '')+str(p[0]),'#64748b',12,'middle')
s+=note(700,468,'FY2026 is a NASSCOM projection (lighter bar). Scope differs slightly between reports.','#64748b',12)
save('4-global.svg',s)
# 5 Meta headcount
W,H=1280,420
s=head(W,H,'One company, the whole cycle: Meta headcount 2019–2024','Year-end employees (company filings via StockAnalysis and Barron\'s, secondary). The 2020–22 hiring surge and the 2023 "year of efficiency" in one chart')
P=M['meta_headcount']['points']
for i,p in enumerate(P):
    h=p[1]/90000*270; x=120+i*180
    s+=f'<rect x="{x}" y="{370-h}" width="120" height="{h}" rx="8" fill="{"#dc2626" if p[0]==2023 else "#2563eb"}"/>'+note(x+60,364-h,f'{p[1]:,}','#0f172a',13,'middle',True)+note(x+60,392,str(p[0]),'#64748b',13,'middle')
save('5-meta.svg',s)
print(sorted(os.listdir(OUT)))

# 6: 2006-2015 panel (batch 2)
s=head(1200,520,'Tech jobs 2006–2015 in three numbers','Sources: Challenger via eWeek ⚠️; BLS OES; NASSCOM via press ⚠️. Real dollars via CPI-U, our arithmetic.')
L=[p for p in M['layoffs']['points'] if p[0]<2012]
s+=note(60,110,'US tech-sector job cuts announced (Challenger)','#0f172a',15,'start',True)
for i,p in enumerate(L):
    h=p[1]/200000*280; x=80+i*140
    s+=f'<rect x="{x}" y="{440-h}" width="96" height="{h}" rx="6" fill="#dc2626"/>'+note(x+48,434-h,f'{p[1]/1000:.0f}k','#0f172a',13,'middle',True)+note(x+48,464,str(p[0]),'#64748b',12,'middle')
W=M['us_swdev_median_wage']['points']; W=[p for p in W if p[0] in (2010,2016)]
s+=note(440,110,'Software developer median pay (BLS)','#0f172a',15,'start',True)
for i,p in enumerate(W):
    r=real(p[0],p[1]); h=r/140000*280; x=460+i*150
    s+=f'<rect x="{x}" y="{440-h}" width="96" height="{h}" rx="6" fill="#2563eb"/>'+note(x+48,434-h,f'${r/1000:.0f}k','#0f172a',13,'middle',True)+note(x+48,464,str(p[0]),'#64748b',12,'middle')+note(x+48,486,f'(${p[1]/1000:.1f}k reported)','#64748b',11,'middle')
s+=note(440,508,'Bars in 2024 dollars. 2010 = applications developers.','#64748b',11)
I=[p for p in M['india_tech_workforce']['points'] if p[0] in (2015,2020)]
s+=note(830,110,'India IT-BPM direct jobs (NASSCOM)','#0f172a',15,'start',True)
for i,p in enumerate(I):
    h=p[1]/5*280; x=850+i*150
    s+=f'<rect x="{x}" y="{440-h}" width="96" height="{h}" rx="6" fill="#ea580c"/>'+note(x+48,434-h,f'{p[1]}M','#0f172a',13,'middle',True)+note(x+48,464,'FY'+str(p[0]),'#64748b',12,'middle')
save('6-2006-2015.svg',s)
