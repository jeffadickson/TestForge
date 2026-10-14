# Original research and requirements baseline v0.1

Historical baseline, 14 October 2026. This readable transcription preserves the original content. The expanded [market research](../research/MARKET_RESEARCH.md) supersedes its shortlist; in particular, it adds Nominal. Proposed requirements and numerical targets are not demonstrated product capabilities. Source IDs resolve in [SOURCES.md](../research/SOURCES.md).

## Flight Hardware Test Framework

Research and requirements baseline

Version 0.1  •  14 October 2026  •  Prepared for Jeff Dickson

### Recommended direction

Build a controlled procedure and evidence system around a durable local station runtime. Use a web browser for authoring, execution, witnessing, review and analysis. The station must execute approved work and preserve its record without a connection to the central database, identity service or Internet. Synchronization and reconciliation are explicit workflow activities.

Evaluate OpenTAP and OpenHTF as replaceable execution adapters before committing to a new sequencer. Use Epsilon3 as the strongest procedure-management benchmark. Keep the authoritative execution journal independent of a general application framework, including Loom or Frappe.

### Scope and status

This baseline specifies human and automated flight-hardware testing from procedure preparation through execution, reconciliation, analysis and archival closure. It covers manual steps, Python, VISA and USB instruments, calibration evidence, redlines, separate QA and operator signatures, multiple approvers, read-only observers and long-running offline work.

The requirements below are proposed system requirements, not claims of an implemented or flight-qualified system. Numerical targets are initial engineering acceptance targets to be ratified against representative test campaigns. Product findings are documentation-based; no vendor product was bench-qualified for this study. Institutional test, safety, quality and records policies govern the eventual deployment.

### Principal design decisions

Persist locally before acknowledging a step, signature or result. Replicate centrally afterward, even when the network is healthy.

Separate execution state, measurement verdict, synchronization state and review disposition. A passed measurement does not mean an accepted test record.

Give one station authority over each active run and its hardware. Disconnected copies cannot independently command the same article.

Never automatically replay an ambiguous hardware operation after a crash. Recover evidence, establish hardware state and obtain an explicit disposition.

Bind signatures to exact versions and evidence. Preserve corrections and retests as new records rather than overwriting history.

### Document map

Product research and framework assessment; station architecture and synchronization; lifecycle and data contracts; 96 requirements with acceptance criteria; verification scenarios; staged delivery and unresolved decisions; source register.

## Research findings and product fit

The market separates instrument-oriented test executives from human procedure and quality systems. Combining those capabilities is feasible, but an execution engine does not establish the complete approval and evidence model. “Not established” below means the reviewed documentation does not prove the requested behavior; it is not a claim that the product cannot provide it.

| Candidate | Documented capability | Fit for this framework |
| --- | --- | --- |
| NI TestStand | Sequences, Python and other code adapters, result processing and database reporting. [S01–S03] | Instrument automation benchmark; controlled web procedures and approval reconciliation need separate evaluation. |
| Epsilon3 | Controlled procedures, redlines, approvals, APIs and offline procedure features. [S04–S08] | Closest functional benchmark for the human workflow; proprietary platform. |
| OpenTAP | Extensible .NET engine, Python integration, resource and result plugins. [S09–S12] | Leading C# execution candidate; quality workflow remains application work. |
| OpenHTF | Python phases, measurements, hardware plugs and attachments. Apache 2.0. [S13] | Leading Python execution candidate; add durable procedure and approval layer. |
| OpenC3 COSMOS | Browser Script Runner, Python/Ruby, suites, telemetry and script lifecycle. [S14–S16] | Strong spacecraft command and telemetry candidate; evaluate license and edition boundaries. |
| Yamcs and Open MCT | Command, stack and script activities; telemetry and mission visualization. [S17–S19] | Integration targets when spacecraft command and telemetry dominate; not a proven complete QA procedure system. |

### How to interpret the evidence

Documentation establishes that the relevant building blocks exist. It does not establish power-loss durability, offline identity guarantees, safe recovery of irreversible actions, or approval behavior after conflicting edits. Require witnessed fault-injection demonstrations and record the exact product edition, version and plugin set.

The absence of an Internet dependency must be tested from a cold restart. A page left open before disconnecting is insufficient evidence of a deployable offline system.

## Commercial systems and procedure management

### NI TestStand

TestStand is the NI product most likely intended by “Test Runner.” It supports reusable code modules, including Python, and configurable reporting and database logging. On-the-fly result processing can write during execution. Its Offline Results Processing Utility converts raw results into reports and database tables later or on another machine. This is a relevant precedent for decoupling execution from central storage. [S01–S03]

Do not equate deferred result processing with the complete requested offline workflow. Demonstrate offline identity, operator and QA signatures, approved redlines, insertions, calibration snapshots, run ownership and post-reconnect reconciliation. Also test the exact persistence boundary: collected in memory, written to a file and durably committed are different states. A custom operator interface is not evidence of browser-native operation.

### Epsilon3

Epsilon3 is the closest documented match for controlled human procedures: released revisions, review, sign-offs, redlines and external integrations. Its published changes explicitly describe completing steps offline, starting prepared procedures offline, adding comments and attachments offline, and synchronizing afterward. It also advertises on-premise deployment. [S04–S08]

Those features substantially overlap the requested system; the rationale for building is control over behavior, source and integration, rather than a claim that no product exists. Ask for a demonstration of a fully disconnected restart, Python execution at the stand, local multi-user witnesses, expired credentials, stale calibration, conflicting redlines and a partially uploaded waveform. Older changelogs establish feature history, not present limits or crash guarantees.

### Evaluation script for both vendors

Use the same representative procedure: identify an engineering article, verify calibration, acquire an operator and independent QA sign-off, run a bounded voltage measurement, insert an approved diagnostic step, lose the network, restart the station, finish locally, reconnect, resolve a stale reference, upload a large attachment and separately approve analysis.

Demand a complete machine-readable export containing identities, timestamps, versions, revisions, attempts, original and corrected values, signatures and raw attachments. A PDF report alone is not sufficient portability. Request edition-specific licensing, disconnected activation requirements, deployment topology, data export rights and a documented recovery procedure; pricing was not established by this review.

## Open execution and spacecraft platforms

### OpenTAP

