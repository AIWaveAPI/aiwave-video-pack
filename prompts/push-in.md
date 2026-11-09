# Push In / 推镜头

> Category: camera move · Free sample from the AIWave cinematic prompt library ·
> Draft example. The author-reported single run has no public output artifact.

## English prompt

```
camera language: slow dolly-in from full shot to chest-level close-up at even speed, background compressing into bokeh as the emotion builds, reserved for brewing emotion and moments of resolve
```

## 中文提示词

```
镜头语言：缓慢推近（slow dolly in），从人物全景匀速推至胸部特写，推速配合情绪渐强，背景随推近逐渐压缩虚化，用于情绪酝酿与下定决心的人物内在时刻
```

## Negative prompt

```
推镜抖动, 推速忽快忽慢, 焦点漂移, 画面畸变, 面部扭曲, 变形手指, 文字水印
```

## How to use

Use the English prompt as a starting point for a camera-move request. Whether placing it first changes the output requires repeated controlled comparisons; none are supplied here.

## Evidence status

- **Model:** `kling-video-o1` (via aiwave.live)
- **Date:** 2026-11-01
- **Author-reported runs:** N=1. The original clip, request parameters and task receipt are not included here, so this run cannot be independently checked.
- **Unverified:** output quality and the claim that earlier prompt position causes a more reliable camera move. No controlled comparison is supplied.

## Reproduce

```bash
export AIWAVE_API_KEY="your_key"   # use your own key; check group eligibility and current price first
curl -sS https://aiwave.live/v1/video/generations \
  -H "Authorization: Bearer $AIWAVE_API_KEY" -H "Content-Type: application/json" \
  --data-binary @- <<'JSON'
{"model":"kling-video-o1","prompt":"camera language: slow dolly-in from full shot to chest-level close-up at even speed, background compressing into bokeh as the emotion builds, reserved for brewing emotion and moments of resolve"}
JSON
# Save the returned task ID. Poll GET /v1/video/generations/<task_id> until a terminal state.
# If submission times out, inspect task status and usage before submitting again; a second POST may create a second paid job.
```
