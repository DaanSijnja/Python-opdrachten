import cv2 as cv

img = cv.imread('Practicum\week 5\gekleurde blokjes (1).jpg')
img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

hsv_low = (170,100,127)
hsv_high = (180,255,255)

mask = cv.inRange(img_hsv,hsv_low,hsv_high)

contours = cv.findContours(mask,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
contour_img = cv.drawContours(img.copy(),contours,-1,(255,255,255), 1)


cv.imshow('img',img)
cv.imshow('mask',mask)
cv.imshow('Contour',contour_img)
cv.waitKey(0)

cv.destroyAllWindows()