from PIL import Image, ImageFilter
im = Image.open("../images/DSC_0625.jpeg") # open colour image

im = im.convert('L') # convert image to grayscale
im.filter(ImageFilter.EDGE_ENHANCE_MORE)

im.save('../images/result.jpeg')