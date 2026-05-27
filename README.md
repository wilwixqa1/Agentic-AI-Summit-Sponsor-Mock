# Agentic AI Summit 2026 — Sponsor Section Mockups

Three design options for the sponsor section of the summit website.

**Stack:** FastAPI + Jinja2, deployed on Railway

## Options

- **Option A — Conference Classic**: PyTorch Conference style. Tiered rows, bordered cards, horizontal rule dividers.
- **Option B — Academic Minimal**: NeurIPS/ICML style. Ultra-compact, borderless logos, subtle tier labels.
- **Option C — Dark Modern**: a16z Speedrun style. Dark background, glowing tier badges, frosted glass cards.

## Local Development

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Sponsor Data

Sponsor list is maintained in `main.py` and passed to all templates via Jinja2 context.
