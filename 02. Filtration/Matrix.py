class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.raw = [[0 for x in range(width)] for y in range(height)]

    def get(self, x, y):
        if ((x < 0) or (x > self.width - 1) or
                (y < 0) or (y > self.height - 1)):
            return None
        return self.raw[y][x]

    def apply(self, func):
        for y in range(self.height):
            for x in range(self.width):
                self.raw[y][x] = func(x, y)

    def get_neighbours(self, x, y):
        neigbours = []

        for d_x in range(-1, 2, 1):
            for d_y in range(-1, 2, 1):
                if self.get(x + d_x, y + d_y) is not None:
                    neigbours.append((x + d_x, y + d_y))

        return neigbours
