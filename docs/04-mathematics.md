# 4. 📐 Mathematical Modelling

## 4.1 Adsorption Kinetics — Linear Driving Force Model

$$\frac{dq}{dt} = k_{\text{LDF}}(T) \cdot (q_{\text{eq}} - q)$$

The rate constant follows Arrhenius:

$$k_{\text{LDF}}(T) = k_0 \cdot \exp\left(-\frac{E_a}{RT}\right)$$

Where $k_0 = 0.01$ s⁻¹ (pre-exponential), $E_a = 40{,}000$ J/mol, $R = 8.314$ J/(mol·K).

---

## 4.2 Daily Water Yield Integral

$$Y_{\text{day}} = \int_{t_{\text{ads}}}^{t_{\text{des}}} \left(\frac{dq}{dt}\right)^+ dt$$

Only positive (adsorbing) contributions count toward yield.
Optimisation variables:
- $t_{\text{ads}}$ — adsorption start time
- $t_{\text{des}}$ — desorption start time
- Duration of each phase

---

## 4.3 Deep Q-Network Architecture

**State space** $s_t = [H_t,\ T_t,\ C_t,\ q_t,\ h_t]$ (5-dimensional)

**Network topology**:
```
Input (5)  →  Dense(128, ReLU)  →  Dense(64, ReLU)  →  Dense(32, ReLU)  →  Q-values(3)
```

**Training hyperparameters**:

| Parameter | Value |
|-----------|-------|
| Replay buffer size | 10,000 transitions |
| Batch size | 64 |
| Learning rate | 1e-4 |
| Discount factor γ | 0.99 |
| Target network update | Every 1,000 steps |
| Epsilon (initial) | 1.0 |
| Epsilon (final) | 0.01 |
| Epsilon decay | 0.995 per episode |

**Dueling architecture** (Dependent Claim 9):
$$Q(s, a) = V(s) + A(s, a) - \frac{1}{|A|}\sum_{a'}A(s, a')$$

Separates state value $V(s)$ from action advantage $A(s,a)$ for faster convergence.

---

## 4.4 Condensation Efficiency Model

$$\eta_{\text{cond}} = 1 - \exp\left(-\frac{h_c A_c (T_{\text{dew}} - T_{\text{cond}})}{L \dot{m}_{\text{vap}}}\right)$$

Target: $\eta_{\text{cond}} > 85\%$ through optimised fin geometry.

---

## 4.5 Economic Optimisation

**Cost of water** ($/litre):

$$C_w = \frac{C_{\text{capex}} + C_{\text{opex}} \cdot n_{\text{years}}}{Y_{\text{total}}}$$

At Phase 2 targets ($150 unit cost, 3 L/day, 10 years):

$$C_w = \frac{150 + 10}{3 \times 365 \times 10} \approx \$0.0044\text{/litre}$$

Competitive with piped water in rural Algeria ($0.003–0.01/litre).
