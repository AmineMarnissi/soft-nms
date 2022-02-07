import cv2
import numpy as np

# load image as YUV (or YCbCR) and select Y (intensity)
# or convert to grayscale, which should be the same.
# Alternately, use L (luminance) from LAB.
img = cv2.imread("barn.jpg")
Y = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)[:,:,0]

# compute min and max of Y
min = np.min(Y)
max = np.max(Y)

# compute contrast
contrast = (max-min)/(max+min)
print(min,max,contrast)