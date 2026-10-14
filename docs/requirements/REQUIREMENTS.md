# TestForge requirements baseline

122 proposed requirements, dated 2026-10-14. None is declared implemented or verified. P0: required before a controlled flight-hardware pilot. P1: full operational scope, staged only when explicitly excluded from the pilot. Numerical targets are proposals. Generated from [requirements.json](requirements.json); edit that catalog and rerun `python3 tools/render_requirements.py`.

See the [evaluation plan](../research/EVALUATION_PLAN.md) for combined campaigns and [architecture](../architecture/ARCHITECTURE.md) for responsibility boundaries.

## PROC — Procedure service

### PROC-01 — Stable identity (P0)

The system shall assign permanent IDs to procedures, revisions and steps, independent of displayed numbering.

**Acceptance:** Insert a step and verify historical signatures and result links still reference the original steps.

### PROC-02 — Immutable release (P0)

The system shall freeze a released revision and its dependent content; edits shall create a new revision.

**Acceptance:** Modify a draft and verify an existing released package and its digest remain unchanged.

### PROC-03 — Structured steps (P0)

The system shall support instructions, typed inputs, measurements, scripts, hold points, witnesses, attachments and subprocedures.

**Acceptance:** Execute a representative procedure containing every supported step type with required inputs enforced.

### PROC-04 — Execution guards (P0)

The system shall enforce prerequisites, allowed branches, loops and mandatory hold points in the runtime.

**Acceptance:** Attempt a direct API bypass of a hold point and confirm rejection and an audit event.

### PROC-05 — Release validation (P0)

The system shall reject missing references, invalid units, unresolved required roles and unsupported package dependencies.

**Acceptance:** Run invalid-package fixtures and verify release is blocked with actionable diagnostics.

### PROC-06 — Configuration applicability (P0)

The system shall restrict procedure use by article identity, configuration and approved applicability rules.

**Acceptance:** Start against a mismatched hardware revision and confirm an explicit blocking result.

### PROC-07 — Import and export (P1)

The system shall import structured procedures as drafts and export full content with stable identities and revision history.

**Acceptance:** Round-trip a procedure and identify any unsupported imported content before release.

### PROC-08 — Requirement mapping (P0)

The system shall link steps and analyses to versioned verification requirements and methods.

**Acceptance:** Change a requirement revision and verify affected released procedures and evidence are flagged for review.

### PROC-09 — Reusable content provenance (P1)

The system shall record the source revision and expansion of every template, snippet and included procedure in each released package.

**Acceptance:** Revise a reused snippet; verify an existing run is unchanged and affected future drafts can be identified.

**Basis:** Derived refinement: reuse requires dependency provenance, not a mutable reference.

**Sources:** S51, S52 (see [source register](../research/SOURCES.md)).

**Refines:** PROC-02, PROC-03.

### PROC-10 — Import reconciliation (P1)

The system shall produce a source-to-draft mapping and unresolved-conversion report for imported procedures, requiring author disposition before release.

**Acceptance:** Import a document with merged tables, warnings, units and ambiguous numbering; verify no missing item is silently accepted.

**Basis:** Derived refinement: a fast import is useful only if meaning survives conversion.

**Sources:** S51 (see [source register](../research/SOURCES.md)).

**Refines:** PROC-07, PROC-05.

### PROC-11 — Default value provenance (P0)

The system shall distinguish default, copied, manually observed and instrument-acquired values and prohibit an unconfirmed default from satisfying a required observation.

**Acceptance:** Start a run with an in-limit default; verify it cannot produce a measured pass or witness signature before an authorized observation.

**Basis:** TestForge policy derived from the risk of prefilled observations.

**Sources:** S52 (see [source register](../research/SOURCES.md)).

**Refines:** PROC-03, DATA-01.

### PROC-12 — Explainable branch decisions (P0)

The system shall persist each branch decision with its expression revision, input values and selected path, treating missing or invalid operands as unresolved.

**Acceptance:** Exercise section and variable branches with false, missing and stale operands; reproduce each decision from exported evidence.

**Basis:** Derived refinement: branching must remain reconstructable after inputs change.

**Sources:** S53 (see [source register](../research/SOURCES.md)).

**Refines:** PROC-04, EXEC-03.

### PROC-13 — Iteration identity (P1)

The system shall identify each planned batch iteration separately from a retest attempt and bind its inputs, signatures and dependencies to that iteration.

