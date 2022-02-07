# background_substraction --- generate the foreground binary mask in a scene from the background

import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')

while True:
    ret, frame = cap.read()

    if frame is None:
        break

    cv2.imshow("frame", frame)

    k = cv2.waitKey(30)
    if k == 'q' or k == 27:
        break

cap.release()
cv2.destroyAllWindows()
