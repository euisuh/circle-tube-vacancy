import numpy as np, mpmath as mp
from common import *
mp.mp.dps=80
TWO=2*np.pi
def build(a,K):
    beta=cf_to_beta(a+[1]*0)
    q=convs(a)
    def eta(k):
        qk=q[k+1]; return abs(mp.nint(qk*beta)-qk*beta)
    return beta,q,eta
def kappa_blocks(a,K0,K1):
    beta,q,eta=build(a,0)
    out=[]
    for k in range(K0,K1):
        qk=q[k+1]; qm=q[k]; ek=eta(k); em=eta(k-1)
        for r in range(1,a[k]+1):
            N=(r+1)*qk+qm-1; ell=em-(r-1)*ek
            out.append((k,r,float(N*ell),N,ell,qk,ek,em))
    return beta,q,out
def E_at(c,Q,N,classes):
    # classes: list of (gap_turns, count); N total
    D=max(g for g,n in classes if n>0)*N*np.pi
    qlo=min(Q,c/D) if D>0 else Q
    if qlo>=Q: return 0.0
    qs=np.linspace(qlo,Q,6001)
    s=c/qs  # in radians-units where s/N distance
    m=np.zeros_like(qs)
    for g,n in classes:
        if n>0: m+=n*np.maximum(TWO*g-2*s/N,0)
    m/=TWO
    f=qs*m**2
    return float(2*np.trapezoid(f,qs))
def run(name,a,K0,K1):
    beta,q,out=kappa_blocks(a,K0,K1)
    al=np.pi*float(beta); Q=np.sin(al)
    # kappa estimate: max over blocks in last third (phase-complete for periodic/eventually periodic)
    kap=max(o[2] for o in out[len(out)//2:])
    ccov=np.pi*Q*kap
    print(f"== {name}: kappa~{kap:.5f} ccov={ccov:.5f}")
    for fac in (0.9,0.99,1.01,1.05):
        c=fac*ccov; row=[]
        for k in range(K0,K1,max(1,(K1-K0)//6)):
            best=0
            for (kk,r,v,N,ell,qk,ek,em) in out:
                if kk!=k and kk!=k+1: continue
                # sample t via N from block end back by fractions of q_k
                for frac in (0.0,0.02,0.05,0.1,0.2,0.4):
                    t=int(float(qk)*0) # placeholder
                    j=int(frac*float(qk)); Nn=N-j; tt=int(qk)-1-j
                    if tt<0: continue
                    Nf=float(Nn)
                    cl=[(float(ek),float(Nn-qk)),(float(ell),float(qk-tt)),(float(em-r*ek),float(tt))]
                    best=max(best,E_at(c,Q,Nf,cl))
            row.append(best)
        print(f" c={fac:4.2f}c_cov  max_t E over blocks k, k+1: "+" ".join(f"{x:.2e}" for x in row))
cases={
 "golden":([2]+[1]*70,20,60),
 "silver":([2]*70,20,60),
 "[2,(1,2)^]":([2]+[1,2]*35,20,60),
 "[(1,3)^]":([2]+[1,3]*35,20,60),
 "[3,1,1,(2,2,1)^]":([3,1,1]+[2,2,1]*25,20,60),
 "early large then noble":([2,9,8,7]+[1]*70,20,60),
 "{1,2,4}-per":([2]+[4,1,2,1]*20,20,60),
}
for n,(a,k0,k1) in cases.items(): run(n,a,k0,k1)
