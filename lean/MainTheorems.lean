import AR18RaceManMachine.PaperInterface

namespace AR18RaceManMachine

theorem proposition2ComparativeStaticsCore_impl :
    proposition2ComparativeStaticsCoreSpec := by
  intro sigmaHat epsilonL lambdaI lambdaN epsilonGamma
    hsigma hepsilon hlambdaI hlambdaN hgamma
  have hfree : sigmaHat < freeElasticity sigmaHat epsilonGamma lambdaI := by
    simp only [freeElasticity]
    have : 0 < lambdaI / epsilonGamma := by positivity
    linarith
  have hfreePos : 0 < freeElasticity sigmaHat epsilonGamma lambdaI := by linarith
  have hdenI : 0 < sigmaHat + epsilonL := by positivity
  constructor
  · simp only [constrainedAutomationEffect]
    exact div_neg_of_neg_of_pos (by linarith) hdenI
  constructor
  · simp only [constrainedNewTaskEffect]
    positivity
  constructor
  · exact hfree
  constructor
  · simp only [constrainedNewTaskEffect]
    positivity
  constructor
  · simp only [capitalRelativePriceEffect]
    positivity
  · simp only [capitalRelativePriceEffect]
    positivity

theorem proposition3WageRentalDecomposition_impl :
    proposition3WageRentalDecompositionSpec := by
  intro laborShare productivityI productivityN relativeI relativeN
    hs hsl hprodI hprodN hrelI hrelN
  simp only [wageChange, rentalChange]
  constructor
  · nlinarith
  constructor
  · nlinarith
  constructor
  · intro h
    nlinarith
  constructor
  · intro h
    nlinarith
  constructor
  · intro h
    nlinarith
  constructor
  · intro h
    nlinarith
  constructor
  · ring
  constructor
  · ring
  · ring

end AR18RaceManMachine
