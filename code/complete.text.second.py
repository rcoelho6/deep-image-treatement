import cv2
import numpy as np

#img = cv2.imread('/home/rafael/workspace/deep-image-treatement/img/pedido_multipla_escolha.png', 0)
img = cv2.imread('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.jpeg', 0)

#blur = cv2.blur(img,(3,3))
blur = image = cv2.GaussianBlur(img, (5, 5), 0)

#_,thresh = cv2.threshold(blur,240,255,cv2.THRESH_BINARY)
#thresh = cv2.adaptiveThreshold(cv2.bilateralFilter(blur, 1, 0, 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 3)
#thresh = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 5, 45, 45), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 29, 5)

thresh = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 5, 45, 45), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 29, 5)
cv2.imshow("thresh",thresh)

thresh = cv2.bitwise_not(thresh)

element = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(5, 5))

erode = cv2.erode(thresh,element,3)
#cv2.imshow("erode",erode)

#cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite('/home/rafael/workspace/deep-image-treatement/img/pedido_multipla_escolha.first.t.png', img)
#cv2.imwrite('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.first.t.jpeg', img)
