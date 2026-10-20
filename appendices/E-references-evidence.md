<a id="app-e"></a>
# Appendix E. References and Evidence

<a id="s-e-1"></a>
## E.1 Evidence policy

The source draft records official-source access on **2026-10-18**. This edition preserves those historical records without claiming that every page was reverified. Targeted checks on **2026-10-21** cover E-02, E-06, E-12 and E-19; E-31 was added on that date. Dates describe access, not necessarily publication. References describe public behavior at that time; they do not prove availability for every account, platform, version or integration. No installed-runtime test, provider connection test or product prototype was performed.

The register uses short paraphrases. The RFC's state model, consistency rules, workflows and validation design are TechSoft proposals, not claims that OpenAI implements the same architecture. Source absence or failed retrieval cannot establish feature absence.

<a id="s-e-2"></a>
## E.2 Official source register

**Table E-1 — Official references, supported claims and limits**

| ID | Source and final URL | Access date (see E.1) | Supported claim | Inference limit |
|---|---|---|---|---|
| E-01 | [ChatGPT desktop app](https://learn.chatgpt.com/docs/app) | 2026-10-18 | Desktop offers ChatGPT/Codex entry points | No independent Studio endorsement |
| E-02 | [Projects and chats](https://learn.chatgpt.com/docs/projects) | 2026-10-21 | Multiple local folders; primary-folder Git and instruction discovery | No proposed record-schema guarantee |
| E-03 | [Memories](https://learn.chatgpt.com/docs/customization/memories) | 2026-10-18 | Local Codex recall and controls | Recall is not decision approval |
| E-04 | [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | 2026-10-18 | Scoped instruction discovery | No complete semantic-conflict detector |
| E-05 | [Build skills](https://learn.chatgpt.com/docs/build-skills) | 2026-10-18 | Skill discovery and instruction loading | No Studio task-selection contract |
| E-06 | [Codex App Server](https://learn.chatgpt.com/docs/app-server) | 2026-10-21 | Public protocol; documented experimental/production-support limits | No assumed production support, exactly-once dispatch or full missed-event replay |
| E-07 | [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees) | 2026-10-18 | Worktree/local development workflows | Isolation does not prove combined correctness |
| E-08 | [Code review](https://learn.chatgpt.com/docs/code-review) | 2026-10-18 | Review and diff inspection | No Studio acceptance-policy guarantee |
| E-09 | [Scheduled tasks](https://learn.chatgpt.com/docs/automations) | 2026-10-18 | Explicit scheduled workflows | A Studio due date is not a schedule |
| E-10 | [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | 2026-10-18 | Delegated agent workflows | No assumed universal host/event parity |
| E-11 | [Get started with ChatGPT Work](https://learn.chatgpt.com/docs/get-started-with-work) | 2026-10-18 | General reviewable work deliverables | Does not establish Studio's incremental value |
| E-12 | [Codex as a platform](https://developers.openai.com/blog/codex-as-a-platform) | 2026-10-21 | Harness integration/reuse direction | No license, entitlement or support conclusion |
| E-13 | [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security) | 2026-10-18 | Distinct sandbox and approval controls | Studio must validate chosen integration enforcement |

The register retains source URLs and bounded claims from the earlier review. A failed retrieval or changed URL is a reason to recheck a claim, not evidence that a capability is absent. The 2026-10-21 checks are documentary checks only; no integration was exercised.

<a id="s-e-3"></a>
## E.3 Proposal provenance and public materials

The proposal originates in TechSoft's concept drafts and the six supplied UI illustrations. This repository publishes the complete English RFC from that material, with publication corrections recorded in [REVIEW.md](../REVIEW.md). Earlier authoring instructions and review-package metadata are historical inputs, not product requirements or evidence of shipped capabilities.

**Table E-2 — Public proposal materials**

| Material | Purpose | Evidence limit |
|---|---|---|
| [Community discussion](https://community.openai.com/t/codex-studio-a-project-centric-engineering-workspace-for-agentic-software-development/1408219) | Author-supplied link to the community article | The forum body could not be retrieved during this review; no independent content match is claimed |
| [English community manuscript](https://github.com/techsoftye/CodexStudio-) | Separately maintained article and publication images | A concept manuscript, not official OpenAI documentation |
| [RFC chapters](../chapters/) and [appendices](../appendices/) | Editable reference sources for this edition | Proposed behavior, with explicit unresolved decisions |
| [Design gallery](A-design-gallery.md#app-a) and [asset manifest](../assets/manifest.json) | Six unchanged illustrations with dimensions and SHA-256 hashes | Illustrations are not runtime observations or benchmarks |
| [Publication review](../REVIEW.md) | Corrections, document checks and remaining evidence limits | Document validation does not establish product readiness |

<a id="s-e-4"></a>
## E.4 Unverified claims and required evidence

**Table E-3 — Explicit verification gaps**

| Claim not established | Current status | Evidence needed |
|---|---|---|
| Studio exists as an announced or shipped OpenAI product | Not claimed | Official product announcement, if one ever exists |
| Full migration/synchronization of existing conversations into Studio | Requires Validation | Supported API and identity/permission semantics |
| Complete missed-event replay and exactly-once remote side effects | Requires Validation | Versioned runtime guarantees and fault-injection results |
| Every pictured provider works with standalone Studio | Requires Validation | Provider-specific supported integration and authorization tests |
| Standalone packaging is cheaper/faster/lighter | Unmeasured hypothesis | Comparative lifecycle and resource measurements |
| Studio improves productivity or reduces tokens | Unmeasured hypothesis | Chapter 13 study with credible baseline |
| All hidden internal Codex architecture is known | Not claimed | Outside the public evidence and product scope |
| Product name/distribution entitlement is cleared | Unresolved Q-02 | Relevant owner/legal review before external distribution |

<a id="s-e-5"></a>
## E.5 Reverification procedure

Before relying on a historical capability claim for implementation or issuing a new evidence revision, re-open its official source, record changes, identify the chosen runtime and target platforms, and update Appendix B. Preserve the earlier access date in history. Reviewers should challenge both unsupported novelty and unsupported assumptions of compatibility. Public documentation establishes a starting point for integration investigation; the proposed product still requires engineering and user validation.

<a id="s-e-6"></a>
## E.6 Version 1.1 evidence expansion

The source draft records access to the sources below on **2026-10-18**. The targeted checks for this public edition are listed in E.1; the remaining dates are inherited historical records. E-14–E-20 support the group/team comparison; E-21–E-30 support the technology horizon. They establish documented foundations, not tested Studio integrations. Primary vendor/project documentation is not independent evidence of future market adoption.

**Table E-4 — Additional official and primary research/project sources**

| ID | Source | Access date (see E.1) | Supported claim | Limit |
|---|---|---|---|---|
| E-14 | [VS Code multi-root workspaces](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces) | 2026-10-18 | Multiple folders and scoped settings | No cross-project approval guarantee |
| E-15 | [GitLab Groups](https://docs.gitlab.com/user/group/) | 2026-10-18 | Related-project groups and access administration | Studio does not copy permission inheritance |
| E-16 | [GitHub dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers) | 2026-10-18 | Configured development toolchains | No universal platform/device parity |
| E-17 | [Codex Cloud](https://learn.chatgpt.com/docs/cloud) | 2026-10-18 | Reusable multi-repository environments | No Studio group schema or entitlement guarantee |
| E-18 | [Roles and workspace permissions](https://learn.chatgpt.com/docs/enterprise/roles-and-workspace-permissions) | 2026-10-18 | Separate workspace/runtime/provider controls | No unified implicit permission grant |
| E-19 | [Teams and Team Tasks](https://learn.chatgpt.com/docs/enterprise/teams) | 2026-10-21 | Shared tasks and service-account context | Not Studio engineering roles or acceptance policy |
| E-20 | [Codex federation rules](https://developers.openai.com/api/docs/guides/workload-identity-federation/federation-rules) | 2026-10-18 | Bounded workload-to-principal mapping | Existing token lifetime can outlast policy edit |
| E-21 | [Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api) | 2026-10-18 | Real-time voice and visual input | No automatic Studio integration or consent |
| E-22 | [Gemini Robotics](https://deepmind.google/models/gemini-robotics/) | 2026-10-18 | Vision-language-action and local model variants | No general physical-safety guarantee |
| E-23 | [Lingua Franca](https://www.lf-lang.org/) | 2026-10-18 | Research-backed coordination and timing | Not a universal replacement language |
| E-24 | [Scenic](https://scenic-lang.org/) | 2026-10-18 | Probabilistic environment modeling and testing | Simulation does not prove deployment safety |
| E-25 | [Mojo roadmap](https://mojolang.org/docs/roadmap/) | 2026-10-18 | Hardware-oriented language development | Roadmap phases are not delivery dates |
| E-26 | [ROS 2 Rust bindings](https://github.com/ros2-rust/ros2_rust) | 2026-10-18 | Rust integration exists | No market-share or dominance conclusion |
| E-27 | [Microsoft Q# overview](https://learn.microsoft.com/en-us/azure/quantum/qsharp-overview) | 2026-10-18 | Quantum programming language | No practical quantum advantage claim |
| E-28 | [OpenQASM 3 and Qiskit](https://quantum.cloud.ibm.com/docs/en/guides/interoperate-qiskit-qasm3) | 2026-10-18 | Quantum program interchange tooling | Some interoperability remains exploratory |
| E-29 | [Qrisp reference](https://qrisp.eu/reference/index.html) | 2026-10-18 | High-level quantum programming and Jasp compilation | Compilation is not hardware execution |
| E-30 | [IBM Quantum roadmap](https://www.ibm.com/roadmaps/quantum/2030/) | 2026-10-18 | Fault-tolerance and scale targets | Vendor objectives may change; not achieved results |

Version 1.1 extends the concept with Project Groups, a hybrid human/agent role matrix and a technology outlook. These remain product proposals. No actual MetaStore repository, environment, identity configuration or provider workload was inspected or changed. Availability and integration guarantees require a chosen account/version and an authorized feasibility test.

<a id="s-e-7"></a>
## E.7 Goals baseline added for the public edition

**Table E-5 — Additional current official reference**

| ID | Source | Access date | Supported claim | Limit |
|---|---|---|---|---|
| E-31 | [Using Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) | 2026-10-21 | Persistent thread-scoped objectives, lifecycle, budget and evidence checks | Does not establish Studio's task mapping or human acceptance model |

<!-- related-start -->
**Related sections:** [02. Current Product Landscape and Capability Baseline](../chapters/02-capability-baseline.md#ch-02) · [Appendix B. Existing versus Proposed Capability Matrix](../appendices/B-capability-matrix.md#app-b)
<!-- related-end -->
