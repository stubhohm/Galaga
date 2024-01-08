import pygame
import math
import copy
from CONSTANTS import HEIGHT, WIDTH, FPS
from Sprite_Manipulation import scale_sprite
from Player_Input import get_key_pressed, get_key_released

pygame.init()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        key_released = None
        key_pressed = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            key_pressed = get_key_pressed(event)
            key_released = get_key_released(event)


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Galaga"
    )