**Acceptance:** Run three planned cycles and repeat the second after failure; verify four attempts remain with three planned cycle identities.

**Basis:** Derived refinement of batch execution; planned repetition is not a replacement for failed evidence.

**Sources:** S58 (see [source register](../research/SOURCES.md)).

**Refines:** PROC-03, CHG-06.

### PROC-14 — Test condition matrix (P1)

The system shall version the planned combinations of test points, configurations and environmental conditions and report coverage against that matrix.

**Acceptance:** Plan two configurations at three temperatures; execute five combinations and verify the sixth remains uncovered despite all five passing.

**Basis:** Derived test-management requirement; detailed matrix semantics are TestForge design.

**Sources:** S61 (see [source register](../research/SOURCES.md)).

**Refines:** PROC-08, CLOSE-06.

## EXEC — Station runtime

### EXEC-01 — Run identity (P0)

The system shall assign unique run and attempt IDs with article, station, package and personnel context.

**Acceptance:** Start two offline runs and verify their imported records cannot collide.

### EXEC-02 — Durable transitions (P0)

The system shall commit an accepted transition and its event before returning success to the browser.

**Acceptance:** Terminate immediately after acknowledgment and recover the same accepted state.

### EXEC-03 — Explicit outcomes (P0)

The system shall distinguish pass, fail, inconclusive, error, invalid, aborted, skipped and not evaluated outcomes.

**Acceptance:** Inject each outcome and verify it cannot become pass through missing data or an exception.

### EXEC-04 — Hold and resume (P0)

The system shall apply declared hold and browser-disconnect policies, and recheck prerequisites before resumption.

**Acceptance:** Close the browser during acquisition, then change an instrument during a hold; verify the declared response and blocked resume.

### EXEC-05 — Unknown outcome (P0)

The system shall enter recovery required after an interrupted operation whose hardware effect cannot be established.

**Acceptance:** Crash after command transmission but before result persistence; verify no automatic retransmission.

### EXEC-06 — Retry classification (P0)

The system shall require each operation to declare read-only, idempotent or nonrepeatable behavior with an approved retry policy.

**Acceptance:** Verify retries are bounded and a nonrepeatable operation cannot use generic automatic retries.

### EXEC-07 — Resource ownership (P0)

The system shall permit one controlling authority per run and exclusive resource set, including during disconnection.

**Acceptance:** Attempt a second controller and confirm hardware access is denied until a valid handoff.

### EXEC-08 — Handover record (P0)

The system shall record shift handover, active configuration, held operations and transfer of operator responsibility.

**Acceptance:** Resume after a personnel change and verify the new operator acknowledges outstanding conditions.

### EXEC-09 — Scoped hold constraints (P0)

The system shall maintain independent run, section and step holds with reason, owner and explicit release predicates, preserving child holds when a parent clears.

**Acceptance:** Set an issue hold and a separate child QA hold; resolve the issue and verify the child stays held and its owner is displayed.

**Basis:** Derived refinement: a dependency becoming satisfied does not imply all holds are released.

**Sources:** S48, S49 (see [source register](../research/SOURCES.md)).

**Refines:** EXEC-04, CHG-08.

### EXEC-10 — Command resume authorization (P0)

The system shall require an authorized local resume decision and renewed hardware readiness checks before a cleared workflow constraint can permit a hardware command.

**Acceptance:** Clear a remote issue while a local step is paused; verify no command is sent until the local gate is completed.

**Basis:** TestForge policy intentionally separates automatic administrative progress from hardware resumption.

**Sources:** S48 (see [source register](../research/SOURCES.md)).

**Refines:** EXEC-04, HW-07.

### EXEC-11 — Duration semantics (P0)

The system shall define elapsed, active and hold time separately and record the clock and pause/reset policy used by duration-dependent acceptance rules.

**Acceptance:** Pause a dwell, move wall time backward and restart the station; verify the configured rule cannot count unobserved time as valid dwell.

**Basis:** Derived refinement; measured task duration alone does not prove a valid physical soak.

**Sources:** S57, S59 (see [source register](../research/SOURCES.md)).

**Refines:** DATA-04, PROC-04.

## AUTH — Identity and approval service

### AUTH-01 — Individual identity (P0)

The system shall authenticate individual operators, witnesses and approvers without shared sign-off accounts.

**Acceptance:** Verify two people using one workstation retain distinct authenticated signature records.

### AUTH-02 — Independent witness (P0)

