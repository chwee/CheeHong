import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image



img = Image.open('stinkbug.png')
width, height = img.size
print(width, height)
#flat array
pixels = list(img.getdata())
print(len(pixels))
#print(pixels)

# for item in pixels:
# 	r= item[0]
# 	print(r)

f = lambda item:item[0]
print(list(map(f,pixels)))





#for display only
img = mpimg.imread('stinkbug.png')
imgplot = plt.imshow(img)
plt.show()