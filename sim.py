#!/usr/bin/env python3
"""Audit AR18's static wage decomposition. Sources: NBER June 2017,
Prop. 2 pp. 11-12, Prop. 3 pp. 12-14, equations B9-B10 p. B-13.
Own specialization: eta=0, B=1, gamma(i)=exp(A*i), nu(L)=L**2/2.
No empirical calibration and no claim to verify the dynamic equilibrium.
"""
from pathlib import Path
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'ar18-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import sympy as sp
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parent
FIG_DIR = ROOT / 'extra' / 'figures'
VIOLET, CYAN, ROSE, AMBER = '#6D28D9', '#0E7490', '#E11D48', '#F59E0B'


def symbolic_checks():
    x,z,P,lam,s,eps,sl = sp.symbols('x z P Lambda s epsilon sL', real=True)
    sol=sp.solve([sl*x+(1-sl)*z-P, x-z+lam/(s+eps)], [x,z])
    assert sp.simplify(sol[x]-(P-(1-sl)*lam/(s+eps))) == 0
    assert sp.simplify(sol[z]-(P+sl*lam/(s+eps))) == 0
    PN,LN=sp.symbols('PN LambdaN', real=True)
    reinst=sp.solve([sl*x+(1-sl)*z-PN,x-z-LN/(s+eps)],[x,z])
    assert sp.simplify(reinst[x]-PN-(1-sl)*LN/(s+eps)) == 0
    # Positive W preserves the sign: solve the zero boundary exactly.
    assert sp.solve(sol[x], P)[0] == (1-sl)*lam/(s+eps)
    W,R,B,gamma=sp.symbols('W R B gamma', positive=True)
    pi=B**(s-1)*((W/gamma)**(1-s)-R**(1-s))/(1-s)
    assert sp.simplify(sp.limit(pi,s,1)-sp.log(W/(R*gamma))) == 0
    # Independently differentiate the closed-form Cobb-Douglas specialization.
    I,K,A=sp.symbols('I K A', positive=True)
    n=1-I
    q=K*sp.sqrt(n)/I
    logw=sp.log(B)+I*sp.log(q)+A*(1-I**2)/2
    dlogw=sp.diff(logw,I)
    expected=sp.log(q)-A*I-(1+n)/(2*n)
    assert sp.simplify(dlogw-expected) == 0
    kcrit=I/sp.sqrt(n)*sp.exp(A*I+(1+n)/(2*n))
    # Derivative at the symbolic threshold, evaluated in the declared I in (0,1).
    qcrit=sp.exp(A*I+(1+n)/(2*n))
    assert sp.simplify(q.subs(K,kcrit)-qcrit) == 0
    n0=sp.symbols('n0', positive=True)
    assert sp.simplify(sp.log(qcrit.subs(I,1-n0))-A*(1-n0)-(1+n0)/(2*n0)) == 0
    assert sp.simplify(sp.diff(dlogw,K)-1/K) == 0
    # Frontier nonempty iff A*n > (1+n)/(2*n).
    assert sp.simplify((A-(A*I+(1+n)/(2*n)))-(A*n-(1+n)/(2*n))) == 0
    # Labor supply from the actual household FOC, not an exogenous L shortcut.
    l=sp.symbols('L',positive=True)
    omega=l/(1-l*l)
    elastic=sp.simplify(omega/(l*sp.diff(omega,l)))
    assert sp.simplify(elastic-(1-l*l)/(1+l*l)) == 0
    assert sp.simplify(omega*l/(1+omega*l)-l*l) == 0
    # Student's handwritten specialization: fixed L, eta=0, B=1.
    a,b=sp.symbols('a b', positive=True)
    fixed_productivity=(a-b)/(1-s)
    fixed_wage=(fixed_productivity-a/sl)/s
    fixed_share=-((1-sl)*a/sl+b)/s
    assert sp.simplify(fixed_wage-fixed_productivity-fixed_share) == 0
    # With gamma_K=1, b=(1-sl)/(I-N+1), a/sl=gamma(I)^(s-1)/H.
    fixed_lambda=a/sl+b/(1-sl)
    assert sp.simplify(fixed_wage-(fixed_productivity-(1-sl)*fixed_lambda/s)) == 0
    pL,pK=sp.symbols('pL pK', positive=True)
    assert sp.simplify(sp.limit((pL**(1-s)-pK**(1-s))/(1-s),s,1)-sp.log(pL/pK)) == 0
    print('Handwritten fixed-L audit: PASS (wage, labor share, general-form equivalence, sigma=1 limit)')
    print('SymPy: PASS (B9-B10, reinstatement, sigma=1 limit, exact K threshold, household supply)')
    print('Domains: W,R,B,gamma>0; 0<sL<1; s,epsilon>0; 0<I<1 in the closed form.')


