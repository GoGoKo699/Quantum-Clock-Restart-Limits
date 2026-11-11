# Accuracy of an elapsed-time estimate

Higher tick regularity can be obtained by increasing the mean tick period, so precision alone does not answer how well a clock estimates elapsed time. In the complete-reset model, a calibrated tick count gives an operational answer that includes every unsuccessful attempt and every unobserved reset. The quantum advantage survives this accounting, with a one-third logarithmic exponent for timing diffusion rather than the two-thirds exponent for per-tick precision.

## Calibrated count readout

Let $`T_1,T_2,\ldots`$ be the actual iid intertick times, including all fault delays, with mean $`\mu`$ and variance $`\sigma^2`$. Define

```math
\begin{aligned}
S_n&=\sum_{j=1}^nT_j,\\
N(t)&=\max\{n:S_n\le t\},\\
\widehat t&=\mu N(t).
\qquad\text{(T1)}
\end{aligned}
```

The mean period is calibrated before operation. During operation the output is the designated tick count; a list of precisely timestamped events would instead supply an external clock. No reset times or hidden internal transitions are made available to the estimator.

**Theorem T1 — asymptotic timing diffusion.** For each fixed admissible clock,

```math
\begin{aligned}
\lim_{t\to\infty}
\frac{\mathrm{Var}(\widehat t)}t
&=\lim_{t\to\infty}
\frac{\mathbb E[(\widehat t-t)^2]}t\\
&=\frac{\sigma^2}{\mu}
=\frac{\mu}{P}
=:\mathcal D.
\qquad\text{(T2)}
\end{aligned}
```

The dimensions of $`\mathcal D`$ are time. A smaller value means a smaller long-time squared error per unit elapsed time. In particular, $`1/P`$ is the count Fano factor, whereas $`\mathcal D=\mu/P`$ also charges the clock's period.

