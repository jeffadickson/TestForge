# Maintaining the documentation

The canonical editable requirement catalog is `docs/requirements/requirements.json`. After editing it, run `python3 tools/render_requirements.py` and `python3 tools/check_docs.py`. The generated Markdown carries the same IDs, text, priorities and acceptance checks. These checks verify document consistency only; they do not execute any hardware acceptance test.

The original v0.1 Word file and its transcription are archival. Do not silently rewrite them to match later conclusions. Current market conclusions live in `docs/research/MARKET_RESEARCH.md`; new findings should identify the source and observation date. A vendor feature claim is not a witnessed test result.

`docs/research/sources.json` mirrors the source register for tooling. Keep it and `SOURCES.md` consistent. The optional `tools/rebuild_original_baseline.py` requires `python-docx` and generates historical outputs in ignored `build/baseline-v0.1/`; it intentionally preserves its old embedded requirement set. It is included for provenance, not as the current authoring system. Word pagination depends on fonts and renderer; inspect a new rendered document before distributing it.

The first commit establishes the repository index; a subsequent research commit adds the complete documentation set. Repository storage is the source of truth for this project. No external project code, user account secrets or vendor containers are vendored here.

Requirements added by the Epsilon3 and TestStand studies carry `origin`, `sources`, `related` and `basis` fields. `basis` distinguishes our derived design from vendor claims; `related` identifies the original requirements being refined. Keep these fields when editing, and preserve original stable IDs. The renderer includes the traceability fields and the checker validates their references. The current catalog contains 136 entries; the historical 96-entry baseline is intentionally unchanged.
