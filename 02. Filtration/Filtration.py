def apply_component_filter(image, filter, size, pixel_component, x, y, x_max, y_max):
    result = 0
    delta = size // 2
    for i in range(0, size):
        for j in range(0, size):
            if not ((x - delta + j < 0) or (x - delta + j > x_max - 1) or (y - delta + i < 0) or (y - delta + i > y_max - 1)):
                result += filter[i][j] * image[y - delta +
                                               i][x - delta + j][pixel_component]
    return result


def apply_filter(image, filter, size, x, y, x_max, y_max):
    result = 0
    delta = size // 2
    for i in range(0, size):
        for j in range(0, size):
            if not ((x - delta + j < 0) or (x - delta + j > x_max - 1) or (y - delta + i < 0) or (y - delta + i > y_max - 1)):
                result += filter[i][j] * image[y - delta + i][x - delta + j]
    return result
