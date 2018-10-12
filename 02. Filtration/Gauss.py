import math


def calculate_kernel(size):
    SIGMA = 1.5
    delta = size // 2
    kernel = [[0] * size] * size

    for y in range(0, size):
        for x in range(0, size):
            kernel[y][x] = 1 / (2 * math.pi * SIGMA ** 2) * \
                math.exp(-((x - delta)**2 + (y - delta)**2) / (2 * SIGMA**2))

    return kernel


def apply_filter(image, filter, size, x, y, x_max, y_max):
    r = g = b = 0
    delta = size // 2

    for i in range(0, size):
        for j in range(0, size):
            if not ((x - delta + j < 0) or (x - delta + j > x_max - 1) or (y - delta + i < 0) or (y - delta + i > y_max - 1)):
                r += filter[i][j] * image[x - delta +
                                          j][y - delta + i][0]
                g += filter[i][j] * image[x - delta +
                                          j][y - delta + i][1]
                b += filter[i][j] * image[x - delta +
                                          j][y - delta + i][2]

    return (math.ceil(r), math.ceil(g), math.ceil(b))


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

    x_max = image.width
    y_max = image.height
    for x in range(0, x_max):
        for y in range(0, y_max):
            pixels[x, y] = apply_filter(
                buf_matr, kernel, kernel_size, x, y, x_max, y_max)

    return filtered_image
