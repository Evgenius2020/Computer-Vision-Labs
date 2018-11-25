import math


def rgb_to_v(rgb):
    r = rgb[0] / 255
    g = rgb[1] / 255
    b = rgb[2] / 255

    return max(r, g, b)


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


def v_to_rgb(v):
    return (v * 255, v * 255, v * 255)