The core is .NET-based under MPL 2.0. Its plans contain steps and resources; result listeners separate acquisition from reporting. Official documentation describes SQLite and PostgreSQL listeners and a Python plugin. This is a strong match for a C# host with Python test code. [S09–S11]

The Runner documentation exposes programmatic sessions and run events, but also references registration and licensing. Do not assume every editor, driver, runner or cloud component shares the core license. Prefer a small owned adapter to the core until dependencies and deployment rights are enumerated. A result listener is useful integration plumbing; the station must still prove commit-before-acknowledgment and recovery behavior. [S12]

### OpenHTF

OpenHTF is a Python library with phase functions, measurement validation, instrument plugs and binary attachments. Its Apache 2.0 repository provides inspectable code and examples. It is attractive when test engineers want conventional Python. Its run verdict and teardown machinery are useful, but a persisted multi-day human workflow, independent sign-offs and offline reconciliation remain application requirements. [S13]

Evaluate one measurement sequence through OpenHTF and one through OpenTAP using the same event contract. Judge cancellation, hangs, hardware resource exclusion, result streaming and dependency packaging. Do not select solely from syntax or an attractive editor.

### OpenC3 COSMOS

COSMOS provides a browser Script Runner, Python/Ruby scripting, suites and script lifecycle controls. Its line stepping and command/telemetry integration make it relevant for spacecraft integration and test. Human-facing execution controls need policy constraints in a controlled flight test. [S14–S15]

Current license documentation describes a Builder License with hosted-service and commercial redistribution restrictions, plus commercial and evaluation alternatives. Enterprise features include user accounts and RBAC. Treat this as source-visible software with specific restrictions, not as equivalent to OpenHTF’s Apache license or OpenTAP’s MPL core. Inspect the exact chosen release and plugins before adoption. [S16]

### Yamcs and Open MCT

Yamcs tracks command, stack and script activities. Open MCT is a mission-data visualization framework; AMMOS identifies Yamcs and Open MCT as core elements of its multi-center mission-control direction. They are relevant integrations for telemetry and commanding, rather than a substitute for the required quality record. Requirements for calibrated bench instruments and independent procedure closure remain ours to verify. [S17–S19]

## Loom and Frappe assessment

### Loom source inspection

The inspected artifact is Loom_Framework_v0.12.zip, current version 12. README, architecture and requirements documents, DocumentService.cs, Storage.cs, SqliteStore.cs, Program.cs and data-type documentation were examined. This was source inspection, not a new execution or security qualification. [S26]

Useful existing pieces include C# metadata and typed repositories, SQLite transactions with audit writes, optimistic version checks, stable field identities, schema migration support, binary compression and external data references. SqliteStore explicitly enables WAL; the application should additionally set and verify its intended durability settings instead of relying on provider defaults.

The current host uses simulated roles and loopback restrictions, explicitly not production login. Its document lifecycle is Draft, Submitted and Cancelled. Durable jobs, a transactional outbox, generalized workflows, synchronization and production deployment are listed as open work. Queries are bounded in-process scans; the store refuses lists above 10,000 records. Combined inline binary data has an 8 MiB document limit. These are concrete reasons not to use the existing generic record store as a high-volume acquisition journal or waveform archive.

### Frappe assessment

Frappe offers a web application framework, document metadata, permissions and workflow transitions. Its database API defines transaction behavior, and background jobs use a queue with after-commit enqueue support. These capabilities suit central authoring, asset registers, assigned review work and reporting. [S20–S22]

A queued job is not automatically a recoverable hardware operation. A Frappe site on a laptop would still need its own server dependencies and a designed synchronization protocol. The reviewed docs do not establish a turnkey disconnected flight-test journal with split-brain protection. Model multiple required approvers as explicit approval records and policy checks; do not infer them from a single workflow-state label.

| Layer | Proposed starting point | Boundary |
| --- | --- | --- |
| Station runtime | .NET service and dedicated SQLite journal | May reuse selected Loom types; must own recovery, identity, resource fencing and sync. |
| Test scripts | Versioned Python workers | OpenHTF or OpenTAP adapter; instruments remain behind controlled ownership. |
| Central application | Frappe pilot or dedicated API | Own authoring and review; choose one authority for approvals and records. |
| Loom integration | Versioned application adapter | Exchange metadata and result references through an API; no direct uncontrolled database writes. |

Recommendation: keep the station contract framework-neutral. Frappe is the shorter route to a central administrative application; Loom is a plausible longer-term C# reuse path. Neither choice removes the need to engineer and verify the local execution core.

## Deployment and local authority

### Three operating modes

Connected station: the browser talks to the local station service; the station commits locally and replicates centrally. Isolated station: the same browser and service run with prepared packages and local identities. Isolated site: multiple browser clients on a local network use one site station authority while the enterprise network is unavailable. A browser on another device cannot access that station when all communication to it is lost.

### Component responsibilities

| Component | Responsibility |
| --- | --- |
| Browser application | Procedure display, inputs, live results, role actions and synchronization status; locally served assets without CDN dependencies. |
| Station authority | Validate step guards; journal events; manage signatures and authority; supervise Python workers; hold instrument ownership. |
| Local storage | Transactional event journal and outbox; content-addressed raw files; prepared packages, reference snapshots and authorization bundles. |
| Instrument gateway | Resource locks and command authorization; protocol adapters; operation IDs and reconciliation hooks. Hardware protection remains independently enforced. |
| Synchronization service | Resumable replication, hash verification, deduplication, evidence completeness and receipts; no hardware command replay. |
| Central services | Released procedures, users, assets, requirement links, review tasks, search, analysis records and retention. Derived views can be rebuilt from retained events. |

### Why the station service is necessary

The browser is the user interface, not the sole durable recorder or universal instrument driver. Browser-managed storage has quota and eviction behavior; persistent storage reduces some eviction risk but does not eliminate user deletion or device loss. Native VISA and arbitrary USB drivers belong on the station. Browser closure must not silently kill an acquisition. [S23, S24]

Use a local database transaction to commit the accepted action, corresponding event and outbox entry together. Store large artifacts separately with staged writes, verified hashes and explicit incomplete states. SQLite WAL with synchronous FULL is a candidate; durability still depends on the storage stack honoring flushes. Keep the database on a local supported filesystem and use coordinated backup rather than copying only a live database file. [S25]

