#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fairy Floss Theme — vector logo candidates (SVG rendered by headless Chromium).

Every mark carries a gradient fill, a soft drop shadow and highlight sparkles so
it reads as a designed icon rather than flat clip-art. The palette is very pale,
so the fluff uses slightly deepened pink/lavender tones (still the same hues) and
the ink colour for sticks and details.

Playwright screenshots each SVG cell with omit_background=True (true
transparency); PIL only composes the contact sheets, the inline strip and the
official logo/logo.png exported from SELECTED.

Colours come from manifest.json. Change SELECTED and re-run; never hand-copy PNGs.
"""
import json
import math
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))                      # relative paths only (non-ASCII path safety)

SIZE = 128
CELL = 512
PREVIEW = 256
SELECTED = "05"
CAND_DIR = Path("logo/candidates")
LOGO_OUT = Path("logo/logo.png")

with open("manifest.json", "r", encoding="utf-8") as f:
    _m = json.load(f)
_C, _P = _m["theme"]["colors"], _m["theme"]["properties"]


def hx(vals):
    return "#%02X%02X%02X" % tuple(vals)


PINK = hx(_C["frame"])                             # #F7DCE8
LAV = hx(_C["toolbar"])                            # #E8CBF0
CREAM = hx(_C["ntp_background"])                   # #F7EFE4
BLUE = hx(_C["button_background"])                 # #A8CDEC
GREEN = hx(_C["button_background_secondary"])      # #BEE3BC
LINK = hx(_C["ntp_link"])                          # #3A6F9E
INK = hx(_C["ntp_text"])                           # #22303A

# deepened takes on the two signature pastels, so the mark survives a white page
DEEP_PINK = "#E98FBE"
DEEP_LAV = "#B98EDC"

SHADOW = """
  <filter id="ds" x="-35%%" y="-35%%" width="170%%" height="170%%">
    <feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="%s" flood-opacity=".18"/>
  </filter>""" % INK


def svg_open(body, defs=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 256 256">%s%s</svg>' % (CELL, CELL, defs, body))


def spiral_path(cx, cy, r0, r1, turns, steps=300):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        th = 2 * math.pi * turns * t
        r = r0 + (r1 - r0) * t
        pts.append("%.2f %.2f" % (cx + r * math.cos(th), cy - r * math.sin(th)))
    return "M" + " L".join(pts)


def sparkle(cx, cy, r, fill, opacity=".95"):
    return ('<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z" fill="%s" fill-opacity="%s"/>'
            % (cx, cy - r, cx + r * 0.30, cy - r * 0.30, cx + r, cy,
               cx + r * 0.30, cy + r * 0.30, fill, opacity))


def sparkle4(cx, cy, r, fill, opacity=".95"):
    """Four-point sparkle."""
    return ('<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f Q%.1f %.1f %.1f %.1f '
            'Q%.1f %.1f %.1f %.1f Q%.1f %.1f %.1f %.1f Z" fill="%s" fill-opacity="%s"/>'
            % (cx, cy - r, cx + r * 0.18, cy - r * 0.18, cx + r, cy,
               cx + r * 0.18, cy + r * 0.18, cx, cy + r,
               cx - r * 0.18, cy + r * 0.18, cx - r, cy,
               cx - r * 0.18, cy - r * 0.18, cx, cy - r, fill, opacity))


CLOUD = """
<circle cx="92" cy="140" r="33"/>
<circle cx="128" cy="120" r="44"/>
<circle cx="166" cy="140" r="33"/>
<rect x="92" y="133" width="74" height="40" rx="20"/>"""

# ------------------------------------------------------------------ candidates
SVG_01 = svg_open("""
<defs>
  <linearGradient id="cf1" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="M128 172 V220" stroke="%s" stroke-width="9" stroke-linecap="round"/>
<g fill="url(#cf1)" filter="url(#ds)">%s</g>
<ellipse cx="106" cy="112" rx="20" ry="13" fill="#FFFFFF" opacity=".42"/>
%s
%s
""" % (DEEP_PINK, DEEP_LAV, SHADOW, INK, CLOUD,
       sparkle4(196, 96, 13, "#FFFFFF", ".85"),
       sparkle4(64, 108, 9, "#FFFFFF", ".7")))

SVG_02 = svg_open("""
<defs>
  <linearGradient id="cn2" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  <linearGradient id="fl2" x1="0" y1="0" x2="0.7" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="M96 176 L160 176 L128 232 Z" fill="url(#cn2)"/>
