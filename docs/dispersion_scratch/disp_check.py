"""Scratch checks for docs/DISPERSION.md.  NumPy only.  Run: python3 disp_check.py"""
import numpy as np, math
from fractions import Fraction

def cf_from_float_mp(beta_cf, K):
    """beta=[0;a1,a2,...] given as function k->a_k (k>=1). returns q_k, eta_k lists (high precision via mpmath)."""
    import mpmath as mp
    mp.mp.dps = 60
    a = [beta_cf(k) for k in range(1, K+2)]
    # beta value
    x = mp.mpf(0)
    for ak in reversed(a): x = 1/(ak+x)
    beta = x
    q=[1]; qm=0  # q_0=1,q_{-1}=0
    qs=[1]; prev=0
    p=[0]; 
    qkm1, qk = 0, 1
    qs=[1]
    for k in range(1,K+1):
        qkm1, qk = qk, a[k-1]*qk+qkm1
        qs.append(qk)
    etas=[]  # eta_k=||q_k beta||
    for k in range(0,K+1):
        v = qs[k]*beta; d = abs(v-mp.nint(v)); etas.append(d)
    return beta, a, qs, etas

BETAS = {
 'golden [0;2,1,1,..]': lambda k: 2 if k==1 else 1,
 'noble [0;3,1,1,..]': lambda k: 3 if k==1 else 1,
 'noble [0;2,2,1,1,..]': lambda k: [0,2,2][k] if k<=2 else 1,
 'silver [0;2,2,2,..]': lambda k: 2,
 '[0;3,3,3,..]': lambda k: 3,
 'mixed [0;2,1,2,1,..]': lambda k: 2 if k%2 else 1,
 '1/e [0;2,1,1,2,1,1,4,..]': None,
}
def e_cf(k):
    # 1/e = [0;2,1,1,2,1,1,4,1,1,6,...]; e=[2;1,2,1,1,4,1,1,6,...]
    # 1/e : a1=2, then a_{k}: pattern 1,1,2m
    if k==1: return 2
    j=k-2   # j=0,1,2,...: 1,1,2,1,1,4...
    r=j%3; m=j//3
    return 1 if r<2 else 2*(m+1)
BETAS['1/e [0;2,1,1,2,1,1,4,..]'] = e_cf

def beta_value(f, K=60):
    import mpmath as mp
    mp.mp.dps=60
    x=mp.mpf(0)
    for k in range(K,0,-1): x=1/(f(k)+x)
    return x

def gaps_turns(beta, N):
    pts = np.sort((np.arange(N)*beta) % 1.0)
    g = np.diff(np.append(pts, pts[0]+1.0))
    return g, pts

def Nh_sup_formula(f, K):
    """exact sup over blocks (k,r) of ((r+1)q_k+q_{k-1}-1)(eta_{k-1}-(r-1)eta_k) / (N=(r+1)q_k+q_{k-1}-1) -> returns list per k of max_r N*h"""
    beta, a, qs, etas = cf_from_float_mp(f, K)
    out=[]
    for k in range(1,K):
        best=0
        for r in range(1,a[k]+1):   # a[k] = a_{k+1}
            N=(r+1)*qs[k]+qs[k-1]-1
            h=etas[k-1]-(r-1)*etas[k]
            best=max(best, float(N*h))
        out.append((k,qs[k],best))
    return out

def test_gap_structure(f, Nmax=3000):
    """Check: N=r q_k+q_{k-1}+t (1<=r<=a_{k+1}, 0<=t<q_k): gaps eta_k x(N-q_k), eta_{k-1}-(r-1)eta_k x(q_k-t), eta_{k-1}-r eta_k x t."""
    beta, a, qs, etas = cf_from_float_mp(f, 40)
    bf=float(beta); bad=0; tot=0
    for k in range(1,12):
        if qs[k]>Nmax: break
        for r in range(1,a[k]+1):
            for t in range(0,qs[k]):
                N=r*qs[k]+qs[k-1]+t
                if N>Nmax: continue
                g,_=gaps_turns(bf,N)
                exp=sorted([float(etas[k])]*(N-qs[k])+[float(etas[k-1]-(r-1)*etas[k])]*(qs[k]-t)+[float(etas[k-1]-r*etas[k])]*t)
                tot+=1
                if np.max(np.abs(np.sort(g)-np.array(exp)))>1e-9: bad+=1
    return tot,bad

