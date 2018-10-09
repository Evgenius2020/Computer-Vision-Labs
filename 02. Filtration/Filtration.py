def extract_piece(image, size, pixel_component, x, y, x_max, y_max):
    piece = [[0] * size] * size
    delta = size // 2
    for i in range(0, size):
        for j in range(0, size):
            if (x - delta + j < 0) or (x - delta + j > x_max - 1) or (y - delta + i < 0) or (y - delta + i > y_max - 1):
                piece[i][j] = 0
            else:
                piece[i][j] = image[x - delta + j][y - delta + i][pixel_component]
    return piece


def apply_filter(matr, filter, size):
    result = 0
    for i in range(0, size ** 2):
        result += matr[i // size][i % size] * filter[i // size][i % size]
    return result
