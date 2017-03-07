from PIL import Image
import cv2
import numpy as np



import matplotlib.pyplot as plt
image = Image.open("pic1.png")
mask=image.convert("L")

edges = cv2.Canny(np.array(mask),100,200)

th=150 # the value has to be adjusted for an image of interest 
#mask = mask.point(lambda i: i < th and 255)
plt.imshow(edges)
plt.show()