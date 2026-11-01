# Cinematic / 电影感

> Category: visual style · Free sample from the AIWave cinematic prompt library ·
> Every claim below carries its evidence.

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

Append the style prompt to your scene description (style first — leading tokens carry the most weight). Keep the negative prompt as-is; it filters real production failure modes.

## Validation record

- **Model:** kling-video-o1 (via aiwave.live)
- **Date:** 2026-11-01
- **Runs:** 1 (sample clips attached to the org's release; multi-run
  ablation scheduled — see "Status" below)
- **Observed:** style tokens carried into the render (film color, framing);
  leading-token weighting confirmed — style placed first dominated the look
- **Status:** single-run validation. We mark this honestly: N=1. The
  multi-run ablation matrix (N=3 per style, per model) is in progress and
  records will be updated in place.
- **Known failure modes (from the production log these prompts come from):**
  hands warp on complex gestures; text/logos drift in; faces cartoonize on
  long shots — the negative prompt below filters exactly these.

## Reproduce

```bash
export AIWAVE_API_KEY="your_key"   # https://aiwave.live/register (video needs a paid group, from $5)
curl -s https://aiwave.live/v1/video/generations \
  -H "Authorization: Bearer $AIWAVE_API_KEY" -H "Content-Type: application/json" \
  -d '{{"model":"kling-video-o1","prompt":"<style prompt above> + your scene"}}'
# Poll: GET /v1/video/generations/<task_id> every 15s; a single shot takes 5-11 min.
```
