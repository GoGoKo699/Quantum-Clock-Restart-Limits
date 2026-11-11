#!/usr/bin/env python3
"""Finite diagnostics for the sharp hazard envelope; no asymptotic proof claim.

Uses exact integrals of piecewise-constant hazards and a seeded random sample.
Only the Python standard library is required.
"""

from __future__ import annotations

import json
import math
import random


def laplace_moments(segments, tail_hazard, gamma):
    """Return E exp(-gamma X), E X exp(-gamma X)."""
    start = 0.0
    survival = 1.0
    p = 0.0
    b = 0.0
    for width, hazard in segments:
        rate = gamma + hazard
        decay = math.exp(-rate * width)
        integral_0 = -math.expm1(-rate * width) / rate
        integral_1 = (1.0 - (1.0 + rate * width) * decay) / rate**2
        weight = math.exp(-gamma * start) * survival
        p += hazard * weight * integral_0
        b += hazard * weight * (start * integral_0 + integral_1)
        survival *= math.exp(-hazard * width)
        start += width
    rate = gamma + tail_hazard
    weight = math.exp(-gamma * start) * survival
    p += tail_hazard * weight / rate
    b += tail_hazard * weight * (start / rate + 1.0 / rate**2)
    return p, b


def cv_squared(p, b, gamma):
    return (1.0 - p * p - 2.0 * gamma * b) / (1.0 - p) ** 2


def envelope(x, r):
    bracket = math.log1p(x) - math.log1p(r) + r / (1.0 + r)
    return 1.0 + 2.0 / x - 2.0 * (1.0 + x) * bracket / x**2


def root_bisect(function, target, lower, upper):
    while function(upper) < target:
        upper *= 2.0
    for _ in range(100):
        middle = (lower + upper) / 2.0
        if function(middle) < target:
            lower = middle
        else:
            upper = middle
    return (lower + upper) / 2.0


def main():
    rng = random.Random(20261111)
    worst_slack = float("inf")
    samples = 0
    for gamma in (0.01, 0.1, 1.0, 10.0):
        for _ in range(300):
            segments = [
                (rng.uniform(0.01, 2.0), rng.uniform(0.0, 1.0))
                for _ in range(rng.randrange(1, 16))
            ]
            p, b = laplace_moments(segments, rng.uniform(0.05, 1.0), gamma)
            x = (1.0 - p) / p
            slack = cv_squared(p, b, gamma) - envelope(x, gamma)
            assert x >= gamma - 1e-11
            assert slack >= -1e-10, (gamma, x, slack)
            worst_slack = min(worst_slack, slack)
            samples += 1

        for delay in (0.0, 0.1, 1.0, 10.0):
            p, b = laplace_moments([(delay, 0.0)], 1.0, gamma)
            expected_p = math.exp(-gamma * delay) / (1.0 + gamma)
            expected_b = expected_p * (delay + 1.0 / (1.0 + gamma))
            assert math.isclose(p, expected_p, rel_tol=1e-12)
            assert math.isclose(b, expected_b, rel_tol=1e-12)
            x = (1.0 - p) / p
            assert abs(cv_squared(p, b, gamma) - envelope(x, gamma)) < 1e-9

    optimizers = []
    for r in (1e-4, 0.001, 0.1, 0.9, 1.0, 2.0):
        target = math.log1p(r) - r / (1.0 + r)
        h = lambda x: math.log1p(x) - 2.0 * x / (x + 2.0)
        k = lambda x: math.log1p(x) - x + x * x / 2.0
        xp = root_bisect(h, target, r, max(2.0, 2.0 * r))
        xd = root_bisect(k, target, r, 2.0) if r < 1.0 else r
        assert abs(envelope(xp, r) - xp / (xp + 2.0)) < 1e-8
        if r < 1.0:
            assert abs(xd * envelope(xd, r) - xd * xd) < 1e-9
        for factor in (0.5, 0.9, 1.1, 2.0):
            x = max(r, factor * xd)
            assert x * envelope(x, r) >= xd * envelope(xd, r) - 1e-9
        optimizers.append({"r": r, "precision_x": xp, "diffusion_x": xd})

    print(json.dumps({
        "status": "passed",
        "random_piecewise_hazards": samples,
        "minimum_observed_envelope_slack": worst_slack,
        "shifted_exponential_equalities": 16,
        "scalar_optimizer_checks": optimizers,
        "scope": "finite numerical diagnostics; analytical proofs remain authoritative",
    }, indent=2))


if __name__ == "__main__":
    main()
