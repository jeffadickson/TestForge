# Evaluation plan and demonstration access

Research date: 2026-10-14. All product executions below are **not yet performed** by this study. Trials were not activated and vendors were not contacted.

## Access paths

| Candidate | Available evaluation route | What it establishes |
|---|---|---|
| Epsilon3 | [14-day trial request](https://www.epsilon3.io/trial-request) and guided demo | Access request; actual edition/features must be confirmed |
| NI TestStand | [7-day trial download](https://www.ni.com/en/support/downloads/software-products/download.teststand.html) | Windows development-system evaluation; production licensing separate |
| OpenTAP | [Downloads and SDKs](https://opentap.io/downloads) | Installable core; check each editor/plugin entitlement |
| OpenHTF | [Repository and examples](https://github.com/google/openhtf) | Developer examples, not a complete commercial procedure UI |
| COSMOS | [Local demo setup](https://docs.openc3.com/docs/getting-started/gettingstarted) | Simulated hardware after container installation; Enterprise access separate |
| Yamcs | [Spacecraft quickstart](https://github.com/yamcs/quickstart) | Runnable command/telemetry reference |
| Nominal | [Request demo](https://nominal.io/products/connect) | No time-limited self-service trial verified in this study |
| Sift | [Vendor demo](https://www.siftstack.com/) | Analysis/telemetry evaluation |
| ION | [Product/demo entry](https://www.firstresonance.io/ion) | Manufacturing workflow evaluation |

## Fair comparison protocol

Agree a representative procedure, identities, equipment simulator, raw artifact and expected review policy before any vendor demonstration. Have the same person act as operator and a different person as witness. Record version, edition, deployment topology, plugins, configuration and assistance supplied by the vendor. Use synthetic evidence; do not make an evaluation dependent on real flight records.

For every observation record: requirement IDs, setup, stimulus, expected outcome, actual outcome, evidence location, limitation, evaluator and date. Keep documentation claims separate from witnessed results. “Not demonstrated” is different from “failed.” A vendor unavailable for a trial remains unverified.

## Eighteen acceptance campaigns

These preserve the original baseline scenarios. All are proposed, not results. Group coverage indicates which requirement families a campaign exercises; it is not complete requirement-by-requirement verification closure.

| ID | Stimulus and required behavior | Families |
|---|---|---|
| V01 | Cold-start without WAN, external DNS or central identity; prepared authorized work functions | OFF, AUTH, PROC |
| V02 | Central database absent for a full run; acknowledged local evidence survives and upload failure triggers no command retry | OFF, SYNC, EXEC |
| V03 | Kill worker before dispatch, after dispatch and before outcome commit; preserve honest unknown physical outcomes | EXEC, HW, DATA |
| V04 | Interrupt station power at persistence boundaries; preserve acknowledged events and identify partial artifacts | OFF, DATA |
| V05 | Lose upload acknowledgment and resend; one central record per ID, differing payload rejected | SYNC |
| V06 | Divergent ownership or offline edits; retain both records, block second controller and unsafe merge | EXEC, SYNC, CHG |
| V07 | Calibration expires during soak, later recalled; enforce local policy and identify affected historical evidence | CAL, CLOSE |
| V08 | Revoke offline approver centrally; reconnect creates review issue without erasing original signature context | AUTH, SYNC |
| V09 | Fill disk and corrupt artifact; inhibit new work as specified and preserve incomplete status | DATA, OFF |
| V10 | Hang VISA/USB call; bounded timeout, worker isolation and approved equipment-specific safing | HW, EXEC |
| V11 | Redline limit, insert step, retest failure; preserve original observations and require affected reapproval | PROC, CHG, CLOSE |
| V12 | Finish with missing analysis or attachment; execution may end but final closure remains blocked | CLOSE, SYNC |
| V13 | Three mandatory approvers, one observer, rejection and attempted self-witness; enforce policy | AUTH, CLOSE |
| V14 | Move wall clock backward and restore backup; ordering, uncertainty and evidence completeness remain explicit | DATA, OPS |
| V15 | Seven-day proposed offline soak, target event load and large artifact transfers | OFF, OPS, SYNC |
| V16 | Export closed record and reproduce analysis on clean isolated host | DATA, CLOSE |
| V17 | API bypass, cross-origin request, package tampering and worker privilege attempts | SEC, AUTH, HW |
| V18 | Failed installation, schema migration and rollback/forward recovery | OPS, DATA |

## Questions to send with a demo request

1. Which components and actions require connectivity, including login, activation, package access and signing?
2. What is durable when the UI says saved? Provide the crash/power-loss model and test evidence.
3. What happens if hardware acts but the process dies before saving the response?
4. Can a supervisor or generic job retry inadvertently send the same command again?
5. Are signatures bound to exact content and independent identities? How is offline revocation reconciled?
6. Does a run redline modify the master? What changes invalidate existing approvals and analyses?
7. Can multiple disconnected stations diverge? Who commands the article and how is takeover fenced?
8. What proves an upload is complete, including every attachment? How are duplicates and conflicts handled?
9. Are calibration certificates, correction versions and uncertainty rules retained with each measurement?
10. What can be exported without a live subscription or service, and can another system reproduce analysis?
11. Which functions require Enterprise/add-on licenses? How are offline stations, observers and temporary QA staff priced?
12. What are the supported upgrade, backup and restore procedures over the expected program lifetime?

## Decision record template

For each hard gate record pass / fail / not demonstrated / not applicable with rationale, evidence and selected version. Only after all relevant hard gates pass should comparative scores for usability, integration effort and cost be applied. No aggregate score may conceal a failed command-authority or evidence gate.
