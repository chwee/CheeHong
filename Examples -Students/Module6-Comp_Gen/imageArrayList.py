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
#read all the red value in list
f = lambda item:item[0]
a=list(map(f,pixels))

#List Comp extract red >120
b=[n for n in a if n > 120 and n <130]
print(b)

print(sum(b)/len(b))





#for display only
img = mpimg.imread('stinkbug.png')
imgplot = plt.imshow(img)
plt.show()