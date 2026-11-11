# Reproducing the finite checks

[Scientific overview](../science/README.md) · [Classical proof](../science/classical_optimum.md) · [Hazard proof](../science/restart_and_hazard.md)

The analytical pages establish the unrestricted claims. These programs test independent finite calculations, equality cases, optimizer formulas and admissible sampled devices. A successful run is a reproducibility and counterexample check, not a proof certificate.

## Environment

Use Python 3.10 or later. The classical and quantum matrix calculations use the exact versions pinned in [requirements.txt](requirements.txt); the hazard diagnostic uses only the Python standard library.

    python -m pip install -r verification/requirements.txt

The reported matrix environment is NumPy 2.3.5 and SciPy 1.17.0. No quantum hardware, external dataset, preparation oracle or network access is required.

## Exact classical benchmark

    python verification/check_classical.py --output verification/classical_validation.json

The program computes actual first-tick moments directly from a reset CTMC transient generator, then compares them with the independently evaluated Laplace/restart transform. It samples 1980 clocks of dimensions 2–12 across six strength/noise ratios, including arbitrary rate patterns and mixed initial states.

Additional checks cover:

- 80 adjacent-Erlang mixtures that attain the exact fixed-mean envelope;
- 12 nonadjacent comparisons that are strictly below that envelope;
- a defective nominal clock rescued by resetting;
- nine wide integer scans against the unique continuous optimizer;
- the weak-error asymptotic constant and stage count through R=10^10.

The saved JSON records actual errors and ratios. Sampling does not enumerate all CTMCs; uniformization and the concave-envelope proof establish the all-design optimizer.

## Independent bounded-hazard diagnostic

    python verification/check_hazard_independent.py

This standard-library program integrates piecewise-constant hazards directly to obtain their nominal Laplace moments. It checks 1200 seeded examples against the sharp restarted-variance envelope, 16 delayed-exponential equality cases and six scalar precision/diffusion optimizer cases.

The construction deliberately includes zero-hazard delay segments. Its exact-integral calculation is separate from the closed-form envelope. The seed and sampled ranges are in the source. Floating-point tolerances are appropriate to these finite ranges and do not provide asymptotic uniform error bounds.

To retain its JSON result:

    python verification/check_hazard_independent.py > verification/hazard_validation.json

## Finite quantum devices

    python verification/check_quantum_example.py --output verification/quantum_example_validation.json

The [finite example](../science/finite_example.md) specifies static devices of dimension 16, 24, 32 and 64. Their Hamiltonian spectrum and summed tick effect obey the analytic strength bounds. The program evaluates actual faulty waiting-time moments through no-tick Lyapunov resolvents. At dimensions 16 and 32 it independently solves the full no-tick Liouville generator with the reset faults included, then compares both moment calculations.

The dimension 32 example also beats the universal classical timing-diffusion floor. A baseline-absorber sensitivity test includes a negative case where that device loses its precision advantage. The saved JSON records solver residuals, normalization identities, comparators and the full tested parameters. These computations are floating-point witnesses, not formal interval certificates, and are separate from the asymptotic source-transfer proof.

## Reading the results

The exact classical optimizer and delayed-exponential hazard envelope have different domains. A sharp hazard constant is a relaxed waiting-law optimum, and is not claimed to be realized by a finite autonomous quantum clock. The quantum logarithmic exponent uses the source-normalized analytical construction; finite diagnostics do not replace that source transfer.

All actual waiting times include failed attempts and hidden resets. The elapsed-time statement takes the long observation-time limit at a fixed device before optimizing its size and noise ratio. No generic finite-horizon guarantee follows from a passing numerical suite.

## Hosted mathematical display

The read-only `Verify hosted mathematics` workflow compares every tracked Markdown equation with its actual commit-pinned GitHub rendering at widths 1440 and 760. It runs on `review/**` branch pushes and can also be dispatched once present on the default branch. Its token has only `contents: read`; it uses no repository secrets and makes no source changes.

The collector and structural checker are in `verification/hosted_math/`. With Node.js 18 or later, Python 3.10 or later, Git, Playwright 1.56.1, MathJax 3.2.1 and the corresponding Chromium installed, run:

```bash
node verification/hosted_math/capture_hosted_math.cjs \
  --root "$PWD" --repository GoGoKo699/Quantum-Clock-Restart-Limits \
  --revision "$(git rev-parse HEAD)" \
  --contract verification/hosted_math/headline-contract.json \
  --output /absolute/new-empty-capture-directory
```

Dependencies may be installed outside the checkout and located with `NODE_PATH`. The saved report binds the source hashes, MathML comparisons, runtime and screenshots. The headline contract adds explicit expected text for six principal expressions; update its expression hashes after a deliberate change to those formulas. An automated pass checks structure and selected geometry, not scientific truth or a complete visual review. Inspect the screenshots as well. GitHub Actions artifacts expire; they are reproducible verification outputs rather than permanent scientific data.