The system shall enforce separate operator and QA identities when a step requires independence.

**Acceptance:** Give one account both roles and confirm it still cannot satisfy both signatures.

### AUTH-03 — Approval policies (P0)

The system shall support named approvers, role slots, all-of and explicitly configured quorum rules with ordering.

**Acceptance:** Exercise three required approvers, rejection and optional observers without premature approval.

### AUTH-04 — Signature meaning (P0)

The system shall bind each signature to identity, role, meaning, timestamp, policy and exact subject/evidence digest.

**Acceptance:** Alter the signed content and verify the old signature cannot approve the new revision.

### AUTH-05 — Reauthentication (P0)

The system shall require a configured confirmation and reauthentication policy for consequential signatures.

**Acceptance:** Expire a signing session and verify a normal UI click cannot silently sign.

### AUTH-06 — Offline authority (P0)

The system shall validate locally provisioned, bounded identity and role grants for disconnected actions.

**Acceptance:** Cold-start offline and verify permitted signing works while an expired or out-of-scope grant fails.

### AUTH-07 — Observers and comments (P0)

The system shall separate viewing, commenting, executing, witnessing and approving permissions.

**Acceptance:** Verify a read-only collaborator neither mutates the run nor becomes a required approver.

### AUTH-08 — Delegation and revocation (P0)

The system shall record authorized delegation and reconcile newly discovered revocations without erasing prior signatures.

**Acceptance:** Revoke an offline user centrally and verify reconnect creates an attributable review issue.

### AUTH-09 — Qualification at action time (P0)

The system shall check required skill and certification validity for the specific role and action at execution and signoff time, retaining the evaluated qualification snapshot.

**Acceptance:** Expire QA qualification after run start; verify a new QA signoff is blocked locally and online without erasing earlier signatures.

**Basis:** Derived refinement: an assigned role can be temporarily unusable; offline validity must be explicit.

**Sources:** S50 (see [source register](../research/SOURCES.md)).

**Refines:** AUTH-06, AUTH-08.

### AUTH-10 — Granular evidence signatures (P0)

The system shall allow signatures on identified table rows and content blocks with defined required fields and freeze their signed evidence scope.

**Acceptance:** Sign one row, reorder rows and edit a second row; verify the original signature still identifies the first row and rejects an unsigned change to its evidence.

**Basis:** Derived refinement of row signatures and required versus optional content.

**Sources:** S49, S56 (see [source register](../research/SOURCES.md)).

**Refines:** AUTH-04, PROC-01.

### AUTH-11 — Signature withdrawal (P0)

The system shall record withdrawal of a signature as a new attributed event with reason, preserving the original signature and reevaluating dependent approvals.

**Acceptance:** Withdraw a row signature after QA review; verify the original remains inspectable, closure is blocked and no hardware operation is repeated.

**Basis:** Derived distinction between correcting an approval and physically repeating a test.

**Sources:** S56 (see [source register](../research/SOURCES.md)).

**Refines:** AUTH-04, CHG-07.

### AUTH-12 — Review round integrity (P0)

The system shall bind staged approvals and comment dispositions to a review round and content revision, with required redisposition after a consequential change.

**Acceptance:** Approve engineering review, change an acceptance limit during QA review and verify the obsolete approval cannot authorize release.

**Basis:** Derived refinement: staged review must not retain misleading approval applicability.

**Sources:** S57, S05 (see [source register](../research/SOURCES.md)).

**Refines:** AUTH-03, CHG-07.

## CHG — Change control service

### CHG-01 — Proposed redlines (P0)

The system shall record redlines as explicit proposals with original content, proposed content, reason and affected scope.

**Acceptance:** Show the exact before/after change and proposer for an inserted or altered step.

### CHG-02 — Approval before use (P0)

The system shall block affected execution until the required redline approvals are complete.

**Acceptance:** Propose a changed limit while running and verify the original approved limit remains operative.

### CHG-03 — Run and master scope (P0)

The system shall distinguish run-only changes from proposed changes to the master procedure.

**Acceptance:** Approve a run insertion and verify other runs and the released master do not change.

### CHG-04 — Evidence preservation (P0)

The system shall retain original observations and append corrections with reason, author and time.

**Acceptance:** Correct a signed numeric result and verify both values and affected approvals remain traceable.

### CHG-05 — Skip and defer (P0)

The system shall require reason, authority and disposition for skipped, deferred or not-applicable required steps.

**Acceptance:** Attempt closure with an unauthorized skip and confirm it is blocked.

