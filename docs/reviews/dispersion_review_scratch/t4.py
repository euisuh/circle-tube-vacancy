import numpy as np
phi=(5**.5-1)/2
def disp(beta,lo,hi,step=1):
    best=0;bc=0
    for N in range(lo,hi,step):
        x=np.sort(np.mod(np.arange(1,N+1)*beta,1.0))   # interval version, points n*beta, n=1..N
        d=max(x[0],1-x[-1],np.max(np.diff(x))/2 if N>1 else 0)
        best=max(best,N*d)
        g=np.diff(np.append(x,x[0]+1)).max(); bc=max(bc,N*g)
    return best,bc
print("golden interval sup N d_N, circ sup N*maxgap over N in [4181,6765):",disp(phi,4181,6765,1),"targets",(1+3/5**.5)/2,1+2/5**.5)
