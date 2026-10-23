<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/fairy-floss-theme/main/logo/logo.png" width="128" alt="Fairy Floss Theme logo">
</p>

<h1 align="center">Fairy Floss Theme</h1>

<p align="center">
  A soft pastel Chrome theme in candy pink, lavender, sky blue and mint — sweet, airy, and easy on the eyes.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/manifest-v3-f7dce8" alt="Manifest V3">
  <img src="https://img.shields.io/badge/version-1.0.0-e8cbf0" alt="Version 1.0.0">
  <img src="https://img.shields.io/badge/chrome-light-a8cdec" alt="Light chrome">
  <img src="https://img.shields.io/badge/license-non--commercial-22303a" alt="Non-commercial license">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/fairy-floss-theme/main/store-assets/promo/1400x560.png" alt="Fairy Floss Theme promo" width="700">
</p>

## Overview

Fairy Floss pairs a candy-pink frame with a lavender toolbar, then opens onto a creamy New Tab Page with a warm gold Google logo that matches the mood. Deep blue-grey ink keeps every tab, bookmark and toolbar icon readable on the light chrome, links take a clear sky blue, and a single-row shortcut layout keeps the New Tab Page clean.

It is the sweetest theme in the set: every surface is pale, and all contrast comes from the ink rather than from a dark frame.

## Design Concept

The source palette is four pastels plus two near-neutrals — sky blue, mint, cream, shell white, blush pink and lilac. Because all six sit at a similar lightness, using them as-is would leave nothing to separate the chrome from the page. The theme therefore assigns them by *role*: pink and lavender build the chrome, cream carries the page, blue and mint become buttons, and a single deep blue-grey ink does all the reading work.

| Color | Hex | RGB | Role |
|---|---|---|---|
| Shell | `#FFFDF6` | 255, 253, 246 | Omnibox (near-white) |
| Cream | `#F7EFE4` | 247, 239, 228 | New Tab background |
| Blush | `#F7DCE8` | 247, 220, 232 | Frame |
| Lilac | `#E8CBF0` | 232, 203, 240 | Toolbar / New Tab header |
| Sky | `#A8CDEC` | 168, 205, 236 | Buttons |
| Mint | `#BEE3BC` | 190, 227, 188 | Secondary buttons |
| Deep Ink | `#22303A` | 34, 48, 58 | Tab, bookmark and New Tab text |
| Sky Link | `#3A6F9E` | 58, 111, 158 | New Tab links |

## Features

- Pure color, no wallpaper — fast and distraction-free
- Soft pastel palette: blush, lilac, sky and mint in one gentle family
- Light chrome with deep ink — readable without a dark frame
- Tab text, bookmark text and toolbar icons all share the same ink
- Single-row shortcut row and a color-matched Google logo for a clean New Tab Page
- No configuration needed — install and enjoy

## Screenshots

| Browser | Palette |
|:-:|:-:|
| <img src="https://raw.githubusercontent.com/vaxicy/fairy-floss-theme/main/store-assets/screenshots/en/screenshot-1-browser.png" width="420" alt="Fairy Floss New Tab"> | <img src="https://raw.githubusercontent.com/vaxicy/fairy-floss-theme/main/store-assets/screenshots/en/screenshot-2-palette.png" width="420" alt="Fairy Floss palette"> |

## Installation

### Load unpacked (development)

1. Download or clone this repository.
2. Open `chrome://extensions` in Chrome.
3. Enable **Developer mode** in the top right.
4. Click **Load unpacked** and select this folder (`fairy-floss-theme`).
5. The theme is active immediately.

### Package for the Chrome Web Store

```
chrome://extensions → Pack extension → select this folder → fairy-floss-theme.zip
```

Upload the resulting `.zip` to the [Chrome Web Store developer dashboard](https://chrome.google.com/webstore/devconsole).

## Store listing copy

Ready to paste into the store listing (also kept in `store-assets/store-description.txt`):

> Fairy Floss is a soft pastel Chrome theme: a candy-pink frame, a lavender toolbar, and a creamy New Tab Page with a warm gold Google logo that matches the mood. Deep blue-grey ink keeps every tab, bookmark and toolbar icon readable on the light chrome. Solid colors only, no wallpaper — sweet, airy, and easy on the eyes.

## Project structure

| File | Purpose |
|---|---|
| `manifest.json` | Theme definition (single-file, inlined `theme` field) |
| `logo/logo.png` | 128×128 store icon (transparent background) |
| `store-assets/promo/440x280.png` | Small promo tile |
| `store-assets/promo/1400x560.png` | Marquee promo tile |
| `store-assets/screenshots/en/screenshot-1-browser.png` | Browser mockup screenshot (1280×800) |
| `store-assets/screenshots/en/screenshot-2-palette.png` | Palette introduction screenshot (1280×800) |
| `store-assets/store-description.txt` | Store listing description |
| `scripts/generate-logo-vector.py` | Render all SVG logo candidates with headless Chromium, build contact sheets, export `logo/logo.png` from `SELECTED` |
| `scripts/generate-screenshot-headless.py` | Regenerate the browser mockup via Playwright |
| `scripts/generate-screenshot-2-palette.py` | Regenerate the palette screenshot |
| `scripts/generate-promo.py` | Regenerate both promo tiles |
| `logo/candidates/` | Candidate previews and light/dark contact sheets |
| `LICENSE` | Non-Commercial License (English / 中文) |

## Regenerating assets

Every asset is code-generated, so nothing here is hand-drawn or hand-copied:

```bash
py -3 scripts/generate-logo-vector.py         # candidates + contact sheets + logo/logo.png
py -3 scripts/generate-screenshot-headless.py # store screenshot 1 (browser mockup)
py -3 scripts/generate-screenshot-2-palette.py # store screenshot 2 (palette)
py -3 scripts/generate-promo.py               # promo 440x280 + 1400x560
```

To ship a different icon candidate, change `SELECTED` at the top of `generate-logo-vector.py` and re-run, then re-run the three asset scripts so the promo and screenshots pick up the new logo.

## License

Fairy Floss Theme is released under the Non-Commercial License. See `LICENSE` for full text (English / 中文).
