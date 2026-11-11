# Finite clocks that exceed the classical frontier

[Model](model.md) · [Classical frontier](classical_optimum.md) · [Timing diffusion](timing_diffusion.md) · [Reproduce](../verification/check_quantum_example.py)

A finite phase-clock example exhibits the separation without invoking the large dimension threshold of the [quasiideal proof](quantum_construction.md). At $`\Gamma=1`$ and $`R=2000`$, the specified 32-dimensional clock has numerical precision $`64.438854`$, while the exact optimum over all admissible finite CTMC clocks is $`38.740562`$. Its elapsed-time diffusion is also below the all-CTMC lower bound.

These are numerical witnesses for explicitly specified finite generators. The asymptotic exponent is established separately. The finite examples are neither optimality claims for quantum clocks nor formal interval certificates.

## 1. An explicit device at unit strength

Let $`d`$ be even and label the phase basis by $`j=0,\ldots,d-1`$. Define the Fourier matrix and energy levels by

```math
U_{jr}=\frac1{\sqrt d}e^{2\pi i jr/d},
\qquad
E_r=-1+\frac{2r}{d-1},
\qquad
H=U\mathrm{diag}(E_r)U^{\dagger}.
```

The centered Hamiltonian norm is exactly one. Define signed phase coordinates

```math
u_j=\bigl((j+d/2)\bmod d\bigr)-d/2,
\qquad
v_j=j-d/2.
```

The normalized start state is the following finite Gaussian vector in the phase basis:

```math
\psi_j=C\exp\!\left[
-\frac{\pi u_j^2}{\sigma^2}
+\frac{2\pi i n_0u_j}{d}
\right],
\qquad
\sigma=\frac52,
\quad n_0=\frac{d-1}{2},
\quad \rho_0=|\psi\rangle\langle\psi|.
```

Here $`C`$ makes $`\sum_j|\psi_j|^2=1`$. The tick effect is diagonal in the phase basis:

```math
Q=\mathrm{diag}(q_j),
\qquad
q_j=b+(1-b)\exp\!\left[-\frac{v_j^2}{2w^2}\right],
\qquad
b=10^{-4},
\quad w=\frac32.
```

Consequently $`bI\leq Q\leq I`$ and $`\|Q\|=1`$. There are no intrinsic uncounted channels. The nominal generator uses the tick operators

```math
J_j=\sqrt{q_j}\,|\psi\rangle\langle j|,
\qquad
\sum_jJ_j^{\dagger}J_j=Q.
```

All microscopic tick labels are summed into the same observed tick, and every such tick prepares $`\rho_0`$. Add unobserved fault operators

```math
F_j=\sqrt\gamma\,|\psi\rangle\langle j|,
\qquad
\gamma=R^{-1},
\qquad
\sum_jF_j^{\dagger}F_j=\gamma I.
```

Their generator is exactly the [specified restart fault](model.md): $`\gamma(\rho_0\mathrm{tr}\rho-\rho)`$. The full internal clockwork is reset; no protected auxiliary register is used. The passive output retains only actual ticks. The Hamiltonian and all jump operators are time independent.

This family uses an engineered Fourier Hamiltonian and reset interface. Geometric locality and microscopic synthesis costs are outside the resource model. A dimension-independent bound on the entire Hamiltonian and summed tick effect is nevertheless enforced exactly; no per-channel allowance or growing bandwidth is used.

## 2. Infinite-horizon moments from finite linear equations

The first method computes the complete waiting-time moments through complex Lyapunov equations. It does not truncate a time trace or discard failed attempts.

Set

```math
A=-iH-\frac Q2,
\qquad
A_\gamma=A-\frac\gamma2I.
```

Solve

```math
\begin{aligned}
A_\gamma Y+YA_\gamma^{\dagger}&=-\rho_0,\\
A_\gamma Z+ZA_\gamma^{\dagger}&=-Y,
\end{aligned}
\qquad
u=\mathrm{tr}Y,
\quad z=\mathrm{tr}Z,
\quad p=1-\gamma u.
```

The variables have direct integral meanings:

```math
\begin{aligned}
Y&=\int_0^\infty
e^{-\gamma t}e^{At}\rho_0e^{A^{\dagger}t}\,dt,\\
Z&=\int_0^\infty
t\,e^{-\gamma t}e^{At}\rho_0e^{A^{\dagger}t}\,dt.
\end{aligned}
```

The restart identities give the actual faulty interval moments

