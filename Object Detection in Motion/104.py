# background_substraction --- generate the foreground binary mask in a scene from the background

import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
# pip install opencv-contrib-python
foreground_background = cv2.bgsegm.createBackgroundSubtractorGMG()
#foreground_background = cv2.bgsegm.createBackgroundSubtractorMOG2(detectShadows=False)

while True:
    ret, frame = cap.read()

    if frame is None:
        break

    fgmask = foreground_background.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)



    cv2.imshow("frame", frame)
    cv2.imshow("mask_frame", fgmask)

    k = cv2.waitKey(30)
    if k == 'q' or k == 27:
        break

cap.release()
cv2.destroyAllWindows()
