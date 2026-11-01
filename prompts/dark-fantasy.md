# Dark Fantasy / 暗黑奇幻

> Category: visual style · Free sample from the AIWave cinematic prompt library ·
> Every claim below carries its evidence.

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

Append the style prompt to your scene description (style first — leading tokens carry the most weight). Keep the negative prompt as-is; it filters real production failure modes.

## Validation record

- **Model:** kling-video-o1 (via aiwave.live)
- **Date:** 2026-11-01
- **Runs:** 1 (internal run; sample clips will be attached to a public
  release once the ablation matrix completes — see "Status" below)
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
