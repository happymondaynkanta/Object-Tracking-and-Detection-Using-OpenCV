# meanshift -- move objevt to area of maximim pixel concentration
# object cracking -- the process of tracking a moving object

import cv2
import numpy as np

cap = cv2.VideoCapture('slow_traffic_small.mp4')

while True:
    ret, frame = cap.read()

    if ret == True:

        cv2.imshow("frame", frame)

        k = cv2.waitKey(30)
        if k == 'q' or k == 27:
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
