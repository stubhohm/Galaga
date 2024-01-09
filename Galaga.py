import pygame
import math
import copy
from CONSTANTS import FPS
from Sprite_Manipulation import scale_sprite
from Player_Actions import player_movement, fire_missile
from Services import draw_window
from Object_Movement import alien_movement, missile_movement
from Player import player, missile

pygame.init()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        key_released = None
        key_pressed = None
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                key_released = event.key
        player_movement(key_pressed, player)
        fire_missile(player, missile, key_released)
        alien_movement()
        missile_movement(missile)
        draw_window(missile, player)
        pygame.display.update()

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Galaga"
    )
