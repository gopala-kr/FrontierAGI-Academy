# Generates assets/diagrams/ai-economy/*.svg from data/tech-jobs-history.json (python3 scripts/diagrams_tech_jobs.py)
import html, os
OUT='/home/user/Claude_Project_3_LLM/assets/diagrams/ai-economy/'
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
# --- Part 1: jobs
hbars('1-canaries.svg','Young workers in AI-exposed jobs: the gap is widening','Employment of 22–25-year-olds in the most AI-exposed jobs vs where it would be at their less-exposed peers’ pace',
 [('Data to Jul 2025 (first paper)',15,'#f59e0b','below'),('Data to Jun 2026 (Aug 2026 revision)',19,'#dc2626','below')],25,
 src='Source: Brynjolfsson, Chandar, Chen, Stanford Digital Economy Lab, ADP payroll data. Descriptive, not causal.')
W,H=1100,360; s=head(W,H,'Four ways to measure "AI is changing jobs"','Each lens answers a different question; none of them alone is the answer')+ANIM
L=[('Exposure','Could AI do the tasks?','Task lists × model ability','#7c3aed'),('Usage','What do people use AI for?','Anthropic Economic Index, Fed surveys','#2563eb'),('Payroll','Who is being hired?','ADP payroll (Stanford "Canaries")','#dc2626'),('Occupation mix','Is the job mix shifting?','CPS (Yale Budget Lab)','#0d9488')]
for i,(a,b,c,col) in enumerate(L):
    x=24+i*268; s+=f'<g class="fd" style="animation-delay:{i*.2}s">'+box(x,86,248,112,a,[b,'',c],col,fs=17)+'</g>'
s+=box(24,226,1052,92,'What they say together (Nov 2026)',['Usage is broad and growing; exposure is high in computer, office and finance work;','hiring of young workers in exposed jobs has fallen; the overall job mix has not yet shifted in an AI-shaped way.'],'#0f172a',fs=16)
save('2-four-lenses.svg',s)
W,H=1000,330; s=head(W,H,'How people use Claude.ai: helping vs doing','Share of conversations, Anthropic Economic Index')+ANIM
for i,(lab,a,b) in enumerate([('Previous report',47,49),('Jan 2026 report (Nov 2025 data)',52,45)]):
    y=100+i*90; s+=note(24,y+22,lab,'#0f172a',14,bold=True)
    s+=f'<rect class="gr" x="330" y="{y}" width="{6*a}" height="34" rx="6" fill="#2563eb"/><text x="{336}" y="{y+23}" font-size="13" font-weight="700" fill="#fff">Augmentation {a}%</text>'
    s+=f'<rect class="gr" style="animation-delay:.3s" x="{332+6*a}" y="{y}" width="{6*b}" height="34" rx="6" fill="#f97316"/><text x="{338+6*a}" y="{y+23}" font-size="13" font-weight="700" fill="#fff">Automation {b}%</text>'
s+=note(24,300,'Augmentation = the person works with the AI; automation = the AI does the task. Previous-report values derived from the stated changes (+5 / −4 points).','#64748b',11.5)
save('3-aug-auto.svg',s)
# --- Part 2: productivity
W,H=1100,470; s=head(W,H,'What the controlled studies found','Change in output per hour (or time taken), by study; bars from zero')+ANIM
z=560; s+=f'<line x1="{z}" y1="80" x2="{z}" y2="400" stroke="#334155" stroke-width="1.5"/>'+note(z,76,'0','#334155',12,'middle')
R=[('Customer support, all agents (QJE 2025)',14,'#16a34a','+14% issues/hour'),('Customer support, novice agents',34,'#16a34a','+34%'),('Experienced OSS developers, early 2025 (METR)',-19,'#dc2626','19% slower'),('Same developers: how fast they felt',20,'#94a3b8','felt +20% faster'),('Gen AI users: time saved (St. Louis Fed, 2024)',5.4,'#2563eb','5.4% of hours')]
for i,(lab,v,c,t) in enumerate(R):
    y=100+i*58; w=abs(v)*12; x=z if v>=0 else z-w
    s+=note(24,y+20,lab,'#0f172a',13,bold=True)
    s+=f'<rect class="gr" style="animation-delay:{i*.15}s;transform-origin:{"left" if v>=0 else "right"} center" x="{x}" y="{y+2}" width="{w}" height="26" rx="5" fill="{c}"/>'
    s+=note(z+w+8 if v>=0 else z+8,y+21,t,'#0f172a',12.5,'start',True)
