# face_detection --- haarcascade --- trained on certain positive images (detector) - trainers
# the xml classifier files -- opencv github/data/haarcascades
import cv2
import numpy as np

img = cv2.imread('ari_hap.jpg')
#img = cv2.imread('ariyo_copy.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# import the pretrained OpenCV model XML
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# use the imported model as a classifier (img, scale_factor, min_neighbors)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)


for (x, y, w, h) in faces:
    #print(x+w * y+h)
    #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
    if x+w * y+h > 46000 and x+w * y+h < 120000:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
        print(x+w * y+h)


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