### Ownership and availability

One station owns a run and its resources. Offline authority is an explicit bounded grant, not a short central lease that expires and lets a second station seize the hardware. Handoff requires release or physical isolation of the previous commander. A central outage is tolerated; loss of the local evidence store or required hardware protection is a different failure and must inhibit new work.

## Disconnected preparation and synchronization

### Before disconnecting

Prepare a signed package containing the released procedure and subprocedures, step identities, required documents, scripts and locked dependencies, driver versions, limits, configuration, calibration snapshots, approved overrides, authorized identities and roles, expiry policy and expected storage budget. Verify all files and execute a readiness check with the network disabled. A preparation receipt records exactly what is available.

### During execution

Each event carries an event ID, run ID, station identity, ownership epoch, monotonically increasing local sequence, event schema version, actor, role, local timestamp, clock-quality information, causation ID, payload digest and previous-event digest. Integrity chains make alterations detectable against retained checkpoints; they do not make an administrator-controlled machine intrinsically tamper-proof.

The station acknowledges an action only after the necessary record is durable. A worker records command intent before issuing a hardware operation and records the observed outcome afterward. If the computer fails between these records, the outcome is unknown. A database transaction cannot make a physical side effect atomic.

### On reconnecting

Authenticate the station and exchange protocol versions, ownership and last verified receipts. Do not change the active package.

Send immutable events and artifact chunks with stable IDs. The server accepts retries idempotently and flags the same ID with different content.

Verify sequence continuity, signatures, package hashes and all required artifacts. Receipt of metadata alone is not evidence completeness.

Compare cached authorization, calibration and release state with current records. Create reconciliation tasks for changes; preserve the original execution context.

Issue a durable reconciliation receipt. Retain local evidence until central completeness and backup/retention conditions are met.

Make central closure available only when reconciliation and required reviews are complete. Upload failure never initiates a new measurement.

### Conflict policy

Independent comments and attachments may merge by identity. Conflicting signed results, redlines, approvals or ownership claims must not use last-writer-wins. Preserve both branches, quarantine the disputed transition and assign a named resolver. A newly released procedure must not silently replace the version used by an offline run.

### Offline authorization tradeoff

Immediate central revocation and indefinite disconnected authorization cannot both be guaranteed. Authorize a bounded offline period and permitted actions in advance. Preserve signatures made within the local authorization context; flag subsequently discovered revocations for review. Emergency safing must remain available when normal credentials or authorization expire.

## Lifecycle and evidence model

### Independent state dimensions

| Dimension | Representative states | Meaning |
| --- | --- | --- |
| Procedure | Draft, in review, released, superseded, withdrawn | Defines what was approved to execute. |
| Execution | Prepared, ready, running, held, recovery required, completed, aborted | Describes activity and hardware-control progress. |
| Verdict | Not evaluated, pass, fail, inconclusive, invalid | Describes measurement or requirement evaluation. |
| Replication | Local only, queued, uploading, uploaded, reconciled, conflict | Describes evidence availability and consistency. |
| Review | Open, execution reviewed, analysis open, analysis approved, closed, reopened | Describes acceptance and outstanding obligations. |

Execution completion requires all executed, skipped or deferred steps to have an explicit disposition and the final hardware configuration to be recorded. Execution review can be performed locally when policy allows. Final central closure additionally requires complete reconciliation, analysis acceptance and resolution or authorized disposition of deviations. Closed records reopen through amendments; historical approvals remain visible.

### Canonical entities

Procedure and ProcedureRevision; StepDefinition with permanent identity; Requirement and VerificationLink; ExecutionPackage; TestArticle and ConfigurationSnapshot; Station and AuthorityGrant; Run and StepAttempt; CommandIntent and CommandOutcome; Measurement and ArtifactManifest; CalibrationSnapshot; IdentityGrant and Signature; Redline and Deviation; ReviewTask and AnalysisRevision; SyncReceipt and ReconciliationIssue; ClosureManifest.

A run points to one execution package. Each repeated step creates a new attempt linked to its parent step and preceding attempts. Each measurement points to an attempt, instrument identity, calibration context, units and limits revision. Each analysis points to immutable input hashes and a code/environment version. A signature points to the exact subject revision and evidence digest it approves, not merely a mutable record ID.

### API and worker contract

Expose versioned operations for preparing packages, starting runs, proposing actions, signing subjects, submitting measurements, reserving artifacts, appending events, uploading chunks and acknowledging receipts. Mutation requests carry a request ID, expected version, actor authority and run ownership. Read APIs expose pending and durable states distinctly.

Python workers receive a validated input document, package digest, attempt ID and approved resource handles. They emit structured measurements, progress, artifacts and terminal outcomes. stdout is diagnostic output, not the authoritative measurement protocol. Database adapters use outboxes and stable IDs; a remote database outage never forces an instrument operation to run again.

## Requirements conventions and allocation

The following 96 requirements form the proposed first baseline. Each states an observable obligation and its acceptance check. They are grouped by ownership and mapped to end-to-end qualification scenarios later in the document. All require implementation evidence before release; none is declared satisfied by this study.

| Priority | Interpretation |
| --- | --- |
| P0 | Required before any controlled flight-hardware pilot. Development may use simulators while these are unfinished. |
| P1 | Required for the complete operational framework; staged after the core pilot if the pilot scope explicitly excludes it. |

| Group | Allocated owner | Primary evidence |
| --- | --- | --- |
| PROC | Procedure service | Versioning, import and guard tests |
| EXEC | Station runtime | State and interruption tests |
| AUTH | Identity and approvals | Role, signature and revocation tests |
| CHG | Change control | Redline, retest and invalidation tests |
| HW | Instrument gateway | Bench and fault-injection tests |
| CAL | Asset and calibration adapters | Reference validity and recall tests |
| DATA | Evidence service | Integrity, precision and restore tests |
| OFF | Local runtime | Disconnected cold-start and restart tests |
| SYNC | Replication service | Partition, duplicate and conflict tests |
| CLOSE | Review and analysis | Closure-blocking and traceability tests |
| SEC | Platform security | Access, isolation and tampering tests |
| OPS | Operations and user interface | Load, installation and recovery demonstrations |

### Verification method

