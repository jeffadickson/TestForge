# Epsilon3 deep dive and TestForge requirements extraction

**Reviewed 14 October 2026.** The request's “esilon 2” is interpreted as **Epsilon3, including its Epsilon3 2.0 platform announcement**. This is a public-document assessment, not a hands-on product qualification. No account, paid trial, hardware connection or recovery experiment was performed. Public product pages, changelogs and the API reference form the evidence; unavailable help-center content was not assumed. All sources are linked in the [source register](SOURCES.md).

## Decision and scope

Epsilon3 deserves a serious evaluation as a procedure and operations platform for TestForge's intended workflow. Its documented features address much more than instruction display: structured execution, granular signatures, staged review, run changes, conditional flow, hardware-facing integrations and later reconciliation of offline work. These make it a strong requirements benchmark. They do not establish that its actual deployment can satisfy our full disconnected Python/VISA campaign, durable evidence, local authority and analysis-closure requirements.

The appropriate build-versus-buy question is therefore: **Can a configured Epsilon3 deployment pass the same evidence and recovery gates we would require of TestForge, at acceptable cost and with sufficient inspectability?** A proprietary product can pass those gates; an open implementation can fail them. API availability helps integration but does not establish source access, redistribution rights, deterministic recovery or freedom from vendor services.

This study adds **26 requirements**, bringing the current catalog from **96 to 122**. Each addition includes priority, accountable subsystem, an acceptance check, source IDs, related baseline requirements and an explicit derivation rationale. Existing requirements remain unchanged. The historical v0.1 specification remains archival. The canonical [catalog](../requirements/requirements.json) and [readable requirements](../requirements/REQUIREMENTS.md) hold the normative proposed wording; this report explains the choices.

## What 2.0 means

