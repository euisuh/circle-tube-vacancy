import json, numpy as np, sys
sys.path.insert(0, '.')
d = json.load(open('../results/indep-experiments.json')); R = d['rows']
out = []
def P(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)
P('## Convergence (rows: x0 = Fibonacci, x1 = N=F_m+floor(F_m/3))')
for c in (0.5, 1.0, 2.0, 3.0):
    for tag, sel in (('x=0', lambda r: r['k'] == 0), ('x~1/3', lambda r: r['k'] > 0)):
        rows = [r for r in R if r['kind'] == 'conv' and r['c'] == c and sel(r)]
        rows.sort(key=lambda r: r['m'])
        N = np.array([r['N'] for r in rows], float)
        e1 = np.array([abs(r['V_N'] - r['Vtilde']) for r in rows])
        e2 = np.array([abs(r['V_N'] - r['V_lim']) for r in rows])
        s1 = np.polyfit(np.log(N), np.log(e1), 1)[0]; s2 = np.polyfit(np.log(N), np.log(e2), 1)[0]
        P(f'\nc={c} {tag}: slope log|V_N-Vtilde| vs logN = {s1:.2f}; slope log|V_N-V(x,c)| = {s2:.2f}')
        P('| m | N | V_N | Vtilde | V(x,c) | V_N-Vtilde | V_N-V(x,c) |\n|---|---|---|---|---|---|---|')
        for r in rows:
            P(f"| {r['m']} | {r['N']} | {r['V_N']:.6f} | {r['Vtilde']:.6f} | {r['V_lim']:.6f} | {r['V_N']-r['Vtilde']:+.2e} | {r['V_N']-r['V_lim']:+.2e} |")
P('\n## Phase sweep')
for m in (20, 21):
    for c in (1.0, 2.0):
        rows = sorted([r for r in R if r['kind'] == 'sweep' and r['m'] == m and r['c'] == c], key=lambda r: r['k'])
        P(f'\nm={m} c={c}: argmin over block at x={min(rows,key=lambda r:r["V_N"])["x"]:.4f}; min V_N={min(r["V_N"] for r in rows):.6f}; max |V_N-V|={max(abs(r["V_N"]-r["V_lim"]) for r in rows):.2e}; argmin of V(x,c) at x={min(rows,key=lambda r:r["V_lim"])["x"]:.4f}')
        P('| x | N | V_N | V(x,c) | diff |\n|---|---|---|---|---|')
        for r in rows:
            P(f"| {r['x']:.4f} | {r['N']} | {r['V_N']:.6f} | {r['V_lim']:.6f} | {r['V_N']-r['V_lim']:+.2e} |")
P('\n## Threshold (m=20; V-a^2)')
P('| c | x | N | V_N-a^2 | V_N-a^2+2ac/N | V(x,c)-a^2 | Q*pi*C*(1+x)-c |\n|---|---|---|---|---|---|---|')
C = ((np.sqrt(5)-1)/2)**-2/np.sqrt(5); Q = np.sin(np.pi*(3-np.sqrt(5))/2)
for r in sorted([r for r in R if r['kind'] == 'thresh'], key=lambda r: (r['c'], r['k'])):
    P(f"| {r['c']} | {r['x']:.4f} | {r['N']} | {r['V_N']-r['a2']:+.3e} | {r['V_N']-r['a2']+2*np.sqrt(r['a2'])*r['c']/r['N']:+.3e} | {r['V_lim']-r['a2']:+.3e} | {Q*np.pi*C*(1+r['x'])-r['c']:+.3f} |")
open('../results/indep-analysis.md', 'w').write('\n'.join(out))
