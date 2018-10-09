def extract_piece(image_hsv, size, x, y, x_max, y_max):
    assert(size % 2 == 1)
    piece = [[0] * size] * size
    delta = size // 2
    for i in range(0, size):
        for j in range(0, size):
            if (x - delta + j < 0) or (x - delta + j > x_max - 1) or (y - delta + i < 0) or (y - delta + i > y_max - 1):
                piece[i][j] = 0
            else:
                piece[i][j] = image_hsv[x - delta + j][y - delta + i][2]
    return piece


def apply_filter(matr, filter, size):
    result = 0
    for i in range(0, size ** 2):
        result += matr[i // size][i % size] * filter[i // size][i % size]
    return result
