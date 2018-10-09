import math

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
