# American Comic / 美漫硬派

> Category: visual style · Free sample from the AIWave cinematic prompt library ·
> Every claim below carries its evidence.

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
