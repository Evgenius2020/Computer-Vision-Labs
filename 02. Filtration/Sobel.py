import math
from Filtration import apply_filter
from Convertations import hsv_to_rgb, rgb_to_v
from Matrix import Matrix

sigma_x_matr = Matrix(3, 3)
sigma_y_matr = Matrix(3, 3)
sigma_x_matr.raw = ((-1, 0, 1), (-2, 0, 2), (-1, 0, 1))
sigma_y_matr.raw = ((-1, -2, -1), (0, 0, 0), (1, 2, 1))


def filter_value(image, x, y):
    sigma_x = apply_filter(image, sigma_x_matr, x, y)
    sigma_y = apply_filter(image, sigma_y_matr, x, y)

    return math.sqrt(sigma_x**2 + sigma_y**2)


def filter_vector(image, x, y):
    sigma_x = apply_filter(image, sigma_x_matr, x, y)
    sigma_y = apply_filter(image, sigma_y_matr, x, y)
    value = math.sqrt(sigma_x**2 + sigma_y**2)
    angle = get_angle(sigma_x, sigma_y)

    return (value, angle)


def get_angle(x, y):
    norm = math.sqrt(x**2 + y**2)
    return 0 if norm == 0 else math.acos(x / norm)


def sobel(image):
    im_copy = image.copy()
    pixels = im_copy.load()
    x_max = image.width
    y_max = image.height
    v_matr = Matrix(x_max, y_max)

    for y in range(y_max):
        for x in range(x_max):
            v_matr.raw[y][x] = rgb_to_v(pixels[x, y])

    for y in range(y_max):
        for x in range(x_max):
            filtereredV = filter_value(v_matr, x, y)
            pixels[x, y] = hsv_to_rgb((0, 0, filtereredV))

    return im_copy


def sobel_vectors(image):
    pixels = image.copy().load()
    x_max = image.width
    y_max = image.height
    vectors = Matrix(x_max, y_max)
    v_matr = Matrix(x_max, y_max)
    v_matr.apply(lambda x, y: rgb_to_v(pixels[x, y]))

    for y in range(y_max):
        for x in range(x_max):
            vectors.raw[y][x] = filter_vector(v_matr, x, y)

    return vectors