The 2.0 announcement describes a broader platform spanning execution and adjacent hardware lifecycle functions, not simply a second-generation test sequencer. Treat it as product direction and positioning, then verify individual capabilities against dated releases. The June changelog still identifies underlying releases as v1.214–1.215, illustrating why the marketing name alone is an inadequate configuration identifier. [S46](SOURCES.md#s46--epsilon3-20-announcement), [S49](SOURCES.md#s49--epsilon3-changelog-101).

Connect requires particular care. Its announcement distinguishes cross-organization viewing/sharing from future commenting, signoffs and portals. September's changelog subsequently documents scoped inventory sharing. Do not infer that every announced portal or shared-action capability has shipped, or that external observers hold approval authority. Ask for the exact tenant version, enabled modules, permissions and supported actions in the proposed configuration. [S47](SOURCES.md#s47--epsilon3-connect-announcement), [S48](SOURCES.md#s48--epsilon3-changelog-106).

## Evidence map

“Documented” below means vendor-described, not independently demonstrated. Historical releases establish feature precedents, not a guarantee of current behavior in every edition. TestForge implications are our engineering analysis.

| Area | Documented observation | Implication for TestForge | Sources |
|---|---|---|---|
| Authoring | Word conversion, reusable templates and content snippets | Preserve import meaning and dependency provenance | S51, S52 |
| Inputs | Prefilled defaults and required/optional content blocks | Separate a suggested value from an observed value | S52, S49 |
| Flow | Variables and sections participate in branching; batch steps permit planned repetitions | Persist evaluated decisions and distinguish cycles from retests | S53, S58 |
| Time | Duration can drive branching; step duration accounts for pauses | Define dwell and clock semantics explicitly | S59, S57 |
| Review | Sequential stages with configurable approval clearing | Approval applicability must follow content and review round | S57 |
| Signatures | Row signatures and revocation with history | Use stable evidence scope; withdrawal is distinct from re-execution | S56 |
| People | Project-specific roles and skills that can disable permissions on expiry | Check qualifications at action time, including offline | S50 |
| Holds | Constraints apply at run, section and step levels; release can be automatic or manual | Keep independent holds and local hardware-resume authority | S48 |
| Changes | Approved redlines can be offered across active runs and incorporated into the master | Evaluate each receiving run's state and applicability | S55 |
| Automation | Command failure can fail a step; external telemetry and command interfaces exist | Preserve command outcome distinctions and data validity | S55, S08 |
| Article state | Component changes during runs and serial/lot genealogy | Associate each observation with its effective configuration | S49, S59 |
| Review support | Attachment comparisons, tasks and branching from old procedure versions | Compare compatible context and preserve handover obligations | S54 |
| Workflow | Trigger/condition/action administrative automation | Require durable, duplicate-safe side effects | S51 |
| Test program | Plans, cases, points, requirements and hazards are part of product scope | Track planned condition coverage as well as executed steps | S61 |
| Offline | Step inputs, comments, attachments and prepared starts documented in separate releases | Require an action-by-action offline contract | S05–S07 |
| Offline selection | March 2025 release requires enabling offline use for selected procedures | Eligibility and actual readiness must be distinguishable | S58 |

## Authoring: making procedure content executable without losing meaning

A flight procedure contains more than paragraphs. A warning can constrain several following steps; a table row may identify a unique connector; a copied expected value may look indistinguishable from a measurement. Our import process must expose unresolved structure and require an author to reconcile it before release. Import speed is secondary to preserving instructions, cautions, units and evidence boundaries. This extends PROC-07 through PROC-10 rather than assuming document conversion produces an approved executable procedure.

Reusable content should reduce duplicated maintenance without making released runs mutable. A package should record both the reusable source identity and the exact expanded content used. Updating a common grounding instruction should identify affected drafts and releases, then follow change control. It must not silently alter a signed historical run. PROC-09 makes this dependency explicit; PROC-02 already establishes immutability.

Defaults are useful for metadata and suggested setpoints, but dangerous when treated as evidence. TestForge should present source and confirmation state next to the value. A nominal pressure inserted by a template cannot satisfy a pressure observation. PROC-11 requires this distinction even if the number happens to fall inside limits. Imported and copied values require the same treatment.

The runtime also needs an explanation of why a branch was taken. “Section skipped” is insufficient if a later reviewer cannot reconstruct the variable values and rule revision that selected the path. Missing data must not silently become false. A batch iteration needs its own identity and evidence, while repeating a failed iteration needs a new attempt. PROC-12 and PROC-13 cover these different concerns. PROC-14 extends verification beyond one run to a planned matrix of conditions; five successful cells do not satisfy a six-cell plan.

## People, witnesses and review

An assigned role is not enough to establish current qualification. Skill scope, expiry, applicable procedure and delegated authority matter at the moment of action. AUTH-09 adds an evaluated qualification snapshot. Offline operation should use bounded locally available authority; it cannot discover a remote revocation instantaneously. Reconnection therefore reconciles newly known restrictions without falsifying earlier event history. The acceptable validity interval remains a QA policy decision.

Row-level signatures are valuable for connector inspections, torque tables and repeated observations. The signed subject must be an immutable row identity and evidence digest, never its current screen position. Required and optional fields must be declared before signing. A subsequently entered optional field must not appear covered by a prior signature. AUTH-10 makes scope explicit.

Withdrawal needs its own lifecycle. A mistaken QA click should not force an engineer to repeat a potentially destructive operation just to correct the record. AUTH-11 preserves the original approval, adds the withdrawal event and invalidates dependent acceptance as necessary. It does not assert that the physical test was undone. The existing CHG-06 retest lifecycle remains separate.

Multiple approvers are already covered by AUTH-03. The new AUTH-12 addresses a different failure: retaining an earlier engineering approval after a consequential edit during the QA stage. Review-round identity, comment disposition and the content revision under review should be visible together. Observers may follow the discussion without occupying an approval slot. A notification, read receipt or task completion must never substitute for an approval.

## Execution, holds and redlines

A paused run can have several independent reasons: an unresolved discrepancy, an expired calibration, a QA witness hold, or a prerequisite run still underway. EXEC-09 adds scoped constraints and prevents clearing a parent hold from implicitly clearing its children. The interface should show what blocks progress, who owns it and what evidence will clear it.

Administrative readiness and physical readiness are different. A remote issue changing status does not prove a local fixture is safe to energize. EXEC-10 requires an authorized local resume decision and fresh readiness checks before commands. Equipment-specific interlocks remain independent of this software. This is a TestForge design choice; it is not a claim that Epsilon3's configurable automatic resume is inherently unsafe.

Redline propagation is useful during campaigns with several stations, but the receiving runs may be in very different states. One has not reached the changed step; another is executing it; a third has already signed it. CHG-09 requires separate applicability and impact decisions. A future run can adopt a new approved revision. An active run needs a controlled adoption event. A completed observation retains what was actually done and may require reassessment or retest. Publishing the same text everywhere is not equivalent to completing those decisions.

Duration rules deserve their own acceptance cases. Elapsed wall time, active work time and valid physical dwell are different quantities. A chamber may stop meeting conditions during a pause even though the clock keeps running. EXEC-11 requires an explicit time policy; HW-10 requires valid, fresh observations across the required window. Neither clock rollback nor a stale passing sample should satisfy a soak requirement.

## Python, instruments, databases and APIs

The public integration material documents telemetry, commanding, external data and external run triggers. It does not by itself prove that a requested Python dependency, NI-VISA stack, USB driver or proprietary database client executes locally in the intended offline deployment. Obtain a concrete topology showing the browser, Epsilon3 services, integration middleware, Python process, device driver and instrument. Identify which components require WAN connectivity, licensing or centralized identity. S08 supports integration scope; HW-01 through HW-08 remain the acceptance baseline.

The public API reference includes procedure editing, runs, commanding, roles and related resources. Its draft-step update documentation describes atomic batches and last-writer-wins behavior rather than compare-and-swap. This narrow observation motivates SEC-09; it is not evidence that all product editing behaves that way. API coverage also does not establish approval equivalence or transactional behavior across hardware, records and remote services. [S60](https://docs.epsilon3.io/).

For TestForge, a service credential ingesting a measurement cannot also impersonate a QA witness. SEC-10 makes that boundary explicit. Consequential API edits need revision preconditions and conflict responses. Hardware commands need a durable intent record and an outcome that can remain unknown. HW-09 prevents rejected, failed, timed-out and ambiguous commands from collapsing into a single generic failure with unsafe automatic progression.

Loom/Loon and calibration systems remain integration targets whose current schema and authority contracts are unresolved. Use adapters and retain the records actually consulted, including their provenance and freshness. During an outage, a declared approved snapshot may be usable; an unavailable required lookup must produce a visible blocker. Do not quietly replace the source database with fabricated or stale values. No access to a live internal database was used for this study.

## Offline: the most consequential unresolved fit question

The research establishes that Epsilon3 has documented offline behavior. It would be inaccurate to call it online-only. Early releases cover step data, later comments and attachments, and prepared procedure starts. A later release changes explicit procedure eligibility. Those statements should drive a deployment-specific demonstration, not an assumption of complete disconnected operation.

| Question | Evidence status | Required demonstration |
|---|---|---|
| Can prepared procedures start offline? | Historically documented, S06 | Start after a disconnected reboot using the proposed deployment |
| Are offline comments and attachments supported? | Historically documented, S07 | Capture files, interrupt persistence, recover and reconcile |
| Must a procedure be enabled? | Documented setting in S58 | Show eligibility, all dependencies and readiness together |
| Can local Python/VISA run without vendor services? | Not established by reviewed evidence | Disconnect WAN and central database before hardware execution |
| Can two local users independently sign? | Not established for isolated deployment | Operator and QA on an isolated LAN with bounded credentials |
| Can redlines be approved and adopted offline? | Complete behavior not established | Approve a run change locally and later reconcile a conflicting change |
| Are acknowledged writes power-loss durable? | Not established | Interrupt actual target storage at transaction boundaries |
| What survives browser restart, logout or storage pressure? | Not established | Exercise each condition and inspect retained evidence |
| How are conflicting offline actions resolved? | Signed-record semantics not established | Preserve both branches and prevent silent approval overwrite |
| Can records be reconstructed without subscription services? | Full portability not established | Export and independently verify a complete run and analysis |

OFF-09 requires a capability manifest listing every action and dependency. SYNC-09 makes local commitment, transfer and central verification separately visible. These refine existing local durability and synchronization requirements rather than replacing them. A green network icon is not a completeness receipt.

The station design should remain browser-based with a local service and durable store. Browser storage may cache presentation data, but authoritative evidence must meet the crash and retention requirements on approved storage. The proposed station architecture is not inferred from Epsilon3 internals. A server installed on premises is also not automatically a portable disconnected station; deployment topology must be evaluated separately.

## Analysis, configuration and closure

Comparison views help reviewers spot changes, but similar images or measurements may come from different configurations, limit revisions or calibration chains. DATA-09 requires context beside the comparison. CAL-09 tracks component substitutions at the effective run position so that old evidence cannot accidentally be reassigned to new hardware. This adds configuration chronology without requiring TestForge to become a complete inventory or purchasing platform.

Separate execution completion, analysis approval, reconciliation and final closure remain mandatory in the baseline. Epsilon3's documented test-management and task features motivate useful workflow affordances; the reviewed evidence does not establish equivalence to our complete closure model. A demonstration must show which checks are native, configured or custom, and who can override them.

OPS-10 adds explicit incoming-operator acknowledgment during handover. OPS-11 separates administrative workflow automation from hardware commands and requires durable retry accounting. OPS-09 permits custom metadata without letting an unversioned configuration field alter acceptance rules. These additions address the operational gaps around the runner, where significant evidence loss can occur even when the instrument script works correctly.

## Requirements disposition and delivery priorities

| Disposition | Requirement IDs | Why |
|---|---|---|
| P0 authoring/flow integrity | PROC-11, PROC-12 | Prevent false observations and unreconstructable branching |
| P0 runtime integrity | EXEC-09–11, HW-09–10 | Constrain holds, command outcomes and observation windows |
| P0 identity/review integrity | AUTH-09–12, CHG-09 | Preserve qualification, signature scope and change applicability |
| P0 evidence/offline integration | CAL-09, OFF-09, SEC-09–10, SYNC-09, OPS-10 | Preserve effective context and authoritative state across boundaries |
| P1 capabilities | PROC-09–10, PROC-13–14, CHG-10, DATA-09, OPS-09, OPS-11 | Reuse, import, campaign coverage, comparison and administrative automation |

These are proposed requirements, not a declaration that all must be implemented before the first prototype. P0 denotes the controlled flight-hardware pilot gate. P1 features may be staged only when excluded from that pilot's approved scope. For example, excluding planned batch operation does not waive retest evidence preservation.

Do not expand the initial build into payroll, purchasing, supplier portals, financial planning, full ERP, CAD authoring or AI-generated procedure approval. Keep article/configuration identity and external record links, then integrate existing systems. AI-assisted drafts, if later added, should enter the same controlled authoring process as human drafts. No AI output should acquire release or signoff authority automatically.

## Evaluation and procurement next step

Use the [Epsilon3 evaluation script](EPSILON3_EVALUATION.md) with a vendor-assisted trial. Public trial and pricing pages are already recorded as S30 and S45. A marketing tour can establish usability, but not recovery or instrument compatibility. No trial has been activated and no vendor was contacted as part of this work.

Request a written configuration and quote covering operator, QA, author, administrator and observer access; automation/API access; offline preparation; on-premises or isolated deployment; support; upgrades; exports; and post-termination record access. Ask which demonstrated capabilities depend on optional modules or vendor customization. Obtain the exact compatibility list and documented limits rather than estimating cost from a headline seat price.

Choose buy/configure if the demonstrated solution passes the required workflow, recovery and inspectability gates with acceptable contractual rights. Consider a hybrid only after proving which system owns commands, signatures and evidence during disconnection. Proceed with TestForge implementation if remaining failures are material and reproducible, and the team accepts responsibility for operations, migration, drivers and qualification. This study strengthens the evaluation criteria; it does not yet settle the purchase or architecture decision.