```math
\mu=\frac up,
\qquad
\mathbb E T^2=\frac{2z}{p^2},
\qquad
v=\frac{2z-u^2}{p^2},
\qquad
P=\frac{u^2}{2z-u^2}.
```

The calculation additionally checks the absorption normalization $`\mathrm{tr}(QY)=p`$. The strictly positive baseline makes no-tick survival decay at least as $`e^{-bt}`$, including when the faults are active, so the infinite-horizon integrals and moments are well defined.

An independent calculation constructs the actual no-tick density generator

```math
\mathcal K_\gamma(X)
=AX+XA^{\dagger}
+\gamma\bigl(\rho_0\mathrm{tr}X-X\bigr)
```

as a $`d^2\times d^2`$ matrix. It solves

```math
-\mathcal K_\gamma(M_0)=\rho_0,
\qquad
-\mathcal K_\gamma(M_1)=M_0,
```

and reads $`\mu=\mathrm{tr}M_0`$ and $`\mathbb E T^2=2\mathrm{tr}M_1`$. This second method inserts the fault generator directly and uses no restart transform. It is run for the 16- and 32-dimensional examples.

## 3. Finite results

All rows below use the same $`\sigma,w,b`$ specified above and $`\Gamma=1`$.

| Dimension | $`R`$ | Quantum precision | Exact CTMC optimum | Ratio |
|---:|---:|---:|---:|---:|
| 16 | 100 | 10.217754 | 8.709224 | 1.173211 |
| 24 | 1000 | 39.984522 | 27.402131 | 1.459176 |
| 32 | 2000 | 64.438854 | 38.740562 | 1.663343 |
| 64 | 10000 | 129.426016 | 86.607600 | 1.494396 |

The classical column is the [proved all-CTMC optimum](classical_optimum.md), with arbitrary finite state count, topology, allowed transition rates and start distribution. It is not a dimension-matched ladder used as a restricted baseline. For the four rows, the optimal classical ladder has respectively 17, 55, 77 and 173 stages.

### The 32-dimensional witness also improves elapsed-time accuracy

For its actual faulty intervals,

```math
\mu\simeq41.837423350,
\qquad
v\simeq27.163270149,
\qquad
\mathcal D_{\rm Q}=\frac v\mu\simeq0.649257721.
```

Every admissible CTMC clock at the same rates obeys the [timing-diffusion bound](timing_diffusion.md#classical-timing-benchmark)

```math
\mathcal D_{\rm C}\geq\frac1{\Gamma+\gamma}
=\frac1{1+1/2000}
\simeq0.999500250.
```

Thus this finite example's advantage survives charging the full tick period in the calibrated count estimator. The 24- and 64-dimensional rows also lie below their all-CTMC diffusion bounds; the 16-dimensional row is a precision witness only. These are long-time diffusion comparisons for each fixed device, not uniform startup guarantees.

### A bounded sensitivity check

The absorption baseline is a nominal device parameter that produces counted early ticks. It is separate from the hidden restart-fault rate. Keeping the 32-dimensional device at $`R=2000`$ and changing only that baseline gives:

| Baseline $`b`$ | Quantum precision | Ratio to the CTMC optimum |
|---:|---:|---:|
| $`10^{-10}`$ | 70.741761 | 1.826039 |
| $`10^{-6}`$ | 70.672640 | 1.824254 |
| $`10^{-4}`$ | 64.438854 | 1.663343 |
| $`10^{-3}`$ | 35.766769 | 0.923238 |

The finite separation does not depend on an almost dark baseline of $`10^{-10}`$. Increasing the baseline sufficiently destroys this particular precision witness. The table does not establish general robustness to other noise channels or parameter errors.

## 4. Reproduce and interpret the checks

From the repository root:

```bash
python verification/check_quantum_example.py \
  --output verification/quantum_example_validation.json
```

The [saved numerical record](../verification/quantum_example_validation.json) contains input parameters, resource checks, clean and faulty moments, exact classical comparators, residuals and the independent full-generator results. The largest relative disagreement in the checked mean, variance and precision was below $`4\times10^{-13}`$; the reported linear-equation residuals were below $`10^{-12}`$ in the recorded run.

Those observations check the finite computations and make the comparison reproducible. They do not replace the analytical classical theorem, the large-dimension construction or an interval-arithmetic proof. The numerical margins in the table are much larger than the observed solver disagreement, but no rigorous floating-point error enclosure is claimed.
