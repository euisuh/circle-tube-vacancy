import mpmath as mp, numpy as np, math, random
mp.mp.dps=80
def beta_from(cf):
    v=mp.mpf(0)
    for a in reversed(cf): v=1/(a+v)
    return v
def conv(cf):
    q=[0,1]; 
    for a in cf: q.append(a*q[-1]+q[-2])
    return q[1:]  # q[0]=q_0=1, q[k]=q_k with a_k=cf[k-1]... q_k=a_k q_{k-1}+q_{k-2}
def gaps(beta,N):
    pts=sorted([mp.frac(j*beta) for j in range(N)])
    return [pts[i+1]-pts[i] for i in range(N-1)]+[pts[0]+1-pts[-1]]
tests={'golden-ish [0;2,1,1..]':[2]+[1]*40,'[0;3,1,5,1,9,1,17,1,33,...]':[3,1,5,1,9,1,17,1,33,1,65,1,129],'[0;2,7,3,12,1,20,2,40]':[2,7,3,12,1,20,2,40,3,3],'[0;3,2,2,2...]':[3]+[2]*20}
bad=0;tot=0
for name,cf in tests.items():
    beta=beta_from(cf+[1]*0) if False else beta_from(cf+[mp.inf]) if False else None
    # use truncated CF + tail large to be irrational-like: append tail of 1's
    beta=beta_from(cf+[1]*60)
    q=conv(cf+[1]*60)
    eta=[abs(q[k]*beta-mp.nint(q[k]*beta)) for k in range(len(q))]
    a_=lambda k: (cf+[1]*60)[k-1]  # a_k
    for k in range(2,min(len(cf)-1,9)):
        ak1=a_(k+1)
        for r in range(1,ak1+1):
            N=r*q[k]+q[k-1]
            if N>5000: continue
            g=sorted(gaps(beta,N))
            A=eta[k]; C=eta[k-1]-(r-1)*eta[k]
            cA=sum(1 for x in g if abs(x-A)<mp.mpf(10)**-40); cC=sum(1 for x in g if abs(x-C)<mp.mpf(10)**-40)
            tot+=1
            if not(cA==N-q[k] and cC==q[k] and cA+cC==N): bad+=1; print("C.2 FAIL",name,k,r,N,cA,cC,N-q[k],q[k])
            # s-extension: N=r q_k+q_{k-1}+s
            for s in [1,q[k]//2,q[k]-1]:
                N2=N+s
                if s<=0 or N2>5000: continue
                g=gaps(beta,N2)
                B=eta[k-1]-r*eta[k]; Cc=B+eta[k]
                cn={'A':sum(1 for x in g if abs(x-A)<mp.mpf(10)**-40),'B':sum(1 for x in g if abs(x-B)<mp.mpf(10)**-40),'C':sum(1 for x in g if abs(x-Cc)<mp.mpf(10)**-40)}
                tot+=1
                if not(cn['A']==N2-q[k] and cn['B']==s and cn['C']==q[k]-s): bad+=1;print("3-class FAIL",name,k,r,s,cn)
    # level-k-1 N=q_k claim
    for k in range(3,min(len(cf)-1,9)):
        N=q[k]
        if N>5000: continue
        g=gaps(beta,N); A=eta[k-1];C=eta[k-1]+eta[k]
        cA=sum(1 for x in g if abs(x-A)<mp.mpf(10)**-40);cC=sum(1 for x in g if abs(x-C)<mp.mpf(10)**-40)
        tot+=1
        if not(cA==q[k]-q[k-1] and cC==q[k-1]): bad+=1;print("N=q_k FAIL",name,k,cA,cC)
print("checked",tot,"bad",bad)
