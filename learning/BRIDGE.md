# From quantum trajectories to a clock with hidden restart faults

[Learning route](README.md) · [Thirty milestones](MILESTONES.md) · [Scientific account](../science/README.md)

An emitted event can mark a clock tick. An internal event can also erase the clock’s progress without announcing that anything happened. The distinction between those two records is the starting point of this project: the detector sees genuine ticks, while the clockwork also experiences hidden complete resets.

## The single educational anchor

Howard M. Wiseman and Gerard J. Milburn, **Quantum Measurement and Control** (Cambridge University Press, 2010), is the educational anchor. [Publisher page](https://www.cambridge.org/core/books/quantum-measurement-and-control/F78F445CD9AF00B10593405E9BAC6B9F) · [Book DOI](https://doi.org/10.1017/CBO9780511813948).

| Source location | Foundation used here | Continue in this project |
|---|---|---|
| Chapter 3, “Open quantum systems,” pp. 97–147 | Reduced open-system dynamics and the Lindblad description | [Clock model and strength budgets](../science/model.md#quantum-clock-class) |
| Chapter 4, “Quantum trajectories,” pp. 148–215 | Conditioning on an observed record, quantum jumps, and averaging inaccessible outcomes | [Restart and hazard bounds](../science/restart_and_hazard.md) |

These chapter routes locate the textbook foundations; reading the entire book first is unnecessary. The equations and clock-specific steps below are supplied locally, with links to their proofs.

## 1. Identify the system before writing its dynamics

The density operator $`\rho`$ describes the entire internal clockwork: its data, ancillas and autonomous controller. The Hamiltonian $`H`$ is time independent, and units have $`\hbar=1`$. A passive external counter records emitted ticks but supplies no feedback. It is outside the internal reset map.

The open-system description allows several physical event channels. For a jump operator $`L`$, use

```math
\mathcal D[L](\rho)
=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
```

The positive term describes the state change associated with an event; the anticommutator supplies the corresponding probability loss between events. When that event’s record is inaccessible, its positive term remains in the averaged evolution. Chapter 4’s distinction between conditioned and unconditioned states makes this bookkeeping understandable.

## 2. Specify what an observed tick does

Every genuine tick prepares one fixed state $`\rho_0`$, independently of the incoming clock state. Its summed event map is

```math
\mathcal J(\rho)=\rho_0\mathrm{tr}(K\rho),\qquad K\ge0.
```

Here $`K`$ is an operator giving the tick intensity: over a short interval $`dt`$, the tick probability is $`\mathrm{tr}(K\rho)dt`$ to first order. It is not a tick count. Several microscopic tick channels may realize this map; only their common observed tick is retained. For Kraus operators $`J_a`$ of $`\mathcal J`$, $`\sum_aJ_a^\dagger J_a=K`$.

The nominal, trace-preserving clock generator is

```math
\mathcal L_{\rm nom}(\rho)
=-i[H,\rho]+\sum_b\mathcal D[L_b](\rho)
+\mathcal J(\rho)-\frac12\{K,\rho\}.
```

The $`L_b`$ channels are intrinsic events that are not ticks. Their effects are charged along with those of all tick channels.

## 3. Add a hidden reset, without adding a tick

An imposed fault restores the same $`\rho_0`$ at state-independent Poisson rate $`\gamma`$. Its averaged generator is

```math
\mathcal L_{\rm fault}(\rho)
=\gamma\bigl[\rho_0\mathrm{tr}\rho-\rho\bigr].
```

This map preserves trace. No fault flag, occurrence time or reset label is returned to the observer. It resets every internal register, including a controller or an ancilla that could otherwise remember elapsed progress. A reset opportunity still occurs at rate $`\gamma`$ when its action happens to leave the state unchanged.

The same final state therefore has two operational meanings: a genuine tick increments the external counter, while a fault does not. This specified event record is part of the model, not an inference from the unconditional density matrix alone.

## 4. Condition only on the record that is available

Let $`\widetilde\rho(t)`$ be the unnormalized state conditioned on no observed tick since the last one, starting at $`\widetilde\rho(0)=\rho_0`$. Then

```math
\frac{d\widetilde\rho}{dt}
=\bigl(\mathcal L_{\rm nom}-\mathcal J
+\mathcal L_{\rm fault}\bigr)(\widetilde\rho).
```

Removing $`\mathcal J`$ excludes observed ticks. The hidden fault term remains complete, including its positive reset term, because faults have not been ruled out by the observed record. The intrinsic uncounted dissipators also remain. Conditioning on no tick is different from conditioning on no physical jump of any kind.

The survival probability and first-tick density follow directly:

```math
S(t)=\mathrm{tr}\widetilde\rho(t),\qquad
w(t)=-S'(t)=\mathrm{tr}[K\widetilde\rho(t)].
```

Thus the trace lost from the no-tick state is exactly the probability of an observed tick. A purely non-Hermitian no-jump amplitude would omit hidden reset histories and is not, in general, the state needed here.

## 5. Charge the complete native strength

The clock model imposes

```math
\inf_{c\in\mathbb R}\|H-cI\|\le\Gamma,
\qquad
K+\sum_bL_b^\dagger L_b\le\Gamma I.
```

An overall energy shift has no effect, which explains the centered Hamiltonian norm. The second inequality caps the sum of all nominal event effects. Adding channels does not give each channel a fresh allowance of $`\Gamma`$. The separately imposed faults add total effect $`\gamma I`$.

For the normalized no-tick state, $`K\le\Gamma I`$ bounds the conditional tick hazard by $`\Gamma`$. This is the bridge from a quantum trajectory to the waiting-time constraint in the [hazard theorem](../science/restart_and_hazard.md#sharp-envelope-at-a-fixed-actual-mean). The bound alone does not characterize the classical clock class: its hidden internal transition rates must also share the native budget.

## 6. A two-stage example keeps the records distinct

Take states $`|0\rangle,|1\rangle`$, $`H=0`$, and $`\rho_0=|0\rangle\langle0|`$. Use an internal jump and an observed tick jump

```math
L=\sqrt\Gamma\,|1\rangle\langle0|,
\qquad
J=\sqrt\Gamma\,|0\rangle\langle1|.
```

Their summed native effect is $`L^\dagger L+J^\dagger J=\Gamma I`$. Fault jumps $`F_j=\sqrt\gamma|0\rangle\langle j|`$ reset either internal state and have total effect $`\gamma I`$. A path may advance to $`|1\rangle`$, suffer a hidden fault, advance again, and finally tick. Only the last event increments the counter; all waiting time contributes to the interval.

Without faults the interval $`X`$ is the sum of two independent rate-$`\Gamma`$ exponentials. With faults, the restart identity below gives

```math
p=\left(\frac\Gamma{\Gamma+\gamma}\right)^2,
\qquad
\mathbb E T=\frac{1-p}{\gamma p}
=\frac2\Gamma+\frac\gamma{\Gamma^2}.
```

The added term counts the cost of erased progress. This small clock illustrates the model; it is not asserted to be optimal at every fault rate.

## 7. Turn complete resets into independent attempts

Let $`X`$ now denote the nominal first-tick time of any admissible clock from $`\rho_0`$. Each fault starts a fresh attempt from exactly that same state. Independence of the Poisson fault process gives the standard restart relation

```math
p=\mathbb E[e^{-\gamma X}],\qquad
\mu:=\mathbb E T=\frac{1-p}{\gamma p}.
```

Successive observed tick intervals are iid because every tick also restores $`\rho_0`$. No failed attempt is discarded. A nominal clock can have a noncompletion component, provided $`p>0`$; faults then give repeated opportunities for a successful attempt.

The transform and moment identities are inherited from [stochastic-restart theory](../references/REFERENCES.md#pal2017), and are derived in [the local proof](../science/restart_and_hazard.md#exact-renewal-transform-and-moments). The sharp fixed-mean envelope and the dynamical optimizations are further project work. The textbook supplies the quantum trajectory language, not those clock theorems.

## 8. Follow the two different optimization routes

Set $`R=\Gamma/\gamma`$ and $`P=\mu^2/\mathrm{Var}T`$. A larger $`P`$ means more regular observed ticks.

For a classical finite-state Markov clock, uniformization converts the nominal first-tick problem into a random number of exponential holding times. The [classical proof](../science/classical_optimum.md) then optimizes over all such networks, including arbitrary topology and start distributions. An Erlang ladder is globally optimal, and

```math
P_{\rm C}^*(R)\sim\frac{\sqrt{3R}}2.
```

For quantum achievability, the [quasiideal construction](../science/quantum_construction.md) is inherited from [Woods et al.](../references/REFERENCES.md#woods2022), a primary research dependency rather than a second educational anchor. The project checks its total native strength and mean before applying the restart estimate. Nearly quadratic clean precision and growing fault exposure produce

```math
\lim_{R\to\infty}
\frac{\log P_{\rm Q}^*(R)}{\log R}=\frac23.
```

The upper bound comes from the [restart-and-hazard envelope](../science/restart_and_hazard.md), a relaxation that also allows an ideal deterministic delay. The finite quantum clocks attain its logarithmic exponent; a sharp quantum prefactor or constant-factor matching law is not established.

## 9. Include the time between the ticks

Slowing a clock can improve per-tick regularity. For a calibrated period $`\mu`$, the passive count estimator is $`\widehat t=\mu N(t)`$. Its long-time timing diffusion is

```math
\mathcal D
=\lim_{t\to\infty}\frac{\mathrm{Var}(\widehat t)}t
=\frac{\mathrm{Var}T}{\mu}
=\frac\mu P.
```

This quantity charges the complete period as well as tick regularity. The [timing proof](../science/timing_diffusion.md) establishes a quantum improvement in this metric too. It first takes the observation-time limit for each fixed device and then optimizes designs in the weak-fault limit. It does not provide a uniform short-time guarantee or a free calibration procedure.

## What the bridge establishes

The anchor supplies the open-system and record-conditioning foundations. Standard restart theory supplies the renewal identities, and existing clock research supplies the clean coherent construction and accuracy-resolution antecedents. This project supplies the specified hidden-reset resource model, the sharp relaxed envelope, the exact classical optimization, the bounded-strength quantum transfer and their timekeeping consequences. [Related work](../references/RELATED_WORK.md) gives the detailed attribution.

The [thirty milestones](MILESTONES.md) organize this route from individual events to the full comparison. Keep the scope visible throughout: all internal memory is reset, faults are unobserved, ticks are unsigned, native strengths are globally bounded, and the classical comparator is an autonomous finite-state Markov jump clock. Local decoherence, surviving feedback memory, arbitrary classical oscillators and microscopic thermodynamic reset costs are separate questions.
