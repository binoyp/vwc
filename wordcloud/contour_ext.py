import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('src_imgs/pic1.jpg',0)
# find all the 'black' shapes in the image
mimg =cv2.imread('masks/pic1.png',0)
lower = np.array([0, 0, 0])
upper = np.array([15, 15, 15])
#shapeMask = cv2.inRange(mimg, lower, upper)
(cnts, _) = cv2.findContours(mimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, [cnts[0][2:-2]], -1, (0, 255, 0),thickness=5)
plt.imshow(img)

plt.show()