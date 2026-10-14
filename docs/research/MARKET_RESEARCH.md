# TestForge: market research and build-versus-buy assessment

**Research date:** 14 October 2026. **Status:** engineering assessment, not procurement approval or product qualification. **Scope:** browser-based execution of controlled flight-hardware procedures, instrument automation, scientific evidence, disconnected operation, reconciliation and approval through analysis closure.

## 1. Decision summary

There are credible products in this market. The evidence does **not** justify saying that nobody has solved browser-based hardware testing or offline execution. The strongest reason to build TestForge is control over the exact evidence, recovery, approval and extension contracts required by the project. That reason must be weighed against the considerable cost of maintaining them.

The evaluation shortlist is:

1. **Epsilon3:** closest procedure-management benchmark from the initial research. Evaluate human workflow and controlled revisions first.
2. **Nominal Core + Connect:** an important addition to the initial shortlist. The vendor explicitly advertises Python-based edge testing, offline operation and later synchronization. Evaluate it before claiming our proposed architecture is a market gap. [S36–S39]
3. **NI TestStand:** automation and result-processing benchmark, particularly for an existing NI/VISA estate.
4. **OpenC3 COSMOS:** locally hosted browser command/telemetry and script-runner benchmark; inspect actual Enterprise identity and licensing boundaries.
5. **OpenTAP and OpenHTF:** leading reusable execution-engine candidates for a custom TestForge station. They are components to integrate, not established substitutes for the entire controlled-procedure system.

Yamcs is a strong adjacent command/telemetry candidate. Open MCT is a visualization component. Frappe and Loom are application/data-framework options. Sift and ION illuminate the analysis and manufacturing sides of the market. Treating all these as interchangeable “test runners” would produce a misleading comparison.

**Recommended decision:** retain a build-with-reuse architecture as a proposal; run a common demonstration against commercial candidates and open engines before committing to a production stack. No vendor has been qualified against the 96 TestForge requirements, and no TestForge runtime has been implemented in this repository.

## 2. The actual buying problem

A flight-hardware procedure is simultaneously an instruction, an authorization boundary, a record of the article's configuration, and the origin of verification evidence. A script exiting successfully does not prove the correct hardware was tested, that its calibration was valid, that an independent witness signed, or that the final analysis used the recorded raw data.

TestForge's requested operating pattern includes manual steps, measurements with limits, Python activities, VISA/USB and vendor interfaces, external calibration references, operator and QA participation, redlines during execution, additional approvers, optional observers, and distinct execution and analysis closeouts. It must continue prepared work during central service failure and recover local evidence after interruption.

That creates three overlapping purchasing decisions:

| Decision | Main object being managed | Typical shortlist |
|---|---|---|
| Procedure execution and quality | Released instruction, as-run record, signatures, deviations | Epsilon3; manufacturing systems such as ION |
| Hardware execution and acquisition | Instrument resources, commands, sequences, measurements | TestStand, OpenTAP, OpenHTF, COSMOS, Nominal Connect |
| Data interpretation and acceptance | Telemetry, derived results, annotations, review and reports | Nominal Core, Sift; mission visualization with Yamcs/Open MCT |

The market is converging: Nominal connects procedures to live data, while procedure platforms expose integration APIs. Therefore the procurement exercise must evaluate end-to-end behavior, not freeze vendors into their historical categories. [S08, S38]

## 3. Evidence method and confidence

This assessment uses vendor documentation, project repositories, published licenses, trial pages, and limited source inspection. The [source register](SOURCES.md) preserves 45 entries. References such as S03 resolve there.

- **Documented:** an official source describes the capability. This is evidence of an offered feature, not proof of reliability.
- **Inspected:** a specific file or configuration was read locally. Scope and revision are recorded.
- **Proposed:** an architectural judgment or requirement for TestForge.
- **Unverified:** a behavior was not demonstrated or the source does not establish it. This does not mean the vendor lacks it.

The public COSMOS starter was cloned and inspected, but not run because Docker was unavailable here. Its Enterprise starter requested authentication. Loom inspection used the v0.12 archive, not today's evolving GitHub main branch. No paid trials were activated, no vendor conversations were conducted, and no connected instruments were exercised. Trial lengths and packaging can change; the date above matters.

