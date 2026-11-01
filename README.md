<div align="center">

# AIWave Video Pack

**Three battle-tested cinematic prompts + one camera move. Free.**

[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE)
[![Video routes](https://img.shields.io/badge/render-Kling%20%C2%B7%20Seedance%20%C2%B7%20Hailuo%20%C2%B7%20Wan%20%C2%B7%20Vidu-purple)](https://aiwave.live/models)

</div>

---

Free sample from **AIWave's cinematic prompt library**. These are not
generated filler — every entry was validated on real video productions
against Kling-class models, and each negative prompt filters failure modes
we actually hit (warped hands, watermarks, cartoon drift).

Works with **any** video model. Renders nicely through
[AIWave](https://aiwave.live/register) if you want one key for all five
video vendors.

## The prompts

| File | What it does |
|---|---|
| [`prompts/cinema.md`](prompts/cinema.md) | Cinematic film look — 35mm color science, creamy bokeh, 2.39:1 widescreen |
| [`prompts/us-comic.md`](prompts/us-comic.md) | American comic — Ben-Day dots, four-color print, worm's-eye drama |
| [`prompts/dark-fantasy.md`](prompts/dark-fantasy.md) | Dark fantasy — candlelight chiaroscuro, gothic silhouettes, blood-red accents |
| [`prompts/push-in.md`](prompts/push-in.md) | Push-in camera move — the highest-weight leading token for slow reveals |

Each file: English prompt + 中文提示词 + negative prompt + usage notes.

## Try one in 30 seconds

```bash
export AIWAVE_API_KEY="your_key"   # https://aiwave.live/register
curl https://aiwave.live/v1/video/generations \
  -H "Authorization: Bearer $AIWAVE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"kling-v2-6","prompt":"<paste a style prompt here> + your scene"}'
```

Video routes need a paid account group (from $5 — that also unlocks all 128
text models at VIP rates). Full quickstart:
[aiwave-quickstart](https://github.com/AIWaveAPI/aiwave-quickstart).

## What's NOT in this pack

This is 4 entries out of a **83-entry library with 10 categories** —
including Eastern aesthetics (ink-wash, xianxia, ancient landscape),
a 12-entry micro-expression system for close-ups, pacing modules, and a
storyboard engine that keeps characters consistent across shots.

That system powers **AIWave Canvas**, our cinematic creation platform —
coming soon. Watch this org.

## License

Prompts: [CC BY-NC 4.0](LICENSE) — use them freely in your own videos;
commercial redistribution of the pack itself is not allowed.
