# Codex Studio

### A Project-Centric Engineering Workspace for Agentic Software Development

An independent product proposal by **TechSoft**. Codex Studio explores a dedicated engineering workspace connecting conversations, tasks, approved decisions, repository guidance, execution evidence and project files.

**Start with the [OpenAI Community article](https://community.openai.com/t/codex-studio-a-project-centric-engineering-workspace-for-agentic-software-development/1408219).** This repository contains the complete English RFC, expanding the article into workflows, state models, integration boundaries, validation criteria and open decisions.

[Read the complete RFC](FULL-RFC.md) · [Browse the six concept images](appendices/A-design-gallery.md#app-a) · [See publication corrections](REVIEW.md)

**Status:** public review draft, based on version 1.1; publication revision **2026-10-21**. This is not an announced OpenAI product, a working implementation or an endorsement. The UI images are conceptual mockups; identities, model labels, dates and metrics are illustrative.

## Contents

### Chapters

- [01. Executive Summary](chapters/01-executive-summary.md#ch-01)
- [02. Current Product Landscape and Capability Baseline](chapters/02-capability-baseline.md#ch-02)
- [03. Real-World Problem Statement](chapters/03-problem-statement.md#ch-03)
- [04. Product Rationale, Vision, and Positioning](chapters/04-vision-positioning.md#ch-04)
- [05. Project-Centric Workspace Architecture and UX](chapters/05-workspace-ux.md#ch-05)
- [06. Tasks and Development Planning](chapters/06-tasks-planning.md#ch-06)
- [07. Engineering Decisions and Project Rules](chapters/07-decisions-rules.md#ch-07)
- [08. Execution Results and Evidence](chapters/08-results-evidence.md#ch-08)
- [09. Project Library and Resources](chapters/09-library-resources.md#ch-09)
- [10. Context, Memory, and Agent Orchestration](chapters/10-context-orchestration.md#ch-10)
- [11. Technical Integration and Trust](chapters/11-integration-trust.md#ch-11)
- [12. Product Packaging and Delivery Strategy](chapters/12-delivery-mvp.md#ch-12)
- [13. Validation and Expected Value](chapters/13-validation-value.md#ch-13)
- [14. Risks, Trade-offs, and Open Questions](chapters/14-risks-questions.md#ch-14)
- [15. Proposal to OpenAI and Next Steps](chapters/15-proposal-next-steps.md#ch-15)

### Appendices

- [Appendix A. UI/UX Concept Gallery](appendices/A-design-gallery.md#app-a)
- [Appendix B. Existing versus Proposed Capability Matrix](appendices/B-capability-matrix.md#app-b)
- [Appendix C. End-to-End Developer Scenario](appendices/C-affiliate-scenario.md#app-c)
- [Appendix D. Conceptual Data Model](appendices/D-conceptual-data-model.md#app-d)
- [Appendix E. References and Evidence](appendices/E-references-evidence.md#app-e)

## Reading paths

- **Concept and scope:** Chapters 01, 03–05 and 12.
- **Engineering review:** Chapters 06–11, followed by the scenario and data model in Appendices C–D.
- **Evidence and feasibility:** Chapter 02, Chapters 13–14 and Appendices B and E.
- **Review questions:** Chapter 15; cite a chapter, requirement (`R-…`), validation case (`V-…`) or open question (`Q-…`) when giving feedback.

The local single-user MVP and later Project Group, hybrid-team, multimodal and specialist-domain extensions have separate gates. The full vision is preserved without treating every extension as a prerequisite for the first release.

## Repository guide

| Path | Purpose |
|---|---|
| `chapters/` | Fifteen editable chapters; reference text |
| `appendices/` | Gallery, capability matrix, worked scenario, model and references |
| `FULL-RFC.md` | Generated single-document reading edition |
| `assets/` | Six unchanged PNGs and their [hash manifest](assets/manifest.json) |
| `REVIEW.md` | Publication corrections, review coverage and verification limits |
| `tools/build_rfc.py` | Rebuild and check the document using Python's standard library |

## Maintain this edition

Edit the chapter or appendix sources, then run from the repository root with Python 3.10 or later:

```sh
python tools/build_rfc.py
python tools/build_rfc.py --check
```

The check validates local links, explicit anchors, table structure, identifier references, image hashes and the generated document. It does not exercise a Studio product or certify external integrations. Source access dates and remaining verification gaps are recorded in [Appendix E](appendices/E-references-evidence.md#app-e).

The shorter community manuscript is maintained separately in [CodexStudio-](https://github.com/techsoftye/CodexStudio-). This repository is the English full-RFC edition; its localization requirements describe the proposed product and do not imply bundled translated documents.