### CHG-06 — Retest linkage (P0)

The system shall create a new attempt for every retest and retain prior failed and invalid attempts.

**Acceptance:** Pass a retest and verify the failed attempt remains in reports and requirement disposition.

### CHG-07 — Impact invalidation (P0)

The system shall mark affected downstream evidence and approvals for reevaluation after consequential changes.

**Acceptance:** Change a calibration correction or limit and verify dependent analysis approval becomes stale.

### CHG-08 — Nonconformance (P0)

The system shall link deviations and nonconformances to article, run, affected steps and authorized dispositions.

**Acceptance:** Accept a documented waiver and verify the measured failure is preserved rather than relabeled pass.

### CHG-09 — Cross-run change adoption (P0)

The system shall present a shared redline as a separately evaluated change for each receiving run, with applicability, impact assessment and adoption approval before use.

**Acceptance:** Offer one change to runs with pending, executing and signed affected steps; verify each obtains an explicit disposition and no signed history is rewritten.

**Basis:** TestForge policy; propagation transports a proposal, not authority to overwrite a running baseline.

**Sources:** S55 (see [source register](../research/SOURCES.md)).

**Refines:** CHG-02, CHG-03, CHG-07.

### CHG-10 — Historical revision restoration (P1)

The system shall restore earlier procedure content only into a new draft with ancestry and normal release review.

**Acceptance:** Restore an older revision; verify original releases and run links are unchanged and the restored draft cannot execute as a released revision.

**Basis:** Derived refinement of version rollback semantics.

**Sources:** S54 (see [source register](../research/SOURCES.md)).

**Refines:** PROC-02.

## HW — Workers and instrument gateway

### HW-01 — Script provenance (P0)

The system shall execute only approved script packages with pinned dependencies and recorded hashes in flight mode.

**Acceptance:** Change one script byte or dependency and confirm execution is refused.

### HW-02 — Process isolation (P0)

The system shall run scripts in supervised worker processes with bounded resources and separate credentials.

**Acceptance:** Hang or crash a worker and verify the UI, journal and supervision remain available.

### HW-03 — Driver abstraction (P0)

The system shall provide versioned adapters for VISA, serial, USB and required vendor APIs with simulated equivalents.

**Acceptance:** Run the same measurement contract against a simulator and representative approved equipment.

### HW-04 — Instrument identity (P0)

The system shall verify actual device identity and configured resource mapping before permitting commands.

**Acceptance:** Swap two USB devices or change an address and verify the wrong instrument is blocked.

### HW-05 — Operation journal (P0)

The system shall persist command intent, operation ID and observed outcome without claiming atomic hardware execution.

**Acceptance:** Interrupt at each dispatch boundary and verify an honest completed or unknown classification.

### HW-06 — Bounded cancellation (P0)

The system shall specify command timeouts, cancellation escalation and equipment-specific recovery actions.

**Acceptance:** Block a driver call and demonstrate the approved timeout and independent recovery behavior.

### HW-07 — Safety boundary (P0)

The system shall respect independent interlocks and enforce approved command envelopes and operating modes.

**Acceptance:** Request an out-of-envelope command and verify rejection; prove a failed process cannot defeat the hardware interlock.

### HW-08 — Data protocol (P0)

The system shall ingest typed worker measurements and artifacts through a validated protocol separate from diagnostic logs.

**Acceptance:** Send malformed units, duplicate samples and a truncated artifact; verify explicit rejection or incomplete status.

### HW-09 — Command failure propagation (P0)

The system shall map command rejection, execution failure, timeout and unknown outcome into explicit step dispositions and prevent automatic success or progression through a required failed command.

**Acceptance:** Inject all four outcomes into a multi-command step; verify evidence distinguishes them and no later hazardous command runs implicitly.

**Basis:** Derived refinement: a single Boolean command result loses essential recovery information.

**Sources:** S55 (see [source register](../research/SOURCES.md)).

**Refines:** EXEC-03, EXEC-05, HW-05.

### HW-10 — Telemetry acceptance window (P0)

The system shall evaluate telemetry-based acceptance using a versioned rule defining units, sample validity, freshness and required observation window.

**Acceptance:** Replay a previously passing stale sample, then introduce a data gap during a required dwell; verify neither yields a valid pass.

**Basis:** TestForge-derived integrity rule; vendor integration and duration features motivate it, not establish equivalent behavior.

