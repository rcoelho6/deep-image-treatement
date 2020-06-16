import cv2
import numpy as np

image = cv2.imread('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.jpeg', 0)

kernel = np.ones((5,5),np.uint8)
thread = cv2.threshold(image,210,210,cv2.THRESH_BINARY)[1]
dilate = cv2.dilate(thread, kernel, iterations = 1)
bluer = cv2.medianBlur(dilate,5)

cv2.imwrite('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.thread.jpg', thread)
cv2.imwrite('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.bluer.jpg', thread)
cv2.imwrite('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.dilate.jpg', thread)