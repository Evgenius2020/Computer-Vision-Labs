import math
from Filtration import apply_filter
from Convertations import rgb_to_hsv, hsv_to_rgb

sigma_x_matr = ((-1, 0, 1), (-2, 0, 2), (-1, 0, 1))
sigma_y_matr = ((-1, -2, -1), (0, 0, 0), (1, 2, 1))


def filter(image, x, y, x_max, y_max):
    sigma_x = apply_filter(image, sigma_x_matr, 3, 2, x, y, x_max, y_max)
    sigma_y = apply_filter(image, sigma_y_matr, 3, 2, x, y, x_max, y_max)
    return math.sqrt(sigma_x**2 + sigma_y**2)


def sobel(image):
    buf = image.copy()
    pixels = buf.load()
    hsv_matr = []
    for x in range(0, image.width):
        hsv_matr.append([])
        for y in range(0, image.height):
            hsv_matr[x].append(rgb_to_hsv(pixels[x, y]))

    for x in range(0, image.width):
        for y in range(0, image.height):
            filtereredV = filter(hsv_matr, x, y, image.width, image.height)
            pixels[x, y] = hsv_to_rgb((0, 0, filtereredV))

    return buf
