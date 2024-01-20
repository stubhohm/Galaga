import pygame
from game_data.constants.CONSTANTS import FPS
from game_data.player.player_actions import player_update
from game_data.services.visual_output.draw_window import draw_game_window, draw_menu
from game_data.objects.object_movement import missile_movement
from game_data.objects.player_objects import player
from game_data.alien_behavior.alien_actions import build_alien_armada, alien_armada_update
from game_data.missile_tracking.missile_list import player_missile_list, alien_missile_list
from game_data.calculations_and_datasets.calculations.collision_calculations.collisions import collision_check
from game_data.services.visual_output.star_drawing import generate_stars
from game_data.events.events import check_game_events, resolve_game_events

pygame.init()

def main():
    clock = pygame.time.Clock()
    run = True
    time = 0
    # need to do one time on level start to initialize certain variables
    alien_armada = build_alien_armada(0,0)
    star_clusters = generate_stars()
    events = []
    menu_selection = "Title Menu"
    while run:
        clock.tick(FPS)
        key_released = None
        key_pressed = None
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_q]:
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                key_released = event.key
        if menu_selection == "Play":
            check_game_events(player, alien_armada, time, events)
            alien_armada = resolve_game_events(player, alien_armada, time, events)
            player_update(player, player_missile_list, time, key_released, key_pressed)
            alien_armada_update(alien_armada, alien_missile_list, time, player)
            missile_movement(player_missile_list)
            missile_movement(alien_missile_list)
            collision_check(player_missile_list,player, alien_missile_list, alien_armada)
            draw_game_window(player_missile_list, player, alien_missile_list, alien_armada, star_clusters, time)
            if player.lives == 0 and key_released == [pygame.K_RETURN][0]:
                menu_selection = "High Score Menu"
        else:
            menu_selection = draw_menu(menu_selection, star_clusters, time, key_released, player.score)
        pygame.display.update()
        time = time + 1

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Galaga"
    )
