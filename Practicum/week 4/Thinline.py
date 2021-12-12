#import numpy as np
import cv2

# Lees een plaatje in
img = cv2.imread('thinline.png', cv2.IMREAD_UNCHANGED)

rows,cols = img.shape[:2]
aantal_r = 0
aantal_g = 0
aantal_b = 0

for i in range(rows):
    for j in range(cols):
        b, g, r = img[i,j]
        if r == 255:
            aantal_r = aantal_r + 1
        if g == 255:
            aantal_g = aantal_g + 1
        if b == 255:
            aantal_b = aantal_b + 1
            
print(aantal_r)
print(aantal_g)
print(aantal_b)
