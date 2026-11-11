# Learning the clock restart problem

[Repository overview](../README.md) · [Selected anchor and bridge](BRIDGE.md) · [Thirty milestones](MILESTONES.md) · [Scientific account](../science/README.md)

Imagine a device that emits ticks while its internal state moves through a cycle. A longer cycle can make successive tick intervals more regular. A hidden fault can erase that progress and send the device back to its initial state. The observer receives no fault flag: every interrupted attempt still consumes real time before the next genuine tick.

The project asks how well a finite autonomous clock can operate under these resets when its intrinsic dynamical strength is bounded. Quantum coherence permits a different balance between clean regularity and erased progress than a finite classical Markov clock. The result concerns this specified dynamical model; its effective reset interfaces are supplied, rather than derived from microscopic baths.

## A route from the anchor to the result

The single educational anchor is **Wiseman and Milburn, *Quantum Measurement and Control* (2010)**. Chapters 3 and 4 supply the open-system and quantum-trajectory language. The [bridge](BRIDGE.md) explains the translation to clock events and identifies the additional arguments supplied here.

The settled [milestone map](MILESTONES.md) has two phases. Its order follows the scientific dependencies, rather than the textbook's chapter order.

| Milestones | What they connect | Canonical account |
|---|---|---|
| M01–M06 | Internal states, autonomous generators, total strength and no-tick trajectories | [Model](../science/model.md) |
| M07–M12 | Hidden complete resets, renewal cycles, performance and the full classical comparator | [Model and limits](../science/model.md#physical-interpretation-and-limits) |
| M13–M17 | Restart recursion, actual moments and the sharp relaxed hazard envelope | [Restart and hazard bounds](../science/restart_and_hazard.md) |
| M18–M20 | Uniformization and the exact all-network classical optimum | [Classical proof](../science/classical_optimum.md) |
| M21–M25 | The inherited coherent clock, bounded resources and transfer through faults | [Quantum construction](../science/quantum_construction.md) |
| M26–M28 | A finite witness and calibrated elapsed-time performance | [Finite example](../science/finite_example.md) · [Timing diffusion](../science/timing_diffusion.md) |
| M29–M30 | Attribution, evidence and the complete scoped consequence | [Related work](../references/RELATED_WORK.md) · [Scientific synthesis](../science/README.md) |

## A complete two-stage example

Take a classical device with two internal states, A and B. It starts in A, makes the transition A to B at rate $`\Gamma`$, and emits a tick from B at the same rate. That tick returns it to A. The two transitions occur in different states, so each state's total intrinsic event rate is $`\Gamma`$, within the budget.

Without faults, the first-tick time $`X`$ is a sum of two independent exponential holding times. Each has mean $`1/\Gamma`$ and variance $`1/\Gamma^2`$. Thus
```math
\mathbb E X=\frac{2}{\Gamma},\qquad
\mathrm{Var}X=\frac{2}{\Gamma^2},\qquad P=2.
```
The sum is more regular relative to its mean than one exponential stage, whose precision is one.

Now impose independent reset opportunities at rate $`\gamma=\Gamma`$. A fault in B sends the device to A without a tick. A fault in A leaves its state unchanged and also emits no tick. Neither event is reported; both consume elapsed time. The faulty first-tick generator, using row probabilities and stopping at a tick, is
```math
B=\Gamma\begin{pmatrix}-1&1\\1&-2\end{pmatrix}.
```
The fault opportunities in A do not change this generator, because they leave both the internal state and observed output unchanged. The restart calculation nevertheless includes their elapsed intervals.

The clean Laplace transform is $`\phi(s)=[\Gamma/(\Gamma+s)]^2`$. At $`s=\gamma=\Gamma`$, the success probability before a fault is $`p=1/4`$, and the weighted time is $`b=\mathbb E[Xe^{-\gamma X}]=1/(4\Gamma)`$. Substitution into the [exact restart moments](../science/restart_and_hazard.md#exact-renewal-transform-and-moments) gives
```math
\mu=\frac{1-p}{\gamma p}=\frac3\Gamma,\qquad
v=\frac{1-p^2-2\gamma b}{\gamma^2p^2}=\frac7{\Gamma^2}.
```
Both the longer mean and the increased variance belong to the actual tick interval $`T`$, with no unsuccessful path removed.

## Two performance questions

Tick precision is $`P=\mu^2/v`$. For the example it is $`9/7`$, still above the one-stage value of one. Elapsed-time readout has a different objective. Let $`N(t)`$ be a passive count of genuine ticks and use the supplied period calibration to estimate time by $`\widehat t=\mu N(t)`$. For each fixed finite device,
```math
\mathcal D=\lim_{t\to\infty}\frac{\mathbb E[(\widehat t-t)^2]}{t}
=\frac v\mu=\frac\mu P.
```
The two-stage example has $`\mathcal D=7/(3\Gamma)`$. A one-stage exponential tick clock has $`\mathcal D=1/\Gamma`$, even with these resets. Greater tick precision alone therefore does not establish smaller elapsed-time error: its period also matters. These numbers illustrate the two objectives and are not an optimization over all devices.

The [timing theorem](../science/timing_diffusion.md) takes the long-time limit for each finite device first, then optimizes over devices and takes weak faults. A finite observation horizon growing jointly with device size would require an additional uniform analysis.

## Why the optimal noise laws differ

Write $`R=\Gamma/\gamma`$. A classical ladder with $`n`$ rate-bounded stages has clean relative variance of order $`1/n`$. Its longer traversal creates a fault cost of order $`n/R`$. Balancing these terms suggests $`n`$ of order $`\sqrt R`$. The [classical proof](../science/classical_optimum.md) establishes much more than this heuristic: no other finite Markov topology, start mixture or bounded state-dependent rates improves on a pure Erlang ladder, and
```math
P_{\rm C}^{*}(R)\sim\frac{\sqrt{3R}}2.
```

A coherent packet can have less intrinsic relative spreading for a comparable traversal time. The inherited quasiideal construction gives, for every fixed $`0<\varepsilon<1`$, clean relative variance of order at most $`d^{-2+\varepsilon}`$ and mean of order $`d/\Gamma`$, after the full strength bounds are imposed. Balancing this with a restart cost of order $`d/R`$ gives a precision lower bound proportional to $`R^{(2-\varepsilon)/(3-\varepsilon)}`$. A universal converse completes the logarithmic exponent:
```math
\lim_{R\to\infty}\frac{\log P_{\rm Q}^{*}(R)}{\log R}=\frac23.
```
The [construction](../science/quantum_construction.md) checks the Hamiltonian and the **sum** of all intrinsic jump effects. Exact constant-factor matching to $`R^{2/3}`$ is not proved. The sharp delayed-exponential waiting law in the [hazard relaxation](../science/restart_and_hazard.md) is not claimed to be exactly attainable by a finite quantum clock.

## From asymptotics to a finite device

At $`\Gamma=1`$ and $`R=2000`$, the specified 32-level quantum clock has precision about **64.44**, exceeding the exact all-classical optimum **38.74**. Its timing diffusion is about **0.6493**, below the classical lower bound **0.9995**. The [finite device account](../science/finite_example.md) gives every static ingredient, and the [verification guide](../verification/README.md) supplies independent moment calculations and a sensitivity check. These are floating-point witnesses, not rigorous interval certificates.

All internal clockwork, ancillas and autonomous controls are erased by faults. Only the passive tick counter retains an output record, without feedback. The comparison covers arbitrary finite autonomous classical Markov clocks with bounded total nominal event rate; deterministic continuous-phase classical oscillators lie outside that class. Microscopic reset synthesis, thermodynamic cost, fabrication and locality are outside the resource accounting. These qualifications remain attached to both the finite illustration and the asymptotic advantage.
