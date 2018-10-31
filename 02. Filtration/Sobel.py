import math
from Filtration import apply_filter
from Convertations import hsv_to_rgb, rgb_to_v
from Matrix import Matrix

sigma_x_matr = ((-1, 0, 1), (-2, 0, 2), (-1, 0, 1))
sigma_y_matr = ((-1, -2, -1), (0, 0, 0), (1, 2, 1))


def filter_value(image, x, y):
    sigma_x = apply_filter(image, sigma_x_matr, 3, x, y)
    sigma_y = apply_filter(image, sigma_y_matr, 3, x, y)
    
    return math.sqrt(sigma_x**2 + sigma_y**2)


def filter_vector(image, x, y):
    sigma_x = apply_filter(image, sigma_x_matr, 3, x, y)
    sigma_y = apply_filter(image, sigma_y_matr, 3, x, y)
    value = math.sqrt(sigma_x**2 + sigma_y**2)
    angle = get_angle(x, y)

    return (value, angle)


def get_angle(x, y):
    len = math.sqrt(x**2 + y**2)
    angle = 0 if len == 0 else math.acos(x / len)
    
    if (y >= 0):
        return angle
    else:
        return 2*math.pi - angle


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

    for y in range(y_max):
        for x in range(x_max):
            v_matr.raw[y][x] = rgb_to_v(pixels[x, y])

    for y in range(y_max):
        for x in range(x_max):
            vectors.raw[y][x] = filter_vector(v_matr, x, y)

    return vectors
