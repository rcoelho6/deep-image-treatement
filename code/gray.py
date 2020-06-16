import cv2

image = cv2.imread('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.jpeg', 1)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.gray.jpg', gray)