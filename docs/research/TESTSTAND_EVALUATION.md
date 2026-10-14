# TestStand focused evaluation

**Status: proposed; no cases executed.** Supplements V01–V18 in the [overall evaluation plan](EVALUATION_PLAN.md). The [deep dive](TESTSTAND_DEEP_DIVE.md) distinguishes NI-documented features from TestForge-derived requirements.

Record exact TestStand release/patch, development and deployment OS, license mode, process model, callbacks, result plugins, Python environments, driver versions and fixture configuration. Use simulation and a non-flight fixture for stop, fault and contention tests. Do not inject faults into flight hardware.

Use two article identities, two simulated instruments with distinct resource names, one representative real instrument, a nested sequence, a deliberately blocking module, an external database, a raw-result sink and a custom result processor. Seed a dynamic file dependency, a changed function signature and a forced-pass engineering sequence.

| Case | Procedure | Required evidence | TestForge requirements |
|---|---|---|---|
| T01 Policy provenance | Execute two sequences with common policy, then change a callback | Run package identifies resolved policy and hooks; earlier package unchanged | PROC-15, EXEC-12 |
| T02 Static preflight | Introduce missing module, wrong type, undeclared resource and unresolved cleanup | Machine-readable findings; release prevented until disposition | PROC-16 |
| T03 Setup and cleanup | Fail after acquiring one resource; fail its cleanup; abort another attempt | Separate obligation, attempt and outcome records; unresolved physical state visible | EXEC-13, EXEC-05 |
| T04 Blocking module | Request stop while a simulated module does not return | Measured control latency, escalation and honest unknown-state handling; no assumed immediate safing | HW-06, EXEC-13 |
| T05 Python lifetime | Compare global/execution/thread scopes; restart interpreter with live references | No undeclared state leakage; stale handles rejected; actual environment recorded | HW-11 |
| T06 Call boundary | Pass edge-case values; omit required output; change function signature | Contract failure or exact typed evidence; no silent drop/truncation | HW-12 |
| T07 Cohort barrier | Test three articles with shared action; withdraw one | Bounded barrier outcome and correct per-article attribution | EXEC-14 |
| T08 Resource contention | Acquire two resources in opposite orders; kill one holder | Bounded deadlock disposition and no unsafe reassignment | HW-13 |
| T09 Sink outage | Disconnect database and fail report generation after a measured pass | Raw evidence retained; test and delivery outcomes distinct; required closure gate blocks | DATA-10 |
| T10 Deferred replay | Process raw file twice; lose acknowledgment; change report configuration | Duplicate-safe logical records and versioned processing provenance | DATA-11, SYNC-02 |
| T11 Debug override | Force outcome, move execution pointer or edit variable in engineering mode | Attributable debug events; modified run cannot silently satisfy flight acceptance | SEC-11 |
| T12 Clean install | Deploy to clean isolated host with a missing dynamic resource | Missing dependency identified before command admission | OPS-12 |
| T13 Platform differences | Check Windows and proposed Linux feature sets with required sinks enabled | Explicit capability matrix and rejected unsupported configuration | OPS-13 |
| T14 Diagnostic correlation | Interleave nested calls in two workers and inject a failure | Correct run/thread/worker linkage without mixing evidence | OPS-14 |
| T15 Browser and QA | Demonstrate operator and separate QA browsers, observer and scoped API principal on isolated LAN | Supported interface topology and authorization at authoritative service, not just UI | OFF-06, AUTH-01–07, SEC-01–02 |
| T16 Power loss and closure | Interrupt local persistence; reconnect with missing artifact; complete analysis later | Acknowledged evidence retained within declared fault model; no final closure before reconciliation and analysis approval | OFF-03–04, SYNC-04, CLOSE-01–07 |

Classify each result as pass, fail, unsupported, blocked or not tested. Record screenshots, event exports, manifests, actual steps, deviations and reviewer identity. A vendor promise or a successful demo without the specified fault is not a pass.

## Questions for NI or an integration partner

- Which supported web interface and API bridge would implement the required local browser topology? What authentication and concurrency controls are included?
- Which exact Linux distribution, adapters, Python versions, driver stacks and result sinks are supported in the proposed release? How are disabled plugins replaced, if needed?
- Where do raw results become durable, and which failure modes can lose acknowledged records? What retention and repair tools exist?
- How are processing retries, customized database transactions and partially completed jobs identified? Can we demonstrate repeat ingestion safely?
- What can run without network license or identity services, for how long, and under what license configuration?
- Which parts are source-inspectable and modifiable, and what must remain a vendor binary? What interfaces have a compatibility commitment?
- What is licensed on development, deployed stations, CI agents and separate result-processing hosts? Obtain a configuration-specific quote.

The decision record should identify each unmet gate, available native feature, customization required, effort, ongoing maintenance owner and residual limitation. Preserve the distinction between absent evidence and an established product limitation.
