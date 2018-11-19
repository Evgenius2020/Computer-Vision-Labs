import sys
from PIL import Image
from Sobel import sobel
from Gauss import gauss
from Canny import canny


def main():
    if (sys.argv.__len__() < 2):
        exit()
    filename = sys.argv[1]
    image = Image.open(filename)

    sobel(image).show()
    gauss(image, 15, 1.8).show()
    canny(image, 15, 2).show()


if __name__ == '__main__':
    main()
