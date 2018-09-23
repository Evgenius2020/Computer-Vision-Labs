from convertations import rgb_to_hsv, hsv_to_rgb
import pygame

def h_plus(hsv):
    if (hsv[0] <= 350):
        hsv[0] += 10
    return hsv

def h_minus(hsv):
    if (hsv[0] >= 10):
        hsv[0] -= 10
    return hsv

def s_plus(hsv):
    if (hsv[1] < 0.99):
        hsv[1] += 0.01
    return hsv

def s_minus(hsv):
    if (hsv[1] > 0.01):
        hsv[1] -= 0.01
    return hsv

def v_plus(hsv):
    if (hsv[2] < 0.99):
        hsv[2] += 0.01
    return hsv

def v_minus(hsv):
    if (hsv[2] > 0.01):
        hsv[2] -= 0.01
    return hsv

def hsv_change(surface, change_action):
    for y in range(0, surface.get_height()):
        for x in range(0, surface.get_width()):
            rgb = surface.get_at([x, y])                            
            hsv = rgb_to_hsv(rgb)
            hsv = change_action(hsv)
            rgb = hsv_to_rgb(hsv)
            color = pygame.Color(rgb[0], rgb[1], rgb[2], 255)
            surface.set_at((x, y), color)
