# 5. 🤖 Hybrid AI Integration

## 5.1 Edge AI — Local Unit Intelligence

Each Q-AWG unit runs a **tiny LSTM forecaster** on an ESP32 microcontroller:

**Model specs**:
- Architecture: 2-layer LSTM, 32 hidden units
- Quantisation: INT8 (4× size reduction vs FP32)
- Input: Last 24h of [T, RH, cloud, q]
- Output: 4h-ahead RH prediction
- Inference time: < 50 ms
- Memory: < 64 KB RAM
- Power: < 0.5 mA (negligible vs solar harvesting)

**Prediction use**:
```
If forecast RH(t+1..t+4) > threshold:
    Schedule adsorption phase now
    Pre-position for high-yield window
Else:
    Schedule desorption (solar heating)
    Collect condensed water
```

---

## 5.2 Deep Q-Network Cycle Controller

The DQN agent decides the operational mode every hour:

```python
# Pseudocode — actual implementation in src/simulation/
state = [humidity, temperature, cloud_cover, water_loading, hour]
action = dqn_agent.select_action(state)  # 0=adsorb, 1=desorb, 2=idle
reward = water_yield(t) - lambda * energy_used(t)
dqn_agent.update(state, action, reward, next_state)
```

**Training environment**: Physics simulation from `qawg_simulation.py`
- 1 episode = 1 simulated year of operation
- ~1,000 episodes to convergence
- Final agent achieves 25–40% more yield vs. fixed timer

---

## 5.3 Federated Learning — Collective Intelligence

**Why federated?**
- Weather data is private (military, competitive agriculture)
- Raw sensor data reveals settlement locations (refugee privacy)
- Centralised training requires constant internet (not available off-grid)

**FedAvg protocol**:
```
For each round r:
  1. Server broadcasts current global model w_r
  2. Each node k trains locally: Δw_k = ∇L(w_r, D_k)
  3. Node uploads only gradient Δw_k  (not raw data D_k)
  4. Server aggregates: w_{r+1} = Σ_k (n_k/n) · Δw_k
  5. Improved model redistributed to all nodes
```

**Benefits**:
- No sensitive weather or location data ever leaves device
- Nodes in different climates contribute complementary knowledge
- System improves with scale without privacy cost
- Resilient: any node can operate fully offline indefinitely

---

## 5.4 RLHF — Reinforcement Learning from Human Feedback

**User feedback loop**:

Users (via SMS or simple button interface) report:
- "Water yield was low today" → increase yield weight $w_1$
- "Running during prayer time is disruptive" → add time constraints
- "Water tastes off" → flag cycle for maintenance review

**Reward function adaptation**:
$$R_{\text{updated}} = w_1(t) \cdot \text{yield} - w_2(t) \cdot \text{energy} - w_3(t) \cdot \text{disruption}$$

Weights $w_i(t)$ updated via Bayesian optimisation based on feedback history.

---

## 5.5 LoRaWAN Mesh Communication

**Protocol**: LoRaWAN Class A (lowest power)
**Range**: 5–15 km in open Saharan terrain
**Packet**: 52 bytes/hour per node (T, RH, q, yield, battery, GPS)
**Power**: 50 mWh/day transmit energy (covered by 5cm² solar cell)

**Mesh topology**: Each node acts as both sensor and repeater.
Minimum 3-node overlap for 99.9% connectivity.

**Data shared across mesh**:
- Hourly [T, RH, cloud, q] readings
- Model gradient updates (federated rounds)
- Maintenance alerts
- Water yield totals (for NGO reporting)
