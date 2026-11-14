import numpy as np, random, mpmath as mp
from common import *
random.seed(5); bad=0; tot=0
for trial in range(12):
    a=[random.randint(2,4)]+[random.choice([1,2,3]) for _ in range(25)]
    beta=cf_to_beta(a); q=convs(a); b=float(beta)
    for k in range(1,len(a)-1):
        qk=q[k+1]; qm=q[k]
        if qk>3000: break
        ek=float(abs(mp.nint(qk*beta)-qk*beta)); qmm=qm; em=float(abs(mp.nint(qm*beta)-qm*beta))
        for r in range(1,a[k]+1):
            for t in random.sample(range(qk),min(qk,5)):
                N=r*qk+qm+t
                x=np.sort(np.mod(np.arange(N)*b,1.0)); g=np.diff(np.append(x,x[0]+1))
                L=em-(r-1)*ek
                mult=int(np.sum(np.abs(g-L)<1e-10)); tot+=1
                m1=int(np.sum(np.abs(g-ek)<1e-10)); m3=int(np.sum(np.abs(g-(em-r*ek))<1e-10))
                if mult!=qk-t or m1!=N-qk and not (m1+m3==N-qk+t and abs(ek-(em-r*ek))<1e-10) or abs(g.max()-L)>1e-10: bad+=1; print("BAD",a[:6],k,r,t,mult,qk-t,m1,m3)
print("checked",tot,"bad",bad)
