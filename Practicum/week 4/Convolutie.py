import scipy.signal as sig

img = [[13,8,9],
       [14,16,15],
       [3,5,1]]

kernel = [[2,1],
          [0,-1]]

result = sig.convolve2d(kernel,img)

print(result)
