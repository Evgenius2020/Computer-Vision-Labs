from Matrix import Matrix
from Convertations import hsv_to_rgb, rgb_to_v


def dispatch_colors(image):
    image = image.copy()
    pixels = image.load()
    v_matr = Matrix(image.width, image.height)
    v_matr.apply(lambda x, y: int(rgb_to_v(pixels[x, y])))

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

    color_mapping = [cl_n for cl_n in range(curr_color)]
    for (x, y) in conflicts:
        neighbours = colors.get_neighbours(x, y)
        min_color = None
        for (neighbour_x, neighbour_y) in neighbours:
            neighbour_color = colors.raw[neighbour_y][neighbour_x]
            if neighbour_color == 0:
                continue
            neighbour_color = color_mapping[neighbour_color]
            if (min_color is None or neighbour_color < min_color):
                min_color = neighbour_color
        for (neighbour_x, neighbour_y) in neighbours:
            neighbour_color = color_mapping[colors.raw[neigbour_y][neighbour_x]]
            if neighbour_color == 0:
                continue
            color_mapping[neighbour_color] = min_color
        colors.raw[y][x] = min_color

    changed = 0
    for cl in range(curr_color):
        if color_mapping[cl] != cl:
            changed += 1
    print(color_mapping.__len__())
    print(changed)

    color_scale_coef = 359 / color_mapping.__len__() - changed
    for y in range(0, image.height):
        for x in range(0, image.width):
            color = color_mapping[colors.raw[y]
                                  [x]] * color_scale_coef
            pixels[x, y] = hsv_to_rgb(
                (color, 1, v_matr.raw[y][x]))

    return image
