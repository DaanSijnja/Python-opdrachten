#import numpy as np
import cv2
import random

# Lees een foto in (grijswaarden)
img = cv2.imread('Practicum\week 4\Cheshire.jpg', cv2.IMREAD_GRAYSCALE)

rows,cols = img.shape[:2]

for i in range(rows):
    for j in range(cols):
        # genereer een random getal tussen 0 en 1
        r = random.random()
        # bereken een random getal tussen 0 en 255 (
        # grenzen doen mee.. als het goed is
        gray = r * 255
        img[i,j] = gray
 
cv2.imshow('Willekeurige grijswaarden',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Randomgrijs.jpg', img)