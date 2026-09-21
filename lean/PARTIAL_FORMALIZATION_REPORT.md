# Partial formalization report

## Source and scope

This development uses NBER Working Paper 22252, revised June 2017. The local
ignored PDF and extracted text are byte-pinned in the audit metadata. The
technical status is **partially formalized**.

The checked Lean surface covers two algebraic proof seams:

1. Proposition 2's displayed comparative-static formulas imply the advertised
   signs:

   \[
   -\frac{\Lambda_I}{\hat\sigma+\varepsilon_L}<0,\qquad
   \frac{\Lambda_N}{\hat\sigma+\varepsilon_L}>0,\qquad
   \sigma_{\mathrm{free}}
     =\hat\sigma+\frac{\Lambda_I}{\varepsilon_\gamma}>\hat\sigma.
   \]

   It also proves positivity of the displayed capital responses and the
   new-task response in the free-allocation regime.

2. Proposition 3's decomposition

   \[
   d\ln W=d\ln Y|_{K,L}+(1-s_L)d\ln(W/R),\qquad
   d\ln R=d\ln Y|_{K,L}-s_Ld\ln(W/R)
   \]

   implies the checked wage/rental sign conditions: a positive new-task
   productivity and relative-price effect raises wages; a positive automation
   productivity effect combined with a negative relative-price effect raises
   the rental rate; and the remaining wage/rental signs are determined by the
   displayed comparison of productivity and displacement terms. In the
   unconstrained regime, zero productivity and relative-price effects from
   additional automation give zero wage and rental effects.

These are conditional algebraic consequences of source-displayed formulas.
They do not derive those formulas from the paper's equilibrium model.

## Checked declarations

- `AR18RaceManMachine.proposition2ComparativeStaticsCore`
- `AR18RaceManMachine.proposition3WageRentalDecomposition`

Their transparent semantic targets are
`proposition2ComparativeStaticsCoreSpec` and
`proposition3WageRentalDecompositionSpec`. Both compile without
`sorry`, `admit`, new axioms, opaque proof shortcuts, or
`native_decide`.

## Open boundaries

- The static equilibrium, Assumptions 1--3, and the CES task aggregator have
  not been formalized deeply enough to derive the Proposition 2 response
  formulas.
- Proposition 2's labor-share and employment clauses are not covered.
- Proposition 3's exact fixed-factor productivity formulas and their source
  inequalities are not derived.
- The capital-threshold wage clause in Proposition 3 is not covered.
- Propositions 1 and 4--9, Corollaries 1--2, Lemmas A1--A3, Lemma B1,
  Propositions B1--B4, and the named model assumptions remain unformalized.
- Figures, tables, regressions, empirical results, simulations, captions, and
  ordinary narrative prose are outside the default named-theory proof target.
  Their headings remain source-inventoried as deep-audit material where
  applicable.

## Version-sensitive threshold clause

The June 2017 NBER version says that there is an upper capital threshold above
the lower threshold and that the automation wage effect is positive below the
upper threshold and negative above it. The later AER presentation uses
different threshold notation and direction. This development preserves the
NBER version and does not silently replace or correct it. A full treatment
must first formalize and review the corresponding Appendix B derivation.

## Independent review

An isolated source-first reviewer reread the full 4,298-line, 87-page source,
without consulting Lean or authoring artifacts. It inventoried every named
main-text and appendix result and identified the multi-clause structure of
Propositions 2 and 3. A follow-up visual inspection of printed page 11
confirmed the three formulas shown above; the reviewer corrected an initial
parenthesization error in its own report.

A second context-isolated reviewer examined only the exact Proposition 2 and 3
source spans, Appendix B lines 3112--3194, and the complete three-file Lean
surface. Its bounded diagnostic returned two
`matches_selected_algebraic_atom` judgments, two `not_covered` judgments,
and zero mismatches:

- the Proposition 2 endpoint matches the selected algebraic sign facts shown
  by its expanded definitions, but it is not equivalent to full Proposition 2
  because it lacks the Lambda definitions, equilibrium derivative equalities,
  regime conditions, zero automation effect in the free regime, and
  labor-share/employment conclusions;
- the Proposition 3 endpoint matches the wage/rental decomposition shell and
  its conditional sign consequences, but it is not equivalent to full
  Proposition 3 because it does not bind the relative-price term to the
  Proposition 2 differential, derive productivity effects and factor-price
  orderings, establish either regime, prove the capital threshold, or show
  paper-model instances for the “may reduce” branches.

The source inventory is documented in `docs/SOURCE_INVENTORY.md`. Both
independent reviews are diagnostic inputs to this partial report, not accepted
semantic receipts. No accepted obligation graph, final adversarial panel,
final validation report, or closure receipt is claimed.

## Validation

- Focused target build: `lake build +AR18RaceManMachine`.
- Contribution check: `python3 scripts/paper_contribution.py check
  AR18RaceManMachine --fast`.
- The complete output of the latter is retained in `CHECK_OUTPUT.txt`.
- The formalization protocol validator reports
  `OK formalization-audit-protocol-2026-09-01`.

The closeout planner does not issue an acceptance credential in this uncommitted
contribution tree. Its current required action is to inspect/register the
`lakefile.toml` transition after commit. That mechanical blocker is separate
from the substantive open source-model and source-coverage boundaries above.
