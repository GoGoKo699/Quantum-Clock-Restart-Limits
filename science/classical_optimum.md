# The exact classical optimum under restart errors

A classical clock can make its ticks more regular by passing through many stochastic stages. Unobserved errors interrupt that progress. This account solves the resulting optimization over every finite-state continuous-time Markov clock with a bounded nominal escape rate, allowing its number of states and its transition graph to vary.

The rate budget includes the intended tick transition. It excludes the independently imposed error process. If a budget $`\Lambda`$ instead counts nominal event opportunities together with the imposed reset opportunities, use $`\Gamma=\Lambda-\gamma`$, when $`\Lambda>\gamma`$. A constraint counting only changes of the classical state is different: a reset can leave that state unchanged, although its Poisson opportunity still occurs.

## Model and statement

Fix $`\Gamma>0`$ and $`\gamma>0`$. Between ticks, let the nominal clock have a finite transient-state space, a fixed initial distribution $`\alpha`$, internal transition rates $`w_{ij}\geq0`$, and tick rates $`k_i\geq0`$. We use row vectors. Its killed generator $`Q`$ satisfies

```math
Q_{ij}=w_{ij}\quad(i\ne j),\qquad
Q_{ii}=-r_i,\qquad
r_i=k_i+\sum_{j\ne i}w_{ij}\leq\Gamma.
```

A tick restores $`\alpha`$. An independent Poisson process of rate $`\gamma`$ also restores $`\alpha`$, immediately and without a tick or a useful error flag. Every reset redraws the same initial distribution independently. The observed tick intervals are therefore independent copies of a random variable $`T`$. A nominal clock need not tick almost surely, but it must have positive probability of ticking before an error, so the restarted interval has finite moments.

The performance measure is the renewal precision

```math
\mathcal P=\frac{\mathbb E[T]^2}{\mathrm{Var}T}.
```

Write

```math
q=\frac{\Gamma}{\Gamma+\gamma},\qquad b=1-q.
```

**Theorem — unrestricted finite-state classical optimum.** Under these assumptions,

```math
\boxed{
\mathcal P\leq\mathcal P_{\rm C}^{*}(\Gamma/\gamma)
:=\max_{n\in\mathbb N,\ n\geq1}
\frac{(1-q^n)^2}
{1-q^{2n}-2n(1-q)q^n}.
}
```

Every entry of this maximum is attained by a unidirectional $`n`$-stage Erlang clock: all stages, including its last tick transition, have rate $`\Gamma`$. The imposed errors reset it to its first stage. Consequently the bound is the exact optimum over all finite dimensions, transition graphs, state-dependent rates and fixed starting distributions in the model.

In the weak-error limit,

```math
n_{*}\sim\sqrt{\frac{3\Gamma}{\gamma}},\qquad
\boxed{
\mathcal P_{\rm C}^{*}(\Gamma/\gamma)
\sim\frac12\sqrt{\frac{3\Gamma}{\gamma}}.
}
```

This is a result for finite-state Markov clocks. It is not a bound on deterministic classical phase oscillators, on clocks retaining memory across the imposed resets, or on estimators given the internal jump record.

## Restart moments and uniformization

Let $`X`$ be the first nominal tick time, with $`X=\infty`$ on a trajectory that never ticks. Define its possibly defective Laplace transform

```math
\phi(s)=\mathbb E[e^{-sX}],\qquad s>0,
```

where $`e^{-s\infty}=0`$. If $`R`$ is an independent exponential error time of rate $`\gamma`$, the first attempt either ticks at $`X<R`$ or restarts at $`R<X`$. This renewal decomposition gives

```math
\mathbb E[e^{-sT}]
=\phi(s+\gamma)
+\frac{\gamma[1-\phi(s+\gamma)]}{s+\gamma}
\mathbb E[e^{-sT}]
=\frac{(s+\gamma)\phi(s+\gamma)}
{s+\gamma\phi(s+\gamma)}.
```

Differentiating at $`s=0`$ yields the standard Poisson-restart identities

```math
\mu:=\mathbb E[T]
=\frac{1-\phi(\gamma)}{\gamma\phi(\gamma)},\qquad
\mathbb E[T^2]
=\frac{2[1-\phi(\gamma)+\gamma\phi'(\gamma)]}
{\gamma^2\phi(\gamma)^2}.
```