**Sources:** S08, S59 (see [source register](../research/SOURCES.md)).

**Refines:** DATA-01, DATA-04, HW-08.

## CAL — Asset and reference adapters

### CAL-01 — Asset chain (P0)

The system shall record instrument, channel, probe, cable, fixture and transducer identities needed for measurement traceability.

**Acceptance:** Reconstruct the complete measurement chain from the saved run without live asset-system access.

### CAL-02 — Calibration snapshot (P0)

The system shall retain certificate revision, validity interval, correction data, uncertainty and source retrieval metadata.

**Acceptance:** Disconnect the calibration database and reproduce the context from the prepared package.

### CAL-03 — Validity checks (P0)

The system shall check calibration at preparation and required use points, including expiry during a long test.

**Acceptance:** Cross an expiry boundary and verify the approved hold or disposition policy is enforced.

### CAL-04 — Reference freshness (P0)

The system shall apply configured freshness and expiry policies to each cached external reference.

**Acceptance:** Use a stale required reference offline and verify the action is blocked or explicitly authorized.

### CAL-05 — Controlled exceptions (P0)

The system shall require scoped approval for calibration or reference exceptions and record affected measurements.

**Acceptance:** Verify an exception for one instrument and run does not authorize another.

### CAL-06 — Recall impact (P0)

The system shall identify past measurements and analyses affected by a later calibration recall or out-of-tolerance finding.

**Acceptance:** Recall a certificate and generate the exact affected evidence set with review tasks.

### CAL-07 — Measurement quality (P0)

The system shall retain range, resolution, uncertainty model and approved guard-band decision rules when applicable.

**Acceptance:** Evaluate values near a limit and verify the approved rule and its revision are reported.

### CAL-08 — External adapters (P1)

The system shall provide read adapters with provenance, timeouts, schema validation and independently testable mappings.

**Acceptance:** Change an upstream schema and verify failure is explicit without modifying prior snapshots.

### CAL-09 — Configuration changes during testing (P0)

The system shall record article component changes with before/after configuration, serial or lot identity, effective run position and approval, reevaluating affected verification coverage.

**Acceptance:** Replace a component between two measurements; verify each measurement resolves to the correct configuration and earlier results are not silently assigned to the replacement.

**Basis:** Derived refinement of in-run assembly updates and genealogy.

**Sources:** S49, S59 (see [source register](../research/SOURCES.md)).

**Refines:** PROC-06, CLOSE-06.

## DATA — Evidence service

### DATA-01 — Measurement representation (P0)

The system shall preserve raw values, units, precision, validity flags and evaluated limits without silent conversion.

**Acceptance:** Round-trip large integers, decimals, timestamps and invalid readings without loss or false pass.

### DATA-02 — Raw and derived data (P0)

The system shall retain raw acquisitions separately from reductions, corrections and analysis outputs.

**Acceptance:** Recompute a derived value from retained raw evidence and identify the exact algorithm revision.

### DATA-03 — Large artifacts (P0)

The system shall stream waveforms, images and binary files to bounded local storage with size and digest manifests.

**Acceptance:** Acquire a 10 GB artifact without loading it entirely into memory and detect a truncated final chunk.

### DATA-04 — Timing evidence (P0)

The system shall record source time, receipt time, clock source, synchronization quality and sequence order.

**Acceptance:** Move the wall clock backward and verify event order remains reconstructable and uncertainty is visible.

### DATA-05 — Evidence integrity (P0)

The system shall verify content digests and signed checkpoints when storing, synchronizing and exporting evidence.

**Acceptance:** Alter or remove a retained event or artifact and verify the integrity check detects it.

### DATA-06 — Storage exhaustion (P0)

The system shall monitor capacity and apply a validated reserve policy before new operations can exhaust evidence storage.

**Acceptance:** Fill the disk during acquisition and verify explicit incomplete evidence and the approved safe response.

### DATA-07 — Portable record (P0)

The system shall export human-readable reports and machine-readable events, schemas, manifests and raw artifacts.

**Acceptance:** Open an export on an isolated clean system and verify its completeness without a running server.

### DATA-08 — Retention and restoration (P0)

The system shall retain protected records and verify coordinated backup and restore of journals and artifact files.

**Acceptance:** Restore a backup and compare all committed evidence and manifest hashes with the source.

### DATA-09 — Context-aware comparison (P1)

The system shall show procedure revision, article configuration, calibration and analysis context when comparing results or attachments across runs.