Acceptance checks are minimum evidence, not complete test procedures. Use automated unit and integration tests for guards, versions and deduplication; process and power interruption for persistence; real representative equipment for command behavior; and witnessed operator/QA demonstrations for human workflows. Preserve the software build, environment, test inputs, expected outcome, actual outcome and reviewer for every acceptance result.

## Controlled procedures

Allocation: Procedure service.

### PROC-01  Stable identity  P0

The system shall assign permanent IDs to procedures, revisions and steps, independent of displayed numbering.

Acceptance: Insert a step and verify historical signatures and result links still reference the original steps.

### PROC-02  Immutable release  P0

The system shall freeze a released revision and its dependent content; edits shall create a new revision.

Acceptance: Modify a draft and verify an existing released package and its digest remain unchanged.

### PROC-03  Structured steps  P0

The system shall support instructions, typed inputs, measurements, scripts, hold points, witnesses, attachments and subprocedures.

Acceptance: Execute a representative procedure containing every supported step type with required inputs enforced.

### PROC-04  Execution guards  P0

The system shall enforce prerequisites, allowed branches, loops and mandatory hold points in the runtime.

Acceptance: Attempt a direct API bypass of a hold point and confirm rejection and an audit event.

### PROC-05  Release validation  P0

The system shall reject missing references, invalid units, unresolved required roles and unsupported package dependencies.

Acceptance: Run invalid-package fixtures and verify release is blocked with actionable diagnostics.

### PROC-06  Configuration applicability  P0

The system shall restrict procedure use by article identity, configuration and approved applicability rules.

Acceptance: Start against a mismatched hardware revision and confirm an explicit blocking result.

### PROC-07  Import and export  P1

The system shall import structured procedures as drafts and export full content with stable identities and revision history.

Acceptance: Round-trip a procedure and identify any unsupported imported content before release.

### PROC-08  Requirement mapping  P0

The system shall link steps and analyses to versioned verification requirements and methods.

Acceptance: Change a requirement revision and verify affected released procedures and evidence are flagged for review.

## Execution and recovery

Allocation: Station runtime.

### EXEC-01  Run identity  P0

The system shall assign unique run and attempt IDs with article, station, package and personnel context.

Acceptance: Start two offline runs and verify their imported records cannot collide.

### EXEC-02  Durable transitions  P0

The system shall commit an accepted transition and its event before returning success to the browser.

Acceptance: Terminate immediately after acknowledgment and recover the same accepted state.

### EXEC-03  Explicit outcomes  P0

The system shall distinguish pass, fail, inconclusive, error, invalid, aborted, skipped and not evaluated outcomes.

Acceptance: Inject each outcome and verify it cannot become pass through missing data or an exception.

### EXEC-04  Hold and resume  P0

The system shall apply declared hold and browser-disconnect policies, and recheck prerequisites before resumption.

Acceptance: Close the browser during acquisition, then change an instrument during a hold; verify the declared response and blocked resume.

### EXEC-05  Unknown outcome  P0

The system shall enter recovery required after an interrupted operation whose hardware effect cannot be established.

Acceptance: Crash after command transmission but before result persistence; verify no automatic retransmission.

### EXEC-06  Retry classification  P0

The system shall require each operation to declare read-only, idempotent or nonrepeatable behavior with an approved retry policy.

Acceptance: Verify retries are bounded and a nonrepeatable operation cannot use generic automatic retries.

### EXEC-07  Resource ownership  P0

The system shall permit one controlling authority per run and exclusive resource set, including during disconnection.

Acceptance: Attempt a second controller and confirm hardware access is denied until a valid handoff.

### EXEC-08  Handover record  P0

The system shall record shift handover, active configuration, held operations and transfer of operator responsibility.

Acceptance: Resume after a personnel change and verify the new operator acknowledges outstanding conditions.

## Identity signatures and collaboration

Allocation: Identity and approval service.

### AUTH-01  Individual identity  P0

The system shall authenticate individual operators, witnesses and approvers without shared sign-off accounts.

Acceptance: Verify two people using one workstation retain distinct authenticated signature records.

### AUTH-02  Independent witness  P0

The system shall enforce separate operator and QA identities when a step requires independence.

Acceptance: Give one account both roles and confirm it still cannot satisfy both signatures.

### AUTH-03  Approval policies  P0

The system shall support named approvers, role slots, all-of and explicitly configured quorum rules with ordering.

Acceptance: Exercise three required approvers, rejection and optional observers without premature approval.

### AUTH-04  Signature meaning  P0

The system shall bind each signature to identity, role, meaning, timestamp, policy and exact subject/evidence digest.

Acceptance: Alter the signed content and verify the old signature cannot approve the new revision.

### AUTH-05  Reauthentication  P0

The system shall require a configured confirmation and reauthentication policy for consequential signatures.

Acceptance: Expire a signing session and verify a normal UI click cannot silently sign.

### AUTH-06  Offline authority  P0

The system shall validate locally provisioned, bounded identity and role grants for disconnected actions.

Acceptance: Cold-start offline and verify permitted signing works while an expired or out-of-scope grant fails.

### AUTH-07  Observers and comments  P0

The system shall separate viewing, commenting, executing, witnessing and approving permissions.

Acceptance: Verify a read-only collaborator neither mutates the run nor becomes a required approver.

### AUTH-08  Delegation and revocation  P0

The system shall record authorized delegation and reconcile newly discovered revocations without erasing prior signatures.

Acceptance: Revoke an offline user centrally and verify reconnect creates an attributable review issue.

## Redlines deviations and retests

Allocation: Change control service.

### CHG-01  Proposed redlines  P0

The system shall record redlines as explicit proposals with original content, proposed content, reason and affected scope.

Acceptance: Show the exact before/after change and proposer for an inserted or altered step.

### CHG-02  Approval before use  P0

The system shall block affected execution until the required redline approvals are complete.

Acceptance: Propose a changed limit while running and verify the original approved limit remains operative.

### CHG-03  Run and master scope  P0

The system shall distinguish run-only changes from proposed changes to the master procedure.

Acceptance: Approve a run insertion and verify other runs and the released master do not change.

### CHG-04  Evidence preservation  P0

The system shall retain original observations and append corrections with reason, author and time.

Acceptance: Correct a signed numeric result and verify both values and affected approvals remain traceable.

### CHG-05  Skip and defer  P0

The system shall require reason, authority and disposition for skipped, deferred or not-applicable required steps.

