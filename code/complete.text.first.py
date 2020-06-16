import cv2
import numpy as np

#img = cv2.imread('/home/rafael/workspace/deep-image-treatement/img/pedido_multipla_escolha.png', 0)
img = cv2.imread('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.jpeg', 0)

img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


#img = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
0
#img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#This one is almost (Dark --)
#img = cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 100), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

#This one is almost (Dark --)
#img = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

#Really really near (Dark --)
#img = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 5, 45, 45), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
img = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 1, 0, 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 3)

#img = cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

#img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


#cv2.imwrite('/home/rafael/workspace/deep-image-treatement/img/pedido_multipla_escolha.first.t.png', img)
cv2.imwrite('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.first.t.jpeg', img)
