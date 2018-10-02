import sys
from PIL import Image
from Sobel import sobel


def main():
    if (sys.argv.__len__() < 2):
        exit()
    filename = sys.argv[1]
    lenna = Image.open(filename)
    sobel(lenna).show()


if __name__ == '__main__':
    main()
