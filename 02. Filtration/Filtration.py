

def apply_filter(v_matr, filter, filter_size, x, y):
    result = 0
    center = filter_size // 2
    for d_y in range(filter_size):
        for d_x in range(filter_size):
            val = v_matr.get(x + d_x, y + d_y)
            if val is not None:
                result += filter[d_y][d_x] * \
                    v_matr.raw[y - center + d_y][x - center + d_x]

    return result
