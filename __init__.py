import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("C:\\GitProjects\\PictureMaker\\python code - test\\pictures\\20200111_001403.jpg")

background = cv2.imread("C:\\GitProjects\\PictureMaker\\python code - test\\backgrounds\\20191228_122652.jpg")
background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)

dimensions = image.shape

image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

lower_limit = np.array([110, 110, 110])     ##[R value, G value, B value]
upper_limit = np.array([220, 220, 220])

outer_mask = cv2.inRange(image_copy, lower_limit, upper_limit)
mask = (255 - outer_mask)

masked_image = np.copy(image_copy)
masked_image[outer_mask !=0 ]  = [0,0,0]

crop_background = background #[0:3096, 0:4128]
crop_background[mask != 0] = [0, 0, 0]

final_image = crop_background + masked_image

top = dimensions[1]
botton = 0
left = dimensions[0]
right = 0

contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for contour in contours:
        if 200 > len(contour):
                continue

        for point in contour:
                if right < point[0][0]:
                        right = point[0][0]

                if left > point[0][0]:
                        left = point[0][0]

                if botton < point[0][1]:
                        botton = point[0][1]

                if top > point[0][1]:
                        top = point[0][1]

final_image = cv2.rectangle(final_image, (left,top), (right, botton), (255,0,0), 50)
plt.imshow(final_image)
plt.show()
