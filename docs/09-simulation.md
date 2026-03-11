# 9. 💻 Simulation Code

See `/src/simulation/qawg_simulation.py` for the full implementation.

## Model Overview

The simulation implements:
- **Modified Langmuir isotherm** with quantum dot enhancement factor η_QD
- **Diurnal humidity/temperature cycles** (sinusoidal, 24h period)
- **Linear driving force kinetics** (LDF model — industry standard)
- **ODE integration** via `scipy.integrate.odeint`

## Key Parameters

| Parameter | Symbol | Value | Unit | Source |
|-----------|--------|-------|------|--------|
| Max loading | q_max | 0.30 | kg/kg | MOF-303 literature |
| Equil. constant | K₀ | 1e-4 | 1/Pa | Fitted to isotherm |
| Activation energy | Eₐ | 40,000 | J/mol | LDF model |
| Rate constant | k₀ | 0.01 | 1/s | Fitted |
| QD enhancement | η_QD | 1.30 | — | 30% boost |
| Base temperature | T_base | 20.0 | °C | Algeria spring |
| Temp amplitude | ΔT | 10.0 | °C | Diurnal swing |
| Base vapour pressure | P_base | 10.0 | hPa | ~60% RH at 20°C |

## Usage

```python
from qawg_simulation import QAWGSimulator, MOFParameters, compare_qd_enhancement

# Basic simulation
simulator = QAWGSimulator()
t, q = simulator.simulate(duration_hours=24)
yield_total = simulator.calculate_yield(t, q)
print(f"Daily yield: {yield_total:.4f} kg water per kg MOF")

# Compare with/without quantum dots
compare_qd_enhancement()
# Output:
#   Yield without QD: 0.0317 kg/kg
#   Yield with QD:    0.0412 kg/kg
#   Improvement: 30.0%

# Custom parameters
params = MOFParameters(
    q_max=0.35,        # Higher-capacity MOF variant
    qd_factor=1.45,    # Optimised QD loading
    Ea=38000,          # Lower activation energy
)
sim2 = QAWGSimulator(params)
t2, q2 = sim2.simulate(duration_hours=48)  # 2-day simulation
```

## Expected Output

```
Running Q-AWG Simulation...
Total water yield: 0.0412 kg water per kg MOF

Comparing QD enhancement...
Yield without QD: 0.0317 kg/kg
Yield with QD:    0.0412 kg/kg
Improvement: 30.0%
```

## Scaling to Real Device

For a 1 kg MOF bed at 30% RH in Algerian conditions:
- Daily yield: 0.041 kg/kg × 1 kg MOF = **41 g/day**
- At 5 kg MOF per unit: **~0.2 L/day (Phase 1 target)**
- At 50 kg MOF per installation: **~2 L/day (Phase 2 target)**

Note: Real yield depends on airflow, cycle timing, and condenser efficiency.
The simulation provides a theoretical upper bound. Experimental validation
is planned for Phase 1 (months 6–12).

## Future Simulation Modules

- [ ] `thermal_model.py` — full energy balance (solar, convection, radiation)
- [ ] `rl_environment.py` — OpenAI Gym environment for DQN training
- [ ] `mesh_simulation.py` — multi-unit federated learning simulation
- [ ] `economic_model.py` — LCOW (levelised cost of water) calculator
- [ ] `climate_scenarios.py` — NOAA weather data integration