**Acceptance:** Compare visually similar records with different limit revisions and configurations; verify incompatibilities are visible before a comparison can support approval.

**Basis:** Derived refinement: visual similarity is not proof of interchangeable evidence.

**Sources:** S54 (see [source register](../research/SOURCES.md)).

**Refines:** DATA-02, CLOSE-03.

## OFF — Local station runtime

### OFF-01 — Local web application (P0)

The system shall serve all required UI assets and APIs locally without runtime Internet dependencies.

**Acceptance:** Start the browser and station after a reboot with every external network disconnected.

### OFF-02 — Prepared package (P0)

The system shall verify package completeness, signatures, dependencies, reference validity and storage before offline readiness.

**Acceptance:** Remove each required package element in turn and verify readiness fails.

### OFF-03 — Local source of record (P0)

The system shall record every acknowledged input, signature, transition and result locally before replication.

**Acceptance:** Disable the central database throughout a run and recover every acknowledged record locally.

### OFF-04 — Crash durability (P0)

The system shall recover committed events and identify incomplete operations after process or power interruption.

**Acceptance:** Inject interruptions across commit boundaries on the target storage and verify no acknowledged event is lost.

### OFF-05 — Disconnected duration (P0)

The system shall support a proposed seven-day isolated campaign within an approved authority and capacity budget.

**Acceptance:** Complete a seven-day soak without external authentication, licensing, package or time-service dependencies.

### OFF-06 — Offline collaboration (P0)

The system shall support authorized local operator and witness use through one station authority, with explicit connectivity status.

**Acceptance:** Use two browsers on an isolated LAN and reject conflicting execution actions.

### OFF-07 — Readiness boundaries (P0)

The system shall distinguish central service failure from unavailable local storage, invalid authority or missing safety prerequisites.

**Acceptance:** Verify central outage permits prepared work while loss of local durable storage inhibits new operations.

### OFF-08 — Portable transport (P1)

The system shall support encrypted, signed export/import bundles when network synchronization is unavailable.

**Acceptance:** Import the same removable-media bundle twice and verify deduplication and custody records.

### OFF-09 — Offline capability manifest (P0)

The system shall declare offline support and preparation prerequisites for every enabled action and adapter and reject package readiness when required operations are unavailable.

**Acceptance:** Prepare a run requiring start, QA signoff, redline, camera capture, Python/VISA, analysis and upload; disconnect and verify each declared capability or a pre-departure blocker.

**Basis:** Derived refinement: procedure cache eligibility does not prove the entire workflow can operate offline.

**Sources:** S05, S06, S07, S58 (see [source register](../research/SOURCES.md)).

**Refines:** OFF-02, OFF-07.

## SYNC — Replication service

### SYNC-01 — Transactional outbox (P0)

The system shall atomically store each accepted event and its replication obligation in the local transaction.

**Acceptance:** Crash after commit and before upload; verify the event remains queued after restart.

### SYNC-02 — Idempotent ingest (P0)

The system shall deduplicate retransmissions by stable identity and reject identical IDs with different content.

**Acceptance:** Retry a batch after losing its acknowledgment and verify exactly one central record per event.

### SYNC-03 — Resumable transfer (P0)

The system shall resume verified artifact chunks without marking incomplete evidence as complete.

**Acceptance:** Disconnect repeatedly during a 10 GB upload and verify the final digest and missing-chunk accounting.

### SYNC-04 — Completeness receipt (P0)

The system shall issue reconciliation receipts only after required sequences, signatures and artifacts validate.

**Acceptance:** Upload all metadata but omit one attachment and verify closure remains blocked.

### SYNC-05 — Conflict quarantine (P0)

The system shall preserve conflicting signed records and require explicit resolution instead of last-writer-wins.

**Acceptance:** Submit two incompatible offline branches and verify both survive with a blocked disputed transition.

### SYNC-06 — Ownership fencing (P0)

The system shall reject stale ownership epochs and prevent resynchronization from authorizing a second hardware commander.

**Acceptance:** Reconnect an old station after handoff and verify it cannot resume instrument control.

### SYNC-07 — Reference reconciliation (P0)

The system shall compare execution snapshots with later releases, recalls and revocations and generate review tasks.

**Acceptance:** Reconnect after a calibration recall and verify affected runs are flagged without history edits.

### SYNC-08 — Retention acknowledgment (P0)

The system shall retain local evidence until complete central receipt and configured backup/retention gates are met.

