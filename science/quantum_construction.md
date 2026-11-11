# A bounded-strength quantum clock family

[Model](model.md) · [Restart theorem](restart_and_hazard.md) · [Classical optimum](classical_optimum.md) · [References](../references/REFERENCES.md)

Quantum achievability uses an existing autonomous clock construction. The new step is to place that construction inside the present strength budget and then control its response to unobserved restart faults. No new ideal-clock accuracy theorem is claimed here.

The source is the quasiideal reset clock of [Woods, Silva, Pütz, Stupar and Renner](../references/REFERENCES.md#woods2022). We use its fixed-period asymptotics first and rescale the completed generator afterward. This keeps the Hamiltonian bandwidth, the sum of all tick effects and the mean tick time in the same resource account.

## 1. The clean-clock resource lemma

Fix a strength $`\Gamma\gt 0`$. For every fixed $`\epsilon\in(0,1)`$, there is a family of finite-dimensional, time-independent quantum reset clocks, indexed by sufficiently large even dimensions $`d`$, with

```math
\begin{aligned}
\min_{c\in\mathbb R}\|H_d-cI\|&\lt \frac{\Gamma}{4},\\
Q_d:=\sum_k J_{d,k}^{\dagger}J_{d,k}&\leq\Gamma I,\\
\frac{2\pi}{3}\frac d\Gamma
\leq\mu_{0,d}&\leq8\pi\frac d\Gamma,\\
c_{0,d}:=\frac{\mathrm{Var}X_d}{\mu_{0,d}^{2}}
&\leq24d^{-2+\epsilon}.
\end{aligned}
```

Here $`X_d`$ is the clean first-tick time, and $`\mu_{0,d}=\mathbb E X_d`$. Every tick resets the entire clockwork to one fixed pure state $`\rho_{0,d}`$. There are no intrinsic uncounted dissipators. The dimension threshold depends on $`\epsilon`$, as do the constants implicit in the source's asymptotic estimates.

Restricting to even dimensions simplifies a rounding convention; it does not affect any exponent below. Odd-dimensional versions are also supplied by the source.

### What is inherited

The source proves that quasiideal clocks can have accuracy arbitrarily close to quadratic in their dimension. Its Appendix F specifies the Hamiltonian, initial state, positive absorption potential and tick-reset operators, and proves the required accuracy bound. The source's ideal family and accuracy theorem are inherited.

The resource lemma above additionally checks the total operator effect of the many tick channels, makes a definite timescale choice, and bounds the actual mean despite possible long tails. Those checks are necessary before using dimension accuracy to infer a precision law at bounded native strength.

## 2. Fixed-period source parameters

Start with the source's period set to one. Its Hamiltonian is

```math
H_d^{(0)}=2\pi\sum_{r=0}^{d-1}r\,|E_r\rangle\langle E_r|.
```

The Fourier basis is

```math
|\theta_k\rangle
=\frac1{\sqrt d}\sum_{r=0}^{d-1}
e^{-2\pi i rk/d}|E_r\rangle.
```

The superscript $`(0)`$ indicates the fixed-period source model, before the physical timescale is chosen. It is unrelated to the clock's reset state.

For the desired exponent loss $`\epsilon`$, set

```math
\begin{gathered}
a=\frac\epsilon5,
\qquad
\epsilon_5=\epsilon_8=\frac a{16},
\qquad
\epsilon_6=2a,
\qquad
\epsilon_7=\frac a4,
\qquad
\epsilon_9=\frac a2,\\
\sigma=d^{2a},
\qquad
\alpha_0=1,
\qquad
n_0=\frac{d-1}{2},
\qquad
k_0=0,
\qquad
\delta=d^{a/16},\\
N=\left\lceil\frac{12}{a}-3\right\rceil,
\qquad
\kappa=0.792.
\end{gathered}
```

The symbols $`\epsilon_5,\ldots,\epsilon_9`$ are the source's proof parameters. The source's auxiliary spatial width will be denoted $`\gamma_{\mathrm s}`$ below; it is distinct from the physical fault rate $`\gamma`$.

These choices meet all constraints in the source's Eqs. (589)–(590). In particular,

```math
\begin{aligned}
0&\lt \epsilon_5\lt \epsilon_6\lt 1,\\
\epsilon_5+\epsilon_8&\lt \epsilon_7\lt \frac{a}{2},\\
0&\lt \epsilon_9\lt a,\\
3-4\epsilon_5-\epsilon_9&\gt 0.
\end{aligned}
```

For sufficiently large dimensions, the remaining constraint is

```math
\frac{4}{\sigma}\lt d^{a/2}\leq\frac{d}{\sigma}.
```

The last upper inequality reduces to $`5a/2\leq1`$, which holds because $`a\lt 1/5`$. This explicit choice uses the source's accuracy bound before its final renaming of the parameter $`\eta`$.

### Initial state

Use the normalized pure state from the source's Eqs. (370)–(375):

```math
|\psi_{0,d}\rangle
=A_d\sum_{k\in\mathcal S_d(0)}
e^{-\pi k^2/\sigma^2}
e^{2\pi i n_0 k/d}|\theta_k\rangle,
\qquad
\rho_{0,d}=|\psi_{0,d}\rangle\langle\psi_{0,d}|.
```

Here $`\mathcal S_d(0)`$ is the set of the $`d`$ nearest integers specified by the source, Fourier labels are understood modulo $`d`$, and $`A_d`$ normalizes the state. Placing $`n_0`$ at the midpoint of the energy spectrum makes the source's parameter $`\alpha_0`$ exactly one.

### Positive absorption potential

Define

```math
I_N=\int_{\mathbb R}\mathrm{sinc}^{2N}(x)\,dx,
\qquad
\mathrm{sinc}(x)=\frac{\sin(\pi x)}{\pi x},
\qquad
C_0=1+2\pi N+\frac{2N+1}{I_N}.
```

The constant $`C_0`$ depends on $`\epsilon`$ through $`N`$, and is independent of $`d`$. Choose the source's filter scale as

```math
\nu_d
=\frac{\log(\pi\sigma^2)}{2\pi C_0\kappa}
\frac{d^{1-a/16}}{\delta\sigma}.
```

The source calls this filter scale $`n`$; $`\nu_d`$ avoids confusion with an energy index. It need not be an integer, and tends to infinity for this parameter choice.

For even $`d`$, set

```math
\begin{aligned}
m_d&=2\left\lfloor\frac12d^{a/2}\sigma+1\right\rfloor,
&\gamma_{\mathrm s}&=\frac{m_d-2}{d},\\
x_{\mathrm{vr}}&=\frac{d^{a/4}\sigma}{\pi d},
&x_0&=\pi+x_{\mathrm{vr}}+\pi\gamma_{\mathrm s}.
\end{aligned}
```

The normalized, strictly positive periodic potential is

```math
\begin{aligned}
B_d&=\frac{1-2\pi/(\delta d^2)}{I_N},\\
\bar V_{0,d}(x)
&=\frac1{\delta d^2}
+\nu_d B_d\sum_{p\in\mathbb Z}
\mathrm{sinc}^{2N}\!\bigl(\nu_d(x-x_0-2\pi p)\bigr).
\end{aligned}
```

This is the source's Eqs. (359)–(369), with the displayed parameter choices. Its integral over a period is one. The positive baseline makes eventual ticking certain and all waiting-time moments finite for every fixed dimension.

The fixed-period absorption operator and tick jumps are

```math
\begin{aligned}
V_d^{(0)}
&=2\pi\delta\sum_{k=0}^{d-1}
\bar V_{0,d}(2\pi k/d)|\theta_k\rangle\langle\theta_k|,\\
J_{d,k}^{(0)}
&=\sqrt{4\pi\delta\,\bar V_{0,d}(2\pi k/d)}
\,|\psi_{0,d}\rangle\langle\theta_k|.
\end{aligned}
```

The complete fixed-period generator is

```math
\mathcal L_d^{(0)}(\rho)
=-i[H_d^{(0)},\rho]
+\sum_{k=0}^{d-1}\mathcal D[J_{d,k}^{(0)}](\rho).
```

Each jump output is proportional to $`\rho_{0,d}`$. The no-tick amplitude generator is $`-iH_d^{(0)}-V_d^{(0)}`$, and the first-tick density is $`2\mathrm{tr}(V_d^{(0)}\rho(t))`$, as in the source's Eqs. (346)–(351).

## 3. Bounding the sum of all tick effects

The tick budget is the norm of the summed effect, rather than the rate of an individual channel. The factor of two is fixed by the jump operators:

```math
Q_d^{(0)}
=\sum_k J_{d,k}^{(0)\dagger}J_{d,k}^{(0)}
=2V_d^{(0)}.
```

The source's derivative estimate, Lemma 28/Eq. (530), implies

```math
\max_x\bar V_{0,d}(x)\leq\nu_d C_0.
```

The displayed choice of $`C_0`$ is one explicit admissible constant. To check it, the Fourier transform of $`\mathrm{sinc}^{2N}`$ is an $`N`$-fold convolution of the triangular density. It is nonnegative, supported on $`[-N,N]`$ and has supremum at most one. The nonconstant Fourier coefficients of the periodic potential are therefore supported on $`|\ell|\leq2\pi\nu_dN`$. Summing their absolute values, including the constant baseline separately, bounds the zeroth derivative by

```math
\nu_d\left(1+\frac{2N+1}{I_N}\right).
```

A derivative of order $`r`$ adds at most a factor $`(2\pi\nu_dN)^r`$. Since $`C_0`$ dominates both constants, it satisfies the source's full derivative bound

```math
\max_x|\bar V_{0,d}^{(r)}(x)|
\leq\nu_d^{r+1}C_0^{r+1},
\qquad r\geq0.
```

This also keeps the constant independent of the chosen dimension.

### Choose the physical timescale

Rescale the fixed-period generator by

```math
\lambda_d=\frac{\Gamma}{4\pi d},
\qquad
H_d=\lambda_d H_d^{(0)},
\qquad
J_{d,k}=\sqrt{\lambda_d}\,J_{d,k}^{(0)}.
```

The physical period is now $`T_d=4\pi d/\Gamma`$. Uniform rescaling preserves precision and multiplies all waiting times by $`1/\lambda_d`$. It gives

```math
\min_c\|H_d-cI\|
=\lambda_d\pi(d-1)\lt \frac\Gamma4.
```

For the total tick effect,

```math
\begin{aligned}
\|Q_d\|
&\leq\lambda_d4\pi\delta\nu_dC_0\\
&=\Gamma\,
\frac{\log(\pi d^{4a})}{2\pi\kappa}
d^{-33a/16}.
\end{aligned}
```

The last ratio tends to zero. Thus $`Q_d\leq\Gamma I`$ for all sufficiently large dimensions. No growing Hamiltonian bandwidth or uncounted jump activity is hidden in the rescaling.

## 4. Clean precision and the actual mean

At period one, the source's Eq. (588), with the constraints explicitly checked above, gives

```math
\mathcal P_{0,d}
\geq\frac1{12}\frac{d^{2-a}}{\sigma^2}
+o\!\left(\frac{d^{2-a}}{\sigma^2}\right)
=\frac1{12}d^{2-\epsilon}+o(d^{2-\epsilon}).
```

Consequently $`c_{0,d}\leq24d^{-2+\epsilon}`$ eventually. This precision is unchanged by the uniform physical rescaling.

The mean requires a separate check. A sharply peaked density alone would not exclude a rare tail that changes its first moment.

Let $`S_d^{(0)}(t)`$ be the fixed-period no-tick survival probability. The source's actual survival bounds, Eqs. (420)–(427) and (466)–(469), include its wavepacket approximation errors. Their time window starts at $`t_1=1/2`$ and ends at $`t_2=1/2+o(1)`$. For the displayed parameters,

```math
\gamma_{\mathrm s}=\Theta(d^{-1+5a/2}),
\qquad
x_{\mathrm{vr}}=o(\gamma_{\mathrm s}),
\qquad
\delta\longrightarrow\infty.
```

The Gaussian and wavepacket error terms in the source's Eqs. (421), (426), (498)–(503) and (561) vanish faster than the powers needed here. Its potential-tail estimate (585) is

```math
\delta\tilde\epsilon_V
=O_\epsilon\!\left(
\frac{d^{-2+9a/2}}{(\log d)^{2N-1}}
\right)+O(d^{-2})
=o(\gamma_{\mathrm s}^{2}).
```

The resulting fixed-period survival estimates are

```math
S_d^{(0)}(1/3)\geq1-o(1),
\qquad
S_d^{(0)}(1)\leq o(1).
```

For large $`d`$, if $`X_d^{(0)}`$ denotes the source tick time, they imply

```math
\Pr(X_d^{(0)}\geq1/3)\geq\frac12,
\qquad
\Pr(X_d^{(0)}\leq1)\geq\frac12.
```

The first inequality gives $`\mathbb E X_d^{(0)}\geq1/6`$. If its mean were greater than two, the second inequality would imply

```math
\mathrm{Var}X_d^{(0)}
\geq\frac12\bigl(\mathbb E X_d^{(0)}-1\bigr)^2
\gt \frac18\bigl(\mathbb E X_d^{(0)}\bigr)^2.
```

Its precision would then be below eight, contradicting the diverging lower bound already established. Thus the actual mean lies in $`[1/6,2]`$ eventually. Rescaling proves

```math
\frac{T_d}{6}\leq\mu_{0,d}\leq2T_d,
```

which is the mean bound in the resource lemma. The argument controls rare tails without requiring a uniform third-moment estimate.

## 5. Add the same unobserved restart channel

For any fixed orthonormal basis $`\{|e_\ell\rangle\}`$, add fault jumps

```math
F_{d,\ell}=\sqrt\gamma\,
|\psi_{0,d}\rangle\langle e_\ell|.
```

Their combined generator and total effect are

```math
\begin{aligned}
\sum_\ell\mathcal D[F_{d,\ell}](\rho)
&=\gamma\bigl(\rho_{0,d}\mathrm{tr}\rho-\rho\bigr),\\
\sum_\ell F_{d,\ell}^{\dagger}F_{d,\ell}&=\gamma I.
\end{aligned}
```

Thus fault times have the specified state-independent Poisson rate, and a fault returns every clockwork degree of freedom to the same state prepared by an actual tick. Fault labels are not counted or supplied to a decoder. The noisy native tick hazard remains at most $`\Gamma`$, while the separately charged faults add effect $`\gamma I`$.

Both the clean and faulty generators are time independent. This construction needs no timed switching, protected ancillary memory or external clock record. Its autonomy is the time-homogeneous Markovian autonomy of the stated model. A microscopic implementation of the coherent pure reset state, including its energy and reservoir resources, is not supplied by this mathematical construction and is not claimed to have zero cost.

## 6. Precision after faults

The [second-moment restart estimate](restart_and_hazard.md) applies whenever $`c_{0,d}\leq1`$ and $`\gamma\mu_{0,d}\leq1/4`$:

```math
\frac{\mathrm{Var}T_d^{\mathrm{fault}}}
{(\mathbb E T_d^{\mathrm{fault}})^2}
\leq c_{0,d}+40\gamma\mu_{0,d}.
```

Using the resource lemma and $`R=\Gamma/\gamma`$ gives

```math
\frac{\mathrm{Var}T_d^{\mathrm{fault}}}
{(\mathbb E T_d^{\mathrm{fault}})^2}
\leq24d^{-2+\epsilon}+320\pi\frac dR.
```

Choose $`d`$ to be the nearest larger even integer of order $`R^{1/(3-\epsilon)}`$. It eventually exceeds the source and resource thresholds, and $`\gamma\mu_{0,d}\to0`$. The two displayed error contributions then have the same power, so

```math
\boxed{
\mathcal P_{\mathrm q}^{\star}(R)
\geq c_\epsilon R^{(2-\epsilon)/(3-\epsilon)}
\qquad\text{for every fixed }\epsilon\in(0,1).
}
```

The positive constant $`c_\epsilon`$ and the onset of this bound may depend on $`\epsilon`$. Combining these lower bounds with the [universal quantum upper bound](restart_and_hazard.md) yields

```math
\boxed{
\lim_{R\to\infty}
\frac{\log\mathcal P_{\mathrm q}^{\star}(R)}{\log R}
=\frac23.
}
```

The order of the argument matters: fix $`\epsilon\gt 0`$, take the small-fault limit with the specified dimension choice, and then let the fixed exponent loss approach zero. This establishes the optimal logarithmic exponent. It leaves subpower factors and the exact asymptotic constant unresolved, and does not assert $`\mathcal P_{\mathrm q}^{\star}(R)=\Theta(R^{2/3})`$.

The [classical optimum](classical_optimum.md) is $`\Theta(R^{1/2})`$ under the same intrinsic rate scale and complete-restart faults. Quantum coherence therefore changes the optimal dependence on fault strength in this model. The inherited clean-clock advantage supplies the construction; the restart theorem and resource transfer establish how that advantage survives the specified faults.
