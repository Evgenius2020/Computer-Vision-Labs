from Sobel import sobel_vectors, sobel
from Gauss import gauss
from Convertations import hsv_to_rgb
import math


def cmp_direction(vec_matr, x, y, delta_x, delta_y, x_max, y_max):
    if ((x + delta_x < 0) or (x + delta_x > x_max - 1) or (y + delta_y < 0) or (y + delta_y > y_max - 1)):
        return vec_matr[y][x][0]
    else:
        return 0 if (vec_matr[y + delta_y][x + delta_x][0] > vec_matr[y][x][0]) else vec_matr[y][x][0]


def filter_non_maximum(vec_matr, x, y, x_max, y_max):
    angle = vec_matr[y][x][1] * 180 / math.pi
    angle = (angle // 45) * 45 + 180
    if angle == 0:
        return cmp_direction(vec_matr, x, y, 0, -1, x_max, y_max)
    elif angle == 45:
        return cmp_direction(vec_matr, x, y, 1, -1, x_max, y_max)
    elif angle == 90:
        return cmp_direction(vec_matr, x, y, 1, 0, x_max, y_max)
    elif angle == 135:
        return cmp_direction(vec_matr, x, y, 1, 1, x_max, y_max)
    elif angle == 180:
        return cmp_direction(vec_matr, x, y, 0, 1, x_max, y_max)
    elif angle == 225:
        return cmp_direction(vec_matr, x, y, -1, 1, x_max, y_max)
    elif angle == 270:
        return cmp_direction(vec_matr, x, y, -1, 0, x_max, y_max)
    elif angle == 315:
        return cmp_direction(vec_matr, x, y, -1, 1, x_max, y_max)


def canny(image, gauss_kernel_size, gauss_sigma):
    image = gauss(image, gauss_kernel_size, gauss_sigma)
    pixels = image.load()
    vec_matr = sobel_vectors(image)

    x_max = image.width
    y_max = image.height
    v_matr = []
    for y in range(0, y_max):
        v_matr.append([])
        for x in range(0, x_max):
            v_matr[y].append(filter_non_maximum(vec_matr, x, y, x_max, y_max))

    for y in range(0, y_max):
        for x in range(0, x_max):
            pixels[x, y] = hsv_to_rgb((0, 0, v_matr[y][x]))

    return image
