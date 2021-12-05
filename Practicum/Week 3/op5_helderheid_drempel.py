import cv2 as cv

def helderheid_drempel(img,d_laag,d_hoog):
    h, w = img.shape

    for i in range(h):
        for j in range(w):
            if(img[i,j] > d_hoog):
                img[i,j] = d_hoog
            if(img[i,j] < d_laag):
                img[i,j] = d_laag
    
    return img

image = cv.imread('Practicum\Week 3\Appels.jpg',0)
img_helderheid = helderheid_drempel(image.copy(),30,200)

cv.imshow('orignieel',image)
cv.imshow('Helderheid aangepast',img_helderheid )

cv.imwrite('Helderheidaangepast.jpg',img_helderheid)

while True: 
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break
cv.destroyAllWindows()