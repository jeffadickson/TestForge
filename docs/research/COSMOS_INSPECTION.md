# COSMOS inspection record

Date: 2026-10-14. Evidence level: source/configuration inspection only.

## Repository and revision

- Public starter: https://github.com/OpenC3/cosmos-project.git
- Inspected commit: `cd01c9bb8848f7811b46580e1074fef9ab976162`
- Enterprise starter attempted: https://repos.openc3.com/OpenC3/cosmos-enterprise-project.git
- Enterprise result: authentication requested; source not obtained. This is an access result, not evidence that an Enterprise demo is unavailable.
- Runtime result: Docker executable was unavailable in the research environment; no COSMOS service or demo was launched.

## Observed files

| File | Observation | Scope limit |
|---|---|---|
| README.md | Starter launches released containers; not full application source | No audit of application internals |
| .env | `OPENC3_TAG=7.4.1`; `OPENC3_DEMO=true` | Mutable upstream defaults, not a validated release selection |
| compose.yaml | Bucket store, time-series DB, Redis, command/telemetry API, script-runner API, operator, proxy and initialization services | Composition does not prove durability or runtime behavior |
| compose.yaml | Web ports 2900 and 2943 bound to loopback | Network exposure requires deliberate configuration |
| LICENSE.md | Builder license restrictions on hosted services and commercial distribution of changes | Full selected component terms remain authoritative |

No third-party source or configuration credentials are copied into TestForge. Source can be reviewed at the pinned [commit](https://github.com/OpenC3/cosmos-project/tree/cd01c9bb8848f7811b46580e1074fef9ab976162).

## Documented demo path

With Docker Desktop and Git installed on Windows, from a new evaluation directory:

```powershell
git clone https://github.com/OpenC3/cosmos-project.git
cd cosmos-project
.\openc3.bat run
```

Then browse to `http://localhost:2900`. Pin an agreed release before a repeatable evaluation. The documented demo includes simulated commands/telemetry, Script Runner and Test Runner examples. This recipe is documentation-derived, not a successful run in this environment. Stop with `openc3.bat stop`; cleanup removes persisted evaluation data and is not part of normal shutdown.

The install guide documents transferring saved container images and cached Python dependencies for disconnected deployment. Test separately whether every required dependency, identity service and plugin is available offline. Offline installation does not establish later reconciliation with another authoritative record.

## Highest-value next checks

1. Run the included demo and record selected image versions/digests.
2. Obtain the appropriate edition to evaluate separate named identities and role enforcement.
3. Determine whether script approval satisfies procedure-specific witness and redline needs.
4. Observe restart after command dispatch; establish whether a script restarts, resumes or remains unresolved.
5. Export raw telemetry, script revision, step context and approvals together.
6. Exercise a disconnected local campaign and clarify the supported sync topology.

Sources: [S14–S16 and S32–S34](SOURCES.md). The market assessment explains the edition/license implications.
