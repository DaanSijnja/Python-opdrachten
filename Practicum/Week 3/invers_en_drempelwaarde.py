import cv2 as cv

threshold = 0
prev_treshold = threshold + 1
window_drempelwaarde = 'Drempelwaarde'

def threshold_trackbar(val):
  
    global threshold

    threshold = val
    cv.setTrackbarPos('treshold',window_drempelwaarde ,threshold)



def invers(img):

    h, w = img.shape

    for i in range(h):
        for j in range(w):
            p = img[i,j]
            img[i,j] = 255 - p

    return img
    
def drempel(img,waarde):
 
    h, w = img.shape

    for i in range(h):
        for j in range(w):
            p = img[i,j]
            img[i,j] = (p > waarde)*255

    return img




cv.namedWindow(window_drempelwaarde)
cv.createTrackbar('treshold', window_drempelwaarde , 0, 255, threshold_trackbar)

image = cv.imread('Practicum\Week 3\Appels.jpg',0)
invers_img = invers(image.copy())
cv.imshow('orignieel',image)
cv.imshow('inverse',invers_img)

while True: 
    
    if(threshold != prev_treshold):
        drempel_img = drempel(image.copy(),threshold)
        prev_treshold = threshold
    
    cv.imshow(window_drempelwaarde,drempel_img)
    
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break

cv.destroyAllWindows()