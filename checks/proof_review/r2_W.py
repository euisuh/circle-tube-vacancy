import numpy as np, math
lam=(5**.5-1)/2
beta=lam**2; al=math.pi*beta; a=math.cos(al);Q=math.sin(al)
def Vd(c):
    if c>=math.pi*Q: return a*a
    return a*a+Q*Q-4*c*Q/math.pi+3*(c/math.pi)**2+2*(c/math.pi)**2*math.log(math.pi*Q/c)
def num(M,c,n=200001):
    q=(np.arange(n)+.5)/n*Q; return a*a+2*(q*M(c/q)**2).sum()*Q/n
for c in [0.3,1,2,3,3.5]:
    print(c,Vd(c),num(lambda s:np.maximum(1-s/math.pi,0),c), "W",num(lambda s:np.maximum(.5-s/math.pi,0)+.5,c))
# N=r q_k+q_{k-1} unbounded numerics
import mpmath as mp
def cfval(cf):
    v=0.0
    for a in reversed(cf): v=1/(a+v)
    return v
cf=[3,1,400,1,1]
beta=cfval(cf+[1]*5); q=[1,3]
for a_ in (cf+[1]*5)[1:]: q.append(a_*q[-1]+q[-2])
print(q[:5])
