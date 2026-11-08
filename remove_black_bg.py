from PIL import Image

paths = [
    r'd:\tugas\coffee-shop-garage 18\image\1.jpeg',
    r'd:\tugas\coffee-shop-garage 18\image\3.jpeg',
    r'd:\tugas\coffee-shop-garage 18\image\kopi gula aren.png',
    r'd:\tugas\coffee-shop-garage 18\image\kopi-gula-aren-slider.png',
]

for src in paths:
    img = Image.open(src).convert('RGBA')
    pixels = img.load()
    width, height = img.size
    removed = 0

    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if r < 40 and g < 40 and b < 40:
                pixels[x, y] = (0, 0, 0, 0)
                removed += 1

    out = src.replace('.jpeg', '-transparent.png').replace('.png', '-transparent.png')
    img.save(out, format='PNG')
    print(f'saved: {out} (removed pixels: {removed})')
