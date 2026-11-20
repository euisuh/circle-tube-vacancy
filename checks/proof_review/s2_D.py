import sympy as sp
x,s,u,l=sp.symbols('x s u l',positive=True)
lam=(sp.sqrt(5)-1)/2
def M(xx,ss):
    ell=[u*(1+xx)*lam**i for i in range(3)]
    f=[(lam-xx)/(1+xx),(lam**2+xx)/(1+xx),xx/(1+xx)]
    return ell,f
def pos(e): return e  # linear piece
def piece(xx,ss,act):
    ell,f=M(xx,ss); return sum(f[i]*(ell[i]-ss) for i in act)
# pi*M_x on regions: atoms active when s<ell_i. Order for 0<=x<=lam: ell2<=ell1<=ell0 for mu_x; mu_0: ell(0): u l^2<ul<u
rows=[("s<=u l^2(1+x)",[0,1,2],[0,1,2]),
("[ul^2(1+x),ul]",[0,1],[0,1,2]),  # mu_x: atoms 0,1 active ; mu_0: all (u l^2 weight 0 -> use 0,1)
]
# generic: compute piecewise with Piecewise via numeric sample & symbolic by region
def pM(xx,ss):
    ell,f=M(xx,ss)
    return sum(f[i]*sp.Max(ell[i]-ss,0) for i in range(3))
claims=[ # (lo,hi,D expr)
 (0,u*lam**2*(1+x),0),
 (u*lam**2*(1+x),u*lam,x/(1+x)*(s-u*lam**2*(1+x))),
 (u*lam,u*lam*(1+x),lam*(lam-x)*(u*lam-s/(1+x))),
 (u*lam*(1+x),u,x/(1+x)*(1+lam)*(s-u*lam*(1+x))),
 (u,u*(1+x),(lam-x)*(u-s/(1+x))),
 (u*(1+x),u*(1+x)*2,0)]
import random
bad=0
for xv in [0.0,0.05,0.2,0.4,0.6,0.618,sp.Rational(1,3)]:
  for uv in [3.678]:
    for lo,hi,D in claims:
        for t in [0.1,0.5,0.9]:
            subs={x:xv,u:uv}
            lov=float(lo.subs(subs)) if hasattr(lo,'subs') else float(lo)
            hiv=float(hi.subs(subs))
            sv=lov+t*(hiv-lov)
            ssub={x:xv,u:uv,s:sv}
            true=float(pM(x,s).subs(ssub)-pM(0,s).subs(ssub))
            cl=float(D.subs(ssub)) if hasattr(D,'subs') else 0.0
            if abs(true-cl)>1e-9: bad+=1; print("MISMATCH",xv,lov,hiv,sv,true,cl)
print("mismatches",bad)
# exact symbolic check of each claimed row on its own interval (linear -> compare as identities)
def lin(xx,ss,which): pass
ell,f=M(x,s); ell0,f0=M(0,s)
def ident(act_x,act_0,D):
    e=sum(f[i]*(ell[i]-s) for i in act_x)-sum(f0[i]*(ell0[i]-s) for i in act_0)-D
    return sp.simplify(sp.nsimplify(sp.simplify(e)))
print("row1 (s<=ul^2(1+x)): ",ident([0,1,2],[0,1],0))
print("row2:",ident([0,1],[0,1],claims[1][2]))
print("row3:",ident([0,1],[0,1][:2],claims[2][2]) if False else None)
# row3 [ul,ul(1+x)]: mu_x atoms 0,1 active (ell1=ul(1+x)>=s), mu_0 only atom0 (ell0=u): 
print("row3:",ident([0,1],[0],claims[2][2]))
print("row4 [ul(1+x),u]: mu_x atom0 only, mu_0 atom0:",ident([0],[0],claims[3][2]))
print("row5 [u,u(1+x)]: mu_x atom0, mu_0 none:",ident([0],[],claims[4][2]))
# row2 recheck properly: s in [ul^2(1+x), ul]: mu_x active: ell2 =ul^2(1+x)<s so atoms 0,1; mu_0: s<=ul so atoms 0,1 -> 
# breakpoints continuity
for k in range(5):
    a_=claims[k][1]; 
    print("cont at bp",k, sp.simplify(sp.simplify(claims[k][2].subs(s,a_)) - sp.simplify(claims[k+1][2].subs(s,a_))) if hasattr(claims[k][2],'subs') else sp.simplify(0-claims[k+1][2].subs(s,a_)))
# Eell = pi
print("E ell/u =",sp.simplify(sum(fi*ei for fi,ei in zip(f,ell))/u), " u*that-pi:",sp.simplify(u*lam*(1+lam**2)-sp.pi*0) )
ul=sp.pi/(sp.sqrt(5)*lam**2); print(sp.simplify(sp.simplify(sum(fi*ei for fi,ei in zip(f,ell)).subs(u,ul))-sp.pi))
