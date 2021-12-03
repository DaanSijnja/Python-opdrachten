import cv2 as cv

def helderheid_optellen(img,waarde):
    h, w = img.shape
    for i in range(h):
        for j in range(w):

            if(img[i,j] + waarde > 255):
                img[i,j] = 255
            else:
                if(img[i,j] + waarde < 0):  
                    img[i,j] = 0
                else:
                    img[i,j] += waarde
    return img

def helderheid_vermedigvuldigen(img,waarde):
    h, w = img.shape

    for i in range(h):
        for j in range(w):
            if(img[i,j] * waarde > 255):
                img[i,j] = 255
            else:
                if(img[i,j] * waarde < 0):  
                    img[i,j] = 0
                else:
                    img[i,j] *= waarde

    return img

def gemiddelde_helderheid(img):
    h, w = img.shape
    totaal_pixels = h*w
    totaal_pixel_waardes = 0
    for i in range(h):
        for j in range(w):
            totaal_pixel_waardes += img[i,j]

    return totaal_pixel_waardes//totaal_pixels

def contrast_verlagen(img,waarde): 
    h, w = img.shape

    gem_helderheid = gemiddelde_helderheid(img)

    for i in range(h):
        for j in range(w):
            img[i,j] = (img[i,j]-gem_helderheid)/waarde + gem_helderheid

    return img



image = cv.imread('Practicum\Week 3\Kroatie_grijs.jpg',0)

img_helderheid_opg = helderheid_optellen(image.copy(),20)
img_helderheid_vegm = helderheid_vermedigvuldigen(image.copy(),1.5)
img_contrast = contrast_verlagen(image.copy(),2)

cv.imshow('orignieel',image)
cv.imshow('Helderheid Opgetelt',img_helderheid_opg)
cv.imshow('Helderheid Vermedigvuldigd',img_helderheid_vegm)
cv.imshow('Contrast',img_contrast)

while True: 
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break
cv.destroyAllWindows()