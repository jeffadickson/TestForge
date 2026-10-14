# Epsilon3 evaluation script

**Status: proposed, not executed.** Reviewed 2026-10-14. Supplements V01–V18 in the [evaluation plan](EVALUATION_PLAN.md). Use these cases for Epsilon3 and TestForge so the comparison remains fair. Record product build, edition, feature flags, deployment topology, OS/browser, integration versions and configuration before testing. Use a simulator or non-flight fixture for interruption and command-failure cases.

## Fixture and record

Prepare two article configurations, a procedure with two QA-signed table rows, a numeric default, a script command, a telemetry dwell, an attachment, a child procedure, an issue-linked hold and three planned iterations. Create distinct operator, QA, engineer, observer and service identities. Give one qualification a controlled expiry. Seed a calibration snapshot and a changed replacement record. Establish expected event IDs and artifact digests before each fault exercise.

For every case retain: setup, actual sequence, captured evidence, observed outcome, deviations, operator and reviewer, and requirement IDs. Classify **pass, fail, unsupported, blocked or not tested**. A presentation, undocumented workaround or promised roadmap feature is not a pass. Vendor-specific exceptions need explicit disposition against our requirements.

| Case | Action and fault | Acceptance evidence | Requirements |
|---|---|---|---|
| E01 Import and reuse | Import warnings and merged tables; then update a shared snippet | Reconciliation report, provenance and unchanged released expansion | PROC-09, PROC-10 |
| E02 Defaults and branching | Leave a passing default untouched; branch on missing and stale values | No observed pass from default; persisted rule/input decisions | PROC-11, PROC-12 |
| E03 Cycles and coverage | Run three cycles; retest failed cycle two; omit a planned condition | Separate cycle/attempt IDs and explicitly incomplete matrix | PROC-13, PROC-14 |
| E04 Qualification | Expire QA skill after start, both connected and isolated | New signature denied; historic signature and evaluated authority retained | AUTH-09, AUTH-06 |
| E05 Granular signing | Sign one row, reorder it, edit adjacent data, withdraw original signature | Stable signature scope, withdrawal history, downstream gate reset | AUTH-10, AUTH-11 |
| E06 Review rounds | Change a limit after engineering approval during QA stage | Obsolete approval no longer applies; comments have explicit dispositions | AUTH-12 |
| E07 Scoped holds | Set parent issue hold and child QA hold; clear one remotely | Remaining hold persists; no spontaneous hardware command | EXEC-09, EXEC-10 |
| E08 Redline distribution | Offer one change to pending, executing and signed runs | Separate adoption/impact decisions; preserved executed baseline | CHG-09 |
| E09 Command failures | Inject rejection, known failure, timeout and uncertain physical effect | Distinct outcomes and controlled recovery without unsafe replay | HW-09, EXEC-05 |
| E10 Dwell | Inject stale samples, gaps, hold time, clock rollback and restart | Only valid observation windows satisfy acceptance | HW-10, EXEC-11 |
| E11 Configuration and comparison | Swap a component mid-run; compare older images and data | Effective configuration attached to evidence; incompatibilities visible | CAL-09, DATA-09 |
| E12 Offline campaign | Prepare, disconnect WAN/database, reboot; execute with local QA and Python/VISA | Capability manifest, local authority, durable records and visible blockers | OFF-09, OFF-01–07 |
| E13 Storage/reconciliation | Interrupt persistence; upload metadata without one attachment; lose receipts | No acknowledged loss within approved fault model; precise pending/verified states | OFF-04, SYNC-09, SYNC-04 |
| E14 Competing mutations | Submit concurrent API edits; attempt QA signoff with ingestion token | Revision conflict and denied impersonation; traceable service actions | SEC-09, SEC-10 |
| E15 Administrative workflows | Deliver event twice; interrupt issue creation and destination response | One logical issue or visible unresolved action; no hardware side effect | OPS-11 |
| E16 Handover | Transfer run with unresolved command and outstanding tasks | Incoming acknowledgment plus recovery before control | OPS-10 |
| E17 Restore and metadata | Restore an old revision and change custom metadata schema | New draft ancestry; original run schemas and evidence preserved | CHG-10, OPS-09 |
| E18 Full closure and exit | Leave analysis pending, omit one upload, then export after completion | Closure blocked until all gates pass; independent reconstruction of raw and derived evidence | CLOSE-01–07, DATA-07 |

## Questions to settle in the demonstration

1. Where is each acknowledged write durable, and what are the supported failure and recovery boundaries? What happens when browser storage is cleared or the local host is lost?
2. Which exact actions work offline: start, sign, witness, withdraw, redline, add steps, execute scripts, acquire data, capture attachments, analyze, and close provisionally?
3. Does a disconnected cold start depend on previously authenticated sessions, external licensing, central secrets, CDNs or time services? How is local authority bounded?
4. How are duplicate command submissions and unknown physical outcomes distinguished from ordinary API retries? Which component owns instrument exclusion?
5. How does simultaneous offline editing reconcile signed records? Can we inspect both histories and the resolution evidence?
6. Which source/runtime components are inspectable, extensible and supportable by us? What contractual and technical limits affect custom Python and drivers?
7. Can we export complete event and approval history, raw files, schemas, calibration/configuration references and analysis provenance without vendor assistance? Can we verify those exports independently?
8. Which review, skills, automation, test-management and deployment features are licensed separately? What support and upgrade commitments apply to an isolated station?

## Decision record

Record each unmet requirement with severity, proposed configuration or implementation remedy, owner, cost, verification method and residual limitation. Repeat a case only to verify a concrete remedy. Keep uncertainty visible; “not demonstrated” must not be rewritten as “product cannot do this.” No buy/build decision follows automatically from the number of UI features shown.
