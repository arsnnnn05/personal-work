"""Build print files for design #3 'Frohe Wauchnachten' from the Gemini illustration."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

RED = (168, 50, 45, 255)
src = Image.open("source_03_dackel_pullover.webp").convert("RGBA")

# Drop stray specks (tiny isolated opaque blobs), then crop to the dog.
a = np.array(src)
lab, n = ndimage.label(a[..., 3] > 20)
sizes = ndimage.sum(np.ones(lab.shape), lab, range(1, n + 1))
for i, s in enumerate(sizes, 1):
    if s < 20:
        a[lab == i, 3] = 0
dog = Image.fromarray(a)
dog = dog.crop(dog.getbbox())

def font(size, wght=700):
    f = ImageFont.truetype("fonts/Fraunces.ttf", size)
    f.set_variation_by_axes([72, wght, 100, 1])  # opsz, wght, SOFT, WONK
    return f

def text_block(lines, size):
    f = font(size)
    boxes = [f.getbbox(l) for l in lines]
    w = max(b[2] - b[0] for b in boxes)
    lh = int(size * 1.05)
    img = Image.new("RGBA", (w + 20, lh * len(lines) + 20), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for i, (l, b) in enumerate(zip(lines, boxes)):
        d.text(((img.width - (b[2] - b[0])) // 2 - b[0], 10 + i * lh - b[1]), l, font=f, fill=RED)
    return img.crop(img.getbbox())

def save(img, name, pad=60):
    out = Image.new("RGBA", (img.width + 2 * pad, img.height + 2 * pad), (0, 0, 0, 0))
    out.paste(img, (pad, pad), img)
    out.save(name, dpi=(300, 300))
    print(name, out.size)

# A) Stacked: dog above text (sweatshirt front, tote, mug side)
txt = text_block(["Frohe", "Wauchnachten"], 260)
txt = txt.resize((int(dog.width * 1.05), int(txt.height * dog.width * 1.05 / txt.width)), Image.LANCZOS)
gap = 70
W = max(dog.width, txt.width)
A = Image.new("RGBA", (W, dog.height + gap + txt.height), (0, 0, 0, 0))
A.paste(dog, ((W - dog.width) // 2, 0), dog)
A.paste(txt, ((W - txt.width) // 2, dog.height + gap), txt)
save(A, "print_03_frohe_wauchnachten_stacked.png")

# B) Side by side: dog left, text right (11oz mug, reads well around the curve)
txt2 = text_block(["Frohe", "Wauch-", "nachten"], 300)
scale = dog.height * 0.62 / txt2.height
txt2 = txt2.resize((int(txt2.width * scale), int(txt2.height * scale)), Image.LANCZOS)
gap = 120
B = Image.new("RGBA", (dog.width + gap + txt2.width, dog.height), (0, 0, 0, 0))
B.paste(dog, (0, 0), dog)
B.paste(txt2, (dog.width + gap, (dog.height - txt2.height) // 2), txt2)
save(B, "print_03_frohe_wauchnachten_mug.png")

# Previews on the mug colour (white) and the shop cream, for checking only
for name in ["print_03_frohe_wauchnachten_stacked.png", "print_03_frohe_wauchnachten_mug.png"]:
    im = Image.open(name)
    bg = Image.new("RGBA", im.size, (244, 236, 221, 255))
    bg.alpha_composite(im)
    bg.convert("RGB").resize((im.width // 3, im.height // 3)).save(name.replace("print_", "preview_").replace(".png", ".jpg"), quality=85)
