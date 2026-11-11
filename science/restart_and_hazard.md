# Restart noise and the sharp bounded-hazard envelope

The complete-reset interface in the [model](model.md) makes each intertick interval a first-passage process subject to independent Poisson restart. The renewal identities below are inherited from stochastic-restart theory. The fixed-noisy-mean optimization then gives a sharp envelope for every intrinsic tick distribution with bounded hazard. Its optimizing distribution is a delayed exponential; that relaxed optimizer is not assumed to be a finite autonomous quantum clock.

## Notation and regularity

Let $`X`$ be the intrinsic first-tick time from the reset state, before the additional faults are imposed. Allow $`X=\infty`$ on unsuccessful intrinsic paths, with $`e^{-s\infty}=0`$ for $`s>0`$. Each unobserved fault restores the same complete reset state and starts an independent copy of $`X`$. Fault times form a Poisson process of rate $`\gamma>0`$ and never count as ticks. Write $`T`$ for the resulting actual intertick time and

```math
\phi(s)=\mathbb E[e^{-sX}],\qquad
p=\phi(\gamma)>0,\qquad
b=\mathbb E[Xe^{-\gamma X}]=-\phi'(\gamma).
```

The condition $`p>0`$ excludes a clock that never ticks. It also guarantees that $`T`$ has an exponential tail: choose a finite $`a`$ with $`\Pr(X\le a)>0`$. From every unfinished state, an interval of length $`a+1`$ has a fixed positive probability of containing a fault in its first unit of time, followed by no fault and an intrinsic tick during the next $`a`$ units. Repeating this bound gives a geometric tail on fixed-length intervals. Thus all moments of $`T`$ used below exist, even when the intrinsic distribution has a defective or heavy tail.

Use the actual noisy mean $`\mu=\mathbb E T`$, variance $`\sigma^2=\mathrm{Var}T`$, and tick precision

```math
P=\frac{\mu^2}{\sigma^2},\qquad
R=\frac{\Gamma}{\gamma},\qquad
r=\frac{\gamma}{\Gamma}=R^{-1},\qquad
x=\gamma\mu.
```

The intrinsic hazard assumption is $`0\le h_0(t)\le\Gamma`$ almost everywhere. Equivalently, its survival $`S(t)=\Pr(X>t)`$ is locally absolutely continuous, $`S(0)=1`$, and $`-S'(t)\le\Gamma S(t)`$. A finite-rate clock has no atom at zero. The bounded hazard permits noncompletion at infinity.

## Exact renewal transform and moments

Let $`F_\gamma(s)=\mathbb E[e^{-sT}]`$. Conditioning on whether the intrinsic tick or the first reset occurs first gives

```math
F_\gamma(s)
=\phi(s+\gamma)
+\frac{\gamma[1-\phi(s+\gamma)]}{s+\gamma}
F_\gamma(s).
```

The first term describes a successful attempt. The coefficient of the second term is $`\mathbb E[e^{-sE}\mathbf 1_{E\lt X}]`$ for $`E\sim\mathrm{Exp}(\gamma)`$, after which the completion process starts afresh. Solving yields

```math
\begin{aligned}
F_\gamma(s)
&=\frac{(s+\gamma)\phi(s+\gamma)}
       {s+\gamma\phi(s+\gamma)}.
\qquad\text{(R1)}
\end{aligned}
```

Differentiating at zero gives

```math
\begin{aligned}
\mu&=\frac{1-p}{\gamma p},\\
\mathbb E[T^2]
&=\frac{2(1-p-\gamma b)}{\gamma^2p^2}.
\qquad\text{(R2)}
\end{aligned}
```

and consequently

```math
\begin{aligned}
\sigma^2
&=\frac{1-p^2-2\gamma b}{\gamma^2p^2},\\
\frac1P
&=\frac{1-p^2-2\gamma b}{(1-p)^2}.
\qquad\text{(R3)}
\end{aligned}
```

In particular, fixing $`\mu`$ fixes $`p=1/(1+x)`$. At that fixed mean, minimizing the noisy variance is exactly the problem of maximizing $`b`$.

