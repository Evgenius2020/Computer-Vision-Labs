from PIL import Image
import sys
from Otsu import otsu
import Morphology as m
from Color_Mapping import dispatch_colors


def main():
    if (sys.argv.__len__() < 2):
        exit()
    filename = sys.argv[1]
    image = Image.open(filename)
    image.show()

    # image = otsu(image, 7)
    # image.save("binarized.png")
    # # image.show()

    # pattern = m.create_square_pattern(3)
    # image = m.apply_closing(image, pattern)
    # image = m.apply_opening(image, pattern)
    # image.save("processed.png")

    dispatch_colors(image).show()


if __name__ == '__main__':
    main()
