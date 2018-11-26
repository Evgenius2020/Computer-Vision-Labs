from Matrix import Matrix
from Convertations import hsv_to_rgb, rgb_to_v


def dispatch_colors(image):
    image = image.copy()
    pixels = image.load()
    v_matr = Matrix(image.width, image.height)
    v_matr.apply(lambda x, y: int(rgb_to_v(pixels[x, y])))

    colors = Matrix(v_matr.width, v_matr.height)
    curr_color = 1

    for y in range(colors.height):
        for x in range(colors.width):
            if (v_matr.raw[y][x] == 0):
                continue
            neighbours = ((x - 1, y - 1), (x, y - 1),
                          (x + 1, y - 1), (x - 1, y))
            color = None
            for (n_x, n_y) in neighbours:
                neighbour_color = colors.get(n_x, n_y)
                if neighbour_color is not None and neighbour_color != 0:
                    color = neighbour_color
                    break

            if color is None:
                colors.raw[y][x] = curr_color
                curr_color += 1
            else:
                colors.raw[y][x] = color

    color_mapping = [cl_n for cl_n in range(curr_color)]

    def get_mapping(cl):
        while color_mapping[cl] != cl:
            cl = color_mapping[cl]
        return cl

    for y in range(colors.height):
        for x in range(colors.width):
            if (v_matr.raw[y][x] == 0):
                continue
            neighbours = colors.get_neighbours(x, y)

            min_color = get_mapping(colors.raw[y][x])
            for (n_x, n_y) in neighbours:
                if v_matr.raw[n_y][n_x] != 0:
                    min_color = min(
                        get_mapping(colors.raw[n_y][n_x]), min_color)
            neighbours.append((x, y))
            for (n_x, n_y) in neighbours:
                if v_matr.raw[n_y][n_x] != 0:
                    color_mapping[get_mapping(
                        colors.raw[n_y][n_x])] = get_mapping(min_color)

    changed = 0
    for cl in range(curr_color):
        if color_mapping[cl] != cl:
            changed += 1
    print(color_mapping.__len__())
    print(changed)

    color_scale_coef = 359 / color_mapping.__len__() - changed
    for y in range(image.height):
        for x in range(image.width):
            color = get_mapping(colors.raw[y]
                                [x]) * color_scale_coef
            pixels[x, y] = hsv_to_rgb(
                (color, 1, v_matr.raw[y][x]))

    return image
