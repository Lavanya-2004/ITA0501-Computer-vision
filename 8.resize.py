import cv2
import numpy as np
img=cv2.imread("D:\img.jpg",cv2.IMREAD_COLOR)
img=cv2.resize(img,(400,400))
cv2.imshow("image",img)
cv2.waitKey(0)
