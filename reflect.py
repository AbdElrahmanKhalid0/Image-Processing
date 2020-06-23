import numpy as np
import cv2

IMAGE_FILE = 'IMAGE.jpeg'
img = cv2.imread(IMAGE_FILE)
new_img = np.copy(img)

for row in range(len(img)):
    for pixel in range(len(img[row])):    
        new_img[row][pixel] = img[row][len(img[row]) - pixel - 1]

cv2.imwrite('reflection.jpeg', new_img)