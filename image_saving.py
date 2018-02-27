import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('myimage.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.line(img,(0,0),(150,150),(255,255,0),15)
##cv2.imshow('image',img)
##plt.imshow(img, cmap='gray',interpolation = 'bicubic')
##plt.plot([50,100],[80,100], 'c',linewidth = 2)
##plt.show()

##cv2.imwrite("myimage1.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
