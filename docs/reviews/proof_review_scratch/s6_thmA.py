import numpy as np, math
lam=(5**.5-1)/2
def V_brute(alpha,N,c,nr=500,nphi=6000):
    w=c/N
    pts=np.array([(math.cos(2*j*alpha),math.sin(2*j*alpha)) for j in range(N+1)])
    r=(np.arange(nr)+.5)/nr; phi=(np.arange(nphi)+.5)*2*math.pi/nphi
    R,PH=np.meshgrid(r,phi,indexing='ij'); X=R*np.cos(PH); Y=R*np.sin(PH)
    D=np.full(X.shape,9.)
    for j in range(N):
        A=pts[j];B=pts[j+1];d=B-A;t=np.clip(((X-A[0])*d[0]+(Y-A[1])*d[1])/(d@d),0,1)
        D=np.minimum(D,np.hypot(X-A[0]-t*d[0],Y-A[1]-t*d[1]))
    return 2*(((D>w).mean(axis=1))*r).sum()/nr
def Vtilde(alpha,N,c,nq=4000):
    a=math.cos(alpha);Q=math.sin(alpha)
    th=np.sort(((2*np.arange(N)+1)*alpha)%(2*math.pi)); g=np.diff(np.r_[th,th[0]+2*math.pi])
    q=(np.arange(nq)+.5)/nq*Q
    m=np.array([np.maximum(g-2*c/(N*qq),0).sum() for qq in q])/(2*math.pi)
    return a*a+2*(q*m**2).sum()*Q/nq
for beta,Ns,c in [(lam**2,[34,55,89],2.0),(math.sqrt(2)-1-0.0, [], 2.0),((2**.5-1)*0.9,[40,64,100],2.0),(1/math.pi,[40,64,100],2.0)]:
    if not Ns: continue
    al=math.pi*beta
    for N in Ns:
        vb=V_brute(al,N,c); vt=Vtilde(al,N,c)
        print(f"beta={beta:.4f} N={N} V_brute={vb:.5f} Vtilde={vt:.5f} diff={vb-vt:+.5f}")