No market-share numbers, total addressable market, comparative reliability rates, or pricing estimates are asserted. Customer logos and vendor performance claims are not acceptance evidence for our installation.

## 4. Product assessments

### 4.1 Epsilon3 — procedure-first commercial benchmark

**Documented:** rich procedures, controlled revisions, review and redlines; integration interfaces; historical changelogs describe offline step input, prepared offline starts, and offline comments/attachments. The plans page describes cloud, on-premises and hybrid options for specified plans and a per-user annual model with free view-only users. A contact-form request offers a 14-day trial. [S04–S08, S30, S45]

**Assessment:** this is a high-priority benchmark for the operator/QA experience. Its workflow focus aligns with the requested balance of human procedure and automation. The earlier offline announcements are useful evidence, but do not establish all current edition, identity, artifact-size or crash-recovery semantics.

**Demonstrate:** independent operator/witness identities at a disconnected station; inserting a step without rewriting earlier signatures; rejecting stale approvals; cold-start without external identity services; reconciling conflicting edits; preserving a failed attempt after retest; and closing analysis independently from execution. Ask for evidence export including revisions, signatures, raw attachments and provenance—not just a printable run report.

**Disposition:** primary commercial workflow benchmark. Do not dismiss it solely because custom Python is needed; do not treat API availability as source ownership.

### 4.2 Nominal Core + Connect — edge execution and analysis competitor

**Documented:** Connect provides Python-oriented hardware test applications at the edge. The platform page advertises local execution/UI, disconnected use and automatic later synchronization, with Core deployment options including on-premises. Documentation distinguishes Core, Connect and SDKs. [S36, S37, S39]

A separate procedure article describes data-dependent step progression, sending hardware commands, timestamped step events with channel values, and comparing results across tests. This materially strengthens Nominal's relevance beyond visualization. [S38]

**Assessment:** the original shortlist was incomplete without Nominal. Its documented architecture overlaps directly with TestForge's local station plus central evidence proposal. It may reduce integration work between execution and analysis. An open instrument library or API does not establish that the commercial platform itself can be inspected, redistributed or independently maintained. Instro is a separate driver-library candidate requiring its own review. [S44]

**Demonstrate:** precisely which features work offline; how local identities and QA signatures work; behavior after a command is sent but its result is not committed; duplicated uploads; calibration recalls; version-bound approvals; and export sufficient to reproduce analysis outside Nominal. Ask what “deterministic timing” means, with measured bounds and platform assumptions; it is not evidence of hard real-time behavior by itself.

**Disposition:** primary commercial edge/data benchmark. It could change the build-versus-buy decision if it meets the hard gates and acceptable commercial terms.

### 4.3 NI TestStand — test executive and existing-instrument benchmark

**Documented:** sequences can call reusable code modules including Python; reporting and database logging are extensible. On-the-fly processing addresses results during execution. The Offline Results Processing Utility later converts raw results to reports/database records, including processing on another machine. [S01–S03]

The current download page advertises a seven-day Windows trial, and NI's trial page describes access to the development system's sequence development and execution functions. [S29]

**Assessment:** strong candidate when protecting existing NI investment and test code matters. Deferred results demonstrate a useful execution/storage separation. They do not by themselves establish a browser procedure editor, distributed QA signatures, redline control, or conflict-aware offline collaboration.

**Demonstrate:** use the actual Python interpreter, VISA implementation and representative device drivers; kill the controlling process around a command boundary; replay deferred results twice; reconstruct raw data and revision provenance; and show the intended browser operator experience. Obtain separate pricing for development, deployment/debugging and necessary modules rather than treating one trial as the production entitlement.

**Disposition:** benchmark or possible backend adapter. Buying the executive does not eliminate the surrounding evidence and approval design work.

### 4.4 OpenTAP and PathWave — .NET execution core with a separate tooling ecosystem

**Documented:** OpenTAP's source repository contains the core sequencer, CLI, package machinery and basic steps; the core uses MPL 2.0. Plans, instruments/resources, verdicts and result listeners form the automation model. Official documentation describes Python integration and database/result-listener options. [S09–S11]

Core downloads and SDKs are available. Keysight's PathWave tools are a separate product layer; OpenTAP announced a no-cost community license for PathWave in the 9.29 release, while Runner documentation contains its own licensing and registration context. Do not assume every editor, driver, runner or plugin inherits the core license. [S12, S31, S42, S43]

