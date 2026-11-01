# Push In / 推镜头

> Category: camera move · Free sample from the AIWave cinematic prompt library ·
> Every claim below carries its evidence.

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

Put the camera move at the very front of your prompt — leading tokens carry the most weight on Kling-class models.

## Validation record

- **Model:** kling-video-o1 (via aiwave.live)
- **Date:** 2026-11-01
- **Runs:** 1 (see style modules for the ablation schedule)
- **Observed:** camera-move tokens at the front of the prompt produce the
  move; buried mid-prompt they often drop out — leading-position weighting
- **Status:** single-run validation (N=1), ablation in progress
- **Known failure modes:** rapid moves (crash-zoom class) can smear on
  5s clips; combine with pacing, not speed.

## Reproduce

```bash
curl -s https://aiwave.live/v1/video/generations \
  -H "Authorization: Bearer $AIWAVE_API_KEY" -H "Content-Type: application/json" \
  -d '{{"model":"kling-video-o1","prompt":"<camera move> + <scene> + <style>"}}'
```
