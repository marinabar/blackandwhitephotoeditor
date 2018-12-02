from PIL import Image
img = Image.open("avantages-quil-y-a-a-grandir-dans-un-petit-village.jpg")
pixels = img.load()
for i in range(img.width):
    for j in range(img.height):
        r, g, b = pixels[i, j]
        z = (r + g + b) // 3
        r =z
        g =z
        b = z
        pixels[i, j]=(r, g, b)
img.show()
