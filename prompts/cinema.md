# Cinematic / 电影感

> Category: visual style · Free sample from the AIWave cinematic prompt library ·
> Draft example. The author-reported single run has no public output artifact.

## English prompt

```
cinematic film look, 35mm film color science, shallow depth of field with creamy bokeh, soft volumetric god rays raking across frame, low-key lighting with lifted shadows, natural skin tones, restrained horizontal lens flare, 2.39:1 widescreen composition with breathing room, subject on thirds, foreground occlusion for depth
```

## 中文提示词

```
电影级画面质感，35mm胶片色调，浅景深背景奶油虚化，柔和体积光斜穿画面，暗部保留细节的低调布光，肤色还原自然，克制的水平蓝色光晕，2.39:1宽画幅构图留呼吸感，主体置于三分线，前景遮挡物制造纵深层次
```

## Negative prompt

```
低清晰度, 模糊, 噪点明显, 过曝死白, 变形手指, 面部扭曲, 文字水印, logo, 多余肢体, 画面撕裂
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
{"model":"kling-video-o1","prompt":"cinematic film look, 35mm film color science, shallow depth of field with creamy bokeh, soft volumetric god rays raking across frame, low-key lighting with lifted shadows, natural skin tones, restrained horizontal lens flare, 2.39:1 widescreen composition with breathing room, subject on thirds, foreground occlusion for depth"}
JSON
# Save the returned task ID. Poll GET /v1/video/generations/<task_id> until a terminal state.
# If submission times out, inspect task status and usage before submitting again; a second POST may create a second paid job.
```
