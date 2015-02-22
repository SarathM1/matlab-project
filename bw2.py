from PIL import Image
import numpy as np
import pylab
import matplotlib.cm as cm

f = pylab.figure()

col = Image.open("rgb.png")			# Open image, can use any format as i/p
gray = col.convert('L')				# Convert to grayscale
gray.save("rgb_gray.JPG")
bw = np.asarray(gray).copy() 			# converts image to matrix of pixel values
print bw					# Just to show o/p of above statement, avoid in final code	
						# Pixel range is 0...255, 256/2 = 128
bw[bw < 128] = 0    				# Thresholding : If intensity < 128(threshold) => black
bw[bw >= 128] = 255 				# Else if intensity > 128 => White



imfile = Image.fromarray(bw)			# Read raw data and convert to file
imfile.save("rgb_bw2.JPG")				# Save as image file , dont forget to specify o/p format
imfile.show()

# From here on the rest of code is to displa image side by side
for n, fname in enumerate(('rgb_bw2.JPG','rgb.png','rgb_gray.JPG')):  
    image = Image.open(fname)
    arr = np.asarray(image)
    #f.add_subplot(2, 1, n)  			# this line outputs images on top of each other
    f.add_subplot(1, 3, n)  			# this line outputs images side-by-side
    pylab.imshow(arr,cmap=cm.Greys_r)
pylab.title('Edit this title')			# Edit string to change title
pylab.show()


