# Autonomous clocks with hidden restart faults

[Scientific overview](README.md) · [Restart bounds](restart_and_hazard.md) · [Classical optimum](classical_optimum.md) · [Quantum construction](quantum_construction.md)

## Task and performance

A clock emits identical, unsigned ticks without an external switching schedule. Every tick restores the whole internal clockwork to one fixed state. An independent, unobserved Poisson fault also restores that same state but emits no tick. The task is to optimize the timing statistics over all finite clock designs, while charging their intrinsic dynamical strengths and the entire waiting time, including failed intervals.

Let $`T`$ denote an interval between observed ticks, with mean $`\mu`$ and variance $`v`$. Tick precision, also called accuracy in parts of the clock literature, is
```math
P=\frac{\mu^2}{v}.
```
This definition concerns regularity of actual output ticks. For each fixed device, the passive output count $`N(t)`$ has long-time rate $`1/\mu`$. Its calibrated count estimator $`\widehat t=\mu N(t)`$ has timing diffusion
```math
\mathcal D=\lim_{t\to\infty}\frac{\operatorname{Var}(\widehat t)}{t}
=\frac{v}{\mu}.
```
The [timing account](timing_diffusion.md) proves the ordered-limit statement and distinguishes precision from elapsed-time accuracy. The mean is a supplied calibration of the specified device, rather than an unknown parameter estimated jointly with time.

## Quantum clock class

The internal Hilbert space is finite dimensional. A normal tick is a completely positive map
```math
\mathcal J(\rho)=\rho_0\operatorname{tr}(K\rho),\qquad K\geq0,
```
where $`\rho_0`$ is the fixed initial state. Choose any Kraus operators $`J_a`$ for this map, so that $`\sum_aJ_a^\dagger J_a=K`$. Several microscopic channels may implement an observed tick. Their unobserved labels are summed; the reset condition is imposed on that summed map, whose normalized output is always $`\rho_0`$.

The time-independent nominal generator is
```math
\mathcal L_{\rm nom}(\rho)
=-i[H,\rho]+\sum_b\mathcal D[L_b](\rho)
+\mathcal J(\rho)-\frac12\{K,\rho\},
```
where
```math
\mathcal D[L](\rho)=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
```
The $`L_b`$ channels are uncounted intrinsic events. The declared strength scale $`\Gamma>0`$ obeys
```math
\inf_{c\in\mathbb R}\|H-cI\|\leq\Gamma,\qquad
K+\sum_bL_b^\dagger L_b\leq\Gamma I.
```
The second bound is on the total nominal event effect, including all tick channels. It is not a separate allowance of $`\Gamma`$ for each channel. The resource convention uses the specified physical event decomposition. Adding irrelevant identity jumps does not strengthen a clock.

Faults add
```math
\mathcal L_{\rm fault}(\rho)
=\gamma\big[\rho_0\operatorname{tr}\rho-\rho\big],
\qquad \gamma>0.
```
For a spectral decomposition $`\rho_0=\sum_a p_a|a\rangle\langle a|`$, this has jump operators
```math
F_{aj}=\sqrt{\gamma p_a}\,|a\rangle\langle j|,
\qquad \sum_{a,j}F_{aj}^\dagger F_{aj}=\gamma I.
```
Thus reset opportunities form a state-independent Poisson process of rate $`\gamma`$. They count as imposed faults even when a reset happens to leave the current clock state unchanged. Their labels and occurrence times are inaccessible. The fault effect is additional to the nominal $`\Gamma`$ budget.

All internal registers, ancillas and autonomous control degrees of freedom belong to the clockwork and are reset by a fault. A passive external output counter may retain ticks; it cannot feed information back into the device. A protected auxiliary clock, an observed fault flag, an external timed control schedule or a surviving feedback memory changes this class.

## Classical clocks under the same event budget

The classical subclass has a finite set of internal states, a fixed start distribution $`\alpha`$, and time-homogeneous transition rates. At state $`i`$, let $`a_{ij}\geq0`$ be its uncounted rate to state $`j\ne i`$, and let $`k_i\geq0`$ be its tick rate. Every tick restarts $`\alpha`$, and
```math
\sum_{j\ne i}a_{ij}+k_i\leq\Gamma
\quad\hbox{for every }i.
```
A marked tick is included even if the subsequent draw from $`\alpha`$ returns the same internal state. The first-tick transient generator $`B`$ therefore has entries
```math
B_{ij}=a_{ij}\ (j\ne i),\qquad
B_{ii}=-\sum_{j\ne i}a_{ij}-k_i.
```
Fault reset opportunities at rate $`\gamma`$ also restart $`\alpha`$. The exact optimum permits arbitrary finite state count, nonreversible transitions, arbitrary topology and arbitrary start distributions. Detailed balance is not assumed.

