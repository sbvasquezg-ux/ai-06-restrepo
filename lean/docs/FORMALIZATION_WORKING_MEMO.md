# Formalization working memo

## Frozen source

- NBER Working Paper 22252, revised June 2017.
- PDF SHA-256: `441d01202afd56ef8002fc24ffc2beb51191741c0b5accb11d2534620dd616b7`.
- Text SHA-256: `364324083516ef31703b52dbaad0405a22a39cd796d0b718587fc01d69ad995e`.
- Official URL: https://www.nber.org/papers/w22252
- No arXiv source was used or found during intake.

## Closed Lean seams

1. Proposition 2 algebraic sign core: positivity of the constrained automation,
   new-task, capital, and free-allocation responses, plus
   `sigmaFree > sigmaHat`, assuming the strictly positive elasticities and
   Lambda terms displayed in the proposition.
2. Proposition 3 wage/rental decomposition: positive wage effect of new tasks,
   positive rental effect of automation, the exact inequalities separating
   positive and negative wage/rental effects, the zero effect of additional
   automation in the unconstrained regime, and the identity that wage change
   minus rental change equals the relative-price change.

Both seams are kernel-checked without `sorry`, `admit`, axioms, or
`native_decide`.

## Open proof boundaries

- Derive the Proposition 2 response formulas from the full static equilibrium
  and Assumptions 1--3.
- Derive labor-share and employment responses from the equilibrium labor
  supply schedule.
- Derive the Proposition 3 fixed-factor productivity coefficients from the
  CES task aggregator and prove their signs under the source assumptions.
- Formalize the NBER capital-threshold clause using the Appendix B proof at PDF
  pages 58--59. Do not substitute the published AER threshold orientation.
- Formalize the remaining main-text and appendix named results in dependency
  order.

## Version-sensitive finding

The June 2017 NBER Proposition 3 statement differs from the later AER
presentation in the direction and notation of the capital-threshold wage
clause. No correction is asserted here. The current Lean surface omits that
clause until its NBER Appendix B derivation has been modeled and independently
reviewed.

## Audit state

The source inventory is not frozen or independently certified. No
source-to-Spec `matches` judgment, final adversarial judgment, accepted graph,
or closeout receipt has been created. The current technical status is
`partially formalized`.