**Assessment:** the best initial fit for a C# station host, subject to the common interruption experiment. Its extension interfaces could reduce custom sequencing and driver infrastructure. TestForge would still need run-bound signatures, local durable evidence, change control, synchronization, identity and final acceptance.

**Demonstrate:** invoke a pinned test plan from the station service; feed structured measurements into our evidence protocol; crash a Python worker; cancel an unresponsive vendor call; and retain original failed attempts. Examine whether resource lifetime or retry behavior can accidentally repeat a physical action.

**Disposition:** leading reusable engine candidate. Prefer a narrow adapter so replacing the engine does not replace the evidence model.

### 4.5 OpenHTF — Python execution-library candidate

**Documented:** OpenHTF is an Apache-2.0 Python hardware-testing library. Its abstractions include test phases, measurements, plugs for dependencies/instruments, and attachments; the repository includes examples. The repository explicitly states it is not an official Google product. [S13]

**Assessment:** attractive when test engineers own Python and want lightweight, inspectable execution logic. It should be evaluated as a library around which TestForge supplies controlled procedures and station operations. A developer example is not an out-of-box substitute for the requested multi-approver workflow.

**Demonstrate:** distinguish phase failure, skipped execution, aborted execution and lost outcome; route data through a durable station contract; supervise hung plugs; support manual witness gates; and recover without restarting the entire procedure or silently overwriting attempts.

**Disposition:** comparison candidate against OpenTAP using identical scenarios. Do not choose solely by language convenience; measure integration complexity, evidence preservation and failure semantics.

### 4.6 OpenC3 COSMOS — browser command/telemetry and script execution

**Documented:** browser Script Runner supports operational scripting and execution controls, and the scripting API covers Python/Ruby command and telemetry integration. The demo includes simulated targets and runner examples. [S14, S15, S34]

**Inspected:** `cosmos-project` commit `cd01c9bb8848f7811b46580e1074fef9ab976162` is a deployment starter that pulls containers, not the full application source. It selected image tag `7.4.1`, enabled the demo, bound web ports to loopback, and configured multiple services including Redis, bucket storage, a time-series database, APIs, an operator service and a proxy. Enterprise cloning requested authentication. No containers were launched. [S33; inspection notes](COSMOS_INSPECTION.md)

The install guide describes offline container transport and Python dependency caching. This supports disconnected deployment but does not establish cross-station synchronization of signed procedures. Its resource guidance calls for at least 8 GB allocated to Docker, with 16 GB recommended. [S32]

**Licensing boundary:** the documented default Builder license includes restrictions on providing hosted services and commercial distribution of modifications. The license page places user accounts and role-based access in Enterprise and separately describes evaluation-only plugins. This is source-visible software with component-specific restrictions, not an unrestricted permissive foundation. [S16]

**Assessment:** a valuable hands-on reference, especially for telemetry-rich operations. The free demo cannot establish independent authenticated QA/operator sign-off if the relevant identity features belong to a different edition. Full-stack operational burden also matters for a small portable station.

**Demonstrate:** Enterprise identity and approval semantics, local restart, disconnected authorization, raw-data export, command-outcome recovery, and integration with a separate procedure record. Inspect source before asserting implementation details beyond the starter configuration.

**Disposition:** evaluate as a complete operational tool or instrument/telemetry subsystem. Do not adopt as TestForge's core solely because the demo is visually complete.

### 4.7 Yamcs and Open MCT — adjacent mission-operation components

Yamcs documents activities for command stacks and scripts, and its quickstart runs a spacecraft simulation. It is relevant when command history, telemetry and mission-style operations dominate. Open MCT is a mission-data visualization framework; AMMOS provides useful integration context. [S17–S19, S35]

**Assessment:** potentially valuable integration targets. Neither the reviewed activity description nor a visualization demo establishes the complete procedure-release, witness, redline and separate-analysis workflow. Conversely, rebuilding their telemetry capabilities inside a new procedure tool could be unnecessary scope expansion.

**Demonstrate:** correlate external command/telemetry evidence to run/step/attempt IDs and immutable artifact manifests. Determine which system owns command authorization, which owns raw evidence, and how a lost connection affects each. Avoid two independent components both believing they may command the same article.

