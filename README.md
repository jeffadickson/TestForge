# TestForge

A proposed browser-based framework for controlled flight-hardware testing: manual procedures, Python automation, instrument integration, operator/QA sign-offs, redlines, durable local evidence and later synchronization.

**Status: research and requirements baseline. No TestForge runtime is implemented or qualified.**

## Start here

- [In-depth market research and build-versus-buy assessment](docs/research/MARKET_RESEARCH.md)
- [122 proposed requirements and acceptance checks](docs/requirements/REQUIREMENTS.md)
- [Architecture and execution/reconciliation boundaries](docs/architecture/ARCHITECTURE.md)
- [Vendor and engine evaluation plan](docs/research/EVALUATION_PLAN.md)
- [Implementation and research backlog](docs/BACKLOG.md)
- [61-entry source register](docs/research/SOURCES.md)
- [COSMOS repository inspection](docs/research/COSMOS_INSPECTION.md)
- [Historical Loom v0.12 inspection](docs/research/LOOM_V0.12_INSPECTION.md)

- [Epsilon3 / 2.0 deep dive and requirements rationale](docs/research/EPSILON3_DEEP_DIVE.md)
- [Epsilon3 evaluation script: 18 additional scenarios](docs/research/EPSILON3_EVALUATION.md)

## Current direction

Evaluate Epsilon3 and Nominal as commercial benchmarks; TestStand and COSMOS as automation/operations references; OpenTAP and OpenHTF as reusable execution engines. Central framework selection remains open. Browser UI, local-first evidence and separate execution/analysis closure are architectural proposals with explicit acceptance gates.

The Epsilon3 deep dive adds 26 traceable requirements to the original 96 and distinguishes documented features from unverified offline/recovery behavior.

The expanded market assessment adds Nominal to the original shortlist. A claim that offline edge test execution is absent from the market would be incorrect. The intended distinction is inspectable evidence, recovery, approval and integration behavior.

## Preserved baseline

The original [Word specification](docs/archive/Flight_Hardware_Test_Framework_v0.1.docx) and [readable transcription](docs/archive/BASELINE_V0.1.md) preserve the first 96-requirement baseline, architecture, 18 acceptance campaigns and delivery gates. The newer market assessment supersedes its shortlist, not its history.

`docs/requirements/requirements.json` is the editable requirements catalog. The Markdown view is generated from it:

```sh
python3 tools/render_requirements.py
python3 tools/check_docs.py
```

These scripts use the Python standard library. Windows users can use `py -3` in place of `python3`. No hardware, Docker or vendor account is needed to read or validate these documents.

The optional historical Word generator requires `python-docx` and writes only to ignored `build/baseline-v0.1/`. It regenerates the old baseline from its historical embedded data; it is not the current requirements editor. The original delivered Word file is retained byte-for-byte. See [documentation maintenance](docs/MAINTENANCE.md).

## Scope and ownership

This repository contains our research and proposed design, not copies of third-party application source, vendor container images, credentials, calibration databases or actual flight records. Referenced products retain their own licenses. TestForge's distribution license has not yet been selected.
