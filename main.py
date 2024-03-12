import cv2
import numpy as np

img = cv2.imread("Color.png")

# threshold on orange
lower = (0,60,200)
upper = (110,160,255)
thresh = cv2.inRange(img, lower, upper)

# apply morphology and make 3 channels as mask
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
mask = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.merge([mask,mask,mask])

# create 3-channel grayscale version
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# blend img with gray using mask
result = np.where(mask==255, img, gray)


# Display images
cv2.imshow("result", result)
cv2.waitKey(0)