Acceptance: Attempt closure with an unauthorized skip and confirm it is blocked.

### CHG-06  Retest linkage  P0

The system shall create a new attempt for every retest and retain prior failed and invalid attempts.

Acceptance: Pass a retest and verify the failed attempt remains in reports and requirement disposition.

### CHG-07  Impact invalidation  P0

The system shall mark affected downstream evidence and approvals for reevaluation after consequential changes.

Acceptance: Change a calibration correction or limit and verify dependent analysis approval becomes stale.

### CHG-08  Nonconformance  P0

The system shall link deviations and nonconformances to article, run, affected steps and authorized dispositions.

Acceptance: Accept a documented waiver and verify the measured failure is preserved rather than relabeled pass.

## Python and instrument control

Allocation: Workers and instrument gateway.

### HW-01  Script provenance  P0

The system shall execute only approved script packages with pinned dependencies and recorded hashes in flight mode.

Acceptance: Change one script byte or dependency and confirm execution is refused.

### HW-02  Process isolation  P0

The system shall run scripts in supervised worker processes with bounded resources and separate credentials.

Acceptance: Hang or crash a worker and verify the UI, journal and supervision remain available.

### HW-03  Driver abstraction  P0

The system shall provide versioned adapters for VISA, serial, USB and required vendor APIs with simulated equivalents.

Acceptance: Run the same measurement contract against a simulator and representative approved equipment.

### HW-04  Instrument identity  P0

The system shall verify actual device identity and configured resource mapping before permitting commands.

Acceptance: Swap two USB devices or change an address and verify the wrong instrument is blocked.

### HW-05  Operation journal  P0

The system shall persist command intent, operation ID and observed outcome without claiming atomic hardware execution.

Acceptance: Interrupt at each dispatch boundary and verify an honest completed or unknown classification.

### HW-06  Bounded cancellation  P0

The system shall specify command timeouts, cancellation escalation and equipment-specific recovery actions.

Acceptance: Block a driver call and demonstrate the approved timeout and independent recovery behavior.

### HW-07  Safety boundary  P0

The system shall respect independent interlocks and enforce approved command envelopes and operating modes.

Acceptance: Request an out-of-envelope command and verify rejection; prove a failed process cannot defeat the hardware interlock.

### HW-08  Data protocol  P0

The system shall ingest typed worker measurements and artifacts through a validated protocol separate from diagnostic logs.

Acceptance: Send malformed units, duplicate samples and a truncated artifact; verify explicit rejection or incomplete status.

## Calibration and reference information

Allocation: Asset and reference adapters.

### CAL-01  Asset chain  P0

The system shall record instrument, channel, probe, cable, fixture and transducer identities needed for measurement traceability.

Acceptance: Reconstruct the complete measurement chain from the saved run without live asset-system access.

### CAL-02  Calibration snapshot  P0

The system shall retain certificate revision, validity interval, correction data, uncertainty and source retrieval metadata.

Acceptance: Disconnect the calibration database and reproduce the context from the prepared package.

### CAL-03  Validity checks  P0

The system shall check calibration at preparation and required use points, including expiry during a long test.

Acceptance: Cross an expiry boundary and verify the approved hold or disposition policy is enforced.

### CAL-04  Reference freshness  P0

The system shall apply configured freshness and expiry policies to each cached external reference.

Acceptance: Use a stale required reference offline and verify the action is blocked or explicitly authorized.

### CAL-05  Controlled exceptions  P0

The system shall require scoped approval for calibration or reference exceptions and record affected measurements.

Acceptance: Verify an exception for one instrument and run does not authorize another.

### CAL-06  Recall impact  P0

The system shall identify past measurements and analyses affected by a later calibration recall or out-of-tolerance finding.

Acceptance: Recall a certificate and generate the exact affected evidence set with review tasks.

### CAL-07  Measurement quality  P0

The system shall retain range, resolution, uncertainty model and approved guard-band decision rules when applicable.

Acceptance: Evaluate values near a limit and verify the approved rule and its revision are reported.

### CAL-08  External adapters  P1

The system shall provide read adapters with provenance, timeouts, schema validation and independently testable mappings.

Acceptance: Change an upstream schema and verify failure is explicit without modifying prior snapshots.

## Scientific data and evidence

Allocation: Evidence service.

### DATA-01  Measurement representation  P0

The system shall preserve raw values, units, precision, validity flags and evaluated limits without silent conversion.

Acceptance: Round-trip large integers, decimals, timestamps and invalid readings without loss or false pass.

### DATA-02  Raw and derived data  P0

The system shall retain raw acquisitions separately from reductions, corrections and analysis outputs.

Acceptance: Recompute a derived value from retained raw evidence and identify the exact algorithm revision.

### DATA-03  Large artifacts  P0

The system shall stream waveforms, images and binary files to bounded local storage with size and digest manifests.

Acceptance: Acquire a 10 GB artifact without loading it entirely into memory and detect a truncated final chunk.

### DATA-04  Timing evidence  P0

The system shall record source time, receipt time, clock source, synchronization quality and sequence order.

Acceptance: Move the wall clock backward and verify event order remains reconstructable and uncertainty is visible.

### DATA-05  Evidence integrity  P0

The system shall verify content digests and signed checkpoints when storing, synchronizing and exporting evidence.

Acceptance: Alter or remove a retained event or artifact and verify the integrity check detects it.

### DATA-06  Storage exhaustion  P0

The system shall monitor capacity and apply a validated reserve policy before new operations can exhaust evidence storage.

Acceptance: Fill the disk during acquisition and verify explicit incomplete evidence and the approved safe response.

### DATA-07  Portable record  P0

The system shall export human-readable reports and machine-readable events, schemas, manifests and raw artifacts.

Acceptance: Open an export on an isolated clean system and verify its completeness without a running server.

### DATA-08  Retention and restoration  P0

The system shall retain protected records and verify coordinated backup and restore of journals and artifact files.

Acceptance: Restore a backup and compare all committed evidence and manifest hashes with the source.

## Disconnected operation

Allocation: Local station runtime.

### OFF-01  Local web application  P0

The system shall serve all required UI assets and APIs locally without runtime Internet dependencies.

Acceptance: Start the browser and station after a reboot with every external network disconnected.

### OFF-02  Prepared package  P0