**Disposition:** conditional shortlist for telemetry-heavy projects; optional adapters otherwise.

### 4.8 Frappe and Loom — frameworks, not competing test products

Frappe documents configurable document workflows, database APIs, and background jobs including after-commit scheduling. These are useful central application primitives. They do not establish an offline station or transactional hardware execution. [S20–S22]

**Assessment:** evaluate Frappe for authoring, asset/reference administration, work queues, review and reporting. Keep the station protocol independent. A queued job must not become an implicit instruction to retry a hazardous command.

Loom v0.12 was inspected locally. It provides C# typed metadata/repositories, SQLite transactions with audit writes, optimistic versions, migrations and binary/URI facilities. That snapshot also has prototype authorization, a narrow document lifecycle and planned rather than completed broader workflow/synchronization facilities. Its bounded inline blob/list behavior is unsuitable as an assumed unrestricted waveform archive. These are historical snapshot findings, not claims about today's Loom repository. [S26; inspection notes](LOOM_V0.12_INSPECTION.md)

**Disposition:** reuse selected models/adapters when justified. Do not make TestForge wait for a general-purpose framework to become a qualified station runtime.

### 4.9 Sift and First Resonance ION — adjacent alternatives worth tracking

Sift describes telemetry consolidation, rule-based anomaly evaluation, collaborative investigation and reporting, and offers a vendor demo. [S40] It is relevant to the analysis side of the requirement. The reviewed page does not establish disconnected controlled procedure execution or per-step QA signatures; those remain questions rather than negative findings.

ION describes digital work instructions, revision control, live redlines, as-built traceability, visual review/task workflows and APIs. [S41] It is relevant when the procedure is part of a manufacturing traveler and material genealogy. The reviewed page does not establish a Python/VISA station, offline witness authorization or command recovery.

**Assessment:** these products help define integration boundaries. TestForge may need to exchange evidence with an analysis platform or manufacturing record rather than replace it. Evaluate them more deeply only if those ownership boundaries are part of the deployment scope.

## 5. Comparison by responsibility

This is a qualitative fit assessment, not a scored benchmark. “Unverified” means that our research has not established the required behavior.

| Candidate | Best-supported responsibility | Local/offline evidence found | Critical unverified boundary | Evaluation priority |
|---|---|---|---|---|
| Epsilon3 | Controlled human procedures | Historical offline inputs, starts, attachments | Complete cold-start, identities, crash durability and reconciliation | High |
| Nominal | Python edge testing plus data/analysis | Vendor explicitly advertises offline execution and automatic sync | Exact approval, conflict and crash semantics | High |
| TestStand | Sequences and result processing | Raw-result processing can be deferred | Full web procedure and distributed review workflow | High as benchmark |
| OpenTAP | Extensible .NET sequencing | Installable local core | Durable signed run and recovery layer to build | High for reuse |
| OpenHTF | Python hardware-test phases | Installable Python library | Durable signed run and recovery layer to build | High for reuse |
| COSMOS | Browser scripts and telemetry | Container-based local/offline deployment | Signed multi-station reconciliation and Enterprise workflow fit | High for demo |
| Yamcs | Mission commands and telemetry | Local quickstart available | Procedure/QA lifecycle integration | Conditional |
| Open MCT | Data visualization | Framework source available | Not evaluated as execution authority | Optional integration |
| Frappe | Central application workflows | Self-hosted framework, not proof of edge sync | Offline station contract and approval specialization | Conditional framework |
| Loom v0.12 | Typed data and storage primitives | SQLite snapshot inspected | Identity, workflow, replication and storage qualification | Selective reuse |
| Sift | Telemetry review and reporting | Offline execution not established here | Operator procedure and witness semantics | Adjacent |
| ION | Manufacturing execution and genealogy | Offline testing not established here | Direct station automation and disconnected approvals | Adjacent |

## 6. Offline is five separate capabilities

1. **Offline installation:** all executables, images, drivers, packages and browser assets can be provisioned without an external download.
2. **Offline startup:** a rebooted station can authenticate authorized people and load the approved procedure without central identity, DNS, licensing or time services.
3. **Offline execution:** actions, signatures and evidence commit locally while the central database is absent.
4. **Interrupted-operation recovery:** a restarted process truthfully distinguishes completed work from a physical action whose outcome is unknown.
5. **Reconciliation:** later transfer is resumable, deduplicated, complete and conflict-aware, including attachments, revocations and calibration changes.

