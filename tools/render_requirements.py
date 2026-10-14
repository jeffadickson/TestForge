"""Render the editable requirements catalog as GitHub-readable Markdown."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def render():
    requirements = json.loads((ROOT / 'docs/requirements/requirements.json').read_text())
    lines = ['# TestForge requirements baseline', '',
             '96 proposed requirements, dated 2026-10-14. None is declared implemented or verified. '
             'P0: required before a controlled flight-hardware pilot. P1: full operational scope, '
             'staged only when explicitly excluded from the pilot. Numerical targets are proposals. '
             'Generated from [requirements.json](requirements.json); edit that catalog and rerun '
             '`python3 tools/render_requirements.py`.', '',
             'See the [evaluation plan](../research/EVALUATION_PLAN.md) for combined campaigns '
             'and [architecture](../architecture/ARCHITECTURE.md) for responsibility boundaries.', '']
    previous = None
    for r in requirements:
        group = r['id'].rsplit('-', 1)[0]
        if group != previous:
            lines.extend([f"## {group} — {r['owner']}", ''])
            previous = group
        lines.extend([f"### {r['id']} — {r['title']} ({r['priority']})", '',
                      r['requirement'], '', '**Acceptance:** ' + r['acceptance'], ''])
    return '\n'.join(lines)

if __name__ == '__main__':
    (ROOT / 'docs/requirements/REQUIREMENTS.md').write_text(render())