The system shall verify package completeness, signatures, dependencies, reference validity and storage before offline readiness.

Acceptance: Remove each required package element in turn and verify readiness fails.

### OFF-03  Local source of record  P0

The system shall record every acknowledged input, signature, transition and result locally before replication.

Acceptance: Disable the central database throughout a run and recover every acknowledged record locally.

### OFF-04  Crash durability  P0

The system shall recover committed events and identify incomplete operations after process or power interruption.

Acceptance: Inject interruptions across commit boundaries on the target storage and verify no acknowledged event is lost.

### OFF-05  Disconnected duration  P0

The system shall support a proposed seven-day isolated campaign within an approved authority and capacity budget.

Acceptance: Complete a seven-day soak without external authentication, licensing, package or time-service dependencies.

### OFF-06  Offline collaboration  P0

The system shall support authorized local operator and witness use through one station authority, with explicit connectivity status.

Acceptance: Use two browsers on an isolated LAN and reject conflicting execution actions.

### OFF-07  Readiness boundaries  P0

The system shall distinguish central service failure from unavailable local storage, invalid authority or missing safety prerequisites.

Acceptance: Verify central outage permits prepared work while loss of local durable storage inhibits new operations.

### OFF-08  Portable transport  P1

The system shall support encrypted, signed export/import bundles when network synchronization is unavailable.

Acceptance: Import the same removable-media bundle twice and verify deduplication and custody records.

## Synchronization and reconciliation

Allocation: Replication service.

### SYNC-01  Transactional outbox  P0

The system shall atomically store each accepted event and its replication obligation in the local transaction.

Acceptance: Crash after commit and before upload; verify the event remains queued after restart.

### SYNC-02  Idempotent ingest  P0

The system shall deduplicate retransmissions by stable identity and reject identical IDs with different content.

Acceptance: Retry a batch after losing its acknowledgment and verify exactly one central record per event.

### SYNC-03  Resumable transfer  P0

The system shall resume verified artifact chunks without marking incomplete evidence as complete.

Acceptance: Disconnect repeatedly during a 10 GB upload and verify the final digest and missing-chunk accounting.

### SYNC-04  Completeness receipt  P0

The system shall issue reconciliation receipts only after required sequences, signatures and artifacts validate.

Acceptance: Upload all metadata but omit one attachment and verify closure remains blocked.

### SYNC-05  Conflict quarantine  P0

The system shall preserve conflicting signed records and require explicit resolution instead of last-writer-wins.

Acceptance: Submit two incompatible offline branches and verify both survive with a blocked disputed transition.

### SYNC-06  Ownership fencing  P0

The system shall reject stale ownership epochs and prevent resynchronization from authorizing a second hardware commander.

Acceptance: Reconnect an old station after handoff and verify it cannot resume instrument control.

### SYNC-07  Reference reconciliation  P0

The system shall compare execution snapshots with later releases, recalls and revocations and generate review tasks.

Acceptance: Reconnect after a calibration recall and verify affected runs are flagged without history edits.

### SYNC-08  Retention acknowledgment  P0

The system shall retain local evidence until complete central receipt and configured backup/retention gates are met.

Acceptance: Lose the final receipt or fail the central backup gate and verify local cleanup is refused.

## Review analysis and closure

Allocation: Review and analysis services.

### CLOSE-01  Execution checklist  P0

The system shall require step dispositions, required signatures, evidence completeness and final article configuration for execution review.

Acceptance: Leave each item unresolved in turn and verify the review gate explains the blocker.

### CLOSE-02  Separate analysis  P0

The system shall track analysis tasks, owners, inputs and approvals independently from execution completion.

Acceptance: Complete a run with analysis pending and verify it is not labeled fully closed.

### CLOSE-03  Reproducible analysis  P0

The system shall record analysis code, dependencies, parameters, input hashes and output revisions.

Acceptance: Re-run the approved analysis on retained inputs and compare outputs under stated tolerances.

### CLOSE-04  Approval invalidation  P0

The system shall invalidate applicability of analysis approval when its inputs, code or acceptance rules change.

Acceptance: Revise a reduction script and verify a new analysis approval is required.

### CLOSE-05  Closure gate  P0

The system shall permit final closure only after reconciliation, required approvals and authorized deviation dispositions.

Acceptance: Attempt closure with one missing approver, unresolved conflict or incomplete upload and confirm denial.

### CLOSE-06  Requirement disposition  P0

The system shall report verified, failed, waived, invalid and not-yet-verified requirements with evidence links.

Acceptance: Verify a waived failure remains distinct from a measured pass in the verification matrix.

### CLOSE-07  Amendment lifecycle  P0

The system shall reopen closed records through controlled amendments while preserving the prior closure manifest.

Acceptance: Correct an archived analysis and reconstruct both the original and amended acceptance states.

### CLOSE-08  Work queues  P1

The system shall provide ownership, due dates, escalation and observer access for execution and analysis action items.

Acceptance: Assign overdue tasks and verify notifications do not silently approve or close them.

## Security and software assurance

Allocation: Platform and assurance.

### SEC-01  Enforced access  P0

The system shall enforce role, project and article scope at the API and data-access layers.

Acceptance: Attempt cross-project reads and unauthorized mutations directly through APIs and verify denial.

### SEC-02  Local attack surface  P0

The system shall authenticate local clients and protect against cross-origin requests, host spoofing and unauthorized LAN access.

Acceptance: Attempt browser-based requests from an untrusted origin and verify commands cannot be issued.

### SEC-03  Protected secrets  P0

The system shall encrypt sensitive records at rest and in transit, and protect keys and credentials with approved storage and rotation.

Acceptance: Rotate keys without losing historical evidence; verify encrypted storage and transport and absence of secrets in exports.

### SEC-04  Approved software  P0

The system shall verify signed software packages and prohibit unapproved upgrades during active runs.

Acceptance: Offer a new release during a run and verify it cannot change the pinned execution environment.

### SEC-05  Privileged activity  P0

The system shall record administrator actions and restrict modification or deletion of authoritative evidence.

Acceptance: Attempt an administrative edit and verify prevention or a detectable controlled amendment.

### SEC-06  Worker containment  P0

The system shall apply least-privilege filesystem, network and device access to test workers.

Acceptance: Use a test worker to attempt unauthorized file, network and device access and verify rejection.

