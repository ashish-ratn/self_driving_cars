import numpy as np
import cv2

img = cv2.imread('myimage.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(255,0,0),15)
cv2.rectangle(img,(15,25),(200,159),(0,255,0),8)
cv2.circle(img,(100,67),55,(0,0,255),-1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Opencv is amazing',(0,130),font,2,(200,203,23),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
