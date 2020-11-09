import matplotlib.pyplot as plt
import numpy
from PIL import Image

import bmp_creator


t = numpy.linspace(0, 2 * numpy.pi)
x = (numpy.sin(t) ** 3) * 16
y = numpy.cos(t) * 13 - numpy.cos(2 * t) * 5 - numpy.cos(3 * t) * 2 - numpy.cos(4 * t)
fig = plt.figure(figsize=(4, 4))
plt.plot(x, y, 'k')
plt.savefig('res.png')
img = Image.open('res.png').rotate(90)
pixels = img.load()
width, height = img.size
print(width, height)
total_pixels = []
for x in range(width):
    for y in range(height):
        _pix = pixels[x, y]
        mono_pix = 1 if round(sum(_pix)/float(len(_pix))) > 127 else 0
        total_pixels.append(mono_pix)

img.close()
file_name = 'result.bmp'
bmp_creator.create_bmp(file_name, total_pixels, width, height)
