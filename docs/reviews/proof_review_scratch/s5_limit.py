import importlib.util, mpmath as mp
spec=importlib.util.spec_from_file_location("certify","/Users/uiseo/Documents/Circle Research/certify.py")
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
mp.mp.dps=c.iv.dps=30
lam=(mp.sqrt(5)-1)/2; al=mp.pi*lam**2; a=mp.cos(al);Q=mp.sin(al);u=mp.pi/(mp.sqrt(5)*lam**2)
def V(x,cc):
    x=mp.mpf(x)
    ell=[u*(1+x)*lam**i for i in range(3)]; f=[(lam-x)/(1+x),(lam**2+x)/(1+x),x/(1+x)]
    M=lambda s: sum(fi*max(e-s,0) for fi,e in zip(f,ell))/mp.pi
    pts=sorted([cc/e for e in ell if cc/e<Q])
    return a*a+2*mp.quad(lambda q:q*M(cc/q)**2,[0]+pts+[Q])
for x in ['0','1/3']:
  for cc in ['1','2']:
    print(x,cc,mp.nstr(V(mp.mpf(eval(x+'.0')) if '/' not in x else mp.mpf(1)/3,mp.mpf(cc)),20), c.certified_limit(x,cc).mid if hasattr(c.certified_limit(x,cc),'mid') else '')