def forced_allocation(J,K,N=1.0,s=1.5,A=2.0,B=1.0):
    """Prices conditional on effective threshold J; checks adoption separately."""
    a=J-N+1.0
    if not (0<a<1 and K>0 and s>0 and A>0):
        raise ValueError('Interior positive domain required')
    if abs(s-1)<1e-8:
        H=N-J
    else:
        t=A*(s-1)
        H=np.exp(t*J)*np.expm1(t*(N-J))/t
    logq=lambda L:(np.log(H/a)+np.log(K/L))/s
    L=brentq(lambda l:logq(l)-np.log(K)-np.log(l/(1-l*l)),1e-12,1-1e-12,xtol=1e-14)
    q=np.exp(logq(L))
    if abs(s-1)<1e-8:
        logR=np.log(B)-(N-J)*np.log(q)+A*(N*N-J*J)/2
    else:
        logR=np.log(B)+np.log(a+H*q**(1-s))/(s-1)
    R=np.exp(logR); W=q*R
    Y=R*K+W*L
    share=W*L/Y
    epsilon=(1-L*L)/(1+L*L)
    lamI=np.exp(A*J*(s-1))/H+1/a
    lamN=np.exp(A*N*(s-1))/H+1/a
    if abs(s-1)<1e-8:
        PI=np.log(q)-A*J; PN=A*N-np.log(q)
    else:
        PI=B**(s-1)*R**(1-s)*np.expm1((1-s)*(np.log(q)-A*J))/(1-s)
        PN=-B**(s-1)*R**(1-s)*np.expm1((1-s)*(np.log(q)-A*N))/(1-s)
    DI=(1-share)*lamI/(s+epsilon)
    RN=(1-share)*lamN/(s+epsilon)
    residual=abs(q/K-L/(1-L*L))
    return dict(J=J,K=K,N=N,s=s,A=A,B=B,H=H,a=a,L=L,W=W,R=R,Y=Y,q=q,
                share=share,epsilon=epsilon,PI=PI,DI=DI,PN=PN,RN=RN,
                slope=PI-DI,share_slope=-share*(1-share)*(1+epsilon)*lamI/(s+epsilon),
                residual=residual,valid=np.exp(A*J)<q<np.exp(A*N))


def free_threshold(K,N=1.0,s=1.5,A=2.0,B=1.0):
    return brentq(lambda j:np.log(forced_allocation(j,K,N,s,A,B)['q'])-A*j,
                  N-1+1e-7,N-1e-7,xtol=1e-13)


def equilibrium(I,K,N=1.0,s=1.5,A=2.0,B=1.0,Jfree=None):
    if Jfree is None:Jfree=free_threshold(K,N,s,A,B)
    d=forced_allocation(min(I,Jfree),K,N,s,A,B)
    d['binding']=I<Jfree
    if not d['binding']:
        d['slope']=d['share_slope']=0.0
    return d


def numerical_checks():
    maxerr=0.0
    # Finite differences solve the equilibrium anew on both sides.
    for s,K,I in [(1.5,1,.1),(1.5,1,.3),(1,.5,.1),(.7,.5,.12)]:
        d=equilibrium(I,K,s=s)
        assert d['binding'] and d['valid'],(s,K,I,d)
        h=1e-6
        left,right=equilibrium(I-h,K,s=s),equilibrium(I+h,K,s=s)
        fd=(np.log(right['W'])-np.log(left['W']))/(2*h)
        fs=(right['share']-left['share'])/(2*h)
        maxerr=max(maxerr,abs(fd-d['slope']),abs(fs-d['share_slope']))
        assert abs(fd-d['slope'])<2e-7
        assert abs(fs-d['share_slope'])<2e-7
        # N derivative at fixed I,K, accounting for moving lower endpoint N-1.
        left,right=equilibrium(I,K,N=1-h,s=s),equilibrium(I,K,N=1+h,s=s)
        fn=(np.log(right['W'])-np.log(left['W']))/(2*h)
        assert abs(fn-d['PN']-d['RN'])<2e-7
        assert d['residual']<1e-10
        assert abs(d['share']-d['L']**2)<1e-10
        assert d['PI']>0 and d['DI']>0 and d['PN']>0
        print(f's={s:g}, K={K:g}, I={I:g}: W={d["W"]:.8f}, sL={d["share"]:.8f}, '
              f'P={d["PI"]:.8f}, D={d["DI"]:.8f}, dlnW/dI={d["slope"]:.8f}')
    d=equilibrium(.8,1)
    assert not d['binding']
    assert abs(equilibrium(.8001,1)['W']-d['W'])<1e-12
    turn=brentq(lambda i:forced_allocation(i,1)['slope'],.1,.3)
    stop=free_threshold(1)
    assert forced_allocation(turn,1)['valid']
    print(f'Numerical residual/finite-difference checks: PASS; maximum checked error={maxerr:.3e}')
    print(f'Default: B=1, eta=0, sigma=1.5, A=2, N=1, K=1, theta=1, nu=L^2/2')
    print(f'Wage turning point I={turn:.8f}; adoption threshold I*={stop:.8f}')
    return turn,stop


