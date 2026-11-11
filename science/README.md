# Scientific account

[Repository overview](../README.md)

An autonomous clock can improve tick regularity by slowing and spreading over more internal states. Hidden restart faults impose a competing cost: a longer traversal is more likely to be interrupted and repeated. The central question is how this competition changes the best achievable classical and quantum clock, at fixed dynamical strength.

The complete account has five proof components and a finite illustration:

| Part | Question | Authoritative page |
|---|---|---|
| Model | Which events, registers, rates and observations count? | [Clock class and resources](model.md) |
| Universal constraint | How do faults transform waiting times, and what variance is unavoidable? | [Restart and hazard bounds](restart_and_hazard.md) |
| Classical benchmark | Can any finite classical Markov network beat a ladder? | [Exact classical optimum](classical_optimum.md) |
| Coherent construction | Does the inherited quantum clock retain its scaling after every strength is bounded? | [Quantum construction](quantum_construction.md) |
| Timekeeping | Does the advantage remain when every elapsed interval is counted? | [Timing diffusion](timing_diffusion.md) |
| Finite illustration | Can a specified bounded-strength device exceed the all-classical benchmark? | [Finite example](finite_example.md) |

For $`R=\Gamma/\gamma\to\infty`$, tick precision obeys
```math
P_{\rm C}^{*}(R)\sim\frac{\sqrt{3R}}2,\qquad
P_{\rm Q}^{*}(R)=R^{2/3+o(1)}.
```
The first is an exact asymptotic equivalent, supported by an exact finite-$`R`$ classical optimizer. The second fixes a logarithmic exponent; constant-factor quantum matching is not established. The sharp hazard envelope is attained in a relaxed waiting-time class, and is not asserted to be exactly attainable by finite autonomous quantum dynamics.

For the calibrated tick-count estimator, the long-time limit is taken at each fixed finite device before weak-fault optimization. Under that order,
```math
\mathcal D_{\rm C}^{*}=\Theta(\Gamma^{-1}),\qquad
\Gamma\mathcal D_{\rm Q}^{*}=R^{-1/3+o(1)}.
```
The quantum advantage therefore persists in an elapsed-time metric as well as in tick regularity. This is a statement about autonomous finite-state Markov classical clocks versus the specified finite quantum clock class, with complete unobserved resets; it is not a bound on arbitrary classical oscillators or generic decoherence.

Use [source comparisons](../references/RELATED_WORK.md) to separate inherited ingredients from the added result. The [verification guide](../verification/README.md) maps the finite checks to the analytical claims they support.
