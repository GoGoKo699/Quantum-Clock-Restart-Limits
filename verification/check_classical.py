#!/usr/bin/env python3
"""Finite scientific checks of the bounded-rate classical restart frontier.

Dependencies: numpy, scipy. Run from any directory. --output optionally saves
the JSON record; stdout always contains that same record. This is numerical
validation of consequential finite cases, not a substitute for the proof.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import solve
from scipy.optimize import brentq


SEED = 81623


def assert_close(actual, expected, *, rtol=3e-8, atol=3e-10, label="value"):
    if not np.isclose(actual, expected, rtol=rtol, atol=atol):
        raise AssertionError(f"{label}: actual={actual!r}, expected={expected!r}")


def delta_c(ell):
    """Stable 1-(1-exp(-ell))/ell, including very weak errors."""
    if ell < 0.02:
        return sum(((-1) ** (j + 1)) * ell**j / math.factorial(j + 1)
                   for j in range(1, 14))
    return 1 + math.expm1(-ell) / ell


def sinh_minus_z(z):
    if abs(z) < 0.1:
        return sum(z ** (2 * j + 1) / math.factorial(2 * j + 1)
                   for j in range(1, 9))
    return math.sinh(z) - z


def tanh_deficit(z):
    """(z/2-tanh(z/2))/z, evaluated without small-z cancellation."""
    if z < 0.1:
        return (z*z/24 - z**4/240 + 17*z**6/40320
                - 31*z**8/725760 + 691*z**10/159667200)
    return 0.5 - math.tanh(z/2)/z


def erlang_precision(n, ratio):
    ell = math.log1p(1/ratio)
    dc = delta_c(ell)
    z = n * ell
    if z > 40:
        e = math.exp(-z)
        return (1 - e)**2 / (1 - e*e - 2*(1-dc)*z*e)
    return 2*math.sinh(z/2)**2 / (sinh_minus_z(z) + dc*z)


def optimal_ladder(ratio):
    ell = math.log1p(1/ratio)
    dc = delta_c(ell)
    target = dc/(2*(2-dc))
    hi = 1.0
    while tanh_deficit(hi) < target:
        hi *= 2
    zstar = brentq(lambda z: tanh_deficit(z) - target, 0, hi,
                   xtol=1e-15, rtol=2e-14)
    candidates = sorted({max(1, math.floor(zstar/ell)),
                         max(1, math.ceil(zstar/ell))})
    n = max(candidates, key=lambda k: erlang_precision(k, ratio))
    return n, erlang_precision(n, ratio), zstar/ell


def direct_moments(Q, alpha, gamma):
    """Absorb ticks, add reset transitions, solve actual generator moments."""
    dimension = len(alpha)
    A = Q + gamma * (np.ones((dimension, 1))*alpha - np.eye(dimension))
    first = solve(-A, np.ones(dimension))
    mean = float(alpha @ first)
    second = float(2*alpha @ solve(-A, first))
    variance = second - mean*mean
    if not (mean > 0 and variance > 0):
        raise AssertionError("nonpositive direct first-passage moments")
    return mean, variance, mean*mean/variance


def transform_moments(Q, alpha, gamma):
    """Use only the clean killed generator's Laplace resolvent."""
    dimension = len(alpha)
    tick = -Q @ np.ones(dimension)
    resolved = solve(gamma*np.eye(dimension)-Q, tick)
    p = float(alpha @ resolved)
    derivative = -float(alpha @ solve(gamma*np.eye(dimension)-Q, resolved))
    mean = (1-p)/(gamma*p)
    second = 2*(1-p+gamma*derivative)/(gamma*gamma*p*p)
    return mean, second-mean*mean, p


def fixed_mean_frontier(p, ratio):
    ell = math.log1p(1/ratio)
    q = math.exp(-ell)
    # Endpoints may round to either neighboring interval; both give the same h.
    n = max(1, math.floor(-math.log(p)/ell + 2e-13))
    low, high = q**(n+1), q**n
    weight = (p-low)/(high-low)
    h = weight*n*high + (1-weight)*(n+1)*low
    cv2 = (1-p*p-2*(1-q)*h)/(1-p)**2
    return cv2, n, weight


def ladder_mixture(lengths, weights):
    """Disjoint unit-rate ladders with an explicitly mixed reset state."""
    dimension = sum(lengths)
    Q = np.zeros((dimension, dimension))
    alpha = np.zeros(dimension)
    offset = 0
    for length, weight in zip(lengths, weights):
        alpha[offset] = weight
        for j in range(length):
            Q[offset+j, offset+j] = -1
            if j+1 < length:
                Q[offset+j, offset+j+1] = 1
        offset += length
    return Q, alpha