They remain valid for a defective nominal distribution. Indeed $`0<\phi(\gamma)<1`$ and the exponentially weighted derivatives are finite, even if an unweighted nominal moment diverges. Equivalently, a positive-probability successful attempt and independent restarts give a geometric number of attempts with exponentially controlled durations.

Uniformize the killed chain at rate $`\Gamma`$. The substochastic transition matrix is $`U=I+Q/\Gamma`$, and absorption is the tick. Self-loops supply the unused portion of the rate budget. If $`K\in\{1,2,\ldots,\infty\}`$ is the absorption-step count, then

```math
X=\sum_{j=1}^{K}E_j,\qquad
E_j\overset{\rm iid}{\sim}{\rm Exp}(\Gamma),
```

with the holding times independent of the embedded chain. Therefore, with the conventions $`q^\infty=0`$ and $`\infty q^\infty=0`$,

```math
p:=\phi(\gamma)=\mathbb E[q^K],\qquad
h:=\mathbb E[Kq^K],\qquad
\phi'(\gamma)=-\frac{h}{\Gamma+\gamma}.
```

The mean and squared coefficient of variation become

```math
\mu=\frac{1-p}{\gamma p},\qquad
\mathrm{CV}(T)^2
=\frac{1-p^2-2bh}{(1-p)^2}.
```

In particular $`0<p\leq q`$, so an attainable observed mean must satisfy $`\mu\geq\Gamma^{-1}`$. No assumption on reversibility, detailed balance or the number of states entered this reduction.

## The exact frontier at a fixed observed mean

Fix $`\mu\geq\Gamma^{-1}`$, equivalently $`p=(1+\gamma\mu)^{-1}\in(0,q]`$. Minimizing the variance is equivalent to maximizing $`h`$. On $`[0,q]`$ define

```math
g(y)=-\frac{y\log y}{\ell},\qquad
\ell=-\log q=\log(1+\gamma/\Gamma),\qquad g(0)=0.
```

Then $`g(q^j)=jq^j`$ and $`g''(y)=-1/(\ell y)<0`$ for $`y>0`$. Let $`\bar g`$ linearly interpolate these values on each interval $`[q^{j+1},q^j]`$, with $`\bar g(0)=0`$. The chord slopes are decreasing as $`y`$ increases, so $`\bar g`$ is concave. Since $`Y=q^K`$ lies on the interpolation grid,

```math
h=\mathbb E[\bar g(Y)]\leq\bar g(\mathbb E[Y])=\bar g(p).
```

Choose the integer $`n\geq1`$ for which $`q^{n+1}\leq p\leq q^n`$. Then

```math
h\leq h_{\max}(p)=A_np+B_n,
\qquad
A_n=n-\frac{q}{1-q},\qquad
B_n=\frac{q^{n+1}}{1-q}.
```

Thus the exact minimum squared coefficient of variation at this observed mean is

```math
\boxed{
V_{\rm C}(p)
=\frac{1-p^2-2b(A_np+B_n)}{(1-p)^2}.
}
```

Equality requires $`K`$ to be supported on the adjacent integers $`n,n+1`$, apart from a redundant zero-weight endpoint. It is attainable: use one $`(n+1)`$-stage rate-$`\Gamma`$ ladder, initialized at its first or second stage with the probabilities

```math
\Pr(K=n)=\lambda
=\frac{p-q^{n+1}}{q^n-q^{n+1}},\qquad
\Pr(K=n+1)=1-\lambda.
```

Both the tick and the imposed error restore this same initial mixture. Alternatively, a pure initial state and a probabilistic first-step skip implement the same absorption-step distribution. Hence the fixed-mean statement does not depend on allowing a mixed initial condition.

The concavity argument also covers nominal trajectories with $`K=\infty`$. They cannot improve this frontier: equality at positive $`p`$ uses the neighboring finite absorption counts.

## Why a pure Erlang clock is globally optimal

It remains to optimize the observed mean. On a fixed interpolation interval put $`A=A_n`$, $`B=B_n`$ and $`C=1-2bB`$. The best attainable precision there is

