import cv2 as cv
import matplotlib.pyplot as plt
import os
import numpy

#load image
image_path = "Vision/test.png"


image = cv.imread(image_path,cv.IMREAD_COLOR)
print(os.path.isfile(image_path))

# cv.imshow("Image", image)
'''
#convert image to grayscale image
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# cv.imshow("Gray Image", gray_image)  #to show the gray image

#read the harr_face_detect_classifier.xml
harr_cascade = cv.CascadeClassifier("Vison\haar.xml")

face_cords = harr_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=1 )

for x, y, w, h in face_cords:
    cv.rectangle(image, (x,y), (x+w, y+h), (255, 0,0), thickness=2)

#show image
cv.imshow("Face Detect", image)

cv.waitKey(0)
'''