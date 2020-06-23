import numpy as np
import cv2

IMAGE_FILE = 'IMAGE.jpeg'
img = cv2.imread(IMAGE_FILE)
new_img = np.copy(img)

# the height is equal to the width
def get_surrounding_pixels(img, height, current_pixel_row, current_pixel_index):
    """returns the surrounding pixels of a certain pixel, including the pixel itself"""

    height_half = int(height/2)

    if current_pixel_row < height_half or current_pixel_index < height_half or current_pixel_index + height_half >= len(img[0]) or current_pixel_row + height_half >= len(img):
        return None

    # print(f'row: {current_pixel_row}, pixel: {current_pixel_index} => can be handeled')
    surrounding_pixels = []
    i = -height_half
    for j in range(height):
        # ----------
        # |**|  |  |
        # |  |**|  |
        # |  |  |**|
        # ----------
        if current_pixel_row + i + j != current_pixel_row and current_pixel_index + i + j != current_pixel_index:
            # checking that the current pixel is not the center pixel
            surrounding_pixels.append(img[current_pixel_row + i + j][current_pixel_index + i + j])

        # ----------
        # |  |  |**|
        # |  |**|  |
        # |**|  |  |
        # ----------
        if current_pixel_row + i + j != current_pixel_row and height + (current_pixel_index + i - j) - 1 != current_pixel_index:
            surrounding_pixels.append(img[current_pixel_row + i + j][height + (current_pixel_index + i - j) - 1])

    for j in range(1, height - 1):
        # ----------
        # |  |  |  |
        # |**|  |  |
        # |  |  |  |
        # ----------
        surrounding_pixels.append(img[current_pixel_row + i + j][current_pixel_index + i])

        # ----------
        # |  |  |  |
        # |  |  |**|
        # |  |  |  |
        # ----------
        surrounding_pixels.append(img[current_pixel_row + i + j][current_pixel_index - i])

    for j in range(1, height - 1):
        # ----------
        # |  |**|  |
        # |  |  |  |
        # |  |  |  |
        # ----------
        surrounding_pixels.append(img[current_pixel_row + i][current_pixel_index + i + j])

        # ----------
        # |  |  |  |
        # |  |  |  |
        # |  |**|  |
        # ----------
        surrounding_pixels.append(img[current_pixel_row - i][current_pixel_index + i + j])

    for j in range(1, height-1):
        # ----------------
        # |  |  |  |  |  |
        # |  |  |  |  |  |
        # |  |**|  |**|  |
        # |  |  |  |  |  |
        # |  |  |  |  |  |
        # ----------------
        if current_pixel_index + i + j != current_pixel_index:
            surrounding_pixels.append(img[current_pixel_row][current_pixel_index + i + j])

        # ----------------
        # |  |  |  |  |  |
        # |  |  |**|  |  |
        # |  |  |  |  |  |
        # |  |  |**|  |  |
        # |  |  |  |  |  |
        # ----------------
        if current_pixel_row + i + j != current_pixel_row:
            surrounding_pixels.append(img[current_pixel_row + i + j][current_pixel_index])

    # appending the current center pixel to the array
    surrounding_pixels.append(img[current_pixel_row][current_pixel_index])

    return surrounding_pixels


for row in range(len(img)):
    for pixel in range(len(img[row])):
        # the 11 is the number of the pixels that the surrounding square consists of (11*11)
        # and that square is the one which will determine this pixel color, and by the increase
        # of this number the blur effect will increase too
        surrounding_pixels = get_surrounding_pixels(img, 11, row, pixel)
        if surrounding_pixels:
            pixels_count = len(surrounding_pixels)
            
            red_sum = sum([ p[0] for p in surrounding_pixels ])
            green_sum = sum([ p[1] for p in surrounding_pixels ])
            blue_sum = sum([ p[2] for p in surrounding_pixels ])

            red_avg = red_sum / pixels_count
            green_avg = green_sum / pixels_count
            blue_avg = blue_sum / pixels_count

            new_img[row][pixel][0] = red_avg
            new_img[row][pixel][1] = green_avg
            new_img[row][pixel][2] = blue_avg


cv2.imwrite('blur.jpeg', new_img)