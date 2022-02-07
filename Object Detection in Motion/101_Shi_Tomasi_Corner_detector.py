# Shi_Tomasi_Corner detector -- dont want to detect all the corners in the image

import cv2
import numpy as np

img = cv2.imread('pic1.png')
cv2.imshow('img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# (img, max_number_of_corners_to_detect, quality_level, mean_distances_bet_corners_detected)
corners = cv2.goodFeaturesToTrack(gray, 25, 0.10, 10)
# corners = cv2.goodFeaturesToTrack(gray, 100, 0.10, 10)

# convert all detected corner points to int64 (int0 ==> is an alias for int64)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)  # (img, center_point, radius, color, thickness)

cv2.imshow("dst", img)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
