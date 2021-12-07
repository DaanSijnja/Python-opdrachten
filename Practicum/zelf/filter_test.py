'''
    Gemaakt door Daan Sijnja, Student Mechatronica Haagse Hogeschool: 20177747
    @Description:
        Een stuk code dat een convolutie filter toepast op een afbeelding

'''

import cv2 as cv                                                            #import openCV voor het gebruik van image reading en writting
import numpy as np                                                          #import numpy om te gebruiken voor het maken van arrays


def kernel_snippet(img,kernel_size,i,j):
    '''
        @Input:
            img: Een afbeelding Matrix

            kernel_size: De grote van kernel als een tuple (height, width)

            i, j: Coordinaten op de img

        @Return:
            img_snippet: Een snippet van de img Matrix 

        @Description:
            Deze functie maakt een snippet van de img ter grote van de kernel
    
    '''
    h_kern, w_kern = kernel_size                                            # pak de Height en Width uit kernel_size

    img_snippet = np.zeros((h_kern,w_kern,3),dtype=int)                     # maak een lege matrix voor img_snippet

    for k in range(h_kern):                                                 # k gaat van 0 tot de Height - 1 van de kernel
        for l in range(w_kern):                                             # l gaat van 0 tot de Width - 1  van de kernel
            img_snippet[k,l] = img[i-k,j-l]                                 # maak een snippet van de originele img
       
    return img_snippet                                                      # return img_snippet



def kernel_gem(img,kernel,i,j):    
    '''
        @Input:
            img: Een image matrix

            kernel: Matrix waarmee de convolutie uitgevoerd moet worden

            i, j: image coordinaten

        @Return:
            pixel: De waarde van de pixel op de locatie i,j


        @Description:
            Deze functie pakt het gemiddelde van de pixels met een kernel

    '''                         
    h, w = kernel.shape                                                     # pak de Height en Width van de Matrix kernel
    kernel_size = h*w                                                       # bereken de grote van de Matrix kernel

    img_snippet = kernel_snippet(img,(h,w),i,j)                            # maak een img snippet van de grote van de kernel

    pixel = [0,0,0]                                                         # init een waarde voor pixel
    pixel_som = [0,0,0]                                                     # init een waarde voor het pixel gemiddelde

    for i in range(h):                                                      # i gaat van 0 tot de Height - 1 van de Matrix kernel
        for j in range(w):                                                  # j gaat van 0 tot de Width - 1 van de Matrix kernel
            for l in range(3):                                              # l gaat van 0 tot 3 want in een RGB waarde zitten 3 waardes
                pixel_som[l] += img_snippet[i,j,l]*kernel[i,j]              # maak een som van alle pixels waardes van de img_snippet*kernel
            
    for k in range(3):                                                      # k gaat van 0 tot 3 want in een RGB waarde zitten 3 waardes
        pixel[k] = round(pixel_som[k]/kernel_size)                          # bereken het gemiddelde en rond dit af
    
    return pixel                                                            # return pixel




def convolutie(img, kernel,mode):
    '''
        @Input:
            img:

            kernel:

            mode:

        @Return:
            imgcopy:

        @Description:
            Deze funtie voer convolutie uit met een image en een kernel op de geselecteerde modes 
    '''

    h_img, w_img, c = img.shape
    
    imgcopy = img.copy()

    for i in range(h_img):
        pers = ((i+1)/h_img)*100

        if(pers % 5 == 0.0):
            print('percent done:',int(pers))
        for j in range(w_img):
            pixel = kernel_gem(img,kernel,i,j)
            imgcopy[i,j] = pixel
    
    return imgcopy




kernel = np.array(
        [
        [1,1,1],
        [1,1,1],
        [1,1,1]
        ]
        ) 

        


image = cv.imread('Practicum\zelf\R.jpg',cv.IMREAD_ANYCOLOR)

new_img = convolutie(image,kernel,'gem')

cv.imshow('kleurkaartje',new_img)
cv.imwrite('Practicum\zelf\Ra.jpg',new_img)
cv.waitKey(0)
cv.destroyAllWindows()
