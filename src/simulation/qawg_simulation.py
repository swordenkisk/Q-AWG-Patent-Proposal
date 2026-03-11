"""
Q-AWG Simulation Module
========================
Quantum-Enhanced Atmospheric Water Generator — Physics Simulation

Implements:
  - Modified Langmuir isotherm with quantum dot enhancement
  - Linear Driving Force (LDF) kinetics
  - Diurnal humidity/temperature cycles
  - Daily yield calculation
  - QD enhancement comparison

Author  : Belhalhali Mohamed Amine
Location: Tlemcen, Algeria
Date    : March 2026
GitHub  : github.com/swordenkisk/Q-AWG-Patent-Proposal
License : Proprietary — Patent Pending
"""

import numpy as np
from scipy.integrate import odeint
from dataclasses import dataclass
from typing import Tuple, Optional


# ─── MOF Parameters ───────────────────────────────────────────────

@dataclass
class MOFParameters:
    """
    Physical parameters for MOF-303 adsorbent with quantum dot enhancement.
    All values from literature or fitted to experimental data.
    """
    q_max    : float = 0.30   # kg water / kg MOF  — saturated capacity
    K0       : float = 1.34e7   # 1/Pa               — equilibrium constant pre-exponential
    Ea       : float = 40000  # J/mol              — activation energy (adsorption)
    k_base   : float = 1342.0 # 1/s                — LDF rate constant (pre-exponential)
    qd_factor: float = 1.30   # dimensionless      — QD enhancement (+30%)


# ─── Simulator ────────────────────────────────────────────────────

