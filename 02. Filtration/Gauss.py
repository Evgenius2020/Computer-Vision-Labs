import math
from Convertations import hsv_to_rgb, rgb_to_hsv
from Filtration import apply_filter

SIGMA = 2


def calculate_kernel(size):
    delta = size // 2
    kernel = [[0] * size] * size
    for y in range(0, size):
        for x in range(0, size):
            kernel[y][x] = 1 / (2 * math.pi * SIGMA ** 2) * \
                math.exp(-((x - delta)**2 + (y - delta)**2) / (2 * SIGMA**2))

    return kernel


def gauss(image, kernel_size):
    assert(kernel_size % 2 == 1)
    kernel = calculate_kernel(kernel_size)
    filtered_image = image.copy()
    pixels = filtered_image.load()
    buf_matr = []

    for x in range(0, image.width):
        buf_matr.append([])
        for y in range(0, image.height):
            buf_matr[x].append(pixels[x, y])

    for x in range(0, image.width):
        for y in range(0, image.height):
            filtereredR = apply_filter(
                buf_matr, kernel, kernel_size, 0, x, y, image.width, image.height)
            filtereredG = apply_filter(
                buf_matr, kernel, kernel_size, 1, x, y, image.width, image.height)
            filtereredB = apply_filter(
                buf_matr, kernel, kernel_size, 2, x, y, image.width, image.height)
            rgb = (math.ceil(filtereredR), math.ceil(
                filtereredG), math.ceil(filtereredB))
            pixels[x, y] = rgb

    return filtered_image