### SEC-07  Assurance record  P0

The system shall maintain requirements-to-test traceability, dependency inventory, known limitations and reviewed release evidence.

Acceptance: Audit a candidate release and resolve every P0 requirement to recorded acceptance evidence.

### SEC-08  Environment separation  P0

The system shall distinguish simulation, development, engineering and flight operation in access rules and stored records.

Acceptance: Attempt to present simulated measurements as flight evidence and verify the provenance is unmistakable.

## Operations usability and performance

Allocation: Platform operations and user interface.

### OPS-01  Operational display  P0

The system shall show article identity, revision, active step, ownership, hardware status, local persistence and sync backlog.

Acceptance: An operator identifies the authoritative run and unsynchronized evidence without navigating away.

### OPS-02  Clear actions  P0

The system shall distinguish hold, resume, abort, skip, repeat and emergency safing with appropriate role and confirmation rules.

Acceptance: Run a witnessed usability exercise and verify no ambiguous button initiates a repeat or closes a failed step.

### OPS-03  Accessible interaction  P1

The system shall support keyboard operation, readable contrast, non-color status cues and documented supported browsers.

Acceptance: Complete a procedure without a mouse and verify errors remain identifiable without color.

### OPS-04  Reference load  P0

The system shall meet proposed targets of 10,000 steps per procedure and 100 structured events per second per station.

Acceptance: Run the reference load with a proposed p95 local action acknowledgment below 500 ms, excluding instrument latency.

### OPS-05  Startup and recovery  P0

The system shall restore the UI and a truthful recovered run state within a proposed 60 seconds on approved hardware.

Acceptance: Restart a loaded station; verify readiness timing without automatically resuming hardware actions.

### OPS-06  Observability  P0

The system shall expose correlated health, logs and metrics without treating diagnostic telemetry as the evidence record.

Acceptance: Disable telemetry export and verify execution evidence remains complete and locally inspectable.

### OPS-07  Install and upgrade  P0

The system shall support reproducible offline installation, controlled schema migration and rollback or forward-recovery procedures.

Acceptance: Install on a clean isolated host and rehearse a failed upgrade without losing historical records.

### OPS-08  Capacity and support  P0

The system shall document storage sizing, backups, restore, instrument compatibility and incident recovery for operators.

Acceptance: A second engineer follows the runbook to restore a station and identify an unresolved command outcome.

## Fault handling and acceptance campaigns

The following campaigns exercise the requirements together. These are proposed tests, not results. Start with simulated hardware and then repeat equipment-specific cases on approved engineering hardware. Capture station build, package hash, fault timing and observed physical state.

| Case | Stimulus and required result | Coverage |
| --- | --- | --- |
| V01 | Cold-start without WAN, DNS or central identity. Prepared work and local sign-offs function; invalid grants are blocked. | OFF, AUTH, PROC |
| V02 | Fail the central database for a full run. All acknowledged steps persist locally; no hardware retries arise from upload failure. | OFF, SYNC, EXEC |
| V03 | Kill a worker before dispatch, after dispatch and before outcome commit. Unknown physical effects require reconciliation. | EXEC, HW, DATA |
| V04 | Cut station power at persistence boundaries. No acknowledged event disappears; unfinished artifacts remain incomplete. | OFF, DATA |
| V05 | Lose an upload acknowledgment and resend. One central event is retained; differing payload under the same ID is rejected. | SYNC |
| V06 | Create divergent offline ownership or edits. Both records survive; no second controller or automatic merge is accepted. | EXEC, SYNC, CHG |
| V07 | Expire a calibration during a soak and later recall its certificate. Enforce the local policy and identify affected history. | CAL, CLOSE |
| V08 | Revoke an offline approver centrally. Reconnect creates a review task and preserves the original signing context. | AUTH, SYNC |
| V09 | Fill the disk and corrupt an artifact. New operations are inhibited as specified; evidence cannot be silently completed. | DATA, OFF |
| V10 | Hang a VISA or USB call. Demonstrate timeout, worker containment and equipment-specific independent safing. | HW, EXEC |
| V11 | Redline a limit, insert a step and retest a failure. Preserve original evidence and require dependent reapproval. | PROC, CHG, CLOSE |
| V12 | Finish testing with missing analysis or attachment. Execution can end; final closure remains blocked. | CLOSE, SYNC |

## Qualification scope and delivery sequence

### Additional acceptance campaigns

V13 exercises three mandatory approvers, one read-only observer, a rejected approval and a prohibited self-witness. V14 moves the station clock backward and restores a backup; event order and uncertainty must remain explicit. V15 runs the seven-day offline soak and the load targets while uploading large artifacts. V16 exports a closed record and reproduces its analysis on a clean isolated machine. V17 tests API bypass, cross-origin attacks, tampered packages and worker privilege boundaries. V18 rehearses failed installation, migration and rollback. Together with V01–V12, these cover all requirement groups.

### Delivery gates

| Gate | Scope | Exit evidence |
| --- | --- | --- |
| A  Architecture spike | One browser, local journal, simulated Python measurement and a server ingest endpoint. | Prove V02, V03 and V05 before expanding UI features. |
| B  Controlled procedure prototype | Versioned packages, manual steps, operator/QA identities, redlines and local recovery. | Demonstrate full offline execution and approval invalidation using simulated hardware. |
| C  Engineering bench pilot | Representative VISA/USB devices, calibration adapter, bounded cancellation, raw data and analysis. | Pass relevant equipment fault tests and document safe operating envelopes. |
| D  Controlled flight pilot | Qualified installation and support, all P0 evidence, reviewed security and project procedures. | Independent project acceptance; no unresolved P0 items within pilot scope. |
| E  Operational expansion | Additional sites, importers, removable-media exchange, richer work queues and reporting. | Complete P1 acceptance and validate additional deployment profiles. |

### Prototype that will resolve the largest risks

Use an engineering power-supply and DMM procedure: identify the article; verify instrument identities and calibration; acquire operator and QA permission; command a bounded setpoint; collect readings; approve a diagnostic insertion; disconnect the network; interrupt after dispatch; reconcile actual hardware state; complete locally; synchronize a waveform; generate analysis; obtain independent analysis approval; close the record.