Products may demonstrate one level while marketing the general word “offline.” TestStand deferred results, COSMOS offline deployment, Epsilon3 offline features and Nominal edge synchronization are different evidence points. None should be silently promoted into proof of all five levels. [S03, S05–S07, S32, S36]

The proposed TestForge contract is local-first even while online: acknowledge an input only after durable local commit, and replicate afterward. Otherwise network failure changes the semantics of the same button. Browser-managed storage can be quota-limited or evicted; a local service and database make durability explicit, but actual power-loss behavior still depends on filesystem, storage and flush configuration. [S23, S25]

Authorization has an unavoidable disconnected limitation: a station cannot immediately know about a central revocation or new calibration recall. Prepared authority must therefore be bounded by time, run and scope, and reconnect must trigger review of newly discovered conflicts. This is an engineering tradeoff to approve, not something a synchronization algorithm can eliminate.

## 7. Procurement and licensing questions

Compare total lifecycle cost, not just engine license cost. Request a quote for a concrete deployment: number of stations, authors, operators, QA witnesses, mandatory approvers, read-only observers, simultaneous users, offline sites and retention volume. Separate trial access from production rights.

The cost model should include:

- Authoring, runtime, debug and server entitlements; optional plugins and identity features.
- On-premises/air-gapped packaging, upgrades and supported offline duration.
- Instrument drivers, calibration adapters and retained legacy sequences.
- Storage, ingestion, large artifacts, exports, backups and disaster recovery.
- Migration of approved procedures and validation of imported logic.
- Qualification evidence, release acceptance, security maintenance and operator training.
- Data extraction at contract termination, schema documentation and independent analysis reproduction.
- Internal ownership of custom extensions and ability to maintain them when a supplier changes direction.

No comparable written quotes were obtained, so a numeric price ranking would be speculation. A no-cost core can still require substantial development and operational support. A commercial product can be economical if it removes durable engineering obligations; that must be demonstrated against our actual gaps.

For source freedom, inventory the selected engine, UI, plugin packages, instrument drivers, container images and commercial extensions independently. OpenTAP's core license is not a blanket license for PathWave; an open Nominal driver library is not the Core/Connect platform; COSMOS has an explicit edition and license boundary. These distinctions are decision inputs, not a substitute for reviewing the actual selected terms.

## 8. Build, buy or integrate

### Buy a commercial platform

Most attractive if Epsilon3 or Nominal passes the hard gates, provides acceptable exports and offline deployment, and can support the project's lifecycle. Main advantage: less custom workflow/UI/infrastructure to own. Main risk: critical semantics or deployment options may be inaccessible or costly to change. Require a witnessed failure demonstration and export exercise before purchase.

### Integrate a test executive with a procedure platform

Potentially preserves existing TestStand, COSMOS or OpenTAP investment while adding controlled procedures. Main advantage: reuse specialized functionality. Main risk: split ownership of pass/fail, signatures, retry policy and evidence. Define which component may command hardware and which record is authoritative before writing adapters.

### Build TestForge around an open execution library

Most attractive when source inspection and custom operating semantics are non-negotiable. Main advantage: ownership of evidence/recovery contracts and integration boundaries. Main risk: the team owns installation, migrations, identity, data integrity, human factors, support and qualification indefinitely. Writing a step runner is only a small fraction of that work.

**Proposed architecture:** browser UI served by a local station service; isolated Python activities and versioned instrument adapters; a durable event journal and artifact store; transactional upload obligations; central ingest, review and analysis. OpenTAP/OpenHTF can implement execution behind that contract. Frappe or selected Loom components can serve central application needs without being embedded in the hardware recovery boundary. See [architecture](../architecture/ARCHITECTURE.md).

## 9. What TestForge must prove to justify itself

The defensible opportunity is an inspectable, reproducible record from authorized instruction through physical observation to reviewed acceptance. Browser execution and offline synchronization alone are not sufficient differentiation, because existing products already document them.

Potential differentiators, all still proposals:

