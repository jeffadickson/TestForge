# NI TestStand deep dive: execution, integration and requirements

**Reviewed 14 October 2026.** “TestRunner” is interpreted here as **NI TestStand**, the NI test-executive product discussed earlier. This report does not evaluate every product named TestRunner. It supplements the [market assessment](MARKET_RESEARCH.md) and [Epsilon3 study](EPSILON3_DEEP_DIVE.md). Public NI documentation is the evidence; no installation, licensed trial, real instrument or fault-injection test was performed.

## Assessment

TestStand is a strong benchmark for the machinery underneath a flight-hardware procedure application: reusable sequencing, language adapters, concurrency, instrument coordination, debugging, deployment and result processing. Epsilon3 is the more directly relevant benchmark for collaborative procedure review and human approvals. These are complementary observations, not a claim that either product is incapable of extending into the other's domain.

For TestForge, the most useful lessons are architectural. Separate test-specific logic from shared execution policy; make lifecycle and cleanup behavior explicit; treat Python session lifetime as part of the execution contract; and preserve evidence independently of reporting. A button labeled Stop, a completed sequence, and a successfully generated report each establish different facts. None alone establishes safe hardware state or approved final closure.

This study adds **14 requirements**, increasing the canonical catalog from **122 to 136**. All prior entries are preserved. Each addition has source IDs, a derivation rationale, related requirements and an acceptance check. Normative proposed wording is in [requirements.json](../requirements/requirements.json), with a generated [readable view](../requirements/REQUIREMENTS.md). These are TestForge requirements inferred from the research, not assertions that NI implements every proposed behavior.

## Current-platform correction

