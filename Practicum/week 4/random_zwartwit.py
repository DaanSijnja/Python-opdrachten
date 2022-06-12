import cv2 as cv
import random as rndm

def random_zwart_wit(img):
    h, w = img.shape

    totaal_pixels = h*w

    for i in range(h):
        for j in range(w):
            if(rndm.randint(0,50) == 0):
                img[i,j] = 0
            elif(rndm.randint(0,100) == 0):
                img[i,j] = 255

    return img

image = cv.imread('Practicum\week 4\Cheshire.jpg',cv.IMREAD_GRAYSCALE)

new_img = random_zwart_wit(image)

cv.imshow('zwartwit',new_img)
cv.imwrite('Opdracht3.png', new_img)
cv.waitKey(0)

cv.destroyAllWindows()