import Mathlib

/-!
# Paper interface for Acemoglu--Restrepo (2018)

This file exposes the checked algebraic surface currently formalized from
Propositions 2 and 3 of the June 2017 NBER version. It deliberately does not
claim the paper's equilibrium derivation or the capital-threshold clause of
Proposition 3; those remain source-visible proof boundaries.
-/

namespace AR18RaceManMachine

/-- The technology-constrained response of `log (W / R)` to automation in
Proposition 2. -/
noncomputable def constrainedAutomationEffect (sigmaHat epsilonL lambdaI : ℝ) : ℝ :=
  -1 / (sigmaHat + epsilonL * lambdaI)

/-- The technology-constrained response of `log (W / R)` to new tasks. -/
noncomputable def constrainedNewTaskEffect (sigmaHat epsilonL lambdaN : ℝ) : ℝ :=
  1 / (sigmaHat + epsilonL * lambdaN)

/-- The elasticity when firms may reassign tasks across factors. -/
noncomputable def freeElasticity (sigmaHat epsilonGamma lambdaI : ℝ) : ℝ :=
  sigmaHat + 1 / (epsilonGamma * lambdaI)

/-- The response of `log (W / R)` to capital, for a supplied substitution
elasticity. -/
noncomputable def capitalRelativePriceEffect (sigma epsilonL : ℝ) : ℝ :=
  (1 + epsilonL) / (sigma + epsilonL)

/-- Algebraic sign core of Proposition 2. The unresolved paper-level boundary
is the derivation of these displayed response formulas from Assumptions 1--3
and the static equilibrium. -/
def proposition2ComparativeStaticsCoreSpec : Prop :=
  ∀ sigmaHat epsilonL lambdaI lambdaN epsilonGamma : ℝ,
    0 < sigmaHat →
    0 < epsilonL →
    0 < lambdaI →
    0 < lambdaN →
    0 < epsilonGamma →
      constrainedAutomationEffect sigmaHat epsilonL lambdaI < 0 ∧
      0 < constrainedNewTaskEffect sigmaHat epsilonL lambdaN ∧
      sigmaHat < freeElasticity sigmaHat epsilonGamma lambdaI ∧
      0 < constrainedNewTaskEffect
        (freeElasticity sigmaHat epsilonGamma lambdaI) epsilonL lambdaN ∧
      0 < capitalRelativePriceEffect sigmaHat epsilonL ∧
      0 < capitalRelativePriceEffect
        (freeElasticity sigmaHat epsilonGamma lambdaI) epsilonL

/-- Wage-change decomposition displayed in Proposition 3. -/
def wageChange (productivity laborShare relativePriceChange : ℝ) : ℝ :=
  productivity + (1 - laborShare) * relativePriceChange

/-- Rental-rate-change decomposition displayed in Proposition 3. -/
def rentalChange (productivity laborShare relativePriceChange : ℝ) : ℝ :=
  productivity - laborShare * relativePriceChange

/-- Checked wage/rental sign consequences of the Proposition 3 decomposition.
`productivityI` and `productivityN` are the paper's two positive fixed-factor
productivity effects, while `relativeI` and `relativeN` are the relative-price
effects from Proposition 2. Their equilibrium derivation remains explicit
upstream proof debt. -/
def proposition3WageRentalDecompositionSpec : Prop :=
  ∀ laborShare productivityI productivityN relativeI relativeN : ℝ,
    0 < laborShare →
    laborShare < 1 →
    0 < productivityI →
    0 < productivityN →
    relativeI < 0 →
    0 < relativeN →
      0 < wageChange productivityN laborShare relativeN ∧
      0 < rentalChange productivityI laborShare relativeI ∧
      (productivityI < (1 - laborShare) * (-relativeI) →
        wageChange productivityI laborShare relativeI < 0) ∧
      ((1 - laborShare) * (-relativeI) < productivityI →
        0 < wageChange productivityI laborShare relativeI) ∧
      (productivityN < laborShare * relativeN →
        rentalChange productivityN laborShare relativeN < 0) ∧
      (laborShare * relativeN < productivityN →
        0 < rentalChange productivityN laborShare relativeN) ∧
      wageChange 0 laborShare 0 = 0 ∧
      rentalChange 0 laborShare 0 = 0 ∧
      wageChange productivityN laborShare relativeN -
          rentalChange productivityN laborShare relativeN = relativeN

end AR18RaceManMachine
