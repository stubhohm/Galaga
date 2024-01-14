import pygame
from game_data.constants.CONSTANTS import FPS
from game_data.player.player_actions import player_movement, player_fire_missile
from game_data.services.visual_output.draw_window import draw_window
from game_data.objects.object_movement import missile_movement
from game_data.objects.player_objects import player
from game_data.alien_behavior.alien_actions import build_alien_armada, alien_armada_behavior
from game_data.missile_tracking.missile_list import player_missile_list, alien_missile_list
from game_data.calculations_and_datasets.calculations.collision_calculations.collisions import collision_check
from game_data.services.visual_output.star_drawing import generate_stars 

pygame.init()

def main():
    clock = pygame.time.Clock()
    run = True
    time = -120
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
        alien_armada_behavior(alien_armada,time)
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
