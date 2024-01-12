import pygame
import math
import copy
from CONSTANTS import FPS
from Sprite_Manipulation import scale_sprite
from Player_Actions import player_movement, player_fire_missile
from Services import draw_window, fill_window
from Object_Movement import missile_movement
from Player_Objects import player
from Alien_Actions import build_alien_armada, alien_movement
from Missile_Lists import player_missile_list, alien_missile_list
from Collisions import collision_check
from Star_Drawing import generate_stars

pygame.init()

def main():
    clock = pygame.time.Clock()
    run = True
    time = 0
    # need to do one time on level start, but putting here for now
    alien_armada = build_alien_armada()
    star_clusters = generate_stars()
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
        player_fire_missile(player, player_missile_list, key_released)
        alien_movement(alien_armada,time)
        missile_movement(player_missile_list)
        missile_movement(alien_missile_list)
        collision_check(player_missile_list,player, alien_missile_list, alien_armada)
        draw_window(player_missile_list, player, alien_missile_list, alien_armada, star_clusters, time)
        pygame.display.update()
        time = time + 1


if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Galaga"
    )
