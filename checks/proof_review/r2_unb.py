import mpmath as mp, numpy as np, math
mp.mp.dps=60
cf=[3,1,400,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
v=mp.mpf(0)
for a in reversed(cf): v=1/(a+v)
beta=v
q=[1,cf[0]]
for a in cf[1:]: q.append(a*q[-1]+q[-2])
# q_k index: q[0]=1,q[1]=3 ; a_{k+1}=cf[k]; take k=2: a_3=400
k=2; a=cf[k]; print("q_k",q[k],"q_{k-1}",q[k-1],"a_{k+1}",a)
def m(N,s):
    p=sorted([float(mp.frac(j*beta)) for j in range(N)]); g=np.diff(p+[p[0]+1])*2*math.pi
    return np.maximum(g-2*s/N,0).sum()/(2*math.pi)
for N,lab in [(q[k],'q_k'),(((a+1)//2)*q[k]+q[k-1],'r=ceil(a/2)')]:
    for s in [0.5,1.0,2.0,3.0]:
        Md=max(1-s/math.pi,0); MW=max(.5-s/math.pi,0)+.5
        print(lab,N,s,"m_N=%.4f M_delta=%.4f M_W=%.4f"%(m(N,s),Md,MW))
