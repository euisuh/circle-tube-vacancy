import mpmath as mp, math, numpy as np
from fractions import Fraction
mp.mp.dps=60
lam=(mp.sqrt(5)-1)/2
def noble(prefix):
    # beta=[0;prefix...,1,1,1,...]  tail 1's = 1/(1+..)=lam ; value of [t;1,1,..]=t+lam
    v=lam
    for a in reversed(prefix): v=1/(a+v)
    return v
def convergents(beta,K):
    # q_k from CF of beta via mp
    x=beta; qs=[1]; ps=[0]; a_s=[]
    q_prev,q=0,1; p_prev,p=1,0
    qlist=[1]; etas=[beta]  # eta_0=||q0 beta||=beta  (beta<1/2)
    y=beta; qm1,q0=0,1
    out=[]
    z=1/beta
    as_=[]
    xx=beta
    for i in range(K):
        a=int(mp.floor(1/xx)); as_.append(a); xx=1/xx-a
    q=[0,1]  # q_{-1}=0,q_0=1
    for a in as_: q.append(a*q[-1]+q[-2])
    return as_,q[1:]  # q[0]=q_0
def gaps(beta,N):
    pts=sorted([float(mp.frac(j*beta)) for j in range(N)])
    g=np.diff(pts+[pts[0]+1.0]); return g
def run(prefix,name):
    beta=noble(prefix); print(name,"beta=",mp.nstr(beta,12),"a=cos(pi b)=",mp.nstr(mp.cos(mp.pi*beta),6))
    as_,q=convergents(beta,30)
    # eta_k = ||q_k beta||
    eta=[abs(q[k]*beta-mp.nint(q[k]*beta)) for k in range(len(q))]
    u=float(mp.pi/(mp.sqrt(5)*lam**2))
    k0=len(prefix)+1
    for k in range(k0+2,k0+9):
        qk=int(q[k]);qkm=int(q[k-1])
        for sfrac in [0.0,0.3,0.7,0.99]:
            s=int(sfrac*qkm); N=qk+s
            if N>40000: continue
            g=gaps(beta,N)
            # predicted exact
            pred={'eta_k-1':(float(eta[k-1]),N-qkm),'eta_k':(float(eta[k]),s),'eta_k-2':(float(eta[k-2]),qkm-s)}
            # compare multiset
            vals=np.round(g,12); 
            ok=True; det=[]
            for nm,(e,cnt) in pred.items():
                c=int((abs(g-e)<1e-11).sum()); det.append((nm,c,cnt)); ok&= (c==cnt)
            x=s/qk
            # scaled law vs mu_x
            half=N*g/2*2*math.pi   # N * half gap in angle = N*pi*g
            half=N*math.pi*g
            xs=np.array([u*(1+x)*float(lam)**i for i in range(3)]); fw=np.array([(float(lam)-x),float(lam)**2+x,x])/(1+x)
            S=np.linspace(0,u*(1+x)*1.01,400)
            mN=np.array([np.maximum(half-t,0).sum()/(math.pi*N) for t in S])
            Mx=np.array([(fw*np.maximum(xs-t,0)).sum()/math.pi for t in S])
            print(f"  k={k} q_k={qk} s={s} N={N} counts_ok={ok} {det if not ok else ''} sup|m_N-M_x|={abs(mN-Mx).max():.2e}")
run([3],"[0;3,1,1,...]")
run([2,2],"[0;2,2,1,1,...]")
run([],"golden")
