#import numpy as np
import cv2

# Lees een foto in (grijswaarden)
img = cv2.imread('Practicum\Week 3\Kroatie_grijs.jpg', 0)
#mg = cv2.resize(img, (800, 600)) 

rows,cols = img.shape[:2]

for i in range(rows):
    for j in range(cols):
        k = img[i,j]
        img[i,j] = (k // 32) * 32
 
cv2.imshow('plaatje',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite('Kroatie_out.jpg', img)
