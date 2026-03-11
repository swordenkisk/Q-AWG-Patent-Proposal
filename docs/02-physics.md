# 2. ⚛️ Advanced Physics

## 2.1 Quantum-Doped MOF Adsorption

Metal-Organic Frameworks are nanoporous crystals with enormous surface area
(>5000 m²/g). Water vapour adsorbs inside the pores via hydrogen bonding.

### Quantum Dot Enhancement

By embedding carbon quantum dots (CQDs) or perovskite quantum dots:

- **Enhanced polarisation**: Quantum confinement increases local electric field,
  strengthening hydrogen bond donors on pore walls
- **Increased capacity**: +30–50% water uptake vs. undoped MOF
- **Tunable enthalpy**: Shifts adsorption energy landscape for low-humidity capture

The quantum dot enhancement factor:

$$\eta_{\text{QD}} = 1 + \alpha \cdot e^{-(d/d_0)^2}$$

Where:
- $\alpha = 0.3$–$0.5$ (enhancement amplitude)
- $d$ = distance from quantum dot surface (nm)
- $d_0$ = effective interaction radius (~2 nm)

### Modified Langmuir Isotherm (with QD Enhancement)

$$q = q_{\text{max}} \cdot \frac{(K \cdot P)^{n}}{1 + (K \cdot P)^{n}} \cdot \eta_{\text{QD}}$$

Where:
- $q_{\text{max}} = 0.3$ kg/kg (MOF-303 saturated capacity)
- $K = K_0 \exp(-E_a / RT)$ (temperature-dependent equilibrium constant)
- $P$ = partial pressure of water vapour (Pa)
- $n$ = heterogeneity parameter (~1 for MOF-303)
- $\eta_{\text{QD}}$ = quantum dot enhancement factor

### Adsorption Kinetics — Linear Driving Force (LDF) Model

$$\frac{dq}{dt} = k_{\text{LDF}}(T) \cdot (q_{\text{eq}} - q)$$

$$k_{\text{LDF}}(T) = k_0 \cdot \exp\left(-\frac{E_a}{RT}\right)$$

This is the standard model used in industrial adsorption modelling (Glueckauf, 1955).

---

## 2.2 Solar-Thermal Metamaterial Desorption

### Selective Solar Absorber

The photonic crystal coating achieves:
- **Absorptance > 95%** in visible + NIR range (0.3–2.5 μm)
- **Emittance < 5%** in mid-IR (2.5–25 μm) → minimal radiative heat loss
- **Operating temperature**: 60–80°C under standard Algerian solar irradiance

### Thermal Energy Balance

$$C_p \frac{dT}{dt} = P_{\text{solar}}(t) - \epsilon \sigma (T^4 - T_{\text{sky}}^4) - h(T - T_{\text{amb}}) - \dot{m}_{\text{des}} \cdot L$$

Where:
- $C_p$ = heat capacity of absorber assembly (J/K)
- $P_{\text{solar}}(t) = G(t) \cdot A \cdot \alpha_{\text{solar}}$ — absorbed solar power (W)
- $\epsilon \sigma (T^4 - T_{\text{sky}}^4)$ — Stefan-Boltzmann radiative loss
- $h(T - T_{\text{amb}})$ — convective loss (h ≈ 5–15 W/m²K)
- $\dot{m}_{\text{des}} \cdot L$ — latent heat consumed by desorption

### Aerogel Insulation Layer

Hydrophobic silica aerogel (thermal conductivity λ ≈ 0.015 W/mK):
- Applied to back/sides of adsorber bed
- Reduces conductive heat loss by >80% vs. uninsulated
- Maintains temperature gradient for efficient condensation

---

## 2.3 Predictive AI Optimisation

### Communication Layer
- **Protocol**: LoRaWAN mesh (up to 10 km range in open terrain)
- **Data shared**: hourly T, RH, q (water loading), yield
- **Frequency**: 1 packet/hour per node (ultra-low power)

### Deep Q-Network Controller

**State space** $s_t$:

| Feature | Symbol | Range |
|---------|--------|-------|
| Current humidity | $H_t$ | 0–100% |
| Air temperature | $T_t$ | 0–50°C |
| Cloud cover | $C_t$ | 0–1 |
| Current loading | $q_t$ | 0–0.3 kg/kg |
| Hour of day | $h_t$ | 0–23 |

**Action space** $a_t$:
- `0` → Adsorb (open to humid night air, no heating)
- `1` → Desorb (activate solar thermal, collect condensate)
- `2` → Idle (hold state, save energy)

**Reward function**:

$$R = \sum_{t} \left( w_1 \cdot \text{water\_yield}(t) - w_2 \cdot \text{energy\_used}(t) \right)$$

Weights $w_1, w_2$ adjusted via RLHF based on user feedback.

### Humidity Forecasting (Edge LSTM)

- **Input**: 24h history of [T, RH, cloud, q]
- **Output**: 4h-ahead RH prediction
- **Architecture**: Quantised INT8, runs on ESP32
- **Memory**: < 128 KB RAM
