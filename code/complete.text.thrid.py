import cv2
import numpy as np

#img = cv2.imread('/home/rafael/workspace/deep-image-treatement/img/pedido_multipla_escolha.png', 0)
img = cv2.imread('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.jpeg', 0)

##gaussian_3 = cv2.GaussianBlur(img, (11,11), 15.0)
##unsharp_image = cv2.addWeighted(img, 1.5, gaussian_3, -0.8, 5, img)

#out = cv2.Laplacian(unsharp_image, cv2.CV_64F)
#out = unsharp_image

image = img
kernel_size=(5, 5)
sigma=10
amount=5
threshold=100

"""Return a sharpened version of the image, using an unsharp mask."""
blurred = cv2.GaussianBlur(image, kernel_size, sigma)
sharpened = float(amount + 1) * image - float(amount) * blurred
sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
sharpened = sharpened.round().astype(np.uint8)
if threshold > 0:
    low_contrast_mask = np.absolute(image - blurred) < threshold
    np.copyto(sharpened, image, where=low_contrast_mask)

out = sharpened

#cv2.imwrite('/home/rafael/workspace/deep-image-treatement/img/pedido_multipla_escolha.third.t.png', img)
cv2.imwrite('/home/rafael/workspace/deep-image-treatement/img/darkmenosmenos.third.t.jpeg', out)
