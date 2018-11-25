from Matrix import Matrix
from Convertations import rgb_to_v, v_to_rgb


def create_rectangle_pattern(width, height):
    rectangle_pattern = Matrix(width, height)
    rectangle_pattern.raw = [[1 for x in range(width)] for y in range(height)]
    return rectangle_pattern


def create_square_pattern(size):
    return create_rectangle_pattern(size, size)


disk_pattern = Matrix(5, 5)
disk_pattern.raw = [[0, 1, 1, 1, 0], [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0]]

cross_pattern = Matrix(3, 3)
cross_pattern.raw = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]


def apply_dilation(image, pattern):
    image = image.copy()
    pixels = image.load()
    v_matr = Matrix(image.width, image.height)
    v_matr.apply(lambda x, y: int(rgb_to_v(pixels[x, y])))

    new_v_matr = Matrix(image.width, image.height)
    for c_y in range(v_matr.height):
        for c_x in range(v_matr.width):
            neighbours = v_matr.get_neighbours(
                c_x, c_y, pattern.width, pattern.height)

            for (x, y) in neighbours:
                if (v_matr.raw[y][x] == 0):
                    continue
                p_x = pattern.width // 2 + c_x - x
                p_y = pattern.height // 2 + c_y - y
                if pattern.raw[p_y][p_x] == 1:
                    new_v_matr.raw[c_y][c_x] = 1
                    break

    for y in range(v_matr.height):
        for x in range(v_matr.width):
            pixels[x, y] = v_to_rgb(new_v_matr.raw[y][x])

    return image


def apply_erosion(image, pattern):
    image = image.copy()
    pixels = image.load()
    v_matr = Matrix(image.width, image.height)
    v_matr.apply(lambda x, y: int(rgb_to_v(pixels[x, y])))

    new_v_matr = Matrix(image.width, image.height)
    for c_y in range(v_matr.height):
        for c_x in range(v_matr.width):
            if v_matr.raw[c_y][c_x] == 0:
                continue

            neighbours = v_matr.get_neighbours(
                c_x, c_y, pattern.width, pattern.height)

            new_v_matr.raw[c_y][c_x] = 1
            for (x, y) in neighbours:
                p_x = pattern.width // 2 + c_x - x
                p_y = pattern.height // 2 + c_y - y
                if pattern.raw[p_y][p_x] == 0:
                    continue
                if v_matr.raw[y][x] == 0:
                    new_v_matr.raw[c_y][c_x] = 0
                    break

    for y in range(v_matr.height):
        for x in range(v_matr.width):
            pixels[x, y] = v_to_rgb(new_v_matr.raw[y][x])

    return image


def apply_closing(image, pattern):
    return apply_erosion(apply_dilation(image, pattern), pattern)


def apply_opening(image, pattern):
    return apply_dilation(apply_erosion(image, pattern), pattern)
