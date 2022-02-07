# background_substraction --- generate the foreground binary mask in a scene from the background

import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')

# pip install opencv-contrib-python
foreground_background = cv2.bgsegm.createBackgroundSubtractorMOG()
#foreground_background = cv2.bgsegm.createBackgroundSubtractorMOG2(detectShadows=False)

while True:
    ret, frame = cap.read()

    if frame is None:
        break

    fgmask = foreground_background.apply(frame)

    cv2.imshow("frame", frame)
    cv2.imshow("mask_frame", fgmask)

    k = cv2.waitKey(30)
    if k == 'q' or k == 27:
        break

cap.release()
cv2.destroyAllWindows()
