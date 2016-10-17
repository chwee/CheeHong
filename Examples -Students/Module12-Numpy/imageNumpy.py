import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
from numpy import array




img = Image.open('stinkbug.png')
width, height = img.size
print(width, height)
#get a numpy array from an image use
arr = array(img)
print(arr)

arr1= arr[100:300, 200:400]
#get an image from a numpy array, use
img = Image.fromarray(arr1)
img.save("output.png")

#for display only
img = mpimg.imread('stinkbug.png')
imgplot = plt.imshow(img)
plt.show()