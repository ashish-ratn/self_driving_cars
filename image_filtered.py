import numpy as np
import cv2

frame = cv2.imread('sample1.jpg')

hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

lower_red = np.array([150,150,50])
upper_red = np.array([180,255,255])

mask = cv2.inRange(hsv,lower_red,upper_red)
res = cv2.bitwise_and(frame,frame,mask=mask)

cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imwrite("mask_sample1.jpg",mask)
cv2.imwrite("res_sample1.jpg",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
