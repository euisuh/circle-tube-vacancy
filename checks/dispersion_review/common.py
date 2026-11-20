import numpy as np, mpmath as mp
mp.mp.dps=60
def cf_to_beta(a):  # a=[a1,a2,...]
    x=mp.mpf(0)
    for v in reversed(a): x=1/(v+x)
    return x
def convs(a):
    q=[0,1]  # q_{-1}, q_0
    for v in a: q.append(v*q[-1]+q[-2])
    return q  # q[i+1]=q_i
def maxgap_all(beta,Nmax):
    """max circular gap h_N (turns) for N=1..Nmax via reverse deletion."""
    j=np.arange(Nmax,dtype=np.float64)
    # high precision-ish: use mp for beta then split hi/lo
    b=float(beta); lo=float(beta-mp.mpf(b))
    x=np.mod(j*b+j*lo,1.0)
    order=np.argsort(x,kind='stable')
    pos=np.empty(Nmax,dtype=np.int64); pos[order]=np.arange(Nmax)
    xs=x[order]
    prv=np.roll(np.arange(Nmax),1).tolist(); nxt=np.roll(np.arange(Nmax),-1).tolist()
    xl=xs.tolist(); posl=pos.tolist()
    # gaps with wrap
    def gap(i,k):
        d=xl[k]-xl[i]
        return d if d>0 else d+1.0
    g=np.diff(np.append(xs,xs[0]+1.0)); cur=float(g.max())
    h=np.empty(Nmax); h[Nmax-1]=cur
    for n in range(Nmax-1,0,-1):  # delete point index n -> N=n
        p=posl[n]; a=prv[p]; b2=nxt[p]
        nxt[a]=b2; prv[b2]=a
        d=xl[b2]-xl[a]
        if d<=0: d+=1.0
        if d>cur: cur=d
        h[n-1]=cur
    return h  # h[N-1]
