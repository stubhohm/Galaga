import pygame
import math
import copy
from CONSTANTS import FPS
from Sprite_Manipulation import scale_sprite
from Player_Actions import player_movement, fire_missile
from Services import draw_window
from Object_Movement import missile_movement
from Player_Objects import player
from Alien_Actions import build_alien_armada, alien_movement
from Missile_Lists import player_missile_list, alien_missile_list

pygame.init()


def main():
    clock = pygame.time.Clock()
    run = True
    player_missiles = player_missile_list
    alien_missiles = alien_missile_list
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
        player_missiles = fire_missile(player, player_missiles, key_released)
        alien_armada = build_alien_armada()
        alien_movement()
        missile_movement(player_missiles)
        missile_movement(alien_missile_list)
        draw_window(player_missiles, player, alien_missile_list, alien_armada)
        pygame.display.update()


if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Galaga"
    )
