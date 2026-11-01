<div align="center">

# AIWave Video Pack

**Validated cinematic prompt modules — every claim carries its evidence.**

[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE)

</div>

---

Free sample from **AIWave's cinematic prompt library** (83 entries, 10
categories — the rest powers our upcoming creation platform).

This pack is not a list of "prompts that sound good". Every module ships
with a **validation record**: which model, which date, how many runs, what we
observed, what fails, and a copy-paste command so **you can verify every
claim yourself**.

## The modules

| File | What it does | Validated on |
|---|---|---|
| [`prompts/cinema.md`](prompts/cinema.md) | Cinematic film look — 35mm color science, creamy bokeh, 2.39:1 | see record |
| [`prompts/us-comic.md`](prompts/us-comic.md) | American comic — Ben-Day dots, four-color print, worm's-eye | see record |
| [`prompts/dark-fantasy.md`](prompts/dark-fantasy.md) | Dark fantasy — candlelight chiaroscuro, gothic silhouettes | see record |
| [`prompts/push-in.md`](prompts/push-in.md) | Push-in camera move — leading-token technique | see record |

Each file contains: English prompt + 中文提示词 + negative prompt +
usage notes + **validation record** (model, date, N, observed effects,
known failure modes) + a reproduction command.

## Verify any claim in 30 seconds

Every number in this org traces to a public endpoint. For example, the
public rate card:

```bash
curl -s https://aiwave.live/api/pricing | python3 -c \
  "import sys,json; d=json.load(sys.stdin); ms=d['models'] if 'models' in d else d['data']; print(len(ms),'routes')"
# → 97 routes (verified 2026-11-01, pricing_version 5a90f2b8...)
```

Same idea for the prompt modules: each one lists the exact curl that
reproduces its validation run. If your result differs, open a
[Discussion](https://github.com/AIWaveAPI/aiwave-video-pack/discussions) —
that's how the records stay honest.

## What's NOT in this pack

The full library includes Eastern aesthetics (ink-wash, xianxia, ancient
landscape), a 12-entry micro-expression system for close-ups, pacing
modules, and a storyboard engine that keeps characters consistent across
shots (verified by frame-comparison on real multi-shot generations).

That system powers **AIWave Canvas** — coming soon. Watch this org.

## License

Prompts: [CC BY-NC 4.0](LICENSE) — use freely in your own videos;
commercial redistribution of the pack itself is not allowed.
