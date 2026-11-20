import numpy as np, mpmath as mp, random, sys
from common import *
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 1)
Nmax=400000
def test(name,a):
    beta=cf_to_beta(a); q=convs(a)
    # beta in (0,1/2) requires a1>=2
    h=maxgap_all(beta,Nmax)
    N=np.arange(1,Nmax+1); Nh=N*h
    worst=0; blocks=0; sup_pred=0
    # eta_k
    eta=[None]*(len(a)+1)
    # eta_k=|q_k beta - p_k|, via mp
    def eta_k(k):
        qk=q[k+1]; return abs(mp.nint(qk*beta)-qk*beta) if True else 0
    for k in range(1,len(a)-1):
        qk=q[k+1]; qm=q[k]
        if qk>Nmax//4: break
        ek=float(eta_k(k)); em=float(eta_k(k-1)) if k>=1 else None
        for r in range(1,a[k]+1):   # a_{k+1}=a[k]
            lo=r*qk+qm; hi=lo+qk-1
            if hi>Nmax: break
            ell=em-(r-1)*ek
            Ns=np.arange(lo,hi+1)
            pred=ell*np.ones(len(Ns))
            err=np.max(np.abs(h[lo-1:hi]-pred))
            worst=max(worst,err/ell); blocks+=1
    # finite kappa estimate over late blocks
    Nstart=Nmax//50
    print(f"{name:28s} blocks {blocks:4d} worst rel gap-err {worst:.2e}  sup_{{N>{Nstart}}} N h_N = {Nh[Nstart:].max():.5f}")
    return Nh
test("golden-ish [2,1,1..]",[2]+[1]*30)
test("silver",[2]*30)
for i in range(6):
    a=[random.randint(2,4)]+[random.choice([1,2]) for _ in range(40)]; test("rand{1,2} "+str(a[:8]),a)
for i in range(4):
    a=[random.randint(2,4)]+[random.choice([1,3]) for _ in range(40)]; test("rand{1,3} "+str(a[:8]),a)
test("early-large then 1",[2,7,9,5]+[1]*30)
test("[3,1,4,1,5,9,2,6,..]",[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8])
