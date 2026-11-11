# Thirty milestones for Quantum Clock Restart Limits

[Learning route](README.md) · [Anchor bridge](BRIDGE.md) · [Scientific account](../science/README.md)

This map follows the scientific problem: how does unobserved complete-reset noise change the best autonomous classical and quantum clock at fixed native strength? Its thirty stable understanding targets apply to any reader. They organize the main argument and its essential boundaries; they do not cover every technical estimate in the source construction.

The single educational anchor is **Howard M. Wiseman and Gerard J. Milburn, *Quantum Measurement and Control* (2010)**. The verified chapter-level pointers used below are Chapter 3, **Open quantum systems**, and Chapter 4, **Quantum trajectories**. The [bridge](BRIDGE.md) identifies their role and translates the notation. A chapter pointer supplies background, not attribution of the project's restart optimization to the textbook. Research-level imported ingredients retain their primary-source citations in the scientific account.

The allocation is **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The background phase joins individual states, generators and observed events into the matched clock model. The narrative phase joins the local restart mechanism, universal and classical optimizations, coherent construction and elapsed-time readout into the complete result. Each phase ends with a global synthesis.

## Phase I — Background/preliminaries, M01–M12

### M01 — Clock state and observable output

- **Central question:** What does the clock's internal state describe, and what information leaves it?
- **Understanding target:** Distinguish a classical state distribution or quantum density operator from the external record of designated ticks. Explain why the internal clockwork and its output counter have different roles.
- **Dependencies and story role:** No earlier milestone. Establishes the local objects before introducing their dynamics.
- **Conceptual connection:** State probabilities become clock predictions only after an observed event interface has been specified.
- **Source pointers:** Anchor, Chapter 3. Project: [Task and performance](../science/model.md#task-and-performance) and [Quantum clock class](../science/model.md#quantum-clock-class).

### M02 — Autonomous time-homogeneous dynamics

- **Central question:** What makes a clock autonomous in this model?
- **Understanding target:** Explain how one fixed generator evolves a state without an external switching schedule. Distinguish a static physical parameter from a control pulse whose timing would require another clock.
- **Dependencies and story role:** M01. Adds the local dynamical rule governing the clockwork.
- **Conceptual connection:** The open-system master equation supplies a model of ongoing operation rather than a sequence of externally scheduled instructions.
- **Source pointers:** Anchor, Chapter 3. Project: [Quantum clock class](../science/model.md#quantum-clock-class) and [Add the same unobserved restart channel](../science/quantum_construction.md#5-add-the-same-unobserved-restart-channel).

### M03 — Hamiltonian motion and its strength

- **Central question:** Which part of the generator supplies coherent motion, and how is its size charged?
- **Understanding target:** Identify the Hamiltonian term and the centered norm bound. Explain why adding a scalar multiple of the identity changes no dynamics, while increasing the spectral width changes the native strength resource.
- **Dependencies and story role:** M02. Introduces the coherent part of the local budget before comparing clock designs.
- **Conceptual connection:** A dimension-dependent accuracy improvement must be rechecked when the Hamiltonian bandwidth is fixed.
- **Source pointers:** Anchor, Chapter 3. Project: [Quantum clock class](../science/model.md#quantum-clock-class) and [Choose the physical timescale](../science/quantum_construction.md#choose-the-physical-timescale).

### M04 — Jump effects and the total event budget

- **Central question:** Why is the sum of jump effects the relevant rate constraint?
- **Understanding target:** Relate each jump operator to its event intensity and sum all intrinsic tick and uncounted effects. Distinguish one global allowance from a separate allowance for each channel.
- **Dependencies and story role:** M02–M03. Completes the local dynamical resource account.
- **Conceptual connection:** More channels or more internal states cannot supply free aggregate jump activity under the declared budget.
- **Source pointers:** Anchor, Chapters 3–4. Project: [Quantum clock class](../science/model.md#quantum-clock-class) and [Bounding the sum of all tick effects](../science/quantum_construction.md#3-bounding-the-sum-of-all-tick-effects).

### M05 — A tick is a reset instrument

- **Central question:** What operation both announces a tick and starts the next clock cycle?
- **Understanding target:** Read the tick map as a state-dependent probability followed by the same normalized reset state. Recognize that several microscopic tick channels can be combined into one observed tick when their labels are discarded.
- **Dependencies and story role:** M01 and M04. Connects the internal dynamics to the elementary output event.
- **Conceptual connection:** A measurement outcome is specified by both its probability and its state update; the latter determines whether clock cycles repeat independently.
- **Source pointers:** Anchor, Chapter 4. Project: [Quantum clock class](../science/model.md#quantum-clock-class) and [An explicit device at unit strength](../science/finite_example.md#1-an-explicit-device-at-unit-strength).

### M06 — Conditioning on no observed tick

- **Central question:** How is a waiting-time law extracted from the open-system evolution?
- **Understanding target:** Distinguish the unconditional state from an unnormalized state conditioned on no tick. Interpret its trace as survival and the tick effect as the conditional hazard; explain why uncounted events remain active.
- **Dependencies and story role:** M04–M05. Turns an event interface into a local first-tick description.
- **Conceptual connection:** Quantum trajectories translate the master equation into the survival and absorption quantities used in the clock comparison.
- **Source pointers:** Anchor, Chapter 4. Project: [Notation and regularity](../science/restart_and_hazard.md#notation-and-regularity) and [Infinite-horizon moments from finite linear equations](../science/finite_example.md#2-infinite-horizon-moments-from-finite-linear-equations).

### M07 — Hidden whole-clock reset faults

- **Central question:** What distinguishes an imposed fault from a genuine tick?
- **Understanding target:** Explain the state-independent Poisson reset map, its separately charged rate, and the absence of an observed fault flag. Identify every internal register as part of the reset, including autonomous controls and memory.
- **Dependencies and story role:** M05–M06. Adds the local noise mechanism whose accumulated effect is the central question.
- **Conceptual connection:** The same state update can have a different operational meaning when one event is reported and the other is hidden.
- **Source pointers:** Anchor, Chapters 3–4. Project: [Quantum clock class](../science/model.md#quantum-clock-class) and [Add the same unobserved restart channel](../science/quantum_construction.md#5-add-the-same-unobserved-restart-channel).

### M08 — Intrinsic first passage and admissibility

- **Central question:** Can an intrinsic clock with a dark component still operate after resets are added?
- **Understanding target:** Interpret the intrinsic time as possibly infinite, its Laplace transform as exponentially weighted completion probability, and positive success before a fault as the admissibility condition. Distinguish intrinsic moments from actual faulty-device moments.
- **Dependencies and story role:** M06–M07. Defines the probability-law inputs without excluding relevant boundary cases.
- **Conceptual connection:** Independent reset attempts can produce finite actual waiting-time moments even when the nominal process has unsuccessful paths.
- **Source pointers:** Anchor, Chapter 4, for conditioned trajectories. Project: [Renewal reduction and admissibility](../science/model.md#renewal-reduction-and-admissibility) and [Notation and regularity](../science/restart_and_hazard.md#notation-and-regularity).

### M09 — Renewal cycles and the passive counter

- **Central question:** Which independence follows from complete resets, and what memory may survive?
- **Understanding target:** Explain why each tick and each fault starts an identical independent attempt. Separate prohibited surviving internal feedback memory from the permitted external tick counter, which only records output and never controls the device.
- **Dependencies and story role:** M05, M07–M08. Joins the local reset rule into the repeated operating process.
- **Conceptual connection:** A physical reset assumption becomes the iid waiting-time structure needed for renewal precision and timekeeping.
- **Source pointers:** Anchor, Chapter 4. Project: [Quantum clock class](../science/model.md#quantum-clock-class), [Renewal reduction and admissibility](../science/model.md#renewal-reduction-and-admissibility), and [Calibrated count readout](../science/timing_diffusion.md#calibrated-count-readout).

### M10 — Tick precision, period and elapsed-time diffusion

- **Central question:** Why does a regular tick sequence not automatically provide the best elapsed-time estimate?
- **Understanding target:** Distinguish the mean period, interval variance, dimensionless precision and timing diffusion. Explain the extra period factor in the calibrated count error and retain every failed interval in elapsed time.
- **Dependencies and story role:** M08–M09. Connects individual-cycle statistics to two distinct operating objectives.
- **Conceptual connection:** Renewal regularity and calibrated timekeeping use the same waiting law but optimize different combinations of its moments.
- **Source pointers:** Anchor, Chapter 4, for the event-record foundation. Project: [Task and performance](../science/model.md#task-and-performance) and [Calibrated count readout](../science/timing_diffusion.md#calibrated-count-readout).

### M11 — The classical Markov comparator

- **Central question:** What classical designs are covered by the comparison?
- **Understanding target:** Specify a finite-state continuous-time Markov clock with arbitrary topology, initial distribution and state-dependent rates. Include the tick in each state's total nominal escape rate, and explain its embedding as a diagonal quantum model.
- **Dependencies and story role:** M02, M04–M05 and M07. Builds the complete classical class rather than selecting a convenient ladder baseline.
- **Conceptual connection:** A fair comparison applies the same event budget and hidden full-reset interface to every allowed classical network.
- **Source pointers:** Anchor, Chapter 3, for the master-equation framework. Project: [Classical clocks under the same event budget](../science/model.md#classical-clocks-under-the-same-event-budget) and [Model and statement](../science/classical_optimum.md#model-and-statement).

### M12 — Assemble the matched optimization problem

- **Central question:** What is held fixed, what is optimized, and what falls outside the result?
- **Understanding target:** State the task using the strength-to-fault ratio, finite but variable dimension, genuine ticks and hidden complete resets. Explain why protected phase references, active external counters, unbounded classical internal rates and deterministic continuous-phase oscillators change the problem.
- **Dependencies and story role:** M01–M11. Integrates the background phase into the global model required by every subsequent theorem.
- **Conceptual connection:** Operational access, state updates and global strength constraints jointly determine which classical and quantum advantage can be claimed.
- **Source pointers:** Anchor, Chapters 3–4, as combined dynamical background. Project: [Optimization and limiting order](../science/model.md#optimization-and-limiting-order) and [Physical interpretation and limits](../science/model.md#physical-interpretation-and-limits).

## Phase II — Narrative/innovation, M13–M30

### M13 — The first-attempt restart recursion

- **Central question:** How does one successful or interrupted attempt generate the complete faulty waiting law?
- **Understanding target:** Separate a tick before the first fault from a fault before the tick, followed by a fresh copy of the process. Explain how this decomposition produces the exact noisy Laplace transform.
- **Dependencies and story role:** M08–M09 and M12. Begins the new account at the smallest repeating mechanism.
- **Conceptual connection:** The trajectory reset interface becomes the inherited first-passage-under-restart recursion; no failed attempt is discarded.
- **Source pointers:** Anchor, Chapter 4, for reset trajectories. Project: [Exact renewal transform and moments](../science/restart_and_hazard.md#exact-renewal-transform-and-moments) and [Restart theory supplies the framework](../references/RELATED_WORK.md#restart-theory-supplies-the-framework).

### M14 — Actual moments from two Laplace quantities

- **Central question:** Which intrinsic quantities determine the actual mean and variance at a fixed fault rate?
- **Understanding target:** Interpret the exponentially weighted success probability and weighted completion time in the restart moment identities. Explain why fixing the actual noisy mean fixes one quantity and leaves a single moment objective to optimize.
- **Dependencies and story role:** M10 and M13. Converts the local recursion into the variables used by both universal and classical bounds.
- **Conceptual connection:** A full stochastic process can be compared through a small set of exact moment data, while still charging all restarts.
- **Source pointers:** Anchor, Chapter 4, for the conditional-event starting point. Project: [Exact renewal transform and moments](../science/restart_and_hazard.md#exact-renewal-transform-and-moments) and [Restart moments and uniformization](../science/classical_optimum.md#restart-moments-and-uniformization).

### M15 — A variance penalty from restart alone

- **Central question:** Why do hidden faults broaden even a perfectly periodic intrinsic completion time?
- **Understanding target:** Explain the Jensen restart floor and its deterministic-delay equality condition. Distinguish that distribution-only result from a physically realizable finite-rate clock and interpret its small-fault penalty.
- **Dependencies and story role:** M14. Isolates the fluctuation mechanism shared by all designs before adding their dynamical restrictions.
- **Conceptual connection:** Randomly erased progress produces timing uncertainty even when the unfinished intrinsic process would have no timing spread.
- **Source pointers:** Anchor, Chapter 4, for hidden-event averaging. Project: [A distribution-only restart floor](../science/restart_and_hazard.md#a-distribution-only-restart-floor). The convexity argument is supplied locally, beyond the anchor background.

### M16 — The sharp bounded-hazard envelope

- **Central question:** At a fixed actual mean, which intrinsic bounded-hazard law minimizes faulty variance?
- **Understanding target:** Explain the delayed-exponential optimizer, the feasible mean range and the single-crossing comparison of survival functions. Keep the sharp relaxed envelope separate from the finite autonomous quantum class.
- **Dependencies and story role:** M06, M14–M15. Adds native tick-rate physics to the restart mechanism and identifies a universal local extremizer.
- **Conceptual connection:** The bounded tick effect constrains survival, turning the moment optimization into an ordered comparison of feasible waiting laws.
- **Source pointers:** Anchor, Chapters 3–4, for effects and conditional hazards. Project: [Sharp envelope at a fixed actual mean](../science/restart_and_hazard.md#sharp-envelope-at-a-fixed-actual-mean) and [The inherited accuracy-resolution bound](../science/restart_and_hazard.md#the-inherited-accuracy-resolution-bound).

### M17 — Optimize the universal precision ceiling

- **Central question:** What clock period best balances intrinsic rate limitation against erased progress?
- **Understanding target:** Explain why the scalar hazard-envelope optimizer is unique and how its weak-fault balance produces a two-thirds precision ceiling. Identify its sharp constant as a relaxed-law constant rather than a proved finite-quantum optimum.
- **Dependencies and story role:** M10 and M16. Joins fixed-mean local bounds into the global converse over every admissible quantum design.
- **Conceptual connection:** Increasing the mean period initially concentrates the tick, but eventually increases exposure to faults; the global optimum lies between these tendencies.
- **Source pointers:** Anchor, Chapters 3–4, for the dynamical setup. Project: [Unique optimum of the relaxed precision envelope](../science/restart_and_hazard.md#unique-optimum-of-the-relaxed-precision-envelope). The optimization and asymptotic comparison are project derivations.

### M18 — Uniformize every classical network

- **Central question:** How can one analyze arbitrary bounded-rate classical clocks without enumerating their graphs?
- **Understanding target:** Explain uniformization as a common Poisson event schedule plus an embedded discrete absorption process. Interpret the intrinsic first-tick law as a mixture of rate-bounded Erlang waiting times, including possible noncompletion.
- **Dependencies and story role:** M11 and M14. Supplies the classical structure missing from a tick-hazard-only bound.
- **Conceptual connection:** The total internal rate budget constrains all hidden stages, so an unrestricted graph still belongs to a common family of first-passage laws.
- **Source pointers:** Anchor, Chapter 3, as master-equation background. Project: [Restart moments and uniformization](../science/classical_optimum.md#restart-moments-and-uniformization). Uniformization and its absorption representation are explained in that project section.

### M19 — Adjacent stages give the fixed-mean classical frontier

- **Central question:** Which mixtures of classical absorption-step counts are best at one actual noisy mean?
- **Understanding target:** Explain the concave interpolation over integer stage counts and why neighboring Erlang lengths attain the frontier. Distinguish this fixed-mean mixture from a claim that every optimal clock must use a mixed reset state.
- **Dependencies and story role:** M14 and M18. Solves the local classical moment problem before optimizing its mean.
- **Conceptual connection:** A continuous convexity bound becomes sharper when the physically allowed absorption counts lie on a discrete grid.
- **Source pointers:** Anchor, Chapter 3, for the underlying stochastic generator only. Project: [The exact frontier at a fixed observed mean](../science/classical_optimum.md#the-exact-frontier-at-a-fixed-observed-mean). The grid-envelope proof is a project result.

### M20 — The global classical optimum is a ladder

- **Central question:** Can any finite classical Markov network outperform the best rate-bounded Erlang ladder?
- **Understanding target:** Explain why optimizing the fixed-mean frontier chooses a pure Erlang endpoint and how unimodality controls the integer optimizer. State the square-root weak-fault law with its sharp constant and its all-design domain.
- **Dependencies and story role:** M12 and M18–M19. Integrates the classical argument into an exact global benchmark.
- **Conceptual connection:** The theorem justifies the ladder comparator through optimization over arbitrary finite topology and dimension, rather than assuming it as a restricted baseline.
- **Source pointers:** Anchor, Chapter 3, for Markov dynamics. Project: [Why a pure Erlang clock is globally optimal](../science/classical_optimum.md#why-a-pure-erlang-clock-is-globally-optimal) and [Locating the optimizer and controlling all scales](../science/classical_optimum.md#locating-the-optimizer-and-controlling-all-scales).

### M21 — Import the clean coherent clock faithfully

- **Central question:** Which quantum ingredient is inherited, and what physical mechanism makes it useful?
- **Understanding target:** Describe a coherent phase wavepacket, a static absorption profile and tick-reset operators. Attribute the near-quadratic clean dimensional accuracy to the quasiideal construction without treating it as an already proved noisy-strength advantage.
- **Dependencies and story role:** M03–M06 and M12. Begins the achievability route with its actual scientific antecedent.
- **Conceptual connection:** Coherent propagation suppresses intrinsic timing spread; restart robustness still requires a separate rate, mean and noise analysis.
- **Source pointers:** Anchor, Chapters 3–4. Project: [The clean-clock resource lemma](../science/quantum_construction.md#1-the-clean-clock-resource-lemma), [What is inherited](../science/quantum_construction.md#what-is-inherited), and [Ideal quantum clocks and the rate account](../references/RELATED_WORK.md#ideal-quantum-clocks-and-the-rate-account).

### M22 — Rescale the complete quantum generator

- **Central question:** Does the coherent construction obey a fixed native strength when dimension grows?
- **Understanding target:** Explain the common physical timescale rescaling and check both centered Hamiltonian norm and the summed effect of all tick operators. Retain the factor relating the absorption potential to the full tick effect.
- **Dependencies and story role:** M03–M04 and M21. Makes the imported mechanism admissible under the same global budget as the converse and classical benchmark.
- **Conceptual connection:** A dimensional accuracy theorem becomes a resource-accounted clock construction only after every dynamical term is scaled consistently.
- **Source pointers:** Anchor, Chapters 3–4. Project: [Bounding the sum of all tick effects](../science/quantum_construction.md#3-bounding-the-sum-of-all-tick-effects) and [Choose the physical timescale](../science/quantum_construction.md#choose-the-physical-timescale).

### M23 — Control the actual clean mean, including tails

- **Central question:** Why is a narrow visible tick peak insufficient to establish the mean-period scaling?
- **Understanding target:** Explain how survival estimates and diverging clean precision control a rare far tail. Distinguish the mean proved from those estimates from an assumed traversal time or a truncated numerical trace.
- **Dependencies and story role:** M08, M10 and M21–M22. Completes the clean moment information required for a valid fault transfer.
- **Conceptual connection:** The strength rescaling changes physical time, while moment control ensures that low-probability events do not invalidate the proposed balance.
- **Source pointers:** Anchor, Chapter 4, for survival and first-tick statistics. Project: [Clean precision and the actual mean](../science/quantum_construction.md#4-clean-precision-and-the-actual-mean).

### M24 — Transfer clean moments through hidden resets

- **Central question:** How much extra variance can faults introduce without assumptions on intrinsic third moments?
- **Understanding target:** Explain the two-moment restart stability estimate and its small-exposure conditions. Use the accompanying mean bounds to keep the actual noisy period comparable to the clean one.
- **Dependencies and story role:** M14 and M23. Connects the admissible clean family to actual faulty performance.
- **Conceptual connection:** Exact restart identities and elementary inequalities avoid an uncontrolled expansion in higher moments or an omitted long tail.
- **Source pointers:** Anchor, Chapter 4, for the renewal interface. Project: [Stability using only the first two intrinsic moments](../science/restart_and_hazard.md#stability-using-only-the-first-two-intrinsic-moments) and [Add the same unobserved restart channel](../science/quantum_construction.md#5-add-the-same-unobserved-restart-channel).

### M25 — Match the quantum logarithmic exponent

- **Central question:** Which finite dimension balances clean quantum spread against reset exposure?
- **Understanding target:** Explain the dimension-dependent balance and combine achievability with the universal ceiling. State the optimal two-thirds logarithmic exponent while preserving the fixed exponent-loss parameter, dimension threshold and unresolved subpower factors or sharp constant.
- **Dependencies and story role:** M17 and M21–M24. Integrates the quantum route into the global classical-versus-quantum precision law.
- **Conceptual connection:** The inherited coherent advantage changes the optimal dependence on imposed fault strength after all native strengths and the actual mean are charged.
- **Source pointers:** Anchor, Chapters 3–4, for the static quantum generator and tick trajectories. Project: [Precision after faults](../science/quantum_construction.md#6-precision-after-faults) and [Optimization and limiting order](../science/model.md#optimization-and-limiting-order).

### M26 — Read a finite witness against the all-classical optimum

- **Central question:** What does an explicit finite device demonstrate beyond an asymptotic construction?
- **Understanding target:** Trace the stated phase-clock generator, resource bounds and infinite-horizon moment calculations to its finite precision comparison. Explain why the classical column is an all-CTMC optimum and why floating-point agreement is a numerical witness rather than a formal interval certificate.
- **Dependencies and story role:** M06, M20 and M22–M25. Connects the global theorem to a concrete admissible clock without replacing its analytical proof.
- **Conceptual connection:** Independent resolvent calculations check an explicit operating model and include hidden resets directly, while the theorem supplies the unrestricted comparator.
- **Source pointers:** Anchor, Chapters 3–4. Project: [An explicit device at unit strength](../science/finite_example.md#1-an-explicit-device-at-unit-strength), [Infinite-horizon moments from finite linear equations](../science/finite_example.md#2-infinite-horizon-moments-from-finite-linear-equations), and [Finite results](../science/finite_example.md#3-finite-results).

### M27 — Convert tick statistics into elapsed-time error

- **Central question:** Does charging the entire tick period remove the advantage?
- **Understanding target:** Explain why the calibrated count estimator has long-time variance per unit time equal to interval variance divided by mean. Identify the bounded startup contribution and the order in which the observation-time and weak-fault limits are taken.
- **Dependencies and story role:** M09–M10 and M24–M26. Joins repeated operation to the operational timekeeping task.
- **Conceptual connection:** Renewal independence permits a long-time count-error theorem; no fault timestamp, externally timed sampling schedule or omitted waiting interval is needed.
- **Source pointers:** Anchor, Chapter 4, for the event record. Project: [Calibrated count readout](../science/timing_diffusion.md#calibrated-count-readout) and [Limits, initialization and attribution](../science/timing_diffusion.md#limits-initialization-and-attribution).

### M28 — Optimize timing diffusion as a distinct task

- **Central question:** How do the optimal elapsed-time laws differ from the precision laws?
- **Understanding target:** Explain the separate relaxed period optimizer, the quantum one-third logarithmic diffusion exponent and the classical diffusion benchmark. Recognize the exact equality of both timing optima at fault rate at least the native scale, and distinguish that statement from tick precision.
- **Dependencies and story role:** M16–M17, M20 and M25–M27. Completes the second operating objective and reconnects it to the finite witness.
- **Conceptual connection:** Multiplying inverse precision by the actual period changes the optimization; coherent timing gains nevertheless survive all elapsed-time costs under the stated ordered limits.
- **Source pointers:** Anchor, Chapters 3–4, for the common model. Project: [Sharp relaxed timing envelope](../science/timing_diffusion.md#sharp-relaxed-timing-envelope), [Quantum timing exponent under the full strength budget](../science/timing_diffusion.md#quantum-timing-exponent-under-the-full-strength-budget), [Classical timing benchmark](../science/timing_diffusion.md#classical-timing-benchmark), and [The 32-dimensional witness also improves elapsed-time accuracy](../science/finite_example.md#the-32-dimensional-witness-also-improves-elapsed-time-accuracy).

### M29 — Separate inherited ingredients, new results and finite evidence

- **Central question:** What remains established here after the closest prior results and the limits of numerical checks are made explicit?
- **Understanding target:** Attribute the clean quasiideal clock, generic restart identities and existing accuracy-resolution or kinetic bounds to their sources. Identify the added sharp fault envelope, exact classical optimization and bounded-strength noisy transfer, while distinguishing analytical quantifiers from sampled verification.
- **Dependencies and story role:** M13–M28. Integrates the proof chain and its evidence into a defensible account of the scientific contribution.
- **Conceptual connection:** A valid imported component, a new consequence and a successful finite calculation play different logical roles; their connection must preserve each model's events and resources.
- **Source pointers:** Anchor, Chapters 3–4, as background rather than a research-priority source. Project: [Relationship to prior work](../references/RELATED_WORK.md), especially [Restart theory supplies the framework](../references/RELATED_WORK.md#restart-theory-supplies-the-framework) and [Ideal quantum clocks and the rate account](../references/RELATED_WORK.md#ideal-quantum-clocks-and-the-rate-account); [Reading the results](../verification/README.md#reading-the-results).

### M30 — State the complete scoped clock advantage

- **Central question:** What can this result now say about a noisy autonomous clock, and which changed assumptions require a new theorem?
- **Understanding target:** Give one connected explanation of the exact classical frontier, quantum logarithmic precision exponent, finite witnesses and elapsed-time advantage. Keep complete hidden resets, the passive-counter exception, global strength budgets, variable finite dimension, ordered limits and uncharged microscopic implementation costs attached to the claim.
- **Dependencies and story role:** M12, M17, M20 and M25–M29. Synthesizes the narrative phase and the full project from its local mechanism to its global consequence.
- **Conceptual connection:** Coherent low-spread progress and fault-induced erased progress produce different optimal quantum and stochastic-clock balances; the conclusion belongs to the specified model, not arbitrary classical oscillators or generic decoherence.
- **Source pointers:** Anchor, Chapters 3–4, through the [bridge](BRIDGE.md). Project: [Scientific account](../science/README.md), [Physical interpretation and limits](../science/model.md#physical-interpretation-and-limits), [Limits, initialization and attribution](../science/timing_diffusion.md#limits-initialization-and-attribution), and [Scope of the comparison](../references/RELATED_WORK.md#scope-of-the-comparison).
