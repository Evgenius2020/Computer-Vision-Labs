import math

def rgb_to_hsv(rgb):
    r = rgb[0] / 360
    g = rgb[1] / 360
    b = rgb[2] / 360

    max_v = max(r, g, b)
    min_v = min(r, g, b)
    delta = max_v - min_v

    if (max_v == min_v):
        h = 0
    elif (max == r):
        if (g >= b):
            h = 60 * (g - b) / delta
        else:
            h = 60 * (g - b) / delta + 360
    elif (max == g):
        h = 60 * (b - r) / delta + 120
    else:
        h = 60 * (r - g) / delta + 240        

    s = 0 if (max_v == 0) else 1 - min_v / max_v
    v = max_v

    return [h, s, v]

def lab_f(x):
    return x**(1 / 3) if (x > (2 / 29)**3) else (1 / 3) *((29 / 6)**2) * x + 4 / 29

def rgb_to_lab(rgb):
    r = rgb[0] / 360
    g = rgb[1] / 360
    b = rgb[2] / 360

    x = 2.768892 * r + 1.751748 * g + 1.13016 * b
    y = r + 4.5907 * g + 0.0601 * b
    z = 0.056508 * g + 5.594292 * b

    x_n = 95.04
    y_n = 100
    z_n = 108.88

    l = 116 * lab_f(y / y_n) - 16
    a = 500 * (lab_f(x / x_n) - lab_f(y / y_n))
    b = 200 * (lab_f(y / y_n) - lab_f(z / z_n))

    return [l, a, b]

def hsv_to_rgb(hsv):
    h = hsv[0]
    s = hsv[1] * 100
    v = hsv[2] * 100

    v_min = (100 - s) * v / 100
    a = (v - v_min) * (h % 60) / 60
    v_inc = v_min + a
    v_dec = v - a

    h_i = [{} for i in range(0, 6)]
    h_i[0]['r'] = v
    h_i[0]['g'] = v_inc
    h_i[0]['b'] = v_min

    h_i[1]['r'] = v_dec
    h_i[1]['g'] = v
    h_i[1]['b'] = v_min

    h_i[2]['r'] = v_min
    h_i[2]['g'] = v
    h_i[2]['b'] = v_inc

    h_i[3]['r'] = v_min
    h_i[3]['g'] = v_dec
    h_i[3]['b'] = v

    h_i[4]['r'] = v_inc
    h_i[4]['g'] = v_min
    h_i[4]['b'] = v

    h_i[5]['r'] = v
    h_i[5]['g'] = v_min
    h_i[5]['b'] = v_dec

    index = math.floor(h / 60) % 6
    r = math.floor(h_i[index]['r'] * 255 / 100)
    g = math.floor(h_i[index]['g'] * 255 / 100)
    b = math.floor(h_i[index]['b'] * 255 / 100)

    return (r, g, b)