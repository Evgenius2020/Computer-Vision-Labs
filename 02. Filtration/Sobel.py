import math
from Filtration import apply_filter
from Convertations import hsv_to_rgb, rgb_to_v, rgb_to_hsv

sigma_x_matr = ((-1, 0, 1), (-2, 0, 2), (-1, 0, 1))
sigma_y_matr = ((-1, -2, -1), (0, 0, 0), (1, 2, 1))


def filter(image, x, y, x_max, y_max):
    sigma_x = apply_filter(image, sigma_x_matr, 3, x, y, x_max, y_max)
    sigma_y = apply_filter(image, sigma_y_matr, 3, x, y, x_max, y_max)
    return math.sqrt(sigma_x**2 + sigma_y**2)


def sobel(image):
    im_copy = image.copy()
    pixels = im_copy.load()
    x_max = image.width
    y_max = image.height
    v_matr = []

    for y in range(0, y_max):
        v_matr.append([])
        for x in range(0, x_max):
            v_matr[y].append(rgb_to_v(pixels[x, y]))

    for y in range(0, y_max):
        for x in range(0, x_max):
            filtereredV = filter(v_matr, x, y, x_max, y_max)
            pixels[x, y] = hsv_to_rgb((0, 0, filtereredV))

    return im_copy