This class embeds in the quantum model using diagonal states, $`H=0`$, transition jumps $`\sqrt{a_{ij}}|j\rangle\langle i|`$, and tick Kraus operators returning $`\alpha`$. It includes more than a particular ladder construction. Conversely, a deterministic continuous-phase oscillator is not a bounded-rate finite-state Markov clock, and is outside the comparison.

## Renewal reduction and admissibility

Let $`X\in[0,\infty]`$ be the nominal first-tick time from the common reset state, before adding faults. A nominal dark component is allowed. Put
```math
p=\mathbb E[e^{-\gamma X}],\qquad e^{-\gamma\infty}=0.
```
A clock is admissible if $`p>0`$. Repeating independent reset attempts then produces a tick almost surely. The resulting $`T`$ has an exponential tail: some finite interval has a positive probability of completion before the next fault, and repeated disjoint intervals give a geometric tail bound. Consequently every faulty-device moment used here is finite, even if $`X`$ has a defective part.

Complete tick and fault resets make successive $`T`$'s iid. The exact Poisson-restart transform and moments are proved in [restart and hazard bounds](restart_and_hazard.md). No branch is postselected, no failed interval is omitted, and no conditional success clock is substituted for the physical output.

## Optimization and limiting order

Set
```math
R=\frac{\Gamma}{\gamma},\qquad r=R^{-1}.
```
Write $`P_{\rm C}^{*}(R)`$ and $`P_{\rm Q}^{*}(R)`$ for suprema of $`P`$ over the classical and quantum classes above. Dimension and the supplied static generator may vary with $`R`$, but all remain finite at each $`R`$. A common rescaling of time changes $`\Gamma,\gamma,\mu,v`$ consistently and leaves $`R`$ and $`P`$ invariant.

The established precision laws are
```math
P_{\rm C}^{*}(R)\sim\frac{\sqrt{3R}}2,\qquad
\lim_{R\to\infty}\frac{\log P_{\rm Q}^{*}(R)}{\log R}=\frac23.
```
The quantum statement fixes the logarithmic exponent. It does not give a sharp prefactor or a constant-factor $`\Theta(R^{2/3})`$ law. It follows from an all-device $`O(R^{2/3})`$ converse and, for every fixed $`0<\varepsilon<1`$, finite quantum clocks with
```math
P\geq c_\varepsilon R^{(2-\varepsilon)/(3-\varepsilon)}
```
for all sufficiently large $`R`$.

For elapsed-time diffusion, first take $`t\to\infty`$ for each fixed finite device. Only then take the infimum over designs and the weak-fault limit. With $`\mathcal D_{\rm C}^{*},\mathcal D_{\rm Q}^{*}`$ denoting these infima,
```math
\mathcal D_{\rm C}^{*}=\Theta(\Gamma^{-1}),\qquad
\Gamma\mathcal D_{\rm Q}^{*}=R^{-1/3+o(1)}.
```
Startup and calibration can matter at observation times that grow jointly with $`R`$. No uniform finite-horizon guarantee follows from the displayed ordered limit.

## Physical interpretation and limits

A coherent wavepacket can traverse many distinguishable clock states with much less spreading than a classical jump sequence. Increasing the traversal time improves the nominal clock, but increases exposure to a fault that erases its progress. The optimal noisy clock balances these two effects. The [exact classical optimizer](classical_optimum.md) and [bounded-strength coherent construction](quantum_construction.md) identify different balances.

The model is an effective autonomous Lindbladian resource theory. It supplies engineered time-independent tick and reset interfaces and bounds their total rates and the Hamiltonian bandwidth. It does not charge microscopic bath preparation, coherent-reset synthesis, fabrication, geometric locality, description complexity or thermodynamic entropy per reset. The result should not be read as an implementation-efficiency or heat-cost theorem.

Faults erase the entire internal device. Independent local dephasing, partial resets, surviving memories, correlated or observed fault times, signed ticks and clocks with nonrenewal output correlations require separate analysis. These boundaries are part of the claim.

The [related-work account](../references/RELATED_WORK.md) credits the inherited clean quantum construction, restart identities, and precision–resolution and kinetic inequalities, and identifies the distinct noise-optimization result.
