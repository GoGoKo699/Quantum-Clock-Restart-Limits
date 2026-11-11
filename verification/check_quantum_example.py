#!/usr/bin/env python3
"""Reproduce finite bounded-strength phase-clock witnesses.

The primary calculation solves d-by-d no-tick Lyapunov equations. For the
16- and 32-dimensional witnesses, an independent d^2-by-d^2 Liouville solve
includes the actual reset-fault generator before computing its moments.
These floating-point checks are not interval certificates or an asymptotic
proof. The exact all-CTMC comparator is imported from check_classical.py.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import (
    eigvalsh,
    lu_factor,
    lu_solve,
    norm,
    solve_continuous_lyapunov,
)

from check_classical import optimal_ladder


SIGMA = 2.5
ABSORBER_WIDTH = 1.5
MAIN_BASELINE = 1e-4


def build_device(dimension, baseline=MAIN_BASELINE):
    """Return exact-form finite device matrices at declared Gamma=1."""
    if dimension < 4 or dimension % 2:
        raise ValueError("this illustrative family uses even dimension >=4")
    if not 0 < baseline < 1:
        raise ValueError("baseline must lie strictly between zero and one")

    indices = np.arange(dimension)
    phase_from_start = (indices + dimension // 2) % dimension - dimension // 2
    phase_from_absorber = indices - dimension // 2
    fourier = np.exp(2j * np.pi * np.outer(indices, indices) / dimension)
    fourier /= np.sqrt(dimension)
    energies = np.linspace(-1.0, 1.0, dimension)
    hamiltonian = (fourier * energies) @ fourier.conj().T

    psi = np.exp(
        -np.pi * phase_from_start**2 / SIGMA**2
        + 2j * np.pi * ((dimension - 1) / 2) * phase_from_start / dimension
    )
    psi /= norm(psi)
    rho0 = np.outer(psi, psi.conj())
    tick_diagonal = baseline + (1 - baseline) * np.exp(
        -phase_from_absorber**2 / (2 * ABSORBER_WIDTH**2)
    )
    tick_effect = np.diag(tick_diagonal)
    no_tick_amplitude = -1j * hamiltonian - tick_effect / 2

    if norm(hamiltonian - hamiltonian.conj().T) > 2e-12:
        raise AssertionError("Hamiltonian is not Hermitian")
    spectrum = eigvalsh(hamiltonian)
    h_halfwidth = float((spectrum[-1] - spectrum[0]) / 2)
    if h_halfwidth > 1 + 2e-12:
        raise AssertionError("Hamiltonian exceeds the common strength budget")
    if not (tick_diagonal.min() > 0 and tick_diagonal.max() <= 1 + 2e-12):
        raise AssertionError("summed tick effect exceeds its budget")

    return {
        "dimension": dimension,
        "baseline": baseline,
        "H": hamiltonian,
        "rho0": rho0,
        "Q": tick_effect,
        "A": no_tick_amplitude,
        "hamiltonian_halfwidth": h_halfwidth,
        "maximum_total_tick_effect": float(tick_diagonal.max()),
        "minimum_total_tick_effect": float(tick_diagonal.min()),
        "state_normalization_error": float(abs(np.trace(rho0) - 1)),
    }


def lyapunov_moments(device, fault_rate):
    """Actual faulty moments, using the rank-one reset resolvent identity.

    If A_gamma=A-gamma I/2, solve
      A_gamma Y+Y A_gamma^dagger=-rho0,
      A_gamma Z+Z A_gamma^dagger=-Y.
    Put u=tr Y, w=tr Z and p=1-gamma u. Then the actual reset-fault
    interval has mean u/p and variance (2w-u^2)/p^2.
    """
    d = device["dimension"]
    ag = device["A"] - fault_rate * np.eye(d) / 2
    rho0 = device["rho0"]
    y = solve_continuous_lyapunov(ag, -rho0)
    z = solve_continuous_lyapunov(ag, -y)
    u = float(np.trace(y).real)
    w = float(np.trace(z).real)
    success = 1 - fault_rate * u
    mu = u / success
    variance = (2 * w - u * u) / success**2
    precision = mu * mu / variance

    residual_y = norm(ag @ y + y @ ag.conj().T + rho0) / norm(rho0)
    residual_z = norm(ag @ z + z @ ag.conj().T + y) / norm(y)
    transfer_probability = float(np.trace(device["Q"] @ y).real)
    if not (success > 0 and mu > 0 and variance > 0):
        raise AssertionError("nonpositive physical moments")
    if max(residual_y, residual_z) > 2e-10:
        raise AssertionError("Lyapunov residual too large")
    if abs(transfer_probability - success) > 2e-10:
        raise AssertionError("absorption normalization identity failed")
    if max(abs(np.trace(y).imag), abs(np.trace(z).imag)) > 2e-8:
        raise AssertionError("moments have a significant imaginary part")

    return {
        "mean": mu,
        "variance": variance,
        "precision": precision,
        "restart_success_probability": success,
        "lyapunov_relative_residual": float(max(residual_y, residual_z)),
        "absorption_identity_error": abs(transfer_probability - success),
    }


def full_liouville_moments(device, fault_rate):
    """Independent full-generator computation; no restart transform used."""
    d = device["dimension"]
    rho0 = device["rho0"]
    a = device["A"]
    identity = np.eye(d)
    trace_row = identity.reshape(-1, order="F")
    rho_vector = rho0.reshape(-1, order="F")
    no_tick_generator = np.kron(identity, a) + np.kron(a.conj(), identity)
    fault_generator = fault_rate * (
        np.outer(rho_vector, trace_row) - np.eye(d * d)
    )
    killed = no_tick_generator + fault_generator
    factor = lu_factor(-killed)
    m0 = lu_solve(factor, rho_vector)
    m1 = lu_solve(factor, m0)
    mu = float((trace_row @ m0).real)
    second = float((2 * trace_row @ m1).real)
    variance = second - mu * mu
    precision = mu * mu / variance
    residual0 = norm((-killed) @ m0 - rho_vector) / norm(rho_vector)
    residual1 = norm((-killed) @ m1 - m0) / norm(m0)
    if max(residual0, residual1) > 2e-10:
        raise AssertionError("full Liouville residual too large")
    if not (mu > 0 and variance > 0):
        raise AssertionError("nonpositive full-generator moments")
    return {
        "mean": mu,
        "variance": variance,
        "precision": precision,
        "full_generator_relative_residual": float(max(residual0, residual1)),
    }


def run_checks():
    witnesses = []
    maximum_solver_disagreement = 0.0
    for d, ratio in [(16, 100.0), (24, 1000.0), (32, 2000.0), (64, 10000.0)]:
        device = build_device(d)
        actual = lyapunov_moments(device, 1 / ratio)
        nominal = lyapunov_moments(device, 0.0)
        optimum_stages, classical_precision, _ = optimal_ladder(ratio)
        if actual["precision"] <= classical_precision * 1.1:
            raise AssertionError("finite witness does not retain the declared margin")

        record = {
            "dimension": d,
            "Gamma_over_gamma": ratio,
            "initial_sigma": SIGMA,
            "absorber_width": ABSORBER_WIDTH,
            "absorber_baseline": MAIN_BASELINE,
            "hamiltonian_halfwidth": device["hamiltonian_halfwidth"],
            "maximum_total_tick_effect": device["maximum_total_tick_effect"],
            "minimum_total_tick_effect": device["minimum_total_tick_effect"],
            "nominal": nominal,
            "faulty": actual,
            "all_CTMC_optimal_ladder_stages": optimum_stages,
            "all_CTMC_optimal_precision": classical_precision,
            "precision_ratio_to_all_CTMC_optimum": actual["precision"] / classical_precision,
            "quantum_timing_diffusion": actual["variance"] / actual["mean"],
            "all_CTMC_timing_diffusion_lower_bound": 1 / (1 + 1 / ratio),
        }
        if d >= 24 and record["quantum_timing_diffusion"] >= record["all_CTMC_timing_diffusion_lower_bound"]:
            raise AssertionError("finite elapsed-time diffusion witness failed")
        if d in [16, 32]:
            independent = full_liouville_moments(device, 1 / ratio)
            disagreement = max(
                abs(independent[key] / actual[key] - 1)
                for key in ["mean", "variance", "precision"]
            )
            if disagreement > 2e-8:
                raise AssertionError("independent full generator disagrees")
            maximum_solver_disagreement = max(maximum_solver_disagreement, disagreement)
            record["independent_full_Liouville"] = independent
            record["maximum_relative_solver_disagreement"] = disagreement
        witnesses.append(record)

    sensitivity = []
    for baseline in [1e-10, 1e-6, 1e-4, 1e-3]:
        device = build_device(32, baseline)
        actual = lyapunov_moments(device, 1 / 2000.0)
        _, classical_precision, _ = optimal_ladder(2000.0)
        sensitivity.append({
            "dimension": 32,
            "Gamma_over_gamma": 2000.0,
            "baseline": baseline,
            "quantum_precision": actual["precision"],
            "all_CTMC_optimal_precision": classical_precision,
            "precision_ratio": actual["precision"] / classical_precision,
            "lyapunov_relative_residual": actual["lyapunov_relative_residual"],
        })

    # A consequence-sensitive negative case: broadening the baseline enough
    # destroys this particular witness. No general robustness claim follows.
    if sensitivity[-1]["precision_ratio"] >= 1:
        raise AssertionError("declared negative sensitivity case changed")

    return {
        "status": "passed",
        "numpy_version": np.__version__,
        "scipy_version": scipy.__version__,
        "strength_convention": "Gamma=1; centered H halfwidth<=1; summed intrinsic tick effect Q<=I",
        "methods": [
            "d-by-d complex Lyapunov resolvents with reset identity",
            "independent actual d^2-by-d^2 no-tick Liouville moments at d=16 and d=32",
            "exact all-CTMC comparator from proved adjacent-ladder frontier",
        ],
        "maximum_relative_solver_disagreement": maximum_solver_disagreement,
        "witnesses": witnesses,
        "baseline_sensitivity": sensitivity,
        "limits": [
            "floating-point numerical witnesses, not formal interval certificates",
            "finite samples do not establish the asymptotic exponent",
            "static phenomenological reset interfaces; no microscopic synthesis-cost claim",
            "the sampled parameters are illustrative and are not claimed optimal",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    record = run_checks()
    payload = json.dumps(record, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
