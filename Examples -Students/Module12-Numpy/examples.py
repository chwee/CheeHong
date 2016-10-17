# from PIL import Image
# im = Image.open('images.png')

# pixels = list(im.getdata())
# width, height = im.size
# print(width , height)
# #pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
# pixels = [pixels[0:width] for i in range(height)]
# print(pixels)

#---------------------------------------------------------------

# from PIL import Image
# im = Image.open("images.png") #Can be many different formats.
# pix = im.load()
# print(im.size) #Get the width and hight of the image for iterating over
# print (pix[x,y]) #Get the RGBA Value of the a pixel of an image
# #pix[x,y] = value # Set the RGBA Value of the image (tuple)

#--------------------------------------------------------------

# from PIL import Image
# im = Image.open("images.png")
# pix_val = list(im.getdata())
# print(pix_val)
# #pix_val_flat = [x for sets in pix_val for x in sets]

#-----------------------------------------------------------

#tutorial 1
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import numpy as np
# img = mpimg.imread('stinkbug.png')
# print(img[0,:])
# print(img[0,2])
# imgplot = plt.imshow(img)
# plt.show()

#tutorial 2
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import numpy as np
# img = mpimg.imread('stinkbug.png')
# lum_img = img[:, :, 0]
# plt.imshow(lum_img)
# plt.show()

#tutorial 3
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import numpy as np
# img = mpimg.imread('stinkbug.png')
# lum_img = img[:,:,0]
# imgplot = plt.imshow(lum_img)
# imgplot.set_cmap('hot')
# plt.show()

#--------------------------------------------------
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


# arr = np.array(img) # 640x480x4 array
# print(arr.shape)
# print(arr[1,:,1:2])

#for display only
img = mpimg.imread('stinkbug.png')
imgplot = plt.imshow(img)
plt.show()