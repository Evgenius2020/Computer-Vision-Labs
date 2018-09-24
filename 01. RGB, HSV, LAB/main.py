import os
import time
import sys
import pygame
from draw_histogram import draw_histogram
from convertations import rgb_to_hsv, rgb_to_lab
from hsv_change import hsv_change, h_plus, h_minus, s_plus, s_minus, v_plus, v_minus


def print_cordinates(caption, coordinates):
    print('{0}: [{1}]'.format(caption, ", ".join(str(x) for x in coordinates)))


def add_button(surface, x_start, text, color):
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    button = pygame.Rect(x_start, 0, 30, 20)
    pygame.draw.rect(surface, color, button)
    surface.blit(myfont.render(text, False, (0, 0, 0)), (x_start, 0))
    return button


def main():
    pygame.init()
    lenna = pygame.image.load("Lenna.png")
    surface = pygame.display.set_mode((lenna.get_width(), lenna.get_height()))
    surface.blit(lenna, (0, 0))

    button_h_plus = add_button(surface, 0, "H+", [255, 0, 0])
    button_h_minus = add_button(surface, 30, "H-", [255, 50, 0])
    button_s_plus = add_button(surface, 70, "S+", [255, 100, 0])
    button_s_minus = add_button(surface, 100, "S-", [255, 150, 0])
    button_v_plus = add_button(surface, 140, "V+", [255, 200, 0])
    button_v_minus = add_button(surface, 170, "V-", [255, 250, 0])

    pygame.display.update()
    draw_histogram(surface)

    while True:
        os.system('clear')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_h_plus.collidepoint(mouse_pos):
                    hsv_change(surface, h_plus)
                elif button_h_minus.collidepoint(mouse_pos):
                    hsv_change(surface, h_minus)
                elif button_s_plus.collidepoint(mouse_pos):
                    hsv_change(surface, s_plus)
                elif button_s_minus.collidepoint(mouse_pos):
                    hsv_change(surface, s_minus)
                elif button_v_plus.collidepoint(mouse_pos):
                    hsv_change(surface, v_plus)
                elif button_v_minus.collidepoint(mouse_pos):
                    hsv_change(surface, v_minus)

                pygame.display.update()
                draw_histogram(surface)

        rgb = surface.get_at(pygame.mouse.get_pos())
        print_cordinates("RGB", rgb)
        print_cordinates("HSV", rgb_to_hsv(rgb))
        print_cordinates("LAB", rgb_to_lab(rgb))
        time.sleep(0.1)


if __name__ == '__main__':
    main()
