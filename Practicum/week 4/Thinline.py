#import numpy as np
import cv2

# Lees een plaatje in
img = cv2.imread('Practicum\week 4\_thinline.png', cv2.IMREAD_UNCHANGED)

rows,cols = img.shape[:2]
aantal_r = 0
aantal_g = 0
aantal_b = 0


def check_color(c,pixel):
    if(c[0] == pixel[0] and c[1] == pixel[1] and c[2] == pixel[2]):
        return True
    return False




for i in range(rows):
    for j in range(cols):
        pixel = img[i,j]

        if(check_color((255,0,0),pixel)):
            aantal_b += 1
        
        if(check_color((0,255,0),pixel)):
            aantal_g += 1

        if(check_color((0,0,255),pixel)):
            aantal_r += 1

            
print(aantal_r)
print(aantal_g)
print(aantal_b)
