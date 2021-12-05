import cv2 as cv
import numpy as np
import math as m


def root_mean_square(img):
    h, w = img.shape
    gem_pixels = np.mean(img)
    totaal = 0
    for i in range(h):
        for j in range(w):
            totaal += (img[i,j]-gem_pixels)**2
    
    return m.sqrt(totaal/(h*w))


image_peren = cv.imread('Practicum\Week 3\Peren.jpg',0)
image_peren_2 = cv.imread('Practicum\Week 3\Peren2.jpg',0)
image_peren_3 = cv.imread('Practicum\Week 3\Peren3.jpg',0)
print(round(root_mean_square(image_peren)))
print(round(root_mean_square(image_peren_2)))
print(round(root_mean_square(image_peren_3)))