class QAWGSimulator:
    """
    Full physics simulator for the Q-AWG device.

    Models the 24-hour adsorption/desorption cycle using:
      - Modified Langmuir isotherm q_eq(P, T) with QD factor
      - Linear Driving Force: dq/dt = k(T) * (q_eq - q)
      - Diurnal T(t) and P(t) sinusoidal profiles
      - ODE integration via scipy.odeint
    """

    R = 8.314   # J/(mol·K) — universal gas constant

    def __init__(self, params: Optional[MOFParameters] = None):
        self.params = params or MOFParameters()

    # ── Environmental profiles ────────────────────────────────────

    def vapor_pressure(self, t_sec: float,
                       base_hpa: float = 10.0,
                       amplitude_hpa: float = 5.0) -> float:
        """
        Water vapour pressure over 24h diurnal cycle [hPa].
        Higher at night (cooler), lower during hot afternoon.
        """
        period = 24 * 3600
        # Phase: max at midnight (t=0), min at noon (t=period/2)
        return base_hpa + amplitude_hpa * np.cos(2 * np.pi * t_sec / period)

    def temperature_c(self, t_sec: float,
                      base_c: float = 20.0,
                      amplitude_c: float = 10.0) -> float:
        """
        Air temperature over 24h diurnal cycle [°C].
        Max at ~14:00 (t ≈ period*0.6), min at ~04:00.
        """
        period = 24 * 3600
        phase_shift = np.pi * 0.3   # shift peak to ~14:00
        return base_c + amplitude_c * np.sin(2 * np.pi * t_sec / period + phase_shift)

    # ── Adsorption physics ────────────────────────────────────────

    def equilibrium_loading(self, P_hpa: float, T_k: float) -> float:
        """
        Equilibrium water loading from modified Langmuir isotherm [kg/kg].

        q_eq = q_max * (K*P)/(1 + K*P) * eta_QD

        QD enhancement: eta_QD = qd_factor (1.30 for 30% boost)
        """
        P_pa = P_hpa * 100   # hPa → Pa
        K    = self.params.K0 * np.exp(-self.params.Ea / (self.R * T_k))
        KP   = K * P_pa
        theta = KP / (1.0 + KP)
        return self.params.q_max * theta * self.params.qd_factor

    def _dqdt(self, q: float, t_sec: float) -> float:
        """
        Linear Driving Force rate: dq/dt = k(T) * (q_eq - q)
        Used as ODE right-hand side for scipy.odeint.
        """
        P  = self.vapor_pressure(t_sec)
        Tc = self.temperature_c(t_sec)
        Tk = Tc + 273.15

        q_eq = self.equilibrium_loading(P, Tk)

        # Temperature-dependent rate constant (Arrhenius)
        k = self.params.k_base * np.exp(-self.params.Ea / (self.R * Tk))

        return k * (q_eq - q)

    # ── Simulation ────────────────────────────────────────────────

    def simulate(self,
                 duration_hours: float = 24,
                 initial_loading: float = 0.0,
                 n_points: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
        """
        Run full simulation over the specified duration.

        Args:
            duration_hours  : Simulation duration [hours]
            initial_loading : Starting water loading [kg/kg]
            n_points        : Number of time steps

        Returns:
            t_hours : Time array [hours]
            q       : Water loading array [kg/kg]
        """
        t_sec = np.linspace(0, duration_hours * 3600, n_points)
        q = odeint(self._dqdt, initial_loading, t_sec).flatten()
        t_hours = t_sec / 3600
        return t_hours, q

    def calculate_yield(self, t: np.ndarray, q: np.ndarray) -> float:
        """
        Total water yield = sum of positive increments in q [kg/kg].
        Corresponds to water adsorbed and later released for collection.
        """
        dq           = np.diff(q)
        positive_dq  = np.maximum(dq, 0.0)
        return float(np.sum(positive_dq))

    def daily_summary(self) -> dict:
        """Run 24h simulation and return key metrics."""
        t, q = self.simulate(24)
        yield_kgkg = self.calculate_yield(t, q)
        return {
            "yield_kg_per_kg_MOF" : round(yield_kgkg, 5),
            "max_loading_kg_kg"   : round(float(q.max()), 5),
            "min_loading_kg_kg"   : round(float(q.min()), 5),
            "qd_factor"           : self.params.qd_factor,
        }


# ─── Comparison ───────────────────────────────────────────────────

def compare_qd_enhancement() -> dict:
    """
    Compare daily water yield with and without quantum dot enhancement.
    Demonstrates the key innovation of Q-AWG.
    """
    # Without QD
    sim_base = QAWGSimulator(MOFParameters(qd_factor=1.0))
    t, q_base = sim_base.simulate()
    y_base = sim_base.calculate_yield(t, q_base)

    # With QD (+30%)
    sim_qd = QAWGSimulator(MOFParameters(qd_factor=1.3))
    _, q_qd = sim_qd.simulate()
    y_qd = sim_qd.calculate_yield(t, q_qd)

    improvement_pct = (y_qd / y_base - 1) * 100 if y_base > 0 else 0.0

    print(f"Yield without QD : {y_base:.4f} kg/kg")
    print(f"Yield with QD    : {y_qd:.4f} kg/kg")
    print(f"Improvement      : {improvement_pct:.1f}%")

    return {
        "yield_without_qd" : round(y_base, 5),
        "yield_with_qd"    : round(y_qd, 5),
        "improvement_pct"  : round(improvement_pct, 1),
    }


def scaling_estimate(mof_mass_kg: float = 5.0,
                     condenser_efficiency: float = 0.85) -> dict:
    """
    Scale simulation results to a real device.

    Args:
        mof_mass_kg          : Mass of MOF adsorbent in device [kg]
        condenser_efficiency : Fraction of desorbed vapour collected

    Returns:
        dict with water yield estimates
    """
    sim    = QAWGSimulator()
    t, q   = sim.simulate()
    y_kgkg = sim.calculate_yield(t, q)

    water_kg_day  = y_kgkg * mof_mass_kg * condenser_efficiency
    water_L_day   = water_kg_day   # ≈ 1 kg/L for water
    water_mL_hour = water_L_day * 1000 / 24

    return {
        "mof_mass_kg"         : mof_mass_kg,
        "water_L_per_day"     : round(water_L_day, 3),
        "water_mL_per_hour"   : round(water_mL_hour, 1),
        "condenser_efficiency": condenser_efficiency,
        "note"                : "Theoretical upper bound — experimental validation required",
    }


# ─── Entry point ──────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  Q-AWG Simulation — Quantum-Enhanced Atmospheric Water")
    print("  Inventor: Belhalhali Mohamed Amine | Tlemcen, Algeria")
    print("  March 2026 | github.com/swordenkisk/Q-AWG-Patent-Proposal")
    print("=" * 60)

    # ── Basic 24h simulation ──────────────────────────────────────
    print("\nRunning Q-AWG Simulation...")
    simulator = QAWGSimulator()
    t, q = simulator.simulate(duration_hours=24)
    total_yield = simulator.calculate_yield(t, q)
    print(f"Total water yield: {total_yield:.4f} kg water per kg MOF")

    # ── QD enhancement comparison ─────────────────────────────────
    print("\nComparing QD enhancement...")
    result = compare_qd_enhancement()

    # ── Device scaling ────────────────────────────────────────────
    print("\nDevice scaling estimates:")
    for mass in [1, 5, 50]:
        est = scaling_estimate(mof_mass_kg=mass)
        print(f"  {mass:3d} kg MOF → {est['water_L_per_day']:.2f} L/day "
              f"({est['water_mL_per_hour']:.0f} mL/hr)")

    # ── Daily summary ─────────────────────────────────────────────
    print("\nDetailed metrics:")
    summary = simulator.daily_summary()
    for k, v in summary.items():
        print(f"  {k:30s}: {v}")

    print("\n" + "=" * 60)
    print("  Q-AWG: Water from air — powered by the Saharan sun.")
    print("=" * 60)
