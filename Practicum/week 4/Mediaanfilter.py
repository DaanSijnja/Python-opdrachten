import cv2 as cv

def bereken_mediaan(snippet):
    #print(snippet)
    mediaan = 127
    h_snippet = len(snippet)
    if(len(snippet) != 0):
        w_snippet = len(snippet[0])
        #print(h_snippet,w_snippet)
    
        new_snippet = []
        for i in range(h_snippet):
            for j in range(w_snippet):
                new_snippet.append(snippet[i,j])
        new_snippet.sort()    
        
        c = len(new_snippet)
        
        if(c != 0):
            mediaan = new_snippet[c//2]
            
    #print(mediaan)
    return mediaan
    


image = cv.imread('Opdracht3.png', cv.IMREAD_GRAYSCALE)
h, w = image.shape
median = image.copy()
for i in range(h):
    for j in range(w):
        if(image[i,j] == 0 or image[i,j] == 255):
            snippet = image[i-1:i+2,j-1:j+2]
            
            image[i,j] = bereken_mediaan(snippet)
            #print(image[i,j])
            
            
            

           
           
cv.imshow('Mediaan filter', image)
cv.imshow('Random grijgs', median)

cv.waitKey(0)
cv.destroyAllWindows()