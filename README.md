# Quantum Clock Restart Limits

How accurately can an autonomous clock keep time when hidden faults restart its entire clockwork?

A more regular clock can spend longer traversing its internal states before each tick. Restart faults create a competing cost: the longer that traversal takes, the more often its progress is erased. With a fixed bound on the Hamiltonian and the sum of all intrinsic jump strengths, this competition produces different optimal noise laws for quantum clocks and classical Markov clocks.

## Principal results

Let $`\Gamma`$ bound intrinsic dynamical strengths and let $`\gamma`$ be the rate of independent, unobserved faults. Every normal tick and every fault restores the same complete internal state. Faults produce no tick and retain no usable memory. Define
```math
R=\Gamma/\gamma,\qquad
P=\frac{(\mathbb E T)^2}{\mathrm{Var}T},
```
where $`T`$ is the actual interval between observed ticks, including all interrupted attempts.

| Result | Established statement | Account |
|---|---|---|
| Exact classical optimizer | At every $`R>0`$, a unidirectional Erlang ladder is optimal among all allowed finite classical Markov networks. | [Classical optimum](science/classical_optimum.md) |
| Weak-fault precision | $`P_{\rm C}^{*}(R)\sim\sqrt{3R}/2`$, while $`P_{\rm Q}^{*}(R)=R^{2/3+o(1)}`$. | [Classical proof](science/classical_optimum.md) · [Quantum construction](science/quantum_construction.md) |
| Sharp variance envelope | A delayed-exponential intrinsic waiting law uniquely minimizes restarted variance at fixed actual mean in the relaxed bounded-hazard class. | [Restart and hazard bounds](science/restart_and_hazard.md) |
| Elapsed-time accuracy | For calibrated tick counting, $`\Gamma\mathcal D_{\rm Q}^{*}=R^{-1/3+o(1)}`$, while $`\Gamma\mathcal D_{\rm C}^{*}\to1`$. | [Timing diffusion](science/timing_diffusion.md) |

The quantum powers are **logarithmic asymptotic exponents**. Exact constant-factor $`\Theta(R^{2/3})`$ precision or $`\Theta(R^{-1/3})`$ timing-diffusion laws are not established. The sharp constants of the relaxed hazard problem are not asserted to be attainable by finite quantum clocks.

The elapsed-time statement uses
```math
\widehat t=\mu N(t),\qquad
\mathcal D=\lim_{t\to\infty}\frac{\mathbb E[(\widehat t-t)^2]}{t}
=\frac{\mathrm{Var}T}{\mu},
\quad\mu=\mathbb E T.
```
For each fixed finite clock, the long observation-time limit is taken first. Only then are clock designs and the weak-fault limit optimized. Startup and calibration can affect a jointly growing finite observation horizon.

## A finite numerical example

An explicit 32-level static phase clock at $`\Gamma=1`$ and $`R=2000`$ has tick precision approximately **64.44**, compared with the exact all-CTMC optimum **38.74**. Its calibrated timing diffusion is approximately **0.6493**, below the universal classical lower bound **0.9995** at the same strength and fault rate. Independent full-generator and Lyapunov calculations agree within $`4\times10^{-13}`$ in relative moment comparisons.

The [finite example](science/finite_example.md) gives its state, Hamiltonian, complete tick effect, reset map and sensitivity test. These are reproducible floating-point witnesses, rather than interval certificates or the proof of the asymptotic exponent.

## What the comparison charges

The classical comparison includes arbitrary finite, time-homogeneous Markov clock networks, with the sum of every state's internal-transition and tick rates at most $`\Gamma`$. Quantum clocks obey a centered Hamiltonian norm bound and a total intrinsic jump-effect bound at the same scale. Fault reset opportunities at rate $`\gamma`$ are additional in both classes.

All internal clockwork registers, ancillas and autonomous controllers are reset. A passive output counter may retain ticks but cannot control the device. No observed fault flags, postselection, protected timing reference or external switching schedule are supplied. The [model](science/model.md) states the precise common resource contract.

This is a theorem about specified effective autonomous generators. Microscopic coherent-reset synthesis, bath preparation, fabrication, geometric locality and thermodynamic cost are outside its strength accounting. An unrestricted continuous-phase classical oscillator is outside the finite Markov comparison.

## How the argument works

The imposed Poisson restart process has an exact waiting-time transform. At fixed noisy mean, optimizing its variance becomes a scalar weighted-moment problem. Bounded hazard gives a sharp single-crossing envelope.

For a classical Markov clock, uniformization adds a stronger restriction: its intrinsic waiting time is a mixture of Erlang laws with a common bounded rate. The exact convex envelope selects adjacent ladder lengths at fixed mean, and optimizing the mean selects one pure ladder globally.

The quantum construction inherits quasiideal clocks from Woods et al. Its source parameters are rescaled so that both Hamiltonian bandwidth and total tick strength remain bounded. A second-moment restart estimate then transfers their clean performance to the faulty clock. [Attribution and comparison](references/RELATED_WORK.md) separate those inherited ingredients from the noise-dependent optimization.

## Reading routes

| Goal | Start here |
|---|---|
| Learn the event model and its consequences | [Learning route](learning/README.md) · [Anchor bridge](learning/BRIDGE.md) · [Thirty milestones](learning/MILESTONES.md) |
| Follow the connected scientific story | [Scientific overview](science/README.md) |
| Check assumptions, observations and charged resources | [Model](science/model.md) |
| Reconstruct the universal restart constraint | [Restart and hazard bounds](science/restart_and_hazard.md) |
| Inspect the unrestricted classical benchmark | [Exact classical optimum](science/classical_optimum.md) |
| Check the coherent source transfer and its limits | [Quantum construction](science/quantum_construction.md) |
| Assess actual elapsed-time performance | [Timing diffusion](science/timing_diffusion.md) |
| Locate primary sources and closest comparisons | [Related work](references/RELATED_WORK.md) · [References](references/REFERENCES.md) |
| Inspect an explicit finite quantum clock | [Finite example](science/finite_example.md) |
| Reproduce finite checks | [Verification guide](verification/README.md) |

## Reproduction

From the repository root, with Python 3.10 or later:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_classical.py --output verification/classical_validation.json
python verification/check_hazard_independent.py
python verification/check_quantum_example.py --output verification/quantum_example_validation.json
```

The finite suites compare independent generator and renewal calculations, test exact envelope saturation and optimizer formulas, and sample admissible classical and hazard models. They support implementation and counterexample checks; the topic pages supply the universal proofs. See the [verification guide](verification/README.md) for scope and limitations.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
