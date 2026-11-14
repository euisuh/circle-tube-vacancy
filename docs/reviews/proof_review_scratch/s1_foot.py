import numpy as np, math
def seg_dist(P,A,B):
    d=B-A; t=((P-A)@d)/(d@d); t=np.clip(t,0,1)
    return np.linalg.norm(P-(A+np.outer(t,d)),axis=1)
def run(alpha,N,c,rs,nphi=20000,eps=None):
    a=math.cos(alpha);Q=math.sin(alpha);w=c/N
    pts=[(math.cos(2*j*alpha),math.sin(2*j*alpha)) for j in range(N+1)]
    phi=np.linspace(0,2*math.pi,nphi,endpoint=False)
    bad={}
    for r in rs:
        P=np.c_[r*np.cos(phi),r*np.sin(phi)]
        D=np.full(nphi,9.)
        for j in range(N):
            D=np.minimum(D,seg_dist(P,np.array(pts[j]),np.array(pts[j+1])))
        cov_true=D<=w
        cov=np.zeros(nphi,bool)
        if r>a+w:
            dm=math.acos((a+w)/r);dp=math.acos((a-w)/r) if (a-w)/r<=1 else 0
            for j in range(N):
                th=(2*j+1)*alpha
                dl=(phi-th+math.pi)%(2*math.pi)-math.pi
                cov|=(abs(dl)>=dm)&(abs(dl)<=dp)
        bad[r]=int((cov!=cov_true).sum())
    return a,Q,w,bad
for alpha,N,c in [(math.pi*0.3819660112501051,40,2.0),(math.pi*0.2764,60,3.0),(math.pi*0.47,30,2.0),(math.pi*0.08,50,1.0),(math.pi*0.3819660112501051,25,6.0)]:
    a=math.cos(alpha);eps=(1-a)/3-1e-9
    rs=[a+0.01,a+eps*0.5,a+eps,(a+1-eps)/2,1-eps,0.9999]
    rs=[r for r in rs if r<1]
    a,Q,w,bad=run(alpha,N,c,rs)
    cond=(1-eps)**2-(a-w)**2<Q**2
    print(f"alpha/pi={alpha/math.pi:.4f} N={N} w={w:.3f} a={a:.3f} cond_ok={cond} mismatches(of 20000):",{round(k,3):v for k,v in bad.items()})
