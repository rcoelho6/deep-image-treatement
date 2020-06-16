import cv2
import numpy as np

image = cv2.imread('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.jpeg', 0)

kernel = np.ones((1, 1), np.uint8)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

cv2.imwrite('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.opening.2.jpg', opening)