Equations (R1)–(R3) are standard Poisson-restart identities. The general first-passage framework is due to [Pal and Reuveni](https://doi.org/10.1103/PhysRevLett.118.030603); related moment and restart-optimization identities appear in [Reuveni's earlier work](https://doi.org/10.1103/PhysRevLett.116.170601). Their result that the coefficient of variation equals one at an interior **mean-optimal restart rate** does not solve the present optimization: here $`\gamma`$ is an imposed fault rate and the clock design is optimized for precision.

## A distribution-only restart floor

Set $`Y=e^{-\gamma X}`$, including $`Y=0`$ on noncompletion. Convexity of $`y\ln y`$ on $`[0,1]`$ gives

```math
-\gamma b=\mathbb E[Y\ln Y]\ge p\ln p.
```

Substitution into (R3) yields

```math
\begin{aligned}
\frac1P&\ge f(x),\\
f(x)&=\frac{x^2+2x-2(1+x)\ln(1+x)}{x^2}.
\qquad\text{(R4)}
\end{aligned}
```

Equality holds for a deterministic intrinsic delay. This is a relaxed distributional equality condition, without a bounded-hazard requirement.

The numerator $`A(x)`$ in (R4) satisfies $`A(0)=A'(0)=0`$ and $`A''(x)=2x/(1+x)`$. Therefore

```math
\begin{aligned}
A(x)&=2\int_0^x\frac{(x-u)u}{1+u}\,du\\
&\ge\frac{x^3}{3(1+x)},\\
f(x)&\ge\frac{x}{3(1+x)}.
\qquad\text{(R5)}
\end{aligned}
```

At small $`x`$, $`f(x)=x/3+O(x^2)`$; at large $`x`$, it tends to one. Even a perfectly periodic intrinsic clock therefore suffers a nonzero variance penalty from unobserved resets.

## Sharp envelope at a fixed actual mean

**Theorem R1 — fixed-mean hazard envelope.** Suppose the intrinsic hazard is at most $`\Gamma`$. Then $`x\ge r`$ and

```math
\begin{aligned}
\frac1P&\ge G_r(x),\\
G_r(x)&=1+\frac2x\\
&\quad-\frac{2(1+x)}{x^2}
\left[
\ln\!\left(\frac{1+x}{1+r}\right)
+\frac{r}{1+r}
\right].
\qquad\text{(R6)}
\end{aligned}
```

For every $`x\ge r`$, equality is attained among bounded-hazard waiting distributions by

```math
\begin{aligned}
X_*&=\tau+E,\\
E&\sim\mathrm{Exp}(\Gamma),\\
\tau&=\frac1\gamma
\ln\!\left(\frac{1+x}{1+r}\right).
\qquad\text{(R7)}
\end{aligned}
```

Except for equality almost everywhere of the survival functions, this fixed-mean optimizer is unique.

**Proof.** Since $`h_0\le\Gamma`$, $`S(t)\ge e^{-\Gamma t}`$. Thus

```math
p=1-\gamma\int_0^\infty e^{-\gamma t}S(t)\,dt
\le\frac{\Gamma}{\Gamma+\gamma}
=\frac1{1+r}.
```

Together with $`p=1/(1+x)`$, this proves $`x\ge r`$ and makes the delay in (R7) nonnegative. The proposed survival is

```math
S_*(t)=
\begin{cases}
1,&0\le t\le\tau,\\
e^{-\Gamma(t-\tau)},&t>\tau.
\end{cases}
```

Its Laplace transform is $`p=e^{-\gamma\tau}/(1+r)`$, so it has the required actual noisy mean.

Compare any other feasible survival $`S`$ at the same $`p`$. Before $`\tau`$, $`S-S_*\le0`$. After $`\tau`$, the ratio $`S/S_*`$ is nondecreasing, since its logarithmic derivative is $`\Gamma-h_0(t)\ge0`$. Consequently $`S-S_*`$ can change sign at most once, from negative to positive. The equal-Laplace-transform condition says

```math
\begin{aligned}
\int_0^\infty e^{-\gamma t}[S(t)-S_*(t)]\,dt&=0.
\qquad\text{(R8)}
\end{aligned}
```

Integration by parts also gives

```math
b=\int_0^\infty e^{-\gamma t}(1-\gamma t)S(t)\,dt.
```

The additional weight $`1-\gamma t`$ is strictly decreasing. A signed function with the single-crossing property and the zero weighted integral in (R8) has nonpositive integral against that additional decreasing weight. Hence $`b\le b_*`$. If the two survivals differ on a set of positive measure, the inequality is strict. This proves optimality and uniqueness.

For (R7),

```math
b_*=p\left(\tau+\frac1{\Gamma+\gamma}\right).
```

Substitution into (R3) gives (R6). ∎

This theorem bounds a larger class than finite autonomous quantum clocks: it allows an exactly deterministic waiting segment followed by an exponential trigger. It is a sharp upper bound for the physical clock class, but does not establish physical attainability of its constant.

## Unique optimum of the relaxed precision envelope

Define

```math
K(r)=\ln(1+r)-\frac{r}{1+r},\qquad
h(x)=\ln(1+x)-\frac{2x}{x+2}.
```

For each $`r>0`$, there is a unique $`x_P>r`$ satisfying

```math
\begin{aligned}
h(x_P)&=K(r).
\qquad\text{(R9)}
\end{aligned}
```

Indeed,

```math
h'(x)=\frac{x^2}{(1+x)(x+2)^2}>0,
\qquad
K(r)-h(r)=\frac{r^2}{(r+1)(r+2)}>0,
```

and $`h(x)\to\infty`$. Direct differentiation gives

```math
G_r'(x)
=\frac{2(x+2)}{x^3}[h(x)-K(r)].
```

Thus $`x_P`$ is the unique global minimum. Using (R9) in (R6),

```math
\begin{aligned}
\min_{x\ge r}G_r(x)&=\frac{x_P}{x_P+2},\\
P_{\rm hazard}(r)&=1+\frac2{x_P}.
\qquad\text{(R10)}
\end{aligned}
```

Here $`P_{\rm hazard}`$ denotes the relaxed bounded-hazard optimum, not the proved optimum of finite quantum clocks.

As $`r\downarrow0`$,

```math
K(r)=\frac{r^2}{2}+O(r^3),\qquad
h(x)=\frac{x^3}{12}+O(x^4),
```

so

```math
\begin{aligned}
x_P&\sim 6^{1/3}r^{2/3},\\
\min G_r&\sim\frac{3}{6^{2/3}}r^{2/3},\\
P_{\rm hazard}(r)
&\sim\frac{6^{2/3}}3R^{2/3}.
\qquad\text{(R11)}
\end{aligned}
```

The finite-quantum construction establishes the same logarithmic exponent, not this asymptotic constant. Its source transfer is developed in the [quantum construction](quantum_construction.md). The stricter [classical rate budget](classical_optimum.md) supplies a different, square-root precision optimum: a tick-hazard bound alone would allow arbitrarily fast hidden classical stages and would not establish that separation.

## The inherited accuracy-resolution bound

The actual noisy tick hazard also remains at most $`\Gamma`$: the conditional tick intensity is the expectation of the bounded tick effect in the normalized no-tick state, while faults merely change that state. Therefore

```math
\begin{aligned}
\mathrm{Var}T&\ge\Gamma^{-2},\\
P&\le(\Gamma\mu)^2.
\qquad\text{(R12)}
\end{aligned}
```

One direct proof writes $`T=H^{-1}(E)`$, where $`E\sim\mathrm{Exp}(1)`$ and $`H`$ is the actual cumulative hazard. The hazard cap implies

```math
H^{-1}(v)-H^{-1}(u)\ge\frac{v-u}{\Gamma}
\quad(v\ge u).
```

For independent copies $`T,T'`$ and $`E,E'`$,

```math
\mathrm{Var}T
=\frac12\mathbb E[(T-T')^2]
\ge\frac1{2\Gamma^2}\mathbb E[(E-E')^2]
=\Gamma^{-2}.
```

This is the established decay-rate accuracy-resolution obstruction of [Meier et al.](https://doi.org/10.1103/PhysRevLett.131.220201). Equation (R6) adds the sharp imposed-restart penalty; it does not reattribute (R12).

## Stability using only the first two intrinsic moments

**Lemma R2 — second-moment transfer.** Suppose $`\mu_0=\mathbb E X\lt\infty`$, $`c_0=\mathrm{Var}X/\mu_0^2\le1`$, and $`z=\gamma\mu_0\le1/4`$. Then

```math
\begin{aligned}
\mu_0\left[1-\frac{z(1+c_0)}2\right]&\le\mu,\\
\mu&\le\frac{\mu_0}{1-z}.
\qquad\text{(R13)}
\end{aligned}
```

and

```math
\begin{aligned}
\frac{\mathrm{Var}T}{\mu^2}
&\le c_0+40z.
\qquad\text{(R14)}
\end{aligned}
```

**Proof.** The elementary inequalities $`e^{-u}\ge1-u`$ and $`1-e^{-u}\ge u-u^2/2`$ imply

```math
p\ge1-z,\qquad
1-p\le z,\qquad
1-p\ge z-\frac{\gamma^2\mathbb E X^2}{2}.
```

Insert these inequalities into the mean formula (R2), using $`p\le1`$ for the lower bound. This gives (R13). In particular, $`\mu\ge\mu_0(1-z)`$.

Also $`1-(1+u)e^{-u}\le u^2/2`$ for $`u\ge0`$. Equation (R2) therefore gives

```math
\mathbb E T^2
=\frac{2\mathbb E[1-(1+\gamma X)e^{-\gamma X}]}
       {\gamma^2p^2}
\le\frac{\mathbb E X^2}{p^2}.
```

Combining this with the mean lower bound,

```math
1+\frac{\mathrm{Var}T}{\mu^2}
\le\frac{1+c_0}{(1-z)^4}.
```

On $`0\le z\le1/4`$, convexity and the secant bound give $`(1-z)^{-4}\le1+20z`$. Since $`1+c_0\le2`$, (R14) follows. ∎

No intrinsic third-moment bound or uniform tail expansion is used. If $`z\to0`$ and $`c_0`$ stays bounded, (R13) also proves $`\mu/\mu_0\to1`$. This is the mean control needed when converting clean quasiideal clocks into the reset-noisy family and when accounting for actual elapsed time in [timing diffusion](timing_diffusion.md).
