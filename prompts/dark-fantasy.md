# Dark Fantasy / 暗黑奇幻

> Category: visual style · Free sample from the AIWave cinematic prompt library ·
> Draft example. The author-reported single run has no public output artifact.

## English prompt

```
dark fantasy style, low-key desaturated cold-grey palette, single-source candlelight or moonlight chiaroscuro, gothic pointed arches and thorn motifs, crushed blacks retaining readable silhouettes, blood-red or spectral blue as only accents, floating dust and fog particles, high-contrast subject at focal center, oppressive and mysterious
```

## 中文提示词

```
暗黑奇幻风格，低明度冷灰主调，单一光源烛火或月光切割明暗，哥特式尖拱与荆棘纹样装饰，暗部压黑但保留轮廓可读，血红或幽蓝仅作点缀色，雾气与尘埃颗粒漂浮，画面中心留出高对比主体，压迫感与神秘感并存
```

## Negative prompt

```
明亮欢快, 糖果高饱和, 雾糊成一片, 纯黑无细节, 变形手指, 面部扭曲, 文字水印, 多余肢体
```

## How to use

Use the English prompt as a starting point, then add your scene details. The negative prompt above is optional text guidance; the request below does not send it as a separate API field. Its effect has not been isolated in a controlled comparison.

## Evidence status

- **Model:** `kling-video-o1` (via aiwave.live)
- **Date:** 2026-11-01
- **Author-reported runs:** N=1. The original clip, request parameters and task receipt are not included here, so this run cannot be independently checked.
- **Unverified:** output quality, leading-token weighting, and whether the negative prompt prevents specific artifacts. No controlled comparison is supplied.

## Reproduce

```bash
export AIWAVE_API_KEY="your_key"   # use your own key; check group eligibility and current price first
curl -sS https://aiwave.live/v1/video/generations \
  -H "Authorization: Bearer $AIWAVE_API_KEY" -H "Content-Type: application/json" \
  --data-binary @- <<'JSON'
{"model":"kling-video-o1","prompt":"dark fantasy style, low-key desaturated cold-grey palette, single-source candlelight or moonlight chiaroscuro, gothic pointed arches and thorn motifs, crushed blacks retaining readable silhouettes, blood-red or spectral blue as only accents, floating dust and fog particles, high-contrast subject at focal center, oppressive and mysterious"}
JSON
# Save the returned task ID. Poll GET /v1/video/generations/<task_id> until a terminal state.
# If submission times out, inspect task status and usage before submitting again; a second POST may create a second paid job.
```
