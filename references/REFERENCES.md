# References

[Scientific account](../science/README.md) · [Comparison with prior work](RELATED_WORK.md)

The links below identify the primary sources used for the scientific comparisons. Published articles are listed by their journal metadata; versioned preprints identify the inspected text when equation numbering or a preprint-only result matters.

## reuveni2016

Shlomi Reuveni, **Optimal Stochastic Restart Renders Fluctuations in First Passage Times Universal**, *Physical Review Letters* **116**, 170601 (2016). [Published article](https://doi.org/10.1103/PhysRevLett.116.170601).

The unit coefficient of variation concerns a nonzero Poisson restart rate that minimizes the mean completion time. It is not a universal unit-precision bound at an externally imposed fault rate.

## pal2017

Arnab Pal and Shlomi Reuveni, **First Passage under Restart**, *Physical Review Letters* **118**, 030603 (2017). [Published article](https://doi.org/10.1103/PhysRevLett.118.030603) · [Preprint record](https://arxiv.org/abs/1607.06048).

This supplies the general first-passage restart framework. The restart recursion, Laplace-transform relations and renewal interpretation are inherited ingredients.

## woods2022

Mischa P. Woods, Ralph Silva, Gilles Pütz, Sandra Stupar and Renato Renner, **Quantum Clocks are More Accurate Than Classical Ones**, *PRX Quantum* **3**, 010319 (2022). [Published article](https://doi.org/10.1103/PRXQuantum.3.010319) · [Versioned source, arXiv:1806.00491v3](https://arxiv.org/html/1806.00491v3).

The preprint title uses “more precise”; v3, dated 24 February 2022, is updated in line with the publication. Appendix F supplies the quasiideal reset-clock construction and accuracy estimates used in [the bounded-strength transfer](../science/quantum_construction.md). The relevant source equation numbers refer to this version.

## meier2023

Florian Meier, Emanuel Schwarzhans, Paul Erker and Marcus Huber, **Fundamental Accuracy-Resolution Trade-Off for Timekeeping Devices**, *Physical Review Letters* **131**, 220201 (2023). [Published article](https://doi.org/10.1103/PhysRevLett.131.220201) · [Published-version preprint, arXiv:2301.05173v3](https://arxiv.org/html/2301.05173v3).

The accuracy-resolution bound for bounded memoryless tick generation is an antecedent of the bounded-hazard argument used here.

## starkov2023

Dmitry Starkov and Sergey Belan, **Universal performance bounds of restart**, *Physical Review E* **107**, L062101 (2023). [Published article](https://doi.org/10.1103/PhysRevE.107.L062101) · [Versioned preprint, arXiv:2209.06611v4](https://arxiv.org/html/2209.06611v4).

The inspected v4 is dated 25 March 2023. Its distributional bounds constrain restarted completion times using statistics of the original process, including the harmonic mean, median and mode.

## macieszczak2024

Katarzyna Macieszczak, **Ultimate Kinetic Uncertainty Relation and Optimal Performance of Stochastic Clocks**, arXiv:2407.09839v1 (13 July 2024). [Versioned preprint](https://arxiv.org/html/2407.09839v1) · [Record](https://arxiv.org/abs/2407.09839v1).

The work treats optimal stochastic fluxes and first-passage uncertainty, with a semi-Markov extension that includes quantum reset processes. “Reset” in that framework includes renewal after an observed event; it does not by itself specify the additional unobserved fault channel considered here.

## prech2025

Kacper Prech, Gabriel T. Landi, Florian Meier, Nuriya Nurgalieva, Patrick P. Potts, Ralph Silva and Mark T. Mitchison, **Optimal Time Estimation and the Clock Uncertainty Relation for Stochastic Processes**, *Physical Review X* **15**, 031068 (2025). [Published article](https://doi.org/10.1103/rpls-mp8z) · [Final-author preprint, arXiv:2406.19450v2](https://arxiv.org/abs/2406.19450v2).

The v2 record is dated 1 July 2025; the article was published on 11 September 2025. Its optimal estimation and clock uncertainty relations are important antecedents for the stochastic classical baseline.

## meier2025

Florian Meier, Yuri Minoguchi, Simon Sundelin, Tony J. G. Apollaro, Paul Erker, Simone Gasparinetti and Marcus Huber, **Precision is not limited by the second law of thermodynamics**, *Nature Physics* **21**, 1147–1152 (2025). [Published article](https://doi.org/10.1038/s41567-025-02929-2) · [Preprint, arXiv:2407.07948v1](https://arxiv.org/html/2407.07948v1).

The version of record was published on 2 June 2025. Its coherent ring-clock construction establishes an exponential precision-versus-entropy advantage in its specified thermal interface.

## nelmes2026

Chad Nelmes, Emanuel Schwarzhans, Tony Apollaro, Timothy Spiller and Irene D’Amico, **Approaching the Limit of Quantum Clock Precision**, arXiv:2604.22704v1 (24 April 2026). [Versioned preprint](https://arxiv.org/html/2604.22704v1) · [Record](https://arxiv.org/abs/2604.22704v1).

The paper uses engineered perfect-state-transfer spin chains and terminal-coupling optimization. Its reported precision-resolution scaling is relevant context; its coupling and repeated-operation resources require a separate comparison with this repository’s uniform strength and autonomy conditions.

## yin2025

Ruoyu Yin, Qingyuan Wang, Sabine Tornow and Eli Barkai, **Restart uncertainty relation for monitored quantum dynamics**, *Proceedings of the National Academy of Sciences of the USA* **122**, e2402912121 (2025). [Published article](https://doi.org/10.1073/pnas.2402912121) · [Author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC11725946/) · [Preprint record](https://arxiv.org/abs/2401.01307).

The work studies restart-broadened quantum recurrence resonances under repeated monitoring and verifies its uncertainty relation on a quantum computer.

## clock-entropy

Ruge Lin, **Quantum Clock Entropy Limits**, scientific repository, inspected revision `12c9cd76441ab1bc9fd1eac626cfa3226e4df90c`. [Pinned scientific model](https://github.com/GoGoKo699/Quantum-Clock-Entropy-Limits/blob/12c9cd76441ab1bc9fd1eac626cfa3226e4df90c/science/model.md) · [Precision theorem](https://github.com/GoGoKo699/Quantum-Clock-Entropy-Limits/blob/12c9cd76441ab1bc9fd1eac626cfa3226e4df90c/science/precision_bound.md) · [Noise extension and boundaries](https://github.com/GoGoKo699/Quantum-Clock-Entropy-Limits/blob/12c9cd76441ab1bc9fd1eac626cfa3226e4df90c/science/extensions.md).

This related project concerns a signed current through one counted forward/reverse reset pair and its rate-ratio affinity. Its model and observable differ from unobserved complete-restart faults and unsigned renewal ticks.

## Reading the comparisons

The [related-work account](RELATED_WORK.md) identifies the inherited components, the different operational assumptions and the contribution established here. This bibliography is a scoped comparison corpus, rather than an exhaustive priority claim.
