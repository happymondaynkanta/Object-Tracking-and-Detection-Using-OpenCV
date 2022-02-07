# Harris Corner detector
# Step 1: which windows has high intesity variation at direction X and Y
# Step 2: for each window found, compute a score R
# Step 3: apply threshold to each window

import cv2
import numpy as np

img = cv2.imread('chessboard.png')
cv2.imshow('img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert to float 32 as thats what cornerHarris takes
gray = np.float32(gray)

# cornerHarris(img, neighbourhood_size, sobel_ksize, free_parameter)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# dilate the cornerHarris result
dst = cv2.dilate(dst, None)

# mark all cornes detected greater than 0.01 as red
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow("dst", img)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