def brute_sup_Nh(beta, Nlo, Nhi):
    best=0;arg=0
    for N in sorted(set(list(range(Nlo,Nhi,max(1,(Nhi-Nlo)//300)))+[Nhi-1])):
        g,_=gaps_turns(beta,N); v=N*g.max()
        if v>best: best,arg=v,N
    return best,arg

def interval_disp(beta,N):
    pts=np.sort((np.arange(1,N+1)*beta)%1.0)
    inner=np.diff(pts).max()/2 if N>1 else 0
    return max(inner,pts[0],1-pts[-1])

def Vtilde_excess(beta, N, c):
    """Vt_N(c)-a^2 = 2 int_0^Q q m_N(c/q)^2 dq, a=cos(pi beta). midpoint rule in s=c/q (q=c/s): 2 c^2 int_{c/Q}^inf m^2 s^-3 ds"""
    Q=math.sin(math.pi*beta)
    g,_=gaps_turns(beta,N); g=2*math.pi*g
    gmax=g.max(); s_hi=N*gmax/2; s_lo=c/Q
    if s_lo>=s_hi: return 0.0
    # exact piecewise: use fine grid
    M=4000; s=np.linspace(s_lo,s_hi,M+1); sm=0.5*(s[1:]+s[:-1]); ds=np.diff(s)
    gs=np.sort(g)
    cs=np.concatenate([[0],np.cumsum(gs)])
    thr=2*sm/N
    idx=np.searchsorted(gs,thr)   # gaps > thr are gs[idx:]
    cnt=len(gs)-idx; tot=cs[-1]-cs[idx]
    m=(tot-thr*cnt)/(2*math.pi)
    return float(2*c*c*np.sum(m**2*sm**-3*ds))

QS={}; BETA_A={}
if __name__=='__main__':
    print('== 1. three-gap block structure (exact) ==')
    for name,f in BETAS.items():
        tot,bad=test_gap_structure(f,2500); print(f'{name:28s} cases {tot:6d} mismatches {bad}')
    print('\n== 2. limsup N*h_N (turns): block formula vs brute force, and theory ==')
    lam=(math.sqrt(5)-1)/2
    print('1+2/sqrt5 =',1+2/math.sqrt(5))
    for name,f in BETAS.items():
        beta=float(beta_value(f))
        form=Nh_sup_formula(f,40)
        tail=[b for k,q,b in form if q>200]
        # brute: sup over last block available with N<=60000
        qmax=[ (k,q) for k,q,b in form if q<=20000]
        k,q=qmax[-1]
        bs,arg=brute_sup_Nh(beta,q,min(4*q+10, 120000)) if q<30000 else (None,None)
        print(f'{name:28s} formula blocks (q_k>200): {[round(b,4) for b in tail[:6]]}  brute sup over N in [q_k,3q_k] k={k}: {bs and round(bs,4)}')
    print('\n== 3. interval (Niederreiter) dispersion N d_N for golden vs circle half-gap ==')
    beta=float(beta_value(BETAS['golden [0;2,1,1,..]']))
    F=[1,2]
    while F[-1]<300000: F.append(F[-1]+F[-2])
    best_int=0; best_circ=0
    lo=F[-4]
    for N in sorted(set(list(range(lo, F[-3], (F[-3]-lo)//400))+[F[-3]-1])):
        g,_=gaps_turns(beta,N)
        best_circ=max(best_circ,N*g.max())
        best_int=max(best_int,N*interval_disp(beta,N))
    print('circle: N*max gap (turns) sup over N in [%d,%d):'%(lo,F[-3]),best_circ)
    print('interval Niederreiter N*d_N sup over same range:',best_int)
    print('\n== 4. threshold check: max_{N in window} (Vt_N(c)-a^2) for c=Q L (1 -/+ 0.03) ==')
    for name in ['golden [0;2,1,1,..]','noble [0;3,1,1,..]','silver [0;2,2,2,..]','[0;3,3,3,..]','mixed [0;2,1,2,1,..]']:
        f=BETAS[name]; beta=float(beta_value(f)); Q=math.sin(math.pi*beta)
        form=Nh_sup_formula(f,40)
        _,_aa,_qs,_=cf_from_float_mp(f,40); QS[name]=_qs; BETA_A[name]=f
        qs=[q for k,q,b in form]; Ls=[b for k,q,b in form]
        # limsup estimate = max over tail blocks (periodic) ; use the last blocks with q<=3e4
        tail=[(k,q,b) for k,q,b in form if 100<q<=30000]
        L=max(b for k,q,b in tail)*math.pi/math.pi  # N*h_N in turns
        Dlim=math.pi*L   # D_N = pi N h_N
        res=[]
        for fac in (0.8,0.97,1.03):
            c=Q*Dlim*fac
            ex=[]
            for k,q,b in tail[-3:]:
                # block-end N (where N h_N peaks) minus 1% of q_k (keeps max-gap multiplicity ~0.01 q_k), plus a coarse sweep
                qkm1=qs[[kk for kk,_,_ in form].index(k)] if False else None
                Ns=[max(2,int(q*x)) for x in np.linspace(1,3.2,40)]
                aa=BETA_A[name]; 
                for r in range(1,aa(k+1)+1):
                    Ns.append((r+1)*q+QS[name][k-1]-1-int(0.01*q)-1)
                Ns=sorted(set(N for N in Ns if 2<=N<=200000))
                ex.append(max(Vtilde_excess(beta,N,c) for N in Ns))
            res.append((fac,ex))
        print(f'{name:26s} kappa~{L:.4f}  max excess over last 3 blocks: c=0.80cov {[f"{x:.2e}" for x in res[0][1]]} | 0.97cov {[f"{x:.2e}" for x in res[1][1]]} | 1.03cov {[f"{x:.2e}" for x in res[2][1]]}')
    print('\n   unbounded 1/e: excess for c=2,4 at N around a_{k+1} q_k/2 + q_{k-1} blocks')
    f=BETAS['1/e [0;2,1,1,2,1,1,4,..]']; beta=float(beta_value(f))
    b,a,qs,etas=cf_from_float_mp(f,40)
    for k in range(1,40):
        if 30<qs[k]<30000 and a[k]>=4:
            N=(a[k]//2)*qs[k]+qs[k-1]
            print(f' k={k} a_(k+1)={a[k]} N={N} excess(c=2)={Vtilde_excess(beta,N,2.0):.5f} excess(c=4)={Vtilde_excess(beta,N,4.0):.5f}')
