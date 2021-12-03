import cv2 as cv

def percentage_van_pixels(img,pixel_value):
    h, w = img.shape

    total_pixels = h*w
    total_pixels_by_value = 0

    for i in range(h):
        for j in range(w):
            if(img[i,j] > pixel_value):
                total_pixels_by_value += 1
    
    percentage = round((total_pixels_by_value/total_pixels)*100,2)
    return percentage



image = cv.imread('Practicum\Week 3\Kroatie_grijs.jpg',0)

perc = percentage_van_pixels(image,127)
height, width = image.shape

print('Height: ', height, ' Width: ', width, ' Percetage of pixels larger then 127: ', perc,'%' )

