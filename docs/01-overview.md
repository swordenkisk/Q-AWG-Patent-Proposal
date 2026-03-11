# 1. 🧠 Overview

## What is Q-AWG?

The Quantum-Enhanced Atmospheric Water Generator (Q-AWG) is a passive solar
device that harvests drinking water directly from humid air — even in semi-arid
environments — using three synergistic innovations:

1. **Metal-Organic Frameworks (MOFs)** doped with quantum dots for
   ultra-efficient water vapour capture at low humidity
2. **Solar-thermal desorption** using spectrally selective metamaterials
   that convert sunlight directly into the heat needed to release captured water
3. **Reinforcement learning (RL)** that predicts local humidity cycles and
   optimises the capture/release schedule for maximum daily yield

## Key Advantages

| Feature | Conventional AWG | Q-AWG |
|---------|-----------------|-------|
| Energy requirement | High (active cooling) | Near-zero (passive solar) |
| Minimum humidity | 40–50% | 10–20% |
| Deployment | Centralised | Distributed mesh |
| Optimisation | Manual/Timer | AI-predictive |
| Water quality | Requires post-treatment | Clean at source |
| Maintenance | Complex compressors | Simple solid sorbent |

## System Architecture

```
                    ☀️  Solar radiation
                         │
              ┌──────────▼──────────┐
              │  Metamaterial       │  Solar absorber >95%
              │  Selective Absorber │  Mid-IR emitter <5%
              └──────────┬──────────┘
                         │ Heat (60–80°C)
              ┌──────────▼──────────┐
              │  MOF-303 + QD       │  Adsorption (night)
              │  Adsorber Bed       │◄─── Humid air
              └──────────┬──────────┘  Desorption (day)
                         │ Water vapour
              ┌──────────▼──────────┐
              │  Condenser          │  Passive cooling
              └──────────┬──────────┘
                         │ Liquid water
              ┌──────────▼──────────┐
              │  Collection Tank    │  Clean drinking water
              └─────────────────────┘

              ┌─────────────────────┐
              │  Edge AI (ESP32)    │  Humidity prediction
              │  RL Controller      │  Cycle optimisation
              │  LoRaWAN mesh       │  Fleet coordination
              └─────────────────────┘
```

## Target Applications

- **Off-grid communities** — rural Algeria, Sahel, MENA region
- **Disaster relief** — no infrastructure required, deploy in hours
- **Military forward operating bases** — water independence
- **Agricultural irrigation** — supplement rainfall in arid zones
- **Climate refugees** — portable, self-powered water source

## Performance Targets

| Metric | Target (Phase 1) | Target (Phase 2) |
|--------|-----------------|-----------------|
| Daily yield | 1 L/day/unit | 3 L/day/unit |
| Min humidity | 20% | 10% |
| Energy input | Solar only | Solar only |
| Unit cost | $500 | $150 |
| Lifespan | 5 years | 10 years |
