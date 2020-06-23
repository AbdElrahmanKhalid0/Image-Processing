import numpy as np
import cv2

IMAGE_FILE = 'IMAGE.jpeg'
img = cv2.imread(IMAGE_FILE)
new_img = np.copy(img)

for row in range(len(img)):
    for pixel in range(len(img[row])):
        ### the graph
        # upper_left = img[row-1][pixel-1]
        # upper = img[row-1][pixel]
        # upper_right = img[row-1][pixel+1]
        # right = img[row][pixel+1]
        # lower_right = img[row+1][pixel+1]
        # lower = img[row+1][pixel]
        # lower_left = img[row+1][pixel-1]
        # left = img[row][pixel-1]

        # surrounding_pixels = [upper_left if  row > 0 and pixel > 0 else None,
        #                       upper if row > 0 else None,
        #                       upper_right if row > 0 and pixel < len(img[row]) - 1 else None,
        #                       right if pixel < len(img[row]) - 1,
        #                       lower_right if pixel < len(img[row]) and row < len(img) - 1,
        #                       lower if row < len(img) - 1,
        #                       lower_left if row < len(img) - 1 and pixel > 0,
        #                       left if pixel > 0
        #                     ]

        surrounding_pixels = [img[row-1][pixel-1] if  row > 0 and pixel > 0 else None,
                              img[row-1][pixel] if row > 0 else None,
                              img[row-1][pixel+1] if row > 0 and pixel < len(img[row]) - 1 else None,
                              img[row][pixel+1] if pixel < len(img[row]) - 1 else None,
                              img[row+1][pixel+1] if pixel < len(img[row]) - 1 and row < len(img) - 1 else None,
                              img[row+1][pixel] if row < len(img) - 1 else None,
                              img[row+1][pixel-1] if row < len(img) - 1 and pixel > 0 else None,
                              img[row][pixel-1] if pixel > 0 else None
                            ]

        none_count = len([ n for n in surrounding_pixels if n is None ])
        # the added one pixel is for the current pixel itself
        pixels_count = len(surrounding_pixels) + 1 - none_count
        
        red_sum = sum([ p[0] for p in surrounding_pixels + [img[row][pixel]] if p is not None ])
        green_sum = sum([ p[1] for p in surrounding_pixels + [img[row][pixel]] if p is not None ])
        blue_sum = sum([ p[2] for p in surrounding_pixels + [img[row][pixel]] if p is not None ])

        red_avg = red_sum / pixels_count
        green_avg = green_sum / pixels_count
        blue_avg = blue_sum / pixels_count

        new_img[row][pixel][0] = red_avg
        new_img[row][pixel][1] = green_avg
        new_img[row][pixel][2] = blue_avg

        

            

cv2.imwrite('blur.jpeg', new_img)