s+=note(24,440,'Different measures and settings: compare directions, not sizes. Sources: Brynjolfsson, Li & Raymond (QJE 2025); METR (arXiv 2507.09089); St. Louis Fed.','#64748b',11.5)
save('4-studies.svg',s)
hbars('5-funnel.svg','From "uses AI" to "time saved"','US employed adults, Q2 2026 (time saved: Q1 2026)',
 [('Used generative AI for work last week',39.2,'#2563eb','of workers'),('Work hours assisted by AI',6.3,'#7c3aed','of all hours'),('Work hours saved by AI',2.2,'#16a34a','of all hours')],45,
 src='Source: St. Louis Fed Real-Time Population Survey via FRED (RPSGENAIASSISTWRKHRSALL, RPSGENAITSALL). Self-reported.')
W,H=1000,400; s=head(W,H,'US labour productivity, 2026','Nonfarm business output per hour, % change (quarterly figures annualised)')+ANIM
base=330
for i,(lab,v,c) in enumerate([('Q2 2026 (revised)',2.1,'#64748b'),('Q3 2026',3.6,'#2563eb'),('Q3 2026 vs Q3 2025',2.1,'#0d9488')]):
    x=140+i*270; h=v*55
    s+=f'<rect class="gu" style="animation-delay:{i*.2}s" x="{x}" y="{base-h}" width="140" height="{h}" rx="6" fill="{c}"/>'+note(x+70,base-h-10,f'{v}%','#0f172a',18,'middle',True)+note(x+70,base+24,lab,'#0f172a',13,'middle',True)
s+=f'<line x1="100" y1="{base}" x2="960" y2="{base}" stroke="#334155"/>'+note(24,385,'Source: BLS Productivity and Costs, 5 Nov 2026. BLS does not attribute any of this to AI.','#64748b',11.5)
save('6-productivity.svg',s)
W,H=1000,420; s=head(W,H,'The productivity J-curve (illustrative)','Why firm-wide gains can lag behind task-level gains')+ANIM
s+='<line x1="80" y1="240" x2="940" y2="240" stroke="#94a3b8" stroke-dasharray="5 4"/>'+note(84,232,'no change','#64748b',12)
s+='<path class="dr" d="M80 240 C 220 245, 280 320, 380 315 S 560 250, 640 200 S 820 110, 940 90" fill="none" stroke="#2563eb" stroke-width="4"/>'
for x,y,t in [(300,345,'1. Invest: tools, training, redesign. Measured output dips.'),(560,280,'2. Reorganise work around AI.'),(760,120,'3. Gains show up in the statistics.')]:
    s+=note(x,y,t,'#0f172a',13,'middle',True)
s+=note(24,400,'Shape is illustrative (after Brynjolfsson, Rock & Syverson’s productivity J-curve idea); not fitted to data.','#64748b',11.5)
save('7-jcurve.svg',s)
# --- Part 3: adoption
hbars('8-sectors.svg','US businesses using AI, by sector','Share of firms using AI in any business function, Census Business Trends and Outlook Survey, as of 3 May 2026',
 [('Information',39.7,'#7c3aed','now'),('Information, expected in 6 months',42,'#c4b5fd','approx.'),('Finance and insurance',33.9,'#2563eb','now'),('Finance, expected in 6 months',39,'#93c5fd','approx.'),('All US businesses',19.8,'#0f172a','now')],50,
 src='Source: US Census Bureau BTOS (question broadened Nov 2025; earlier figures not comparable). Six-month expectations as reported, rounded.')
hbars('9-workers-firms.svg','Workers vs firms: two different adoption numbers','Why "45% use AI" and "20% use AI" can both be true',
 [('Workers using AI for their job (May 2026)',45,'#2563eb',''),('Employed adults, used gen AI for work last week (Q2 2026)',39.2,'#60a5fa',''),('Large firms scaling AI agents (2026)',40,'#7c3aed',''),('Smaller firms scaling AI agents (2026)',22,'#c4b5fd',''),('US businesses using AI (May 2026)',19.8,'#0f172a','')],50,
 src='Sources: St. Louis Fed; McKinsey State of AI 2026 (survey respondents, >$1B revenue = large); Census BTOS.')
# --- Part 4: cheap intelligence
W,H=1000,460; s=head(W,H,'What the same capability costs over time','Index: cost today = 100; paths at the rates Epoch AI measured (log scale)')+ANIM
import math
X0,X1,Y0,Y1=110,940,90,380
def py(v): return Y1-(math.log10(v)+2)/(4)*(Y1-Y0)  # 100 -> top, 0.01 -> bottom
for v in [100,10,1,0.1,0.01]:
    s+=f'<line x1="{X0}" y1="{py(v)}" x2="{X1}" y2="{py(v)}" stroke="#e2e8f0"/>'+note(X0-10,py(v)+4,f'{v:g}','#64748b',12,'end')