**Acceptance:** Lose the final receipt or fail the central backup gate and verify local cleanup is refused.

### SYNC-09 — Per-operation reconciliation visibility (P0)

The system shall display locally committed, upload pending, uploaded, centrally verified and conflicted states for required events and artifacts without collapsing them into one synced flag.

**Acceptance:** Upload event metadata while withholding an attachment and a signature dependency; verify operators can identify both blockers and final closure remains inhibited.

**Basis:** Derived refinement: optimistic online status must not be mistaken for verified completeness.

**Sources:** S05, S06, S07 (see [source register](../research/SOURCES.md)).

**Refines:** SYNC-04, OPS-01.

## CLOSE — Review and analysis services

### CLOSE-01 — Execution checklist (P0)

The system shall require step dispositions, required signatures, evidence completeness and final article configuration for execution review.

**Acceptance:** Leave each item unresolved in turn and verify the review gate explains the blocker.

### CLOSE-02 — Separate analysis (P0)

The system shall track analysis tasks, owners, inputs and approvals independently from execution completion.

**Acceptance:** Complete a run with analysis pending and verify it is not labeled fully closed.

### CLOSE-03 — Reproducible analysis (P0)

The system shall record analysis code, dependencies, parameters, input hashes and output revisions.

**Acceptance:** Re-run the approved analysis on retained inputs and compare outputs under stated tolerances.

### CLOSE-04 — Approval invalidation (P0)

The system shall invalidate applicability of analysis approval when its inputs, code or acceptance rules change.

**Acceptance:** Revise a reduction script and verify a new analysis approval is required.

### CLOSE-05 — Closure gate (P0)

The system shall permit final closure only after reconciliation, required approvals and authorized deviation dispositions.

**Acceptance:** Attempt closure with one missing approver, unresolved conflict or incomplete upload and confirm denial.

### CLOSE-06 — Requirement disposition (P0)

The system shall report verified, failed, waived, invalid and not-yet-verified requirements with evidence links.

**Acceptance:** Verify a waived failure remains distinct from a measured pass in the verification matrix.

### CLOSE-07 — Amendment lifecycle (P0)

The system shall reopen closed records through controlled amendments while preserving the prior closure manifest.

**Acceptance:** Correct an archived analysis and reconstruct both the original and amended acceptance states.

### CLOSE-08 — Work queues (P1)

The system shall provide ownership, due dates, escalation and observer access for execution and analysis action items.

**Acceptance:** Assign overdue tasks and verify notifications do not silently approve or close them.

## SEC — Platform and assurance

### SEC-01 — Enforced access (P0)

The system shall enforce role, project and article scope at the API and data-access layers.

**Acceptance:** Attempt cross-project reads and unauthorized mutations directly through APIs and verify denial.

### SEC-02 — Local attack surface (P0)

The system shall authenticate local clients and protect against cross-origin requests, host spoofing and unauthorized LAN access.

**Acceptance:** Attempt browser-based requests from an untrusted origin and verify commands cannot be issued.

### SEC-03 — Protected secrets (P0)

The system shall encrypt sensitive records at rest and in transit, and protect keys and credentials with approved storage and rotation.

**Acceptance:** Rotate keys without losing historical evidence; verify encrypted storage and transport and absence of secrets in exports.

### SEC-04 — Approved software (P0)

The system shall verify signed software packages and prohibit unapproved upgrades during active runs.

**Acceptance:** Offer a new release during a run and verify it cannot change the pinned execution environment.

### SEC-05 — Privileged activity (P0)

The system shall record administrator actions and restrict modification or deletion of authoritative evidence.

**Acceptance:** Attempt an administrative edit and verify prevention or a detectable controlled amendment.

### SEC-06 — Worker containment (P0)

The system shall apply least-privilege filesystem, network and device access to test workers.

**Acceptance:** Use a test worker to attempt unauthorized file, network and device access and verify rejection.

### SEC-07 — Assurance record (P0)

The system shall maintain requirements-to-test traceability, dependency inventory, known limitations and reviewed release evidence.

**Acceptance:** Audit a candidate release and resolve every P0 requirement to recorded acceptance evidence.

### SEC-08 — Environment separation (P0)

The system shall distinguish simulation, development, engineering and flight operation in access rules and stored records.

**Acceptance:** Attempt to present simulated measurements as flight evidence and verify the provenance is unmistakable.

### SEC-09 — Optimistic mutation control (P0)

