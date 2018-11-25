from Sobel import sobel_vectors
from Gauss import gauss
from Convertations import hsv_to_rgb
from Matrix import Matrix
import math


def cmp_direction(vec_matr, x, y, d_x1, d_y1, d_x2, d_y2):
    v1 = vec_matr.get(x + d_x1, y + d_y1)
    v2 = vec_matr.get(x + d_x2, y + d_y2)
    if v1 is None:
        v1 = 0
    else:
        v1 = v1[0]

    if v2 is None:
        v2 = 0
    else:
        v2 = v2[0]

    return vec_matr.raw[y][x][0] \
        if (v1 < vec_matr.raw[y][x][0] and vec_matr.raw[y][x][0] > v2) else \
        0


def filter_non_maximum(vec_matr, x, y):
    return 0 if vec_matr.raw[y][x][0] < 0.2 else vec_matr.raw[y][x][0]
    angle = vec_matr.raw[y][x][1] * 180 / math.pi
    angle = (angle // 45) * 45 + 180
    if angle == 0 or angle == 360:
        return cmp_direction(vec_matr, x, y, 0, -1, 0, 1)
    elif angle == 45:
        return cmp_direction(vec_matr, x, y, 1, -1, -1, 1)
    elif angle == 90:
        return cmp_direction(vec_matr, x, y, 1, 0, -1, 0)
    elif angle == 135:
        return cmp_direction(vec_matr, x, y, 1, 1, -1, -1)
    elif angle == 180:
        return cmp_direction(vec_matr, x, y, 0, 1, 0, -1)
    elif angle == 225:
        return cmp_direction(vec_matr, x, y, -1, 1, 1, -1)
    elif angle == 270:
        return cmp_direction(vec_matr, x, y, -1, 0, 1, 0)
    elif angle == 315:
        return cmp_direction(vec_matr, x, y, -1, 1, 1, -1)
    else:
        print(angle)
        return cmp_direction(vec_matr, x, y, 0, -1)


def dispatch_colors(v_matr):
    colors = Matrix(v_matr.width, v_matr.height)
    curr_color = 1
    conflicts = []

    for y in range(0, colors.height):
        for x in range(0, colors.width):
            if (v_matr.raw[y][x] == 0):
                continue
            neighbours_colors = set()
            neighbours = ((x - 1, y - 1), (x, y - 1),
                          (x + 1, y - 1), (x - 1, y))
            for (neighbour_x, neigbour_y) in neighbours:
                neighbour_color = colors.get(neighbour_x, neigbour_y)
                if neighbour_color is not None and neighbour_color != 0:
                    neighbours_colors.add(neighbour_color)
            if neighbours_colors.__len__() == 0:
                colors.raw[y][x] = curr_color
                curr_color += 1
            elif neighbours_colors.__len__() == 1:
                colors.raw[y][x] = neighbours_colors.pop()
            else:
                conflicts.append((x, y))

    # print(curr_color)
    color_mapping = [cl_n for cl_n in range(curr_color)]
    # print(conflicts.__len__())
    for (x, y) in conflicts:
        neighbours = colors.get_neighbours(x, y)
        min_color = None
        for (neighbour_x, neighbour_y) in neighbours:
            neighbour_color = colors.raw[neighbour_y][neighbour_x]
            if neighbour_color == 0:
                continue
            mapped_color = color_mapping[neighbour_color]
            if (min_color is None or mapped_color < min_color):
                min_color = mapped_color
        for (neighbour_x, neighbour_y) in neighbours:
            mapped_color = color_mapping[colors.raw[neigbour_y][neighbour_x]]
            color_mapping[mapped_color] = min_color
        colors.raw[y][x] = min_color

    changed = 0
    for cl in range(curr_color):
        if color_mapping[cl] != cl:
            changed += 1
    # print(changed)

    return colors, color_mapping, color_mapping.__len__() - changed


def canny(image, gauss_kernel_size, gauss_sigma):
    image = gauss(image, gauss_kernel_size, gauss_sigma)
    pixels = image.load()
    vec_matr = sobel_vectors(image)

    x_max = image.width
    y_max = image.height
    v_matr = Matrix(image.width, image.height)
    for y in range(v_matr.height):
        for x in range(v_matr.width):
            v_matr.raw[y][x] = filter_non_maximum(vec_matr, x, y)

    color_matr, color_mapping, colors_n = dispatch_colors(v_matr)
    # print(colors_n)
    color_scale_coef = 360 / colors_n
    for y in range(0, y_max):
        for x in range(0, x_max):
            color = color_mapping[color_matr.raw[y]
                                  [x]] * color_scale_coef
            pixels[x, y] = hsv_to_rgb(
                (color, 1, 1 if v_matr.raw[y][x] > 0 else 0))

    return image
