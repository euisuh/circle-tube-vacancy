import numpy as np, math, random
random.seed(1)
def cfval(cf):
    v=0.0
    for a in reversed(cf): v=1/(a+v)
    return v
worst=1e9;viol=0
for trial in range(40):
    A0=random.choice([1,2,3,5,8])
    cf=[random.randint(1,A0) for _ in range(30)]
    if cf[0]<2: cf[0]=2
    cf=[min(c,A0) if i else max(2,min(cf[0],max(A0,2))) for i,c in enumerate(cf)]
    A0e=max(cf)
    beta=cfval(cf)
    eps=1/((A0e+1)*(A0e+2))
    Nmax=3000
    pts=np.sort((np.arange(Nmax)*beta)%1.0)
    for N in range(30,Nmax,7):
        p=np.sort((np.arange(N)*beta)%1.0); g=np.diff(np.r_[p,p[0]+1])
        vals,cnt=np.unique(np.round(g,11),return_counts=True)
        freq=cnt/N; ell=N*vals*math.pi
        ok=False
        for i in range(len(vals)):
            for j in range(i+1,len(vals)):
                if freq[i]>=eps and freq[j]>=eps and ell[j]>=(1+eps)*ell[i]-1e-9: ok=True
        if not ok: viol+=1; print("LEMMA FAIL",A0e,N,vals,cnt)
        # mass lemma
        tau=eps**2/4
        mass=freq[ell<=math.pi*(1-tau)].sum()
        worst=min(worst,mass/ (eps**2/4))
print("violations",viol,"min mass/(eps^2/4)",worst)