The system shall require expected revision preconditions for consequential API mutations and return conflicts without overwriting newer accepted state.

**Acceptance:** Submit two concurrent limit or redline edits against the same revision; verify only one succeeds and the other must be reviewed against the new state.

**Basis:** TestForge design choice: prevent silent last-writer-wins behavior in consequential edits.

**Sources:** S60 (see [source register](../research/SOURCES.md)).

**Refines:** SEC-01, CHG-07.

### SEC-10 — Service principal boundaries (P0)

The system shall identify service actions separately from human signatures and scope integration credentials by project and permitted action, with recorded rotation and revocation.

**Acceptance:** Use a valid ingestion credential to attempt QA approval or cross-project reads; verify denial and attributable audit events.

**Basis:** Derived refinement: access to automation APIs is not authority to impersonate a witness.

**Sources:** S60, S50 (see [source register](../research/SOURCES.md)).

**Refines:** AUTH-01, SEC-01, SEC-03.

## OPS — Platform operations and user interface

### OPS-01 — Operational display (P0)

The system shall show article identity, revision, active step, ownership, hardware status, local persistence and sync backlog.

**Acceptance:** An operator identifies the authoritative run and unsynchronized evidence without navigating away.

### OPS-02 — Clear actions (P0)

The system shall distinguish hold, resume, abort, skip, repeat and emergency safing with appropriate role and confirmation rules.

**Acceptance:** Run a witnessed usability exercise and verify no ambiguous button initiates a repeat or closes a failed step.

### OPS-03 — Accessible interaction (P1)

The system shall support keyboard operation, readable contrast, non-color status cues and documented supported browsers.

**Acceptance:** Complete a procedure without a mouse and verify errors remain identifiable without color.

### OPS-04 — Reference load (P0)

The system shall meet proposed targets of 10,000 steps per procedure and 100 structured events per second per station.

**Acceptance:** Run the reference load with a proposed p95 local action acknowledgment below 500 ms, excluding instrument latency.

### OPS-05 — Startup and recovery (P0)

The system shall restore the UI and a truthful recovered run state within a proposed 60 seconds on approved hardware.

**Acceptance:** Restart a loaded station; verify readiness timing without automatically resuming hardware actions.

### OPS-06 — Observability (P0)

The system shall expose correlated health, logs and metrics without treating diagnostic telemetry as the evidence record.

**Acceptance:** Disable telemetry export and verify execution evidence remains complete and locally inspectable.

### OPS-07 — Install and upgrade (P0)

The system shall support reproducible offline installation, controlled schema migration and rollback or forward-recovery procedures.

**Acceptance:** Install on a clean isolated host and rehearse a failed upgrade without losing historical records.

### OPS-08 — Capacity and support (P0)

The system shall document storage sizing, backups, restore, instrument compatibility and incident recovery for operators.

**Acceptance:** A second engineer follows the runbook to restore a station and identify an unresolved command outcome.

### OPS-09 — Versioned custom metadata (P1)

The system shall support typed, scoped custom metadata with schema revision and distinguish classification fields from evidence or acceptance fields.

**Acceptance:** Change a custom field type after release; verify historical values retain their schema and consequential fields require controlled revision.

**Basis:** Derived extensibility requirement; customization must not bypass evidence controls.

**Sources:** S49 (see [source register](../research/SOURCES.md)).

**Refines:** PROC-02, DATA-07.

### OPS-10 — Handover acknowledgment (P0)

The system shall require the incoming authorized operator to acknowledge outstanding holds, unknown command outcomes, pending redlines and assigned tasks before taking control.

**Acceptance:** Transfer a run with an unresolved command and reassigned task; verify control stays blocked until acknowledgment and hardware recovery gates are met.

**Basis:** Derived refinement of task tracking and shift continuity.

**Sources:** S54 (see [source register](../research/SOURCES.md)).

**Refines:** EXEC-08, EXEC-05.

### OPS-11 — Durable workflow actions (P1)

The system shall version event-triggered administrative workflows and durably track deduplicated actions, bounded retries and terminal failures without issuing hardware commands directly.

**Acceptance:** Deliver the same failed-step event twice, interrupt issue creation and retry; verify one logical issue and a visible unresolved action if the destination remains unavailable.

**Basis:** Derived reliability requirement for trigger/condition/action automation.

**Sources:** S51 (see [source register](../research/SOURCES.md)).

**Refines:** SYNC-01, SYNC-02, CLOSE-08.