- Explicit handling of unknown command outcomes instead of automatic repetition.
- One hardware authority per run, including offline handoff and stale-station fencing.
- Signatures tied to exact revisions and evidence, with independent QA identity.
- Run-specific redlines that preserve the released master and prior observations.
- Complete reconciliation receipts that account for raw files, not only metadata.
- Calibration snapshots plus later recall impact across measurements and analyses.
- Portable machine-readable evidence and reproducible analysis without a live vendor service.
- A published fault-injection suite that makes the above behavior observable.

These features may exist in competitors. The market research has not established their absence. TestForge's opportunity is to make their implementation and assurance explicit and maintainable for our intended use.

## 10. Common evaluation scenario and hard gates

Use a simulated supply and DMM before any real equipment. Prepare an immutable procedure, instrument identity map, calibration snapshot and Python package. Execute one manual setup step, acquire independent QA permission, set a bounded output, record a measurement, insert an approved diagnostic step, retain a failed result and retest it.

Disconnect the network. Reboot once before starting another prepared run. Interrupt the worker immediately after command dispatch and before outcome commit. Require observation or explicit disposition rather than blind resend. Complete local execution, reconnect, lose an upload acknowledgment, resend, and upload a large artifact in interrupted chunks. Revoke one authority or recall a calibration centrally during the partition. Finish the analysis, obtain independent approvals and attempt closure with one deliberately missing item.

Hard gates before comparative scoring:

| Gate | Required evidence |
|---|---|
| Disconnected operation | Cold-start and approved work without central services |
| Local durability | No acknowledged evidence lost under the specified interruption model |
| Command ambiguity | Unknown outcomes remain visible; no uncontrolled retry |
| Independent identity | One person with two roles cannot satisfy a two-person witness requirement |
| Revision integrity | Redlines/corrections preserve history and invalidate affected approvals |
| Reconciliation | Duplicate transfer is safe; conflicts and missing files block final closure |
| Portability | Reconstruct the run and analysis from exported evidence |
| Maintainability | Supported install/upgrade/restore path and clear component rights |

After gates, score operator effort, integration effort, instrument coverage, source control, administration and total lifecycle cost. Agree weights before demonstrations. Do not produce a precise-looking score from unequal marketing evidence.

## 11. What would change the recommendation

A commercial platform passing the hard gates with acceptable source-access/extension arrangements and portable exports would weaken the case for a full custom application. An existing executive demonstrating strong isolation and recovery behind our protocol would strengthen selective reuse. A dependency requiring online licensing at a disconnected station would be a blocking finding for that deployment profile.

The first prototype should answer three questions: can acknowledged evidence survive interruption; can physical ambiguity remain explicit without repeating a command; and can incomplete/duplicated uploads reconcile correctly? Only after these should authoring polish and broader driver coverage dominate the schedule.

## 12. Research limits and next evidence

This is a deep assessment of a defined shortlist, not an exhaustive census of all ATE, MES, LIMS, requirements-management, HIL or workflow products. Vendor release cadences and maintenance quality were not quantitatively audited. NI VeriStand, other commercial test executives and additional Python lab frameworks may deserve a second pass if hard real-time/HIL, production throughput or laboratory scheduling become primary requirements.

Next evidence: demonstrations of Epsilon3 and Nominal; COSMOS Enterprise access if its identity layer is to be evaluated; identical OpenTAP/OpenHTF adapter prototypes; a representative Windows VISA/USB inventory; project QA acceptance of offline authority; measured data volumes; scoped quotes; and a refresh of Loom against a pinned current commit before implementation reuse.

The [evaluation plan](EVALUATION_PLAN.md) and [backlog](../BACKLOG.md) turn these unknowns into concrete work. The historical baseline remains archived so changes in conclusions are visible.

## Epsilon3 focused follow-up — 14 October 2026

The [deep dive](EPSILON3_DEEP_DIVE.md) examines the 2.0 announcement, recent and historical changelogs, and API semantics. It adds 26 proposed requirements covering qualifications, granular signatures, constrained holds, cross-run changes, default-value provenance, offline capability declarations and integration integrity. The [18-case evaluation script](EPSILON3_EVALUATION.md) separates documented feature claims from behavior that still needs demonstration. This supplements the broader market assessment; it does not establish a completed vendor evaluation.
