# 3. 🧪 Chemical Innovations

## 3.1 MOF-303 Selection

**Material**: Aluminium fumarate MOF (MOF-303, [Al(OH)(fumarate)]_n)

**Why MOF-303?**

| Property | Value | Significance |
|----------|-------|-------------|
| BET surface area | >800 m²/g | Very high water vapour contact |
| Water uptake at 20% RH | ~0.23 kg/kg | Works in semi-arid conditions |
| Hydrothermal stability | >100 cycles | Long operational lifespan |
| Synthesis solvent | Water | Green, scalable chemistry |
| Raw materials | AlCl₃ + fumaric acid | Low cost, widely available |
| Regeneration temperature | 60–80°C | Achievable by solar alone |

MOF-303 is specifically selected for its **S-shaped isotherm** — it adsorbs
a large amount of water over a narrow humidity range, maximising the working
capacity per cycle.

---

## 3.2 Carbon Quantum Dot (CQD) Synthesis from Date Pits

**Innovation**: Using Algerian agricultural waste as a sustainable CQD precursor.

Algeria produces ~500,000 tonnes of dates annually — generating vast quantities
of date pits (noyaux de dattes) that are currently discarded.

### Synthesis Protocol

```
Step 1: Raw material preparation
  → Collect date pits (Phoenix dactylifera)
  → Wash, dry 24h at 80°C
  → Grind to <200 μm powder

Step 2: Hydrothermal carbonisation
  → Dissolve 2g powder in 20 mL deionised water
  → Transfer to Teflon-lined autoclave
  → Heat to 180°C for 12 hours
  → Cool to room temperature naturally

Step 3: Purification
  → Centrifuge at 10,000 rpm for 30 min
  → Filter through 0.22 μm membrane
  → Dialyse 24h (MWCO 1000 Da)

Step 4: Size selection (target: 2–5 nm)
  → Column chromatography (Sephadex G-25)
  → Collect 2–5 nm fraction

Step 5: Surface functionalisation
  → Treat with 3-aminopropyltriethoxysilane (APTES)
  → Introduces –NH₂ groups for MOF bonding
  → Final concentration: 5–10 mg/mL in water
```

### CQD Properties (Expected)
- Size: 2–5 nm (quantum confinement regime)
- Surface groups: –COOH, –OH, –NH₂ (after functionalisation)
- Quantum yield: 15–35% (fluorescent — useful for QC testing)
- Zeta potential: −25 to −35 mV (colloidal stability)

---

## 3.3 One-Pot MOF-QD Composite Synthesis

**Key innovation**: CQDs incorporated *during* MOF crystallisation —
not as a coating. This ensures intimate contact and maximises enhancement.

### Protocol

```
Reagents (for 5 g MOF-QD):
  • AlCl₃·6H₂O ............. 2.41 g
  • Fumaric acid ............. 1.16 g
  • CQD suspension (10 mg/mL). 15 mL (5 wt% CQD loading)
  • Deionised water .......... 50 mL

Procedure:
  1. Dissolve AlCl₃·6H₂O in 25 mL DI water at room temperature
  2. Dissolve fumaric acid in 25 mL DI water (adjust pH to 7 with NH₄OH)
  3. Mix both solutions, add CQD suspension dropwise under stirring
  4. Transfer to Teflon-lined autoclave
  5. Hydrothermal synthesis: 120°C, 24 hours
  6. Cool, filter, wash 3× with ethanol
  7. Activation: 150°C under vacuum for 12 hours
  8. Characterise: PXRD, BET, TGA, water uptake isotherm

Quality check:
  → PXRD peaks match MOF-303 reference (confirms crystal structure)
  → BET surface area >600 m²/g (confirms porosity retention)
  → Water uptake at 20% RH ≥ 0.28 kg/kg (confirms QD enhancement)
```

---

## 3.4 Metamaterial Solar Absorber Coating

Applied to the top surface of the adsorber bed:

**Composition**: Tungsten nanoparticle-doped TiN cermet
- **Absorptance**: >95% at λ = 0.3–2.5 μm
- **Emittance**: <5% at λ = 2.5–25 μm
- **Deposition**: RF sputtering or spray pyrolysis
- **Thickness**: 200–500 nm

**Alternative**: Black chrome coating (lower cost, ~88% absorptance)

---

## 3.5 Thermal Management

**Back insulation**: Hydrophobic silica aerogel blanket (10 mm thick)
- Thermal conductivity: λ = 0.015 W/m·K
- Prevents conductive heat loss during desorption
- Maintains temperature gradient: collector > ambient > condenser

**Condenser design**: Finned aluminium surface on shaded face
- Temperature: ~5°C below ambient (passive radiative cooling at night)
- Condensation efficiency: >85% of released water vapour
