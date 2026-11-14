import sys, random, importlib.util, time
spec=importlib.util.spec_from_file_location("certify","/Users/uiseo/Documents/Circle Research/certify.py")
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
import mpmath as mp
mp.mp.dps=80
lam=(mp.sqrt(5)-1)/2
bad=0
for _ in range(200000):
    p=random.randint(-60,60);q=random.randint(-60,60)
    v=p+q*lam
    t=0 if (p==0 and q==0) else (1 if v>0 else -1)
    if c.sign(p,q)!=t: bad+=1; 
    if bad and bad<4 and c.sign(p,q)!=t: print("sign mismatch",p,q,c.sign(p,q),t)
print("sign mismatches:",bad, "(sign(0,0)=",c.sign(0,0),")")
# frac_point vs mp
for j in list(range(1,3000,7)):
    p,q=c.frac_point(j)
    assert abs((p+q*lam)-mp.frac(j*lam**2))<mp.mpf(10)**-60 and 0<p+q*lam<1,j
print("frac_point ok")
t=time.time(); c.three_gap_exact(600); print("three_gap_exact(600) ok",time.time()-t)
# mutation: wrong count
orig=c.lambda_power
c.lambda_power=lambda n: orig(n+1 if n==5 else n)
try: c.three_gap_exact(200); print("MUTANT1 SURVIVED")
except AssertionError as e: print("mutant1 (wrong gap power) caught")
c.lambda_power=orig
of=c.frac_point
c.frac_point=lambda j:(of(j)[0]+(1 if j==37 else 0),of(j)[1])
try: c.three_gap_exact(200); print("MUTANT2 SURVIVED")
except AssertionError as e: print("mutant2 (perturbed point) caught")
c.frac_point=of
# independent float check of certified_limit vs quad
from scipy import integrate
