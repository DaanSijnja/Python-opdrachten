

import cv2 as cv
import numpy as np

def kernel_som(img_snippet,kernel_size,kernel):

    h, w = kernel.shape

    pixel = [0,0,0]
    pixel_som = [0,0,0]
    for i in range(h):
        for j in range(w):
            for l in range(3):
                pixel_som[l] += img_snippet[i,j,l]*kernel[j,i]
            
    for k in range(3):
        pixel[k] = round(pixel_som[k]/kernel_size)
    
    #print(pixel)
    return pixel


def kernel_snippet(img,kernel,i,j):
    h_kern, w_kern = kernel.shape
    kern_size = h_kern*w_kern

    img_snippet = np.zeros((h_kern,w_kern,3),dtype=int)

    for k in range(h_kern):
        for l in range(w_kern):
            img_snippet[k,l] = img[i-k,j-l]
    
    
    #new_img = cv.rectangle(img.copy(),(i-h_kern//2,j-w_kern//2),(i+h_kern//2,j+w_kern//2),(255,255,255),1)
    
    return kernel_som(img_snippet,kern_size,kernel)

def convolutie(img, kernel):

    h_img, w_img, c = img.shape
    
    imgcopy = img.copy()#np.zeros((h_img+1,w_img+1,3),dtype=int)

    for i in range(h_img):
        pers = ((i+1)/h_img)*100

        if(pers % 5 == 0.0):
            print('percent done:',int(pers))
        for j in range(w_img):
            pixel = kernel_snippet(img,kernel,i,j)
            #print(pixel)
            imgcopy[i,j] = pixel

        
            
    return imgcopy




kernel = np.array(
        [
        [0.5,0.75,0.5],
        [0.75,1,0.75],
        [0.5,0.75,0.5]
        ]
        ) 

        


image = cv.imread('Practicum\zelf\R.jpg',cv.IMREAD_ANYCOLOR)

new_img = convolutie(image,kernel)

cv.imshow('kleurkaartje',new_img)
cv.imwrite('Practicum\zelf\Ra.jpg',new_img)
cv.waitKey(0)
cv.destroyAllWindows()