<g fill="url(#fl2)" filter="url(#ds)">%s</g>
<ellipse cx="104" cy="112" rx="18" ry="11" fill="#FFFFFF" opacity=".45"/>
%s
""" % (BLUE, LINK, DEEP_PINK, DEEP_LAV, SHADOW,
       CLOUD.replace('cy="120"', 'cy="122"'),
       sparkle4(190, 98, 12, "#FFFFFF", ".8")))

SVG_03 = svg_open("""
<defs>
  <linearGradient id="sw3" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="0.55" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="%s" fill="none" stroke="url(#sw3)" stroke-width="21" stroke-linecap="round"
      stroke-linejoin="round" filter="url(#ds)"/>
<circle cx="128" cy="128" r="15" fill="%s"/>
%s
""" % (DEEP_LAV, DEEP_PINK, LINK, SHADOW,
       spiral_path(128, 128, 22, 88, 2.05), CREAM,
       sparkle4(196, 74, 12, "%s" % DEEP_LAV, ".55")))

SVG_04 = svg_open("""
<defs>%s</defs>
<g filter="url(#ds)" fill="none" stroke-linecap="round">
  <path d="M46 158 Q128 86 210 158" stroke="%s" stroke-width="18"/>
  <path d="M58 186 Q128 124 198 186" stroke="%s" stroke-width="18"/>
  <path d="M72 212 Q128 168 184 212" stroke="%s" stroke-width="18"/>
</g>
<circle cx="128" cy="74" r="16" fill="%s"/>
""" % (SHADOW, BLUE, GREEN, DEEP_PINK, DEEP_LAV))

SVG_05 = svg_open("""
<defs>
  <linearGradient id="bd5" x1="0" y1="0" x2="0.8" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<circle cx="128" cy="128" r="102" fill="url(#bd5)"/>
<circle cx="128" cy="128" r="102" fill="none" stroke="%s" stroke-opacity=".22" stroke-width="4"/>
<g fill="%s" transform="translate(128 132) scale(0.72) translate(-128 -128)">%s</g>
%s
%s
""" % (DEEP_LAV, DEEP_PINK, SHADOW, CREAM, CREAM, CLOUD,
       sparkle4(180, 82, 12, "#FFFFFF", ".9"),
       sparkle4(76, 168, 9, "#FFFFFF", ".7")))

SVG_06 = svg_open("""
<defs>
  <linearGradient id="pf6" x1="0" y1="0" x2="0.8" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<path d="M128 178 V222" stroke="%s" stroke-width="8" stroke-linecap="round"/>
<g fill="url(#pf6)" filter="url(#ds)">
  <circle cx="104" cy="146" r="30"/>
  <circle cx="152" cy="146" r="30"/>
  <circle cx="128" cy="118" r="36"/>
  <circle cx="100" cy="118" r="24"/>
  <circle cx="156" cy="118" r="24"/>
