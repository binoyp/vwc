import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('src_imgs/pic2.jpg',0)

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged
# edges = cv2.Canny(img,100,250)
wide = cv2.Canny(img, 10, 200)
tight = cv2.Canny(img, 225, 250)
edges = auto_canny(img)
plt.subplot(221)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(tight,cmap = 'gray')
plt.title('Tight '), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(wide,cmap = 'gray')
plt.title('wide '), plt.xticks([]), plt.yticks([])
plt.show()