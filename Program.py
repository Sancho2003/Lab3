import numpy
import matplotlib.pyplot as plt
from PIL import Image
import os

t = numpy.arange(0, 2*numpy.pi, 0.01)
fig, ax = plt.subplots()
ax.plot(numpy.sin(t)**3, numpy.cos(t)*13 - numpy.cos(2*t)*5 - numpy.cos(3*t)*2 - numpy.cos(4*t))
fig.savefig('1.png')
f = Image.open('1.png')
f.save('1.bmp', 'bmp')
os.remove('1.png')
