import pygame
from game_data.constants.CONSTANTS import WIDTH, HEIGHT
from game_data.constants.COLORS import BLACK, WHITE
from game_data.imported_assets.text.FONTS import *
from game_data.services.visual_output.drawing_sprites import draw_sprite, draw_image, draw_text, draw_beam_image
from game_data.services.visual_output.star_drawing import locate_stars
from game_data.imported_assets.galaga_sprites import fighter_image

# Create Display
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaga")

def fill_window(color):
    WINDOW.fill((color))

def draw_window(player_missile_list, player, alien_missile_list, alien_armada, star_clusters, time):
    WINDOW.fill((BLACK))
    for i in range(len(star_clusters)):
        locate_stars(star_clusters[i], time)
    for i in range(len(alien_armada.platoon)):
        for j in range(len(alien_armada.platoon[i].unit)):
            draw_sprite(WINDOW, alien_armada.platoon[i].unit[j], True)
            if alien_armada.platoon[i].unit[j].beam_image:
                draw_beam_image(WINDOW, alien_armada.platoon[i].unit[j])
    for i in range(len(player_missile_list.missile)):
        draw_sprite(WINDOW, player_missile_list.missile[i], True)
    for i in range(len(alien_missile_list.missile)):
        draw_sprite(WINDOW, alien_missile_list.missile[i], True)
    for i in range(player.lives - 1):
       draw_image(WINDOW, fighter_image[0], (WIDTH * i / 16), 15 / 16 * HEIGHT, 64, 64, 0, False) 
    draw_sprite(WINDOW, player, True)
    if player.shots_fired > 0:
        hit_rate = int((player.hits/player.shots_fired) * 100)
        hit_rate = "Hit rate: " + str(hit_rate)+ "%"
        draw_text(WINDOW,hit_rate, text_font,WHITE, WIDTH * 7 / 8, 0, False)
    draw_text(WINDOW,str(player.score),text_font, WHITE, 0, 0, False)
    if alien_armada.is_defeated:
        draw_text(WINDOW,"YOU WIN",text_font,WHITE, WIDTH/2, HEIGHT/2, True)


def main():
    fill_window(BLACK)


# play sounds
if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Services"
    )