def figures(turn,stop):
    xs=np.linspace(.1,.8,300)
    ds=[equilibrium(i,1,Jfree=stop) for i in xs]
    assert all(d['q']<np.exp(2) for d in ds)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titleweight':'bold'})
    fig,ax=plt.subplots(2,2,figsize=(12,7.2),layout='constrained')
    for panel,key,title,label in [(ax[0,0],'W','Salario real: primero sube, luego cae',r'$W$'),
                                  (ax[0,1],'share','Participación laboral: cae hasta la meseta',r'$s_L$')]:
        vals=np.array([d[key] for d in ds])
        panel.plot(xs,vals,color=VIOLET if key=='W' else CYAN,lw=2.5)
        panel.axvspan(.1,turn,color=AMBER,alpha=.2,label='Tramo con salario creciente')
        panel.axvline(stop,color=ROSE,ls='--',lw=1.4,label=r'$I=\widetilde I$')
        panel.set(title=title,xlabel=r'Frontera tecnológica $I$',ylabel=label)
        panel.legend(fontsize=8,loc='best')
    bs=np.linspace(.1,stop-1e-4,220)
    bd=[forced_allocation(i,1) for i in bs]
    ax[1,0].plot(bs,[d['PI'] for d in bd],color=CYAN,lw=2,label=r'Productividad $P_I$')
    ax[1,0].plot(bs,[d['DI'] for d in bd],color=ROSE,lw=2,label=r'Desplazamiento $D_I$')
    ax[1,0].axvline(turn,color=VIOLET,ls=':',label=f'Igualdad en I={turn:.3f}')
    ax[1,0].set(title='La bisagra: productividad frente a desplazamiento',xlabel=r'$I$ (solo régimen vinculante)',ylabel='Cambio logarítmico por unidad de I')
    ax[1,0].legend(fontsize=8)
    ix=np.linspace(.06,.55,130);ks=np.linspace(.12,3.2,110)
    values=np.full((len(ks),len(ix)),np.nan)
    for row,k in enumerate(ks):
        for col,i in enumerate(ix):
            d=forced_allocation(i,k)
            if d['valid']: values[row,col]=d['slope']
    colors=ListedColormap(['#F7D9E0','#DDD1F7'])
    masked=np.ma.masked_invalid(values)
    ax[1,1].contourf(ix,ks,masked,levels=[-100,0,100],cmap=colors)
    ax[1,1].contour(ix,ks,masked,levels=[0],colors=[VIOLET],linewidths=1.8)
    ax[1,1].axhline(1,color=CYAN,ls='--',lw=1.2)
    ax[1,1].text(.09,2.9,'Violeta: salario sube',fontsize=9,color=VIOLET)
    ax[1,1].text(.33,1.6,'Rosa: salario cae',fontsize=9,color=ROSE)
    ax[1,1].text(.32,.25,'Blanco: fuera del régimen',fontsize=8,color='#14121F')
    ax[1,1].set(title='Frontera P = D en parámetros (I, K)',xlabel=r'$I$',ylabel=r'Capital $K$')
    for panel in ax.flat:
        panel.spines[['top','right']].set_visible(False)
        panel.grid(alpha=.15)
    fig.suptitle('Un salario creciente puede coexistir con menor participación laboral',fontsize=15,color=VIOLET,weight='bold')
    fig.supxlabel('Ejemplo propio: eta = 0, sigma = 1.5, gamma(i) = exp(2i), N = 1; K = 1 salvo el mapa. Oferta endógena.',fontsize=9)
    FIG_DIR.mkdir(parents=True,exist_ok=True)
    for extension in ['pdf','png']:
        fig.savefig(FIG_DIR/f'displacement-productivity.{extension}',dpi=200)
    plt.close(fig)
    print('Figures regenerated: extra/figures/displacement-productivity.pdf and .png')


if __name__=='__main__':
    symbolic_checks()
    figures(*numerical_checks())