```math
F(p)=\frac{(1-p)^2}{C-2bAp-p^2}.
```

Its denominator is positive, since it is the variance numerator of the explicitly constructed clock. Differentiation gives

```math
F'(p)
=\frac{2(1-p)[(bA+1)p+bA-C]}
{(C-2bAp-p^2)^2},\qquad
bA+1=(n+1)b>0.
```

The bracket increases strictly with $`p`$. Any interior stationary point is therefore a minimum. The maximum on the interval occurs at $`p=q^n`$ or $`p=q^{n+1}`$, corresponding to a pure Erlang clock. This proves the theorem's integer maximum.

The maximum is attained at a finite $`n`$. The $`n=1`$ clock has precision one, every $`n>1`$ gives a value strictly larger than one, and the expression converges to one as $`n\to\infty`$ for fixed $`q<1`$.

## Locating the optimizer and controlling all scales

For stable evaluation and asymptotics, set

```math
\ell=\log(1+\gamma/\Gamma),\qquad
c=\frac{1-q}{\ell}\in(0,1),\qquad z=n\ell.
```

The pure Erlang precision is

```math
\mathcal P_n=\frac{\cosh z-1}{\sinh z-cz}.
```

Treating $`z>0`$ as continuous, its derivative has the sign of

```math
(1+c)(\cosh z-1)-cz\sinh z.
```

There is exactly one positive stationary point $`z_*`$, characterized by

```math
\boxed{\frac{\tanh(z_*/2)}{z_*}=\frac{c}{1+c}.}
```

The left side decreases strictly from $`1/2`$ to zero. The derivative is positive below $`z_*`$ and negative above it. Also $`z_*>\ell`$: substituting $`z=\ell`$ into the derivative condition reduces positivity to $`1-q>q\ell`$, or $`e^\ell-1>\ell`$.

Consequently the exact integer optimizer is one of

```math
n\in\{\lfloor z_*/\ell\rfloor,\ \lceil z_*/\ell\rceil\}.
```

Evaluating those two integers settles any tie. This unimodality controls every scale of $`n`$; a large-$`n`$ branch cannot evade the weak-error asymptotic optimum.

Let $`a=\gamma/\Gamma\to0`$. Then

```math
\ell\sim a,\qquad 1-c\sim a/2,
\qquad
\frac{\tanh(z/2)}{z}=\frac12-\frac{z^2}{24}+O(z^4).
```

The unique optimizer equation implies $`z_*\sim\sqrt{3a}`$ and $`n_*\sim\sqrt{3/a}`$. Substituting into

```math
\mathcal P_n
=\frac{z^2/2+O(z^4)}
{(1-c)z+z^3/6+O(z^5)}
```

gives $`\mathcal P_{\rm C}^{*}\sim\sqrt{3/a}/2`$. Integer rounding changes $`z`$ by at most $`\ell=O(a)`$, a vanishing fraction of $`z_*`$, so it does not change the leading constant.

## Relation to the universal restart floor

Dropping the discrete grid and applying Jensen directly to $`g`$ yields the convenient smooth relaxation

```math
\mathrm{CV}(T)^2
\geq\frac{1-p^2+2c\,p\log p}{(1-p)^2}.
```

For $`x=\gamma\mu`$ this is the universal, physics-independent restart floor, plus the nonnegative classical contribution

```math
\frac{(1-c)(-2p\log p)}{(1-p)^2}.
```

In the optimal weak-error regime, $`x\asymp\sqrt a`$, their leading terms are respectively $`x/3`$ and $`a/x`$. Both matter: retaining only either contribution loses the sharp classical constant or the optimization itself.

## Finite verification and its boundary

The reproducible scientific check `verification/check_classical.py` uses NumPy and SciPy. It compares killed-generator first-passage moments directly with the restart transform; checks the exact fixed-mean frontier against generators with adjacent and nonadjacent Erlang lengths; includes a defective nominal clock; compares the two-candidate optimizer with a wide integer scan; and checks the weak-error constants. Random graphs use a fixed seed. These finite checks target algebra, rate accounting and boundary cases. The arbitrary-dimension conclusion follows from the proof above, not from the random sample.