**Proof.** The exponential-tail argument in [restart and hazard](restart_and_hazard.md#notation-and-regularity) gives finite moments of every actual interval. Let $`\nu=N(t)+1`$ and let $`B_t=S_\nu-t`$ be the forward overshoot. Set $`M_n=S_n-n\mu`$. Wald's identities give

```math
\begin{aligned}
\mathbb E M_\nu&=0,\\
\mathbb E M_\nu^2&=\sigma^2\mathbb E\nu,\\
\mu N(t)-t&=B_t-\mu-M_\nu.
\qquad\text{(T3)}
\end{aligned}
```

The stopping time has finite expectation because the actual tick intensity is at most $`\Gamma`$, so $`\mathbb E N(t)\le\Gamma t`$.

For completeness, the overshoot has a uniformly bounded second moment. The renewal measure is an atom at zero plus a density at most $`\Gamma`$, again by the conditional tick-intensity bound. Summing over the possible last renewal gives

```math
\begin{aligned}
\mathbb E B_t^2
&\le\mathbb E T^2
+\Gamma\int_0^\infty
\mathbb E[(T-u)^2\mathbf1_{T>u}]\,du\\
&=\mathbb E T^2+\frac\Gamma3\mathbb E T^3.
\qquad\text{(T4)}
\end{aligned}
```

The right side is finite and independent of $`t`$ for this fixed clock. From $`S_\nu=t+B_t`$ and Wald's mean identity,

```math
\mathbb E\nu=\frac t\mu+O(1),\qquad
\mathbb E[\widehat t-t]=\mathbb E B_t-\mu=O(1).
```

The cross term in the square of (T3) is $`O(\sqrt t)`$ by Cauchy–Schwarz, while its leading martingale term is $`\sigma^2\mathbb E\nu`$. Divide by $`t`$ to obtain the mean-squared-error limit in (T2). The bounded bias has no contribution at that scale, so the variance has the same limit. ∎

This is the usual renewal-clock diffusion relation. It is not a claim that one-interval statistics suffice for a nonrenewal clock: correlations between successive tick intervals can change the long-time variance. The complete reset of every clockwork degree of freedom is essential here.

## Sharp relaxed timing envelope

The [fixed-mean hazard theorem](restart_and_hazard.md#sharp-envelope-at-a-fixed-actual-mean) immediately implies

```math
\begin{aligned}
\mathcal D&\ge\frac{x}{\gamma}G_r(x),\qquad x\ge r.
\qquad\text{(T5)}
\end{aligned}
```

This relaxed timing optimum can also be calculated exactly. Put

```math
K(r)=\ln(1+r)-\frac r{1+r},\qquad
k(x)=\ln(1+x)-x+\frac{x^2}{2}.
```

Since $`k'(x)=x^2/(1+x)>0`$, the equation $`k(x_D)=K(r)`$ has a unique positive solution. Differentiating $`J_r(x)=xG_r(x)`$ gives

```math
\begin{aligned}
J_r'(x)&=\frac2{x^2}[k(x)-K(r)].
\qquad\text{(T6)}
\end{aligned}
```

For $`0\lt r\lt 1`$,

```math
K(r)-k(r)=\frac{r^2(1-r)}{2(1+r)}>0,
```

so $`x_D>r`$ is the unique admissible minimum. At this point $`J_r(x_D)=x_D^2`$. For $`r\ge1`$, the unconstrained root is at or below $`r`$, so the minimum over $`x\ge r`$ is instead the boundary $`x=r`$. Consequently, with $`k(x_D)=K(r)`$ on the first branch,

```math
\mathcal D_{\rm hazard}(r)
=\begin{cases}
x_D^2/\gamma,&0\lt r\lt 1,\\
1/\Gamma,&r\ge1.
\end{cases}
\qquad\text{(T7)}
```

The delayed-exponential distribution in the hazard theorem attains this relaxed optimum. Its deterministic-delay branch is an upper envelope on clock performance, not an asserted finite-quantum construction. For $`r\ge1`$, however, the boundary distribution is simply $`\mathrm{Exp}(\Gamma)`$, realized by a one-state Poisson tick clock. Thus the quantum and classical timing optima both equal $`1/\Gamma`$ exactly when $`\gamma\ge\Gamma`$. This statement concerns timing diffusion, not tick precision.

As $`r\downarrow0`$, $`k(x)=x^3/3+O(x^4)`$ and $`K(r)=r^2/2+O(r^3)`$. Hence

```math
\begin{aligned}
x_D&\sim(3/2)^{1/3}r^{2/3},\\
\mathcal D_{\rm hazard}(r)
&\sim(3/2)^{2/3}\Gamma^{-1}R^{-1/3}.
\qquad\text{(T8)}
\end{aligned}
```

The timing optimizer differs from the precision optimizer $`x_P\sim6^{1/3}r^{2/3}`$. Maximizing $`P`$ and minimizing $`\mathcal D`$ are different tasks, even though their optimal periods have the same power of $`R`$.

## Quantum timing exponent under the full strength budget

Fix $`\Gamma>0`$ and write $`\mathcal D_Q^*(R)`$ for the infimum of (T2) over the finite autonomous quantum clock class in the [model](model.md), with $`\gamma=\Gamma/R`$. Both the centered Hamiltonian norm and the total intrinsic jump effect obey that model's global strength bounds. The [quasiideal source transfer](quantum_construction.md) supplies, for every fixed $`0\lt\epsilon\lt 1`$ and all sufficiently large dimensions $`d`$,

```math
\begin{aligned}
\mu_0&=\Theta_\epsilon(d/\Gamma),\\
c_0&=\frac{\mathrm{Var}X}{\mu_0^2}
\le C_\epsilon d^{-2+\epsilon}.
\qquad\text{(T9)}
\end{aligned}
```

The constants and dimension threshold may depend on $`\epsilon`$. They do not depend on $`R`$ once $`\epsilon`$ is fixed. This is an inherited clean-clock construction whose strength and mean bounds must both be retained; a dimension-only precision claim would not suffice.

For $`z=\gamma\mu_0\to0`$, the second-moment transfer and mean control give

```math
\begin{aligned}
\mathcal D
&=\mu\,\mathrm{CV}(T)^2\\
&\le\frac{\mu_0}{1-z}(c_0+40z)\\
&\le\frac{C_\epsilon'}\Gamma
\left[d^{-1+\epsilon}+\frac{d^2}{R}\right].
\qquad\text{(T10)}
\end{aligned}
```

Choose an integer $`d`$ of order $`R^{1/(3-\epsilon)}`$. Then $`z\to0`$ and

```math
\begin{aligned}
\mathcal D_Q^*(R)
&\le\frac{C_\epsilon''}\Gamma
R^{-(1-\epsilon)/(3-\epsilon)}.
\qquad\text{(T11)}
\end{aligned}
```

The universal relaxed bound (T8) gives the matching lower exponent. Thus

```math
\begin{aligned}
\lim_{R\to\infty}
\frac{\ln[\Gamma\mathcal D_Q^*(R)]}{\ln R}
&=-\frac13.
\qquad\text{(T12)}
\end{aligned}
```

Equivalently, $`\Gamma\mathcal D_Q^*(R)=R^{-1/3+o(1)}`$ in this logarithmic sense. The results do not establish an exact $`\Theta(R^{-1/3})`$ law or the relaxed constant in (T8) for finite quantum clocks.

## Classical timing benchmark

Let $`\mathcal D_C^*(R)`$ be the corresponding infimum over finite-state nominal CTMC clocks, with the **sum** of all nominal internal-transition and tick rates from each state at most $`\Gamma`$. This is a global escape-rate budget; multiplying the number of uncharged parallel clocks would change it.

After the reset faults are added, total escape, including a virtual reset that leaves the same state unchanged, is at most $`\Gamma+\gamma`$. Uniformize at that rate. The actual first-tick time can be written

```math
T=\sum_{j=1}^{K}E_j,\qquad
E_j\stackrel{\rm iid}{\sim}\mathrm{Exp}(\Gamma+\gamma),
```

where the absorption step $`K`$ of the embedded discrete chain is independent of those exponential holding times. Therefore

```math
\begin{aligned}
\mu&=\frac{\mathbb EK}{\Gamma+\gamma},\\
\sigma^2&=\frac{\mathbb EK+\mathrm{Var}K}{(\Gamma+\gamma)^2},\\
\mathcal D_C&\ge\frac1{\Gamma+\gamma}.
\qquad\text{(T13)}
\end{aligned}
```

A single memoryless tick transition of rate $`\Gamma`$, resetting to its only clock state, is unchanged by whole-clock faults. It attains $`\mathcal D_C=1/\Gamma`$. Hence

```math
\begin{aligned}
\frac1{\Gamma+\gamma}
&\le\mathcal D_C^*(R)\le\frac1\Gamma,\\
\lim_{R\to\infty}\Gamma\mathcal D_C^*(R)&=1.
\qquad\text{(T14)}
\end{aligned}
```

This timing claim does not require an unproved exact all-$`R`$ optimum $`1/\Gamma`$. The sharper [classical precision frontier](classical_optimum.md) addresses a different optimization and shows its optimal stage count and square-root regularity law.

Combining (T12) and (T14),

```math
\begin{aligned}
\lim_{R\to\infty}
\frac{\ln[\mathcal D_C^*(R)/\mathcal D_Q^*(R)]}{\ln R}
&=\frac13.
\qquad\text{(T15)}
\end{aligned}
```

The quantum improvement therefore persists when every waiting interval is charged. Its source is a smaller timing diffusion at the matched native strength and imposed complete-reset rate.

## Limits, initialization and attribution

The observation-time limit in (T2) is taken first, for each fixed clock design and fixed $`R`$. Equations (T12) and (T15) then take $`R\to\infty`$, permitting the chosen finite dimension to grow. For the construction, $`\epsilon`$ is fixed while its large-$`R`$ bound is proved; the exponent approaches one third because that fixed $`\epsilon`$ may be chosen arbitrarily small. These statements do not exchange the observation-time, dimension and small-noise limits without control.

At time zero the model supplies the specified reset state, so the first observed interval has the same distribution as subsequent intervals. A one-time preparation delay with finite second moment contributes only a startup term to long-time diffusion when it is included in elapsed time. It can matter at a finite horizon. The mathematical reset interface does not claim zero thermodynamic or fabrication cost for preparing its coherent state, and the result supplies no uniform short-time error guarantee.

The count-only readout, complete renewal reset and global strength budgets delimit the comparison. A protected reference that survives the faults, an observed fault record, or correlations between successive clock cycles require a different analysis. Finite-rate CTMCs are the classical comparator; an unrestricted deterministic classical continuous-phase oscillator is not bounded by (T13).

The generic classical accuracy-resolution and time-estimation constraints are inherited. [Prech et al., PRX 15, 031068 (2025)](https://doi.org/10.1103/rpls-mp8z) establish the clock uncertainty relation and optimal stochastic time estimation through the mean residual waiting time. [Macieszczak's kinetic uncertainty relation](https://arxiv.org/abs/2407.09839) gives a related first-passage and counting framework. Their generic inequalities do not by themselves optimize over an imposed unobserved complete-reset channel. Here the new noise-dependent envelope and its clean-clock transfer determine that optimization. The origin of the quasiideal construction remains [Woods et al., PRX Quantum 3, 010319 (2022)](https://doi.org/10.1103/PRXQuantum.3.010319).
