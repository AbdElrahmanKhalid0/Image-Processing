import numpy as np
import cv2

IMAGE_FILE = 'IMAGE.jpeg'
img = cv2.imread(IMAGE_FILE)

for row in range(len(img)):
    for pixel in range(len(img[row])):
        r = int(img[row][pixel][0])
        g = int(img[row][pixel][1])
        b = int(img[row][pixel][2])
        
        sepiaRed = .393 * r + .769 * g + .189 * b
        sepiaGreen = .349 * r + .686 * g + .168 * b
        sepiaBlue = .272 * r + .534 * g + .131 * b
        
        img[row][pixel][0] = sepiaRed if sepiaRed < 255 else 255
        img[row][pixel][1] = sepiaGreen if sepiaGreen < 255 else 255
        img[row][pixel][2] = sepiaBlue if sepiaBlue < 255 else 255

cv2.imwrite('sepia.jpeg',img)