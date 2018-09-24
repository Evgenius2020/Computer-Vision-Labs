import matplotlib.pyplot as plt
from convertations import rgb_to_lab


def draw_histogram(surface):
    pixels_l = []
    for y in range(0, surface.get_height()):
        for x in range(0, surface.get_width()):
            rgb = surface.get_at([x, y])
            pixels_l.append(rgb_to_lab(rgb)[0])
    plt.hist(pixels_l, 100)
    plt.show()
