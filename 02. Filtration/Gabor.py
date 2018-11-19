import math
import sys

from PIL import Image

from Convertations import hsv_to_rgb, rgb_to_v
from Filtration import apply_filter
from Matrix import Matrix


def gabor_filter_func(x, y, gamma, lam, theta, phi, sigma):
    theta_sin = math.sin(theta)
    theta_cos = math.cos(theta)
    x_stroke = x * theta_cos + y * theta_sin
    y_stroke = -x * theta_sin + y * theta_cos

    return \
        math.exp(-1/2 * (x_stroke**2 + (gamma*y_stroke)**2)/sigma**2) * \
        math.cos(2*math.pi/lam*x_stroke + phi)


def init_filter(gamma, lam, theta, phi, sigma):
    # size_x = int(6 * sigma)
    # size_x = size_x - size_x // 2 + 1
    # size_y = int(6 * sigma / gamma)
    # size_y = size_y - size_y % 2 + 1
    size_x = 3
    size_y = 3
    center_x = size_x // 2
    center_y = size_x // 2

    filter = Matrix(size_x, size_y)
    filter.apply(lambda x, y: gabor_filter_func(
        x - center_x, y - center_y, gamma, lam, theta, phi, sigma))

    return filter


def gabor(image, gamma, lam, theta, phi, sigma):
    image = image.copy()
    pixels = image.load()

    height = image.height
    width = image.width
    v_matr = Matrix(width, height)
    v_matr.apply(lambda x, y: rgb_to_v(pixels[x, y]))

    filter = init_filter(gamma, lam, theta, phi, sigma)
    v_matr_filtered = Matrix(width, height)
    v_matr_filtered.apply(lambda x, y: apply_filter(v_matr, filter, x, y))

    for y in range(height):
        for x in range(width):
            pixels[x, y] = hsv_to_rgb((0, 0, v_matr_filtered.raw[y][x]))

    return image


def main():
    if (sys.argv.__len__() < 2):
        exit()
    filename = sys.argv[1]
    image = Image.open(filename)
    gabor(image, 0.1, 2, 0, 0, 1.12).show()
    gabor(image, 0.1, 2, math.pi / 4, 0, 1.12).show()
    gabor(image, 0.1, 2, math.pi / 2, 0, 1.12).show()
    gabor(image, 0.1, 2, math.pi / 4 * 3, 0, 1.12).show()


if __name__ == '__main__':
    main()