The prior market assessment's Windows trial description remains a description of the development download. It must not be read as a claim that all current execution deployments are Windows-only. NI's 2026 Q3 release documentation introduces deployment of systems developed on Windows to supported Linux targets. The same release history documents Python 3.14 support in 2026 Q1 while excluding free-threaded Python for that adapter. Exact supported versions still need to be pinned for the evaluation. [S74](https://www.ni.com/docs/en-US/bundle/teststand/page/new-features-and-changes.html).

Linux deployment is not documented as feature-identical. The configuration guide says that this deployment mode disables Database Logging and Offline Result Processing plugins and does not support TestStand Environments. This makes feature-level qualification essential for our database-outage scenario. It does not establish that custom persistence is impossible; it establishes that Windows result-processing assumptions cannot simply be carried across. The alternate NI locale served the English guide when the English URL failed to load. [S75](https://www.ni.com/docs/gd-GB/bundle/teststand/page/creating-a-linux-deployment.html).

## Documented capabilities and their limits

| Area | NI documentation establishes | TestForge interpretation / unresolved proof |
|---|---|---|
| Process models | Sequential, Parallel and Batch models separate common test operations from client sequences | Shared lifecycle policy needs versioned approval and provenance |
| Callbacks | Model, engine and front-end extensions with different invocation scopes | Hook composition and failures must not bypass mandatory gates |
| Python | Out-of-process CPython, configurable environments, data conversion and object references | Demonstrate actual driver dependencies, serialization and restart behavior |
| Sessions | Interpreter scope can be global, per execution, per thread or selected by reference | Scope is part of reproducibility and isolation |
| Termination | Terminate runs cleanup; Abort skips it; active modules must return control for stop requests to take effect | UI stop is not an independent emergency stop or guaranteed safing |
| Results | Incremental logging and later processing of raw results are available | Prove durable commit boundaries, replay behavior and completeness separately |
| Parallel execution | Synchronization and shared-resource coordination are supported | Cross-process recovery and uncertain physical effects require stronger ownership rules |
| Analysis | Sequence Analyzer provides built-in and custom predeployment checks | Analysis is a release gate, not proof of physical correctness |
| Deployment | Packaging accounts for test code, framework files, runtimes and drivers | Dynamic dependencies need explicit declarations and isolated-install verification |
| User management | Users, groups and privileges constrain editor/interface functions | NI explicitly distinguishes this from operating-system security |
| Interfaces | Engine API separates presentation from execution and supports custom interfaces | Browser collaboration, offline authorization and QA workflows need their own demonstration |

Sources: S62–S73, plus S02 and S03. All are vendor documentation, not witnessed product results.

## Execution policy and extension points

NI's process model separates common activities such as article identification and results handling from the specific sequence being tested. Sequential, parallel and batch operation are different policies rather than copies of the same test with scattered infrastructure code. Model callbacks allow targeted customization. [S62](https://www.ni.com/docs/en-US/bundle/teststand/page/process-models.html).

TestForge should carry this separation into PROC-15. A released run package should identify the procedure, execution policy, adapters, acceptance rules and data-handling configuration. An organization-wide change to admission or completion policy should not require hand-editing every procedure, but it must still produce a new approved execution definition. Otherwise identical procedure files could execute differently on different stations without an obvious explanation.

Callbacks are powerful because they put behavior around many steps. NI distinguishes model, engine and front-end callbacks; some multiple definitions compose rather than overriding one another. [S63](https://www.ni.com/en/support/documentation/supplemental/07/using-callbacks-in-ni-teststand.html). Our derived EXEC-12 therefore requires resolved hook order, scope and failure handling in the approved package. A logging hook must not accidentally execute a command twice, clear a required failure, or provide a path around QA authorization.

For the initial TestForge build, keep the extension surface small: admission validation, resource setup, invocation, evidence capture, disposition and cleanup. Add hooks where there is a real reuse need. An unrestricted callback mechanism can otherwise make the actual execution behavior harder to inspect than an explicit sequence.

## Python, VISA and the boundary between languages

The Python adapter documents out-of-process execution, functions and objects, environment selection and conversion between Python and TestStand values. That is materially more than launching a script and reading stdout. [S64](https://www.ni.com/docs/en-US/bundle/teststand/page/python-adapter.html). Session documentation distinguishes global, execution and thread scope and notes that an object reference belongs to its originating interpreter session. [S65](https://www.ni.com/docs/en-US/bundle/teststand/page/python-interpreter-sessions.html).

HW-11 makes session lifetime explicit for TestForge. A cached instrument object may be useful within one controlled campaign; it becomes dangerous if a subsequent run silently inherits state. Restart also invalidates process-local handles even when the procedure record survives. Recovery should reconstruct resources from configuration and verify equipment state, not deserialize a stale pointer and assume continuity.

The adapter limitations page identifies practical interoperability constraints, including required argument specification, lack of keyword arguments, certain container-conversion restrictions and the need to store returned values in TestStand variables for logging. [S66](https://www.ni.com/docs/en-US/bundle/teststand/page/python-adapter-known-limitations.html). HW-12 generalizes the lesson: a call contract must cover types, conversions, resolved arguments and required outputs. Successful process completion is insufficient when the measurement never enters the evidence record.

For VISA, distinguish four layers: the procedure, Python or other language module, VISA/backend driver and physical instrument. TestStand's language support does not make every USB device compatible or supply every vendor driver. The trial should use the actual planned DMM, source or generator and required driver stack, including resource identity, timeouts, binary transfers and reconnect behavior. The existing HW-03 and HW-04 requirements already cover adapters and actual device identity, so they are not duplicated here.

Do not read general documentation examples of old Python versions as the current compatibility list. Use the selected TestStand release and its supported adapter/runtime matrix. Similarly, current .NET changes do not imply old assemblies or undocumented APIs remain compatible without testing. Browser clients can be portable while the instrument worker remains platform-specific; those are separate support promises.

## Termination, cleanup and recovery

NI explicitly distinguishes Terminate, which executes cleanup, from Abort, which omits it, and describes the dependence of stop requests on running code modules returning control. [S67](https://www.ni.com/docs/en-US/bundle/teststand/page/terminating-and-aborting-executions.html). This is a useful concrete reminder that software control and physical safing must be assessed separately.

EXEC-13 adds a cleanup obligation record to TestForge. Obligations arise as resources are acquired: a supply may need disabling, a fixture releasing or a session closing. If setup fails halfway through, cleanup must know what was actually acquired. Each attempted action needs an outcome. Calling the cleanup function is not evidence that its command reached the device or that safe state was confirmed.

After a crash or power loss, the system should identify outstanding obligations and enter controlled recovery. It cannot promise that ordinary cleanup code ran after the processor stopped. Independent interlocks remain part of equipment engineering. Existing HW-06 covers cancellation escalation, and EXEC-05 covers uncertain outcomes; the new requirement makes cleanup evidence and obligations explicit.

## Parallel articles and shared resources

NI documents coordination primitives for parallel test activity and instrument sharing. [S73](https://www.ni.com/en/shop/electronic-test-instrumentation/application-software-for-electronic-test-and-instrumentation-category/what-is-teststand/benefits-of-parallel-testing.html). TestForge needs two distinct capabilities if parallel testing enters scope: coordinated cohorts of articles and scheduling of shared instrument sets.

EXEC-14 requires each article to retain its own identity and results even when a chamber cycle is shared. Barrier membership and withdrawal must be defined: if one article is removed, the others cannot wait forever or inherit its missing observations. A shared action can reference several article records, but the evidence must identify which articles actually participated.

HW-13 addresses competing resource sets. Two workers acquiring the same instruments in opposite orders can deadlock. More subtly, a crashed worker may have left a supply energized even after its software lock disappears. Resource release must follow the physical-outcome policy, not merely process death. The baseline ownership fencing still applies across stations and disconnections. These capabilities remain P1 if the pilot expressly excludes concurrent article execution.

## Result processing and genuine offline evidence

NI supports on-the-fly reporting/logging rather than waiting for the end of execution. Its Offline Results Processing Utility can turn saved raw results into reports and database records later or on another computer, using profiles and configurable processing callbacks. [S02](https://knowledge.ni.com/KnowledgeArticleDetails?id=kA00Z000000P9LdSAK&l=en-US), [S03](https://www.ni.com/docs/en-US/bundle/teststand/page/teststand-offline-results-processing-utility.html).

That is relevant evidence for deferred processing, but not proof of our entire offline workflow. Database unavailability, station restart, independently authenticated QA, approved redlines and conflict reconciliation are different failure cases. The utility's processed-file tracking also does not establish transaction-level deduplication across every customized database sink.

DATA-10 keeps acquisition outcome separate from delivery state. A measured pass can coexist with a failed database upload and incomplete final closure. Conversely, a successfully generated report cannot turn a failed measurement into a pass. Required and optional sinks need explicit policy so that a failed dashboard update is not confused with lost authoritative evidence.

DATA-11 adds reproducibility to deferred processing. Record raw-input digests, processor and configuration versions, attempt history and output identities. Repeating an upload after losing its acknowledgment must not create a second logical result. Regenerating a report with a corrected template should create a distinguishable report revision while retaining raw evidence. These refine the existing transactional outbox and analysis provenance requirements.

## Verification, debugging and deployment

The Sequence Analyzer can check several kinds of TestStand project files, apply built-in and custom rules, and report potential problems before deployment. [S68](https://www.ni.com/docs/en-US/bundle/teststand/page/teststand-sequence-analyzer.html). PROC-16 adopts the preflight concept: persist the rule-set revision and findings, with explicit disposition of permitted waivers. A graph or type check will not establish safe stimulus values, but it can reject missing modules, incompatible contracts and unresolved dependencies before a fixture is touched.

NI documents detailed step execution order, including preconditions, callbacks and forced outcome modes. [S72](https://www.ni.com/docs/en-US/bundle/teststand/page/step-execution.html). SEC-11 requires engineering debug actions to remain attributable and distinguishable from normal flight evidence. An operator must not accidentally accept a forced pass as a measured pass. OPS-14 adds correlated run, worker and nested-call diagnostics so investigation remains possible when several operations interleave.

NI's deployment guidance warns that dynamic and implicit dependencies are not all found automatically. Packaging also includes configuration, framework components, drivers and runtimes, not only the test sequence. [S69](https://www.ni.com/en/support/documentation/supplemental/08/teststand-system-deployment-best-practices.html). OPS-12 therefore requires explicit dependency closure and a clean isolated-station installation check. OPS-13 extends this to platform feature differences, including unavailable result sinks. The installer must report a missing capability before admission rather than silently disabling required evidence collection.

## Browser UI, approvals and security

The TestStand API architecture separates user-facing presentation from engine behavior and permits custom interfaces. [S71](https://www.ni.com/en/support/documentation/supplemental/08/programming-with-the-teststand-api.html). This supports evaluating TestStand as a backend in a hybrid architecture. It does not establish that an arbitrary browser can directly use every native engine API, or that current operator controls provide the complete multi-user, disconnected application we need. The precise supported web-interface route remains a demonstration question; this report does not make a blanket claim that web controls are absent.

NI also states that its user manager is not an operating-system security boundary. [S70](https://www.ni.com/docs/en-US/bundle/teststand/page/managing-users.html). Our requirements for independent witnesses, digest-bound signatures, service identities and API enforcement remain necessary even if a test executive already has login and role features. A UI privilege setting cannot substitute for protecting files, keys, local endpoints and hardware ownership.

A hybrid TestForge/TestStand design would put human procedure and approval control in TestForge, with a narrowly defined engine adapter invoking approved sequences. The adapter must declare exactly which commands, retries and cleanup TestStand owns. TestForge would retain local workflow and evidence authority and reconcile later. This remains an option, not a selected implementation; dual execution state machines are a substantial integration burden.

## Recommended use of the research

Evaluate TestStand as an engine benchmark and possible integration backend, not as an automatic replacement for the whole procedure lifecycle. Run the [focused evaluation cases](TESTSTAND_EVALUATION.md), using a pinned release and a representative instrument stack. Compare the same workload with the open-engine candidates already in the market study.

The Windows trial path is recorded in S29. Do not assume its duration or license covers production stations, unattended CI, offline processing on another host or Linux deployment. Obtain a scoped quote and terms for the exact topology; this study is not licensing advice. No trial was activated or vendor contacted.

The immediate implementation lesson is to build a small, inspectable execution kernel with explicit lifecycle, workers, durable evidence and recovery rules. Add richer sequencing only after those contracts can be demonstrated on a simulator and a non-flight fixture. The proposed additions improve the framework definition; they are not claims of a qualified runtime.
