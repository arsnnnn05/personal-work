"""Etsy shop icon (500x500) and banner (3360x840) from the design #3 dog."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

CREAM, RED, GREEN, BROWN = (244, 236, 221), (168, 50, 45), (47, 93, 80), (122, 74, 42)

src = Image.open("designs/source_03_dackel_pullover.webp").convert("RGBA")
a = np.array(src)
lab, n = ndimage.label(a[..., 3] > 20)
sizes = ndimage.sum(np.ones(lab.shape), lab, range(1, n + 1))
for i, s in enumerate(sizes, 1):
    if s < 20:
        a[lab == i, 3] = 0
dog = Image.fromarray(a)
dog = dog.crop(dog.getbbox())

def font(size, wght=700):
    f = ImageFont.truetype("designs/fonts/Fraunces.ttf", size)
    f.set_variation_by_axes([72, wght, 100, 1])
    return f

# Icon: head and collar, centred on a cream disc with a red ring
head = dog.crop((0, 0, int(dog.width * 0.86), int(dog.height * 0.56)))
S = 1000
icon = Image.new("RGBA", (S, S), CREAM + (255,))
d = ImageDraw.Draw(icon)
d.ellipse((20, 20, S - 20, S - 20), outline=RED, width=28)
hh = 860  # tall enough that the straight crop edge falls outside the circle
h = head.resize((int(head.width * hh / head.height), hh), Image.LANCZOS)
icon.alpha_composite(h, ((S - h.width) // 2 + 20, S - hh + 10))
mask = Image.new("L", (S, S), 0)
ImageDraw.Draw(mask).ellipse((20, 20, S - 20, S - 20), fill=255)
out = Image.new("RGBA", (S, S), CREAM + (255,))
out.paste(icon, (0, 0), mask)
ImageDraw.Draw(out).ellipse((20, 20, S - 20, S - 20), outline=RED, width=28)
out.convert("RGB").resize((500, 500), Image.LANCZOS).save("shop/etsy_shop_icon_500.png")

# Banner: dog right, bilingual tagline left (Etsy crops edges on mobile, keep text central-left)
W, H = 3360, 840
b = Image.new("RGBA", (W, H), CREAM + (255,))
dd = ImageDraw.Draw(b)
for x in range(0, W, 120):  # subtle fair-isle stitch row along the bottom, from the sweater
    dd.polygon([(x, H - 40), (x + 60, H - 90), (x + 120, H - 40)], fill=GREEN)
dd.rectangle((0, H - 40, W, H), fill=RED)
dg = dog.resize((int(dog.width * 700 / dog.height), 700), Image.LANCZOS)
b.alpha_composite(dg, (W - dg.width - 520, 20))
f1, f2 = font(150), font(78, 500)
dd.text((700, 230), "Dackel mit Charakter", font=f1, fill=RED)
dd.text((705, 430), "Illustrierte Geschenke · Cadeaux teckel illustrés", font=f2, fill=BROWN)
b.convert("RGB").save("shop/etsy_shop_banner_3360x840.jpg", quality=92)
b.convert("RGB").resize((1120, 280)).save("shop/preview_banner.jpg", quality=85)
print("ok")
