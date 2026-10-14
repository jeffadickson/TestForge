"""Check research-document consistency; does not test a TestForge runtime."""
import json
import re
from pathlib import Path
from render_requirements import render

ROOT = Path(__file__).resolve().parents[1]
requirements = json.loads((ROOT / 'docs/requirements/requirements.json').read_text())
sources = json.loads((ROOT / 'docs/research/sources.json').read_text())
assert len(requirements) == 96
ids = {r['id'] for r in requirements}
assert len(ids) == 96
for r in requirements:
    assert r['priority'] in ('P0', 'P1')
    assert all(r.get(k) for k in ('id', 'title', 'owner', 'requirement', 'acceptance'))
assert (ROOT / 'docs/requirements/REQUIREMENTS.md').read_text() == render(), 'Regenerate requirements Markdown'
source_ids = {s['id'] for s in sources}
assert len(source_ids) == len(sources)
register = (ROOT / 'docs/research/SOURCES.md').read_text()
for s in sources:
    assert f"## {s['id']} —" in register
    assert s['url'] in register
errors = []
for file in ROOT.rglob('*.md'):
    if '.git' in file.parts:
        continue
    text = file.read_text()
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if target.startswith(('https:', 'http:', '#', 'mailto:')):
            continue
        path = target.split('#')[0]
        if not (file.parent / path).exists():
            errors.append(f'{file.relative_to(ROOT)}: broken local link {target}')
    for source_id in re.findall(r'\bS\d{2}\b', text):
        if source_id not in source_ids:
            errors.append(f'{file.relative_to(ROOT)}: unknown source {source_id}')
assert not errors, '\n'.join(errors)
print(f'PASS: {len(requirements)} unique requirements, {len(sources)} sources, generated view and local links')
