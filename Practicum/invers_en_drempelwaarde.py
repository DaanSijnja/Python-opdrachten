import cv2 as cv


def invers(img):
    img
    h, w, _ = img.shape

    for i in range(h):
        for j in range(w):
            p = img[i,j]
            img[i,j] = 255 - p

    return img
    
def drempel(img,waarde):
    img
    h, w, _ = img.shape

    for i in range(h):
        for j in range(w):
            p = img[i,j]
            img[i,j] = (p > waarde)

    return img




image = cv.imread('Appels.jpg',0)

drempel_img = drempel(image,127)
invers_img = invers(image)

cv.imshow('orignieel',image)
cv.imshow('drempel',drempel_img)
cv.imshow('inverse',invers_img)
cv.waitKey(0)
cv.destroyAllWindows()