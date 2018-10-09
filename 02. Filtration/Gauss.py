import math
from Convertations import hsv_to_rgb, rgb_to_hsv
from Filtration import extract_piece, apply_filter

SIGMA = 5


def calculate_kernel(size):
    delta = size // 2
    kernel = [[0] * size] * size
    for y in range(0, size):
        for x in range(0, size):
            kernel[x][y] = 1 / (2 * math.pi * SIGMA ** 2) * \
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
            filtereredR = apply_filter(extract_piece(
                buf_matr, kernel_size, 0, x, y, image.width, image.height), kernel, kernel_size)
            filtereredG = apply_filter(extract_piece(
                buf_matr, kernel_size, 1, x, y, image.width, image.height), kernel, kernel_size)
            filtereredB = apply_filter(extract_piece(
                buf_matr, kernel_size, 2, x, y, image.width, image.height), kernel, kernel_size)
            rgb = (math.ceil(filtereredR), math.ceil(
                filtereredG), math.ceil(filtereredB))
            hsv = rgb_to_hsv(rgb)
            hsv[2] += 0.7
            rgb = hsv_to_rgb(hsv)
            pixels[x, y] = rgb

    return filtered_image
