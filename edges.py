# for additional information about the algorithm 
# https://cs50.harvard.edu/x/2020/psets/4/filter/more/
# https://en.wikipedia.org/wiki/Edge_detection
import numpy as np
import cv2
from math import sqrt

IMAGE_FILE = 'IMAGE.jpeg'
img = cv2.imread(IMAGE_FILE)
new_img = np.copy(img)

for row in range(len(img)):
    for pixel in range(len(img[row])):
        # for each pixel get the Gx and Gy
        gy_red_sum = gy_green_sum = gy_blue_sum = 0
        gx_red_sum = gx_green_sum = gx_blue_sum = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if row + i < 0 or row + i >= len(img) or pixel + j < 0 or pixel + j >= len(img[i]):
                    continue
                
                # Gy
                # in case the pixel was the middle one it will be multiplied by 2
                if j == 0:
                    gy_red_sum += 2 * i * img[row + i][j + pixel][0]
                    gy_green_sum += 2 * i * img[row + i][j + pixel][1]
                    gy_blue_sum += 2 * i * img[row + i][j + pixel][2]
                else:
                    gy_red_sum += 2 * i * img[row + i][j + pixel][0]
                    gy_green_sum += 2 * i * img[row + i][j + pixel][1]
                    gy_blue_sum += 2 * i * img[row + i][j + pixel][2]

                # Gx
                if i == 0:
                    gy_red_sum += 2 * j * img[row + i][j + pixel][0]
                    gy_green_sum += 2 * j * img[row + i][j + pixel][1]
                    gy_blue_sum += 2 * j * img[row + i][j + pixel][2]
                else:
                    gy_red_sum += 2 * j * img[row + i][j + pixel][0]
                    gy_green_sum += 2 * j * img[row + i][j + pixel][1]
                    gy_blue_sum += 2 * j * img[row + i][j + pixel][2]
        
        new_img[row][pixel][0] = round(sqrt(gx_red_sum ** 2 + gy_red_sum ** 2)) if round(sqrt(gx_red_sum ** 2 + gy_red_sum ** 2)) < 255 else 255
        new_img[row][pixel][1] = round(sqrt(gx_green_sum ** 2 + gy_green_sum ** 2)) if round(sqrt(gx_green_sum ** 2 + gy_green_sum ** 2)) < 255 else 255
        new_img[row][pixel][2] = round(sqrt(gx_blue_sum ** 2 + gy_blue_sum ** 2)) if round(sqrt(gx_blue_sum ** 2 + gy_blue_sum ** 2)) < 255 else 255

cv2.imwrite('edges.jpeg', new_img)