def run_checks():
    rng = np.random.default_rng(SEED)
    maximum_relative_moment_error = 0.0
    random_records = []
    for ratio in [0.3, 1, 3, 10, 100, 1000]:
        gamma = 1/ratio
        optimum_n, optimum, _ = optimal_ladder(ratio)
        largest_fraction = 0.0
        count = 0
        for dimension in range(2, 13):
            for repetition in range(30):
                W = rng.random((dimension, dimension))
                np.fill_diagonal(W, 0)
                proposed_tick = rng.random(dimension)*2
                total = 0.05 + rng.random(dimension)*0.95
                W *= (total/(W.sum(axis=1)+proposed_tick))[:, None]
                Q = W - np.diag(total)
                alpha = rng.dirichlet(np.ones(dimension))
                if repetition % 3 == 0:
                    alpha = np.eye(dimension)[repetition % dimension]
                mean, variance, precision = direct_moments(Q, alpha, gamma)
                transformed_mean, transformed_variance, p = transform_moments(Q, alpha, gamma)
                assert_close(mean, transformed_mean, label="random mean")
                assert_close(variance, transformed_variance, label="random variance")
                maximum_relative_moment_error = max(
                    maximum_relative_moment_error,
                    abs(mean/transformed_mean-1), abs(variance/transformed_variance-1))
                floor, _, _ = fixed_mean_frontier(p, ratio)
                if variance/(mean*mean) < floor - 2e-8:
                    raise AssertionError("random generator beats fixed-mean frontier")
                if precision > optimum*(1+2e-8):
                    raise AssertionError("random generator beats global frontier")
                largest_fraction = max(largest_fraction, precision/optimum)
                count += 1
        random_records.append({"Gamma_over_gamma": ratio, "CTMCs_checked": count,
                               "optimal_ladder_stages": optimum_n,
                               "optimal_precision": optimum,
                               "largest_random_fraction_of_optimum": largest_fraction})

    adjacent_count = 0
    nonadjacent_count = 0
    for ratio in [0.3, 1, 10, 100]:
        gamma, q = 1/ratio, ratio/(ratio+1)
        for n in [1, 2, 3, 5]:
            for weight in [0.0, 0.13, 0.5, 0.87, 1.0]:
                Q, alpha = ladder_mixture([n, n+1], [weight, 1-weight])
                mean, variance, _ = direct_moments(Q, alpha, gamma)
                p = 1/(1+gamma*mean)
                floor, _, _ = fixed_mean_frontier(p, ratio)
                assert_close(variance/(mean*mean), floor, rtol=4e-7,
                             label="adjacent ladder frontier saturation")
                adjacent_count += 1
        for lengths in [[1, 3], [2, 5], [1, 2, 6]]:
            weights = np.arange(1, len(lengths)+1, dtype=float)
            weights /= weights.sum()
            Q, alpha = ladder_mixture(lengths, weights)
            mean, variance, _ = direct_moments(Q, alpha, gamma)
            p = 1/(1+gamma*mean)
            floor, _, _ = fixed_mean_frontier(p, ratio)
            if variance/(mean*mean) <= floor + 1e-8:
                raise AssertionError("nonadjacent mixture unexpectedly saturates frontier")
            nonadjacent_count += 1

    # Nominally, half the trajectories remain forever in a nonticking closed state.
    Q = np.array([[-1., 0.], [0., 0.]])
    alpha = np.array([0.5, 0.5])
    mean, variance, precision = direct_moments(Q, alpha, 0.2)
    tm, tv, p = transform_moments(Q, alpha, 0.2)
    assert_close(mean, tm, label="defective mean")
    assert_close(variance, tv, label="defective variance")
    defective_record = {"nominal_nonticking_probability": 0.5,
                        "restart_mean": mean, "restart_variance": variance,
                        "restart_precision": precision, "Laplace_probability": p}

    optimizer_scans = []
    for ratio in [0.001, 0.03, 0.3, 1, 3, 10, 100, 1000, 10000]:
        n, optimum, continuous_n = optimal_ladder(ratio)
        scan_limit = max(80, math.ceil(12*math.sqrt(ratio)))
        scanned_n = max(range(1, scan_limit+1),
                        key=lambda j: erlang_precision(j, ratio))
        assert_close(optimum, erlang_precision(scanned_n, ratio), rtol=2e-12,
                     label="wide integer optimizer scan")
        optimizer_scans.append({"Gamma_over_gamma": ratio, "optimal_stages": n,
                                "continuous_optimum_stages": continuous_n,
                                "scan_through_stages": scan_limit,
                                "optimal_precision": optimum})

    asymptotic_records = []
    for ratio in [1e2, 1e3, 1e4, 1e6, 1e8, 1e10]:
        n, optimum, _ = optimal_ladder(ratio)
        asymptotic_records.append({"Gamma_over_gamma": ratio, "optimal_stages": n,
                                   "stages_over_sqrt_3R": n/math.sqrt(3*ratio),
                                   "precision_over_sqrt_3R_half": optimum/(math.sqrt(3*ratio)/2)})
    if abs(asymptotic_records[-1]["precision_over_sqrt_3R_half"]-1) > 2e-5:
        raise AssertionError("weak-error precision constant has not converged")
    if abs(asymptotic_records[-1]["stages_over_sqrt_3R"]-1) > 2e-5:
        raise AssertionError("weak-error optimal dimension has not converged")

    return {"status": "passed", "seed": SEED,
            "dependencies": {"numpy": np.__version__, "scipy": scipy.__version__},
            "random_generator_checks": random_records,
            "largest_relative_generator_vs_transform_moment_error": maximum_relative_moment_error,
            "adjacent_ladder_saturation_cases": adjacent_count,
            "strict_nonadjacent_mixture_cases": nonadjacent_count,
            "defective_nominal_clock": defective_record,
            "wide_optimizer_scans": optimizer_scans,
            "weak_error_asymptotics": asymptotic_records,
            "scope": "Finite numerical checks; universal claims rely on the analytical proof."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run_checks()
    payload = json.dumps(result, indent=2, allow_nan=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload+"\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
