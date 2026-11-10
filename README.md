<div align="center">

# AIWave Video Pack

**Four copyable video prompt examples with explicit evidence limits.**

[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE)

</div>

---

These are starting points for four visual directions. Each card includes an
English prompt, a Chinese version, optional negative text and a literal JSON
request. The author reports one internal run per card on 2026-11-01, but the
clips and task receipts are not public. Treat output quality and prompt-order
effects as **unverified**, and compare results with your own controlled runs.
Video submissions may be billable; check your group eligibility and current
rate before sending a request.

## The modules

| File | Starting direction | Evidence |
|---|---|---|
| [`prompts/cinema.md`](prompts/cinema.md) | Cinematic film look | Author-reported N=1; no public clip |
| [`prompts/us-comic.md`](prompts/us-comic.md) | American comic | Author-reported N=1; no public clip |
| [`prompts/dark-fantasy.md`](prompts/dark-fantasy.md) | Dark fantasy | Author-reported N=1; no public clip |
| [`prompts/push-in.md`](prompts/push-in.md) | Push-in camera move | Author-reported N=1; no public clip |

The examples use `kling-video-o1`; the live catalog lists it for paid groups
at this check, but catalog membership alone does not prove current route
health. Replace the model only after checking its supported endpoint and your
account's eligibility.

## Check the current catalog before a paid test

The public rate card is machine-readable and can change. Check the exact ID
and group list rather than relying on an old screenshot:

```bash
curl -sS https://aiwave.live/api/pricing | python3 -c \
  "import sys,json; d=json.load(sys.stdin); print(next(({'model_name':m['model_name'],'enable_groups':m.get('enable_groups'),'quota_type':m.get('quota_type')} for m in d['data'] if m.get('model_name')=='kling-video-o1'), 'not listed'))"
```

Each prompt card has a syntactically checked curl payload. The commands send
new video jobs; they do **not** reproduce a deterministic result or the
author's private run. Save the task ID and inspect status and usage before
retrying an uncertain submission.

## Verify the examples locally

`python3 -m unittest discover -s tests -v` checks that all four curl payloads
are valid JSON and carry the exact English prompt shown on their cards. It
does not call a paid video endpoint or verify generation quality.

## License

Prompts are marked [CC BY-NC 4.0](LICENSE). Read the
[Creative Commons terms](https://creativecommons.org/licenses/by-nc/4.0/)
before reuse; the NonCommercial restriction applies to the licensed material.
