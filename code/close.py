import cv2
import numpy as np

image = cv2.imread('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.jpeg', 0)

kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

cv2.imwrite('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.2.close.jpg', opening)