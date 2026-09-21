# Source-only inventory

Canonical source: NBER Working Paper 22252, revised June 2017, 87-page PDF.
The ignored local source files are `source/paper.pdf` (SHA-256
`441d01202afd56ef8002fc24ffc2beb51191741c0b5accb11d2534620dd616b7`)
and `source/source.txt` (SHA-256
`364324083516ef31703b52dbaad0405a22a39cd796d0b718587fc01d69ad995e`).

This inventory was made source-first and independently reread against all
4,298 text lines and 87 rendered PDF pages. It is not a semantic receipt. The
mechanical PDF-text scan misses several headings because mathematical symbols
are joined to their labels; the holistic list below restores them.

## Main-text named theory

- Assumption 1, source text lines 400--406.
- Assumption 2, lines 423--430.
- Assumption 3, lines 477--498.
- Proposition 1, lines 537--546.
- Corollary 1, lines 590--592.
- Proposition 2, lines 596--637.
- Assumption 1 prime, lines 776--782.
- Proposition 4, lines 929--952.
- Proposition 5, lines 1009--1020.
- Assumption 4, lines 1233--1242.
- Proposition 6, lines 1319--1345.
- Corollary 2, lines 1468--1469.
- Assumption 1 double-prime, lines 1538--1561.
- Proposition 7, lines 1573--1589.
- Proposition 8, lines 1661--1668.
- Proposition 9, lines 1730--1760.

## Main-text Proposition 3

- Proposition 3, lines 663--712.
- The NBER June 2017 statement at lines 692--693 says there exists an upper
  threshold strictly above the lower threshold, with the automation wage
  effect positive below that upper threshold and negative above it.
- This threshold clause is version-sensitive. It is not silently replaced by
  the published AER wording.

## Appendix named theory

- Assumption 2 prime, lines 1869--1882.
- Lemma A1, lines 1996--1997; PDF extraction places part of the statement
  before the visible label.
- Lemma A2, lines 2025--2045.
- Lemma A3, lines 2286--2299.
- Proposition B1, lines 2988--3042.
- Lemma B1, lines 3195--3200.
- Proposition B2, lines 3910--3928.
- Assumption 2 double-prime, lines 4121--4128.
- Proposition B3, lines 4133--4142.
- Proposition B4, lines 4157--4177.

## Current scope disposition

All named assumptions, propositions, corollaries, and lemmas above remain
normal-scope inventory items. Only two proof-support surfaces are currently
closed in Lean: the displayed sign algebra from Proposition 2 and the
wage/rental decomposition consequences from Proposition 3. They do not close
the full propositions. The equilibrium derivation from Assumptions 1--3,
employment/labor-share mapping, exact productivity-coefficient derivation, the
capital threshold, and every other named result remain pending.

Figures, tables, captions, regressions, simulations, and ordinary narrative
claims are deep-audit material under the default named-theory policy. Displayed
equations are proof support unless needed to interpret a selected named result.
The independent holistic intake review is complete. Materializing its complete
prose-definition ledger and source-region partition into the v11 machine map
remains pending; no completion flag has been fabricated.
