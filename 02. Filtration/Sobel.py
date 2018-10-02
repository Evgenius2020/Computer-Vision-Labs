import math

sigma_x_matr = ((-1, 0, 1), (-2, 0, 2), (-1, 0, 1))
sigma_y_matr = ((-1, -2, -1), (0, 0, 0), (1, 2, 1))


def rgb_to_hsv(rgb):
    r = rgb[0] / 256
    g = rgb[1] / 256
    b = rgb[2] / 256

    max_v = max(r, g, b)
    min_v = min(r, g, b)
    delta = max_v - min_v

    if max_v == min_v:
        h = 0
    elif max_v == r:
        if g >= b:
            h = 60 * (g - b) / delta
        else:
            h = 60 * (g - b) / delta + 360
    elif max_v == g:
        h = 60 * (b - r) / delta + 120
    else:
        h = 60 * (r - g) / delta + 240

    s = 0 if max_v == 0 else 1 - min_v / max_v
    v = max_v

    return (h, s, v)


def hsv_to_rgb(hsv):
    h = hsv[0]
    s = hsv[1] * 100
    v = hsv[2] * 100

    v_min = (100 - s) * v / 100
    a = (v - v_min) * (h % 60) / 60
    v_inc = v_min + a
    v_dec = v - a

    index = math.floor(h / 60) % 6
    if (index == 0):
        r = math.floor(v * 255 / 100)
        g = math.floor(v_inc * 255 / 100)
        b = math.floor(v_min * 255 / 100)
    elif (index == 1):
        r = math.floor(v_dec * 255 / 100)
        g = math.floor(v * 255 / 100)
        b = math.floor(v_min * 255 / 100)
    elif (index == 2):
        r = math.floor(v_min * 255 / 100)
        g = math.floor(v * 255 / 100)
        b = math.floor(v_inc * 255 / 100)
    elif (index == 3):
        r = math.floor(v_min * 255 / 100)
        g = math.floor(v_dec * 255 / 100)
        b = math.floor(v * 255 / 100)
    elif (index == 4):
        r = math.floor(v_inc * 255 / 100)
        g = math.floor(v_min * 255 / 100)
        b = math.floor(v * 255 / 100)
    elif (index == 5):
        r = math.floor(v * 255 / 100)
        g = math.floor(v_min * 255 / 100)
        b = math.floor(v_dec * 255 / 100)

    return (r, g, b)


def extract_I(image_hsv, x, y, x_max, y_max):
    I = ([0, 0, 0], [0, 0, 0], [0, 0, 0])
    for i in range(0, 3):
        for j in range(0, 3):
            if (x - 1 + j < 0) or (x + j > x_max) or (y - 1 + i < 0) or (y + i > y_max):
                I[i][j] = 0
            else:
                assert (image_hsv[x - 1 + j][y - 1 + i][2] <= 1)
                I[i][j] = image_hsv[x - 1 + j][y - 1 + i][2]
                assert (I[i][j] <= 1)
    return I


def matr_x_sigma(matr, sigma):
    result = 0
    for i in range(0, 9):
        result += matr[i // 3][i % 3] * sigma[i // 3][i % 3]
    return result


def filter(I):
    sigma_x = matr_x_sigma(I, sigma_x_matr)
    sigma_y = matr_x_sigma(I, sigma_y_matr)
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
            filtereredV = filter(
                extract_I(hsv_matr, x, y, image.width, image.height))
            # pixels[y, x] = hsv_to_rgb(
            #   (hsv_matr[y][x][0], hsv_matr[y][x][1], filtereredV))
            pixels[x, y] = hsv_to_rgb((0, 0, filtereredV))

    return buf
