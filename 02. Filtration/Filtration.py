def apply_filter(v_matr, filter, x, y):
    result = 0
    center_x = filter.width // 2
    center_y = filter.height // 2

    for d_y in range(filter.height):
        for d_x in range(filter.width):
            val = v_matr.get(x - center_x + d_x, y - center_y + d_y)
            if val is not None:
                result += filter.raw[d_y][d_x] * val

    return result
