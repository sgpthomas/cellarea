from PIL import Image, ImageFilter, ImageOps
import numpy
import scipy
from scipy import ndimage

"""steps:
1. convert to grayscale
2. run Gaussian blur - average nearby pixels
3. run sobel edge detection
4. run canny edge detector
5. detect what edges make up a cell
6. calculate area of cells for image
7. set it up so that all images in a file are processed and
data is printed out labelled for each image
8. make most efficient/accurate as possible
9. possibly do some kind of standard deviation statistics
"""

im = Image.open("../images/unnamed.jpg") # open colour image

im = im.convert('L') # convert image to grayscale
im.filter(ImageFilter.EDGE_ENHANCE_MORE)

im.save('../images/result.jpeg')

im = scipy.misc.imread('../images/result.jpeg')
im = im.astype('int32')
dx = ndimage.sobel(im, 0)  # horizontal derivative
dy = ndimage.sobel(im, 1)  # vertical derivative
mag = numpy.hypot(dx, dy)  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
scipy.misc.imsave('../images/result2.jpeg', mag)  #sobel

im = scipy.misc.imread("../images/result2.jpeg")
print("length x", len(im[0]))
# print(im[98][122])
# for x in range(len(im)):
#     for y in range(len(im[x])):
#         if (im[x][y] < 100):
#             im[x][y] = 0
scipy.misc.imsave('../images/result3.jpeg', im)

# im = Image.open('../images/result2.jpeg')
# im = im.convert('L')
# im = ImageOps.invert(im)
# im.save('../images/result3.jpeg') #inverted grayscale
