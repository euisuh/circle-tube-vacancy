import itertools, numpy as np
def cfv(seq):
    x=0.0
    for v in reversed(seq): x=1/(v+x)
    return x
def kappa_per(w):
    p=len(w); best=0
    for ph in range(p):
        fut=[w[(ph+i)%p] for i in range(80)]            # a_{k+1},a_{k+2},..
        past=[w[(ph-1-i)%p] for i in range(80)]         # a_k,a_{k-1},..
        t=cfv(fut); s=cfv(past)
        for r in range(1,w[ph]+1):
            best=max(best,(r+1+s)*(1-(r-1)*t)/(1+s*t))
    return best
res=[]
for p in range(1,9):
    for w in itertools.product(range(1,7),repeat=p):
        if all(x==1 for x in w): continue
        res.append((kappa_per(w),w))
res.sort(); print(len(res),"non-noble periodic words; smallest kappas:")
for k,w in res[:8]: print(f"{k:.6f}",w)
print("noble:",kappa_per((1,)),1+2/5**.5)
