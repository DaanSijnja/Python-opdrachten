import cv2 as cv

img = cv.imread('Practicum\week 5\gekleurde blokjes (1).jpg')
img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
low = (170,100,127)
high = (180,255,255)

mask = cv.inRange(img_hsv,low,high)

cv.imshow('Mask',mask)

cnts = cv.findContours(mask,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

cv.drawContours(img,cnts,-1,(255,255,255))

cv.imshow('contouren',img)

cv.waitKey(0)

cv.destroyAllWindows()
