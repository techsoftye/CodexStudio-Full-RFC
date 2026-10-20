# Publication Review

**Edition:** English public review draft based on version 1.1.

**Review date:** 2026-10-21.

**Scope:** fifteen chapters, five appendices and six supplied concept images.

## Corrections in this edition

| Area | Correction and reason |
|---|---|
| Identity | Normalized the company name to **TechSoft** throughout the reference text. Account names inside the original images remain illustrative. |
| Public packaging | Replaced private-review, bilingual-deliverable and ZIP instructions with the scope of this English public repository. Kept the proposed product's localization and RTL requirements. |
| Entry point | Added the author-supplied community article link, full-document link, chapter/appendix contents and reading paths. |
| Baseline | Added documented Codex Goals as an existing foundation to assess, without assuming a Studio integration or equating runtime completion with human acceptance. |
| Runtime feasibility | Made the App Server page's experimental/production-support limitation explicit in Chapter 11 and the capability/evidence tables. Q-01 remains unresolved. |
| Task completion | Made task completion an explicit criterion-checked action in Chapter 06 and Appendix D. Accepting one result alone does not close all work on a task. Added the already-described manual-completion path to the transition table. |
| Independent states | Corrected R-08-01 so it prevents automatic acceptance without contradicting the documented human exception path. Included WaitingApproval in uncertain-connectivity handling. |
| Provider jobs | A confirmed queued job remains Queued; Unknown applies when its state cannot be established. Retained reconciliation before any potentially charged retry. |
| Ownership | Aligned R-11-01 with Project/Project Group ownership while retaining project-owned Tasks and ExecutionAttempts. |
| Provenance and references | Replaced broken links to unpublished authoring materials with available public materials. Distinguished historical source dates from the targeted current checks. |
| Examples | Rephrased conversational references to the author's repositories as illustrative configurations; no real repository audit or experimental results are asserted. |
| Navigation and assets | Corrected image paths for this repository, retained all six PNGs unchanged, and generated a continuous reading edition from the corrected sources. |

The six-tab structure, canonical task form, substantive proposal, optional expansion chapters, stable requirement identifiers and original illustrations are retained. Changes are editorial and consistency corrections to a proposal; they do not implement a product.

## Coverage by part

| Part | Review focus and disposition |
|---|---|
| 01 — Executive summary | Scope, attribution and evidence limits; corrected company name and publication language. |
| 02 — Capability baseline | Existing/proposed distinction and dates; added Goals and explicit dated evidence policy. |
| 03 — Problem statement | Qualitative observations remain separate from measured demand; no unsupported benefit added. |
| 04 — Vision and positioning | Preserved target users, exclusions and optional groups; clarified illustrative provenance. |
| 05 — Workspace UX | Checked six tabs, More Details versus task creation, contextual panels, accessibility and empty/error states. |
| 06 — Tasks | Checked canonical fields, hierarchy and completion guards; corrected explicit result/manual completion transitions. |
| 07 — Decisions and rules | Checked exact-version human approval, supersession, source authority, conflicts and group applicability. |
| 08 — Results | Checked five independent state dimensions, snapshots, review exceptions and retry; clarified R-08-01 and uncertain connectivity. |
| 09 — Library | Checked Project/Session views, file identity, revocation, associations and optional connectors. |
| 10 — Context | Checked required guidance, manifests, drift, environment identity and combined evidence; clarified example wording. |
| 11 — Integration and trust | Checked durable dispatch, recovery, permissions and team boundaries; corrected ownership and queued-job semantics; updated support limitation. |
| 12 — Delivery | Preserved narrow MVP and conditional expansion gates; technology horizon remains a dated outlook, not a delivery promise. |
| 13 — Validation | Checked measures, credible baseline, exceptions and proposed cases; none is reported as an executed product test. |
| 14 — Risks and questions | Retained owners, alternatives and gates; no unresolved integration or authority decision is treated as approved. |
| 15 — Next steps | Replaced obsolete private/bilingual packaging instructions with public English review scope. |
| A — Gallery | Retained six designs and detailed visible/interaction/difference notes; fixed paths and manifest link. |
| B — Capability matrix | Retained existing/proposed/validation distinctions; added B-28 and dated-check qualifications. |
| C — Scenario | Traced planning, authorization, partial verification, correction and group handoff; outcomes remain fictional. |
| D — Data model | Checked ownership, cardinalities, immutable subjects and invariants; separated result acceptance from task completion. |
| E — Evidence | Replaced inaccessible archive links, preserved historical dates and added current source-specific checks and E-31. |

## Verification

The repository check passed on 2026-10-21: 15 chapters, 5 appendices, 6 PNGs, 69 requirements, 18 proposed validation cases, 12 open questions, 11 hypotheses, 21 model invariants, 31 external reference entries and 28 capability rows. It checked local links, explicit anchors, table columns, identifier definitions/references, image dimensions/hashes and exact regeneration of `FULL-RFC.md`.

GitHub's Markdown API rendered README.md and FULL-RFC.md successfully (HTTP 200). The complete edition rendered 55 tables and all six image references with one top-level title. This verifies Markdown rendering, not external website availability or product UI behavior.

A separate preservation comparison confirmed that all 141 files in the original source archive remained unchanged and that all six published PNGs matched their source bytes. No product-test result is implied. The reproducible document check is:

```sh
python tools/build_rfc.py --check
```

## Evidence limits

- The source draft records official-document access on 2026-10-18. This edition rechecked E-02, E-06, E-12 and E-19 on 2026-10-21 and added E-31. Other source dates are inherited records, not a claim of complete current revalidation.
- The community URL was supplied by the author. Its forum body could not be retrieved during this review, so the pasted post was not independently compared with the manuscript.
- The six illustrations retain their original bytes. Their sample metrics, names and controls are not proof of implemented behavior.
- No Studio runtime integration, prototype, provider job, usability study or proposed V-case was executed. Q-01 through Q-12 remain decisions for the responsible future reviewers.

For source URLs and claim limits, see [Appendix E](appendices/E-references-evidence.md#app-e). For the complete proposal, see [FULL-RFC.md](FULL-RFC.md).
