import numpy as np
import cv2

IMAGE_FILE = 'IMAGE.jpeg'
img = cv2.imread(IMAGE_FILE)

for row in range(len(img)):
    for pixel in range(len(img[row])):
        r = int(img[row][pixel][0])
        g = int(img[row][pixel][1])
        b = int(img[row][pixel][2])
        avg = (r+g+b) / 3
        
        img[row][pixel][0] = avg
        img[row][pixel][1] = avg
        img[row][pixel][2] = avg

cv2.imwrite('grey.jpeg',img)
