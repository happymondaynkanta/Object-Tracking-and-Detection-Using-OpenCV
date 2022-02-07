# detect whitw car in Video
import cv2
import numpy as np

cap = cv2.VideoCapture('slow_traffic_small.mp4')

# first frame of video
ret, frame = cap.read()

# initial location of white car
x, y, width, height = 300, 200, 100, 60

track_window = (x, y, width, height)

# set region of interest from first frame
roi = frame[y: y+height, x: x+width]

# get hsv color
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# inRange(img, lower_bound, upper_bound)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255)))

# define the histogram value
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])

cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# set termination criteria (either 10 iteration or move by atleast 1 pt)
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()

    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # use mean shift to get change in location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)

        final_image = cv2.polylines(frame, [pts], True, (0, 255, 0), 2)


        #cv2.imshow("dst", dst)
        cv2.imshow("final_image", final_image)

        k = cv2.waitKey(30)
        if k == 'q' or k == 27:
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
