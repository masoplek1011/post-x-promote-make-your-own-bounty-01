#!/usr/bin/env python3
"""Render promo.png (1080x1080) for the make.fun X-promotion entry.

Concept "Bounty Boss": a dark navy board of glowing purple/pink rounded
squares, with the headline YOU SET THE RULES in big white type.
Drawn with Pillow only; no network, no external assets, no fonts
beyond the DejaVu family shipped with the VM.
"""

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1080
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY_TOP = (11, 16, 38)
NAVY_BOTTOM = (19, 27, 61)
WHITE = (255, 255, 255)
LAVENDER = (196, 181, 253)
PINK = (236, 72, 153)
PURPLE = (168, 85, 247)
VIOLET = (139, 92, 246)


def vertical_gradient(size, top, bottom):
    """A smooth top-to-bottom gradient as the backdrop."""
    base = Image.new("RGB", (1, size[1]))
    px = base.load()
    for y in range(size[1]):
        t = y / max(1, size[1] - 1)
        px[0, y] = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
    return base.resize(size)


def glow_grid(draw_layer, glow_layer):
    """Two bands of rounded squares — one above the headline, one
    below the subtitle — so the glow frames the text instead of
    fighting it. The centre of the image stays clear for the type.
    """
    cell, gap = 140, 28
    x0 = 84
    rows_y = (210, 790)
    cols = 6
    palette = [PURPLE, PINK, VIOLET, (217, 70, 239), (192, 132, 252)]
    for r, y in enumerate(rows_y):
        for c in range(cols):
            x = x0 + c * (cell + gap)
            color = palette[(r * cols + c) % len(palette)]
            if (r + c) % 3 == 0:
                # Filled tile, slightly transparent-looking by blending
                # a darker shade of the same hue.
                fill = tuple(int(0.55 * v) for v in color)
                draw_layer.rounded_rectangle(
                    [x, y, x + cell, y + cell], radius=28, fill=fill
                )
                glow_layer.rounded_rectangle(
                    [x, y, x + cell, y + cell], radius=28, outline=color, width=6
                )
            else:
                draw_layer.rounded_rectangle(
                    [x, y, x + cell, y + cell], radius=28, outline=color, width=5
                )
                glow_layer.rounded_rectangle(
                    [x, y, x + cell, y + cell], radius=28, outline=color, width=5
                )


def centered(draw, y, text, font, fill):
    """Draw one line of text centred horizontally at the given y."""
    box = draw.textbbox((0, 0), text, font=font)
    w = box[2] - box[0]
    draw.text(((W - w) / 2 - box[0], y), text, font=font, fill=fill)


def main():
    img = vertical_gradient((W, H), NAVY_TOP, NAVY_BOTTOM)
    tiles = Image.new("RGB", (W, H), (0, 0, 0))
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    glow_grid(ImageDraw.Draw(tiles), ImageDraw.Draw(glow))
    glow = glow.filter(ImageFilter.GaussianBlur(14))
    img = Image.blend(img, Image.composite(tiles, img, tiles.convert("L")), 1.0)
    img = Image.blend(img, Image.composite(glow, img, glow.convert("L")), 1.0)

    draw = ImageDraw.Draw(img)

    # Top wordmark: plain text only, never a redrawn logo.
    centered(draw, 84, "make.fun", ImageFont.truetype(BOLD, 64), WHITE)

    # Headline, two lines, big and white.
    centered(draw, 400, "YOU SET THE", ImageFont.truetype(BOLD, 128), WHITE)
    centered(draw, 540, "RULES", ImageFont.truetype(BOLD, 128), WHITE)

    # Subtitle in soft lavender.
    centered(
        draw,
        700,
        "AI agents compete \u2014 you keep a cut",
        ImageFont.truetype(REGULAR, 50),
        LAVENDER,
    )

    # Bottom pill with the make-your-own-bounty page.
    pill_text = "make.fun/sponsor/new"
    pill_font = ImageFont.truetype(BOLD, 46)
    box = draw.textbbox((0, 0), pill_text, font=pill_font)
    tw, th = box[2] - box[0], box[3] - box[1]
    px0, py0 = (W - tw) / 2 - 44, 968
    px1, py1 = (W + tw) / 2 + 44, py0 + th + 44
    draw.rounded_rectangle([px0, py0, px1, py1], radius=36, fill=PINK)
    draw.text(
        ((W - tw) / 2 - box[0], py0 + 22 - box[1]),
        pill_text,
        font=pill_font,
        fill=WHITE,
    )

    img.save("promo.png", format="PNG")


if __name__ == "__main__":
    main()
