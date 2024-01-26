import pygame
from ...constants.CONSTANTS import WIDTH, HEIGHT
from ...constants.COLORS import BLACK, WHITE
from ...imported_assets.text.FONTS import *
from .drawing_sprites import draw_sprite, draw_image, draw_text, draw_beam_image
from .star_drawing import locate_stars
from ...imported_assets.galaga_sprites import fighter_image
from ..Menus.menus import menu_selecting


# Create Display
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaga")

def fill_window(color):
    WINDOW.fill((color))

def draw_menu(menu_selection, star_clusters, time, key_released, score):
    WINDOW.fill((BLACK))
    for i in range(len(star_clusters)):
        locate_stars(star_clusters[i], time)
    menu_selection = menu_selecting(key_released, time, WINDOW, menu_selection, score)
    if menu_selection == "Play":
        time = 0
    return menu_selection, time

def draw_stars(star_clusters, time):
    for i in range(len(star_clusters)):
        locate_stars(star_clusters[i], time)

def draw_player(player):
    if player.lives > 0:
        draw_sprite(WINDOW, player, True)

def draw_alien_armada(alien_armada):
    for i in range(len(alien_armada.platoon)):
        for j in range(len(alien_armada.platoon[i].unit)):
            draw_sprite(WINDOW, alien_armada.platoon[i].unit[j], True)
            if alien_armada.platoon[i].unit[j].beam_image:
                draw_beam_image(WINDOW, alien_armada.platoon[i].unit[j])

def draw_missiles(missile_list):
    for i in range(len(missile_list.missile)):
        draw_sprite(WINDOW, missile_list.missile[i], True)

def draw_player_lives(player):
    for i in range(player.lives - 1):
       draw_image(WINDOW, fighter_image[0], (WIDTH * i / 16), 15 / 16 * HEIGHT, 64, 64, 0, False)

def display_hit_rate(player):
    if player.shots_fired > 0:
        hit_rate = int((player.hits/player.shots_fired) * 100)
        hit_rate = "Hit rate: " + str(hit_rate)+ "%"
        draw_text(WINDOW,hit_rate, text_font,WHITE, WIDTH * 9 / 16, 0, False)

def display_score(player):
    draw_text(WINDOW,str(player.score),text_font, WHITE, 0, 0, False)

def display_stage_clear(alien_armada):
    if alien_armada.is_defeated:
        draw_text(WINDOW,"Stage Cleared",text_font,WHITE, WIDTH/2, HEIGHT/2, True)

def display_new_stage(alien_armada, time):
    if alien_armada.platoon[0].start_time - time > 120:
        text = f"Stage {alien_armada.level + 1}"
        draw_text(WINDOW,text,text_font, WHITE, WIDTH/2, HEIGHT/2, True)

def display_game_over_text(player):
    if player.lives == 0:
        text = "Game Over"
        draw_text(WINDOW,text,text_font, WHITE, WIDTH / 2, HEIGHT / 2, True)
        text = "Press Enter to Continue"
        draw_text(WINDOW,text,menu_font, WHITE, WIDTH / 2, HEIGHT * 9 / 16, True)

def draw_game_window(player_missile_list, player, alien_missile_list, alien_armada, star_clusters, time):
    WINDOW.fill((BLACK))
    draw_stars(star_clusters, time)
    draw_player(player)
    draw_alien_armada(alien_armada)
    draw_missiles(player_missile_list)
    draw_missiles(alien_missile_list)
    draw_player_lives(player)
    display_hit_rate(player)
    display_score(player)
    display_new_stage(alien_armada, time)
    display_game_over_text(player)    
    


def main():
    fill_window(BLACK)


# play sounds
if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Services"
    )