</g>
<ellipse cx="106" cy="106" rx="16" ry="10" fill="#FFFFFF" opacity=".40"/>
%s
%s
""" % (DEEP_PINK, DEEP_LAV, SHADOW, INK,
       sparkle4(188, 96, 13, "#FFFFFF", ".85"),
       sparkle4(70, 132, 9, "#FFFFFF", ".65")))

CANDIDATES = [
    ("01", "floss-cloud", "Cotton-candy cloud on a stick — most on-name", SVG_01),
    ("02", "candy-cone", "Fluff on a cone — playful and instantly readable", SVG_02),
    ("03", "sugar-swirl", "Spun-sugar swirl — cleanest abstract mark", SVG_03),
    ("04", "pastel-arcs", "Sky, mint and pink arcs — carries the whole palette", SVG_04),
    ("05", "cloud-badge", "Pale cloud in a candy badge — strongest at 32px", SVG_05),
    ("06", "floss-puff", "Rounded fluff puff — softest silhouette", SVG_06),
]


def font(size, bold=False):
    for name in (("segoeuib.ttf", "seguisb.ttf") if bold else ("segoeui.ttf", "segoeuisl.ttf")):
        p = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def render_cells():
    cells = "".join('<div id="cell%s" style="width:%dpx;height:%dpx">%s</div>' % (num, CELL, CELL, svg)
                    for num, _n, _d, svg in CANDIDATES)
    html = ('<!doctype html><html><head><meta charset="utf-8"><style>'
            'html,body{margin:0;padding:0;background:transparent}'
            '#grid{display:flex;flex-wrap:wrap;width:%dpx}div[id^=cell]{display:block}'
            '</style></head><body><div id="grid">%s</div></body></html>' % (CELL * 3, cells))
    out = {}
    with sync_playwright() as p:
        try:
            b = p.chromium.launch()
        except Exception:
            b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": CELL * 3, "height": CELL * 2})
        pg.set_content(html)
        for num, name, _d, _svg in CANDIDATES:
            path = CAND_DIR / ("%s-%s.png" % (num, name))
            pg.locator("#cell" + num).screenshot(path=str(path), omit_background=True)
            img = Image.open(path).convert("RGBA").resize((PREVIEW, PREVIEW), Image.LANCZOS)
            img.save(path)
            bbox = img.split()[3].getbbox()
            assert bbox, "candidate %s rendered empty" % name
            assert bbox[0] > 6 and bbox[1] > 6 and bbox[2] < PREVIEW - 6 and bbox[3] < PREVIEW - 6, \
                "candidate %s touches the canvas edge: %s" % (name, bbox)
            out[num] = img
            print("candidate %s %s -> alpha bbox %s" % (num, name, bbox))
        b.close()
    return out


def contact_sheet(rendered, bg, txt, sub, path, title):
    cols, rows = 3, 2
    cw, ch = 384, 374
    gap, margin = 28, 40
    W = margin * 2 + cols * cw + (cols - 1) * gap
    H = margin * 2 + 34 + rows * ch + (rows - 1) * gap
    sheet = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(sheet)
    f_title, f_name, f_desc, f_file = font(24, True), font(21, True), font(15), font(14)
    d.text((margin, margin), title, font=f_title, fill=txt)
    y0 = margin + 34
    for i, (num, name, desc, _svg) in enumerate(CANDIDATES):
        r, c = divmod(i, cols)
        x = margin + c * (cw + gap)
        y = y0 + r * (ch + gap)
        big = rendered[num].resize((220, 220), Image.LANCZOS)
        sheet.paste(big, (x + (cw - 220) // 2, y + 14), big)
        d.text((x + 18, y + 250), "%s · %s" % (num, name), font=f_name, fill=txt)
        d.text((x + 18, y + 280), desc, font=f_desc, fill=sub)
        thumb = rendered[num].resize((32, 32), Image.LANCZOS)
        sheet.paste(thumb, (x + 18, y + 330), thumb)
        d.text((x + 60, y + 339), "%s.png  256x256" % name, font=f_file, fill=sub)
        assert y + 300 <= y + 322, "text block collides with the thumbnail row"
    sheet.save(path)
    print("saved:", path, sheet.size)


def inline_strip(rendered, path):
    n, cell, gap, margin = len(CANDIDATES), 108, 22, 30
    W = margin * 2 + n * cell + (n - 1) * gap
    H = margin * 2 + cell + 30
    strip = Image.new("RGB", (W, H), (252, 246, 250))
    d = ImageDraw.Draw(strip)
    f = font(15, True)
    for i, (num, _n, _d, _s) in enumerate(CANDIDATES):
        x = margin + i * (cell + gap)
        img = rendered[num].resize((cell, cell), Image.LANCZOS)
        strip.paste(img, (x, margin), img)
        d.text((x + cell // 2 - 8, margin + cell + 8), num, font=f, fill=(34, 48, 58))
    strip.save(path)
    print("saved:", path, strip.size)


def main():
    CAND_DIR.mkdir(parents=True, exist_ok=True)
    rendered = render_cells()
    contact_sheet(rendered, (252, 246, 250), (34, 48, 58), (130, 118, 132),
                  CAND_DIR / "contact-light.png", "Fairy Floss — vector logo candidates (light)")
    contact_sheet(rendered, (36, 30, 44), (247, 239, 228), (188, 168, 196),
                  CAND_DIR / "contact-dark.png", "Fairy Floss — vector logo candidates (dark)")
    inline_strip(rendered, CAND_DIR / "inline-strip.png")
    sel = [c for c in CANDIDATES if c[0] == SELECTED][0]
    icon = rendered[sel[0]].resize((SIZE, SIZE), Image.LANCZOS)
    icon.save(LOGO_OUT)
    print("official icon from SELECTED=%s (%s):" % (sel[0], sel[1]), LOGO_OUT, icon.size)


if __name__ == "__main__":
    main()
