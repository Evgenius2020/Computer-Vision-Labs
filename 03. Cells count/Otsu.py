import sys
import math

from Convertations import rgb_to_v, v_to_rgb
from PIL import Image
from Matrix import Matrix


def otsu(image, levels):
    image = image.copy()
    pixels = image.load()

    height = image.height
    width = image.width
    v_matr = Matrix(width, height)
    v_matr.apply(lambda x, y: rgb_to_v(pixels[x, y]))

    p_vec = [0 for i in range(levels + 1)]
    for y in range(height):
        for x in range(width):
            p_vec[math.floor(v_matr.raw[y][x] * levels)] += 1

    n_vec = []
    n_t = 0
    mu_t = 0
    for i in range(levels):
        if p_vec[i] == 0:
            continue
        n_t += p_vec[i]
        n = p_vec[i] / (width * height)
        n_vec.append(n)
        mu_t += (i+1) * n
    levels = n_vec.__len__()

    sigma_vec = [0 for i in range(levels)]
    for t in range(1, levels):
        w1_t = 0
        for i in range(t):
            w1_t += n_vec[i]
        w2_t = 1 - w1_t

        mu1_t = 0
        for i in range(t):
            mu1_t += (i+1) * n_vec[i]
        mu1_t /= w1_t
        mu2_t = (mu_t - mu1_t * w1_t) / w2_t

        sigma_vec[t] = w1_t * w2_t * (mu1_t - mu2_t) ** 2

    max_t = None
    max_sigma = 0
    for t in range(levels):
        if max_t is None or sigma_vec[t] > max_sigma:
            max_t = t

    threshold = t / levels
    for y in range(height):
        for x in range(width):
            pixels[x, y] = v_to_rgb(
                int(1) if v_matr.raw[y][x] < threshold else int(0))

    return image


def main():
    if (sys.argv.__len__() < 2):
        exit()
    filename = sys.argv[1]
    image = Image.open(filename)
    otsu(image, 10).show()


if __name__ == '__main__':
    main()
