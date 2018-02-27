import numpy as np
import cv2

img = cv2.imread('myimage.jpg',cv2.IMREAD_COLOR)


##print(px)
##img[55,55] = [255,255,255]


img[55,55] = [255,255,255]
px = img[55,55]
print(px)


##img[177:306,196:304] = [255,255,255]
akshay_face = img[177:306,196:304]
img[0:129,0:108] = akshay_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