The critical success is correct behavior through interruption and review. A long list of instrument drivers or a sophisticated editor does not compensate for ambiguous command recovery, missing evidence or invalid signatures. Choose OpenTAP versus OpenHTF after both implement this same scenario behind the same station contract.

## Open decisions and engineering risks

| Decision | Proposed default | Resolution evidence |
| --- | --- | --- |
| Station platform | Windows first for the actual instrument estate; define Linux support separately. | Inventory VISA stacks, USB drivers and installation rights. |
| Offline window | Seven days as an initial target, bounded per project. | Longest expected campaign and acceptable revocation/calibration staleness. |
| Identity offline | Provisioned individual identities and signed bounded grants. | Institutional identity and QA acceptance of offline signatures. |
| Run ownership | One local authority per run, with explicit handoff. | Procedure for failed-station isolation and controller replacement. |
| Central framework | Frappe evaluation, with an independent station protocol. | Representative approval, record retention and integration prototype. |
| Loom reuse | Typed metadata and adapters where useful; dedicated event/blob storage. | Authentication, workflow and storage qualification before expanding responsibility. |
| Data rates | 100 events/s and 10 GB artifact as initial acceptance workload. | Actual waveform rates, retention, channel count and storage sizing. |
| Safety and stop policy | Equipment-specific; independent hardware protection. | Hazard analysis and tested response for loss of process, power or communication. |
| Final closure | Central reconciliation required; local execution review allowed by policy. | QA rules for remote-site provisional acceptance and later closure. |
| Record retention | No deletion of unsynchronized evidence; institutional retention thereafter. | Records schedule, backup destination and recovery objectives. |

### Failure modes that deserve early design review

A command may have executed despite a timeout. An instrument can retain an output after the controlling process dies. A generic “power off” cleanup may itself be unsafe. A late approval can refer to an obsolete revision. A cached certificate can become invalid while offline. A browser can show a value that never reached durable storage. A centrally accepted event may still lack its raw artifact. A database administrator can rewrite an unauthenticated audit trail. Each has an explicit requirement and acceptance campaign above.

### Framework boundary

A generic durable workflow engine may coordinate long-lived human review, but cannot supply physical exactly-once execution. Temporal documents activity retry and idempotency concepts; apply that distinction to any engine selected. Test execution must own the ambiguity between persisted command intent and observable physical effect. [S27]

NASA verification guidance supports a plan-to-evidence-to-disposition lifecycle and traceability to requirements. It informs this structure; applicability of any NASA or institutional requirement must be assigned by the project rather than inferred from product selection. [S28]

## Source register

Reviewed 14 October 2026. Vendor and project documentation are primary sources. Historical changelogs establish specific feature precedents; product editions and operational guarantees require demonstration. Architecture, requirements, numerical targets and build recommendations are engineering proposals from this study.

### S01  NI TestStand overview

Read source at www.ni.com

Product scope and supported code reuse.

### S02  NI on-the-fly reporting and logging

Read source at knowledge.ni.com

Incremental result processing behavior.

### S03  NI Offline Results Processing Utility

Read source at www.ni.com

Deferred reports and database processing; not a full offline approval guarantee.

### S04  Epsilon3 procedures and work instructions

Read source at www.epsilon3.io

Controlled revisions, review and redlines.

### S05  Epsilon3 offline step execution

Read source at www.epsilon3.io

Historical evidence for offline step inputs and synchronization.

### S06  Epsilon3 offline procedure start

Read source at www.epsilon3.io

Historical evidence for prepared offline starts.

### S07  Epsilon3 offline attachments

Read source at www.epsilon3.io

Historical evidence for offline comments and attachments.

### S08  Epsilon3 integrations and deployment

Read source at www.epsilon3.io

External data and command integration; deployment options also at https://www.epsilon3.io/pricing .

### S09  OpenTAP core repository

Read source at github.com

Core architecture and MPL 2.0 license.

### S10  OpenTAP overview

Read source at doc.opentap.io

Plans, verdicts, resources and result listeners.

## Source register continued

### S11  OpenTAP Python integration

Read source at doc.opentap.io

Python plugin capability.

### S12  OpenTAP Runner

Read source at doc.opentap.io

Session/API facilities and registration/licensing references; selected component terms require verification.

### S13  OpenHTF repository and README

Read source at github.com

Apache 2.0; Python phases, measurements, plugs and attachments.

### S14  OpenC3 Script Runner

Read source at docs.openc3.com

Browser scripting, execution controls, suites and lifecycle.

### S15  OpenC3 scripting API

Read source at docs.openc3.com

Python and Ruby command and telemetry integration.

### S16  OpenC3 licenses

Read source at docs.openc3.com

Current license alternatives, restrictions and enterprise feature boundary.

### S17  Yamcs activities

Read source at docs.yamcs.org

Command, stack and script activities and status.

### S18  NASA Open MCT

Read source at nasa.github.io

Mission visualization framework.

### S19  AMMOS mission control products

Read source at ammos.nasa.gov

Yamcs and Open MCT mission-control integration context.

### S20  Frappe workflows

Read source at docs.frappe.io

Document states, transitions and approval workflow configuration.

## Source register continued

### S21  Frappe database API

Read source at docs.frappe.io

Transaction behavior and database operations.

### S22  Frappe background jobs

Read source at docs.frappe.io

Queue and after-commit execution facilities.

### S23  MDN browser storage quotas and eviction

Read source at developer.mozilla.org

Browser-managed storage persistence and limits.

### S24  PyVISA Python backend

Read source at github.com

Message-based instrument transports; per-device support still needs validation.

### S25  SQLite write-ahead logging

Read source at www.sqlite.org

WAL durability and operational constraints; also https://www.sqlite.org/pragma.html#pragma_synchronous .

### S26  Loom v0.12 local source inspection

Loom_Framework_v0.12.zip  |  version 12

README.md; docs/ARCHITECTURE.md, REQUIREMENTS.md and DATA_TYPES.md; src/Loom.Core/DocumentService.cs and Storage.cs; src/Loom.Sqlite/SqliteStore.cs; src/Loom.Demo/Program.cs.

### S27  Temporal activity definitions

Read source at github.com

Idempotency and activity execution behavior; architectural reference, not a selected dependency.

### S28  NASA product verification guidance

Read source at www.nasa.gov

Verification planning, evidence and discrepancy disposition; project applicability is separate.
