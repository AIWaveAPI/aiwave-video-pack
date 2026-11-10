# American Comic / 美漫硬派

> Category: visual style · Free sample from the AIWave cinematic prompt library ·
> Draft example. The author-reported single run has no public output artifact.

## English prompt

```
American comic book style, bold ink outlines, Ben-Day dot halftone shading, four-color print saturated palette, dramatic worm's-eye perspective, exaggerated muscular anatomy and drapery linework, hard chiaroscuro, space reserved for onomatopoeia and speech balloons, visible print-screen grain
```

## 中文提示词

```
美式漫画风格，粗重墨线勾勒轮廓，本戴网点纸质感阴影，四色印刷高饱和撞色，夸张透视仰角构图，肌肉与衣褶线条张力拉满，硬朗明暗切割，画面预留拟声词与对话气泡位，印刷网纹颗粒感保留
```

## Negative prompt

```
柔和水彩, 日式大眼比例, 3D渲染感, 变形手指, 面部扭曲, 可读乱码文字, 文字水印, 多余肢体
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
{"model":"kling-video-o1","prompt":"American comic book style, bold ink outlines, Ben-Day dot halftone shading, four-color print saturated palette, dramatic worm's-eye perspective, exaggerated muscular anatomy and drapery linework, hard chiaroscuro, space reserved for onomatopoeia and speech balloons, visible print-screen grain"}
JSON
# Save the returned task ID. Poll GET /v1/video/generations/<task_id> until a terminal state.
# If submission times out, inspect task status and usage before submitting again; a second POST may create a second paid job.
```
