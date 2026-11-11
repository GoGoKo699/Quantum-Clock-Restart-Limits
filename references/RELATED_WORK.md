# Relationship to prior work

[References](REFERENCES.md) · [Model](../science/model.md) · [Classical optimum](../science/classical_optimum.md) · [Quantum construction](../science/quantum_construction.md)

## The question resolved here

The clock is autonomous and time homogeneous. It produces genuine ticks, each of which restores the complete clockwork to one fixed state. Independent unobserved Poisson faults restore that same state at rate $`\gamma`$ without producing a tick. Every persistent internal register is included in this reset. A passive external tick counter is exempt: it only records the output and supplies no feedback to the clock. Native classical exit activity, and the quantum Hamiltonian and total native jump effect, obey the explicit strength budget at scale $`\Gamma`$. The comparison concerns renewal precision $`\mathcal P=\mu^2/\mathrm{Var}T`$ and $`R=\Gamma/\gamma`$.

The [classical theorem](../science/classical_optimum.md) optimizes over all finite-state continuous-time Markov chains in this class: a rate-$`\Gamma`$ Erlang ladder is globally optimal, with an exact integer optimization and weak-fault precision $`\mathcal P_{\rm C}^{\star}\sim(\sqrt3/2)\sqrt R`$. The [quantum result](../science/quantum_construction.md) establishes optimal logarithmic exponent $`2/3`$ as $`R\to\infty`$. It does not establish a sharp quantum constant or a constant-factor $`\Theta(R^{2/3})`$ law.

The contribution is the optimized complete-restart robustness comparison under these budgets. Ideal coherent clocks, restart renewal theory and the noiseless accuracy-resolution advantage are antecedents.

## Restart theory supplies the framework

[Pal and Reuveni](REFERENCES.md#pal2017) develop the generic first-passage recursion and transform framework for independent restart. Those ingredients are used directly. The fault process here is fixed by the device’s noise rate; clock design and mean tick time are optimized instead of selecting a favorable restart protocol to speed completion.

[Reuveni](REFERENCES.md#reuveni2016) proves unit relative standard deviation at an interior nonzero Poisson restart rate that minimizes mean completion time. That stationary-point statement does not forbid high precision at an imposed small fault rate. Our objective is variance relative to squared mean, with a native strength budget.

[Starkov and Belan](REFERENCES.md#starkov2023) derive universal bounds on restarted mean completion times in terms of statistics of the original process. These are relevant performance limits, but they do not identify the rate-bounded classical precision optimizer or the quantum fault-strength exponent used here. The present proofs keep restart identities separate from the additional dynamical constraints.

## Ideal quantum clocks and the rate account

[Woods et al.](REFERENCES.md#woods2022) establish the dimensional advantage of coherent clocks and construct quasiideal reset clocks with accuracy arbitrarily close to quadratic in dimension. That clean construction supplies quantum achievability here. The [resource transfer](../science/quantum_construction.md) checks its Hamiltonian bandwidth, the summed effect of all tick channels and the actual mean before adding faults. This repository does not claim a new ideal-clock accuracy theorem.

[Meier et al.](REFERENCES.md#meier2023) prove the fundamental accuracy-resolution relation for memoryless elementary tick generation. Their bounded-rate variance limitation is the physical antecedent of the [bounded-hazard proof](../science/restart_and_hazard.md). The extra step here is the complete-restart fluctuation floor and optimization against native dynamics, including the exact classical result.

[Meier et al.](REFERENCES.md#meier2025) establish an exponential precision-versus-entropy advantage for a coherent ring clock. Their Methods subsection “Undesired environment interactions” also studies losses: environmental decays are registered as ticks and prematurely reinitialize the clock. The stability analysis and Extended Data Fig. 3 identify a finite best chain length at fixed loss strength. This is an important prior noise-and-size optimization. Here faults instead reset the complete internal clockwork without producing a recorded tick, and the optimization covers all clocks in the stated bounded-strength classes. The control parameter is $`\Gamma/\gamma`$; no heat, work or entropy cost is inferred from those rates.

## Stochastic clock uncertainty relations

[Macieszczak](REFERENCES.md#macieszczak2024) derives a tight kinetic uncertainty relation based on configuration lifetimes and extends it to conditional waiting-time statistics in semi-Markov processes, including quantum reset processes. [Prech et al.](REFERENCES.md#prech2025) solve optimal long-time time estimation from classical Markov trajectories and relate the precision ceiling to mean residual time.

These works supply the broader theory behind rate-limited stochastic clocks. Our classical proof additionally exploits the absorption-step representation under uniformization and the specific full-restart map to identify the exact optimizing ladder. The first-tick/renewal figure of merit here is not an optimum over every estimator built from a complete timing or transition record. Fault times are unobserved and cannot serve as extra clock data.

## Engineered transport is a distinct construction route

[Nelmes et al.](REFERENCES.md#nelmes2026) numerically optimize terminal couplings of perfect-state-transfer spin chains and report the limiting precision-resolution exponent. Their bulk profile is $`J_i=J_0\sqrt{i(N-i)}`$. A fixed sink decay rate therefore does not itself bound all coherent couplings or Hamiltonian bandwidth uniformly as $`N`$ grows. Their repeated-operation proposal also uses a coarse timed quench. Applying it to the present class would require a strength rescaling, renewed waiting-time estimates and a compatible autonomous reset implementation. It is not used to certify achievability here.

## Monitored quantum restart has a different uncertainty relation

[Yin et al.](REFERENCES.md#yin2025) study quantum recurrence under repeated measurements and finite restart, including the broadening of mean-recurrence resonances and an associated time-energy relation. Their monitored hitting-time and sampling/restart resources differ from a continuously operating autonomous clock interrupted by independent, unobserved Poisson faults. Their uncertainty relation is not the classical/quantum optimization over $`R`$ established here.

## Relation to Quantum Clock Entropy Limits

The [pinned companion model](REFERENCES.md#clock-entropy) has one complete rank-one forward/reverse pair. Both jump directions are counted, and the observable is the stationary signed current with precision $`j/D`$. Its resource is the logarithm of the rate ratio, interpreted thermodynamically only under further implementation assumptions. It establishes an affinity-only ceiling and a logarithmic affinity-cost order law.

Here all genuine ticks have the same sign, while faults are not counted and restart the entire internal clockwork to the same state as a tick. The imposed map $`\gamma(\rho_0\mathrm{tr}\rho-\rho)`$ is generally nonunital, including the pure reset used in the quantum construction. The companion’s proved unital-background extension consequently does not supply the present fault theorem. Neither result is an entropy interpretation or a general noise theorem for the other model. Shared complete-reset and renewal ideas are credited once; the operational optimization differs.

## Scope of the comparison

These comparisons identify the primary constructions, bounds and model distinctions used in the proof chain. They do not assert exhaustive priority coverage. The classical conclusion concerns stochastic autonomous Markov jump clocks; unrestricted classical deterministic oscillators and free externally timed controls have different resources. The quantum conclusion concerns the specified global complete-restart faults, with no protected internal memory surviving them. Other noise channels, local fault tolerance and microscopic implementation costs require separate results.