for yr in range(0,4): s+=note(X0+yr*(X1-X0)/3,Y1+22,f'Year {yr}','#334155',12,'middle')
for rate,c,lab in [(13,'#dc2626','13× per year (early pace)'),(10,'#f59e0b','~10× per year (industry rule of thumb)'),(4.7,'#2563eb','4.7× per year (pace after two years)')]:
    d='M'+' L'.join(f'{X0+t*(X1-X0)/3:.1f} {py(max(0.01,100/rate**t)):.1f}' for t in [i/20 for i in range(61)])
    s+=f'<path class="dr" d="{d}" fill="none" stroke="{c}" stroke-width="3"/>'
for i,(c,lab) in enumerate([('#dc2626','13× per year (Epoch, early pace)'),('#f59e0b','~10× per year (rule of thumb)'),('#2563eb','4.7× per year (Epoch, after two years)')]):
    s+=f'<rect x="560" y="{100+i*22}" width="14" height="4" fill="{c}"/>'+note(580,105+i*22,lab,'#0f172a',12)
s+=note(24,445,'Source: Epoch AI (Sep 2026): ~47% per quarter at fixed performance, slowing to ~32% per quarter. Paths are arithmetic from those rates.','#64748b',11.5)
save('10-price.svg',s)
W,H=1000,400; s=head(W,H,'Google: tokens processed per month','Log scale. ⚠️ Figures as reported in secondary analysis of Google statements')+ANIM
for i,(lab,v,t) in enumerate([('May 2024',9.7e12,'9.7 trillion'),('May 2025',480e12,'480 trillion'),('May 2026',3.2e15,'3.2 quadrillion')]):
    x=170+i*260; h=(math.log10(v)-12)/3.6*240
    s+=f'<rect class="gu" style="animation-delay:{i*.25}s" x="{x}" y="{330-h}" width="150" height="{h}" rx="6" fill="#0d9488"/>'+note(x+75,320-h,t,'#0f172a',15,'middle',True)+note(x+75,356,lab,'#0f172a',13,'middle',True)
s+='<line x1="120" y1="330" x2="940" y2="330" stroke="#334155"/>'+note(24,388,'Source: Wing VC analysis citing Google disclosures (secondary). Roughly 330× in two years.','#64748b',11.5)
save('11-tokens.svg',s)
W,H=1100,440; s=head(W,H,'When thinking gets cheap, what stays scarce?','Our reading of where value moves')+ANIM
s+=band(24,80,500,320,'GETTING CHEAP','#16a34a')+band(576,80,500,320,'STAYING SCARCE','#dc2626')
for i,t in enumerate(['A first draft of text or code','A summary of a document','A routine answer or classification','A translation','A standard analysis']):
    s+=f'<g class="fd" style="animation-delay:{i*.12}s">'+box(44,110+i*56,460,44,t,None,'#16a34a',fs=14)+'</g>'
for i,t in enumerate(['Compute, power and chips','Trusted, proprietary data','Verification: knowing the answer is right','Distribution and customer trust','Judgement and accountability']):
    s+=f'<g class="fd" style="animation-delay:{.6+i*.12}s">'+box(596,110+i*56,460,44,t,None,'#dc2626',fs=14)+'</g>'
s+=arr(530,240,570,240)
save('12-scarce.svg',s)
print('ok')
hbars('13-functions.svg','Where firms put AI: business functions','Share of AI-using US firms using it in each function, Nov 2025 – Jan 2026',
 [('Sales and marketing',52,'#db2777',''),('Strategy and business development',45,'#7c3aed',''),('Information technology',41,'#2563eb','')],60,
 src='Source: Bonney et al., The Microstructure of AI Diffusion (Census CES-WP-26-25 / NBER w35141). 57% of users integrate AI in three or fewer functions.')
hbars('14-tasks.svg','Which tasks workers use generative AI for','Generative AI adoption rate among workers who do each task (US, 2026)',
 [('Reading documents for technical information',61.3,'#0d9488',''),('Preparing research reports',60.7,'#0891b2',''),('Analysing data for trends',57.5,'#2563eb','')],70,
 src='Source: Bick, Blandin, Deming and Schumacher, What Work Does Generative AI Do? (St. Louis Fed WP 2026-017). Lowest: manual and personal-service tasks.')
