import numpy
import matplotlib.pyplot as plt
from PIL import Image

import Test


t = numpy.linspace(0, 2 * numpy.pi)
x = (numpy.sin(t) ** 3) * 16
y = numpy.cos(t) * 13 - numpy.cos(2 * t) * 5 - numpy.cos(3 * t) * 2 - numpy.cos(4 * t)
fig = plt.figure(figsize=(6, 6))
plt.plot(x, y, 'k')
plt.savefig('result.png')
img = Image.open('result.png').rotate(90)
pixels = img.load()
height, width = img.size
total_pixels = []
for x in range(width):
    for y in range(height):
        pix_ = pixels[x, y]
        mono_pix = 1 if round(sum(pix_)/float(len(pix_))) > 127 else 0
        total_pixels.append(mono_pix)
img.close()
name = 'result.bmp'
Test.create_bmp(name, total_pixels, height, width)
