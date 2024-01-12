import pygame
from CONSTANTS import WIDTH, HEIGHT
from COLORS import BLACK, WHITE
from FONTS import *
from drawing_sprites_playing_sounds import draw_sprite, draw_image, draw_text, play_sound
from Star_Drawing import locate_stars
from Galaga_Sprites import fighter_image

# Colors

# Create Display
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaga")

def fill_window():
    WINDOW.fill((BLACK))

def draw_window(player_missile_list, player, alien_missile_list, alien_armada, star_clusters, time):
    WINDOW.fill((BLACK))
    for i in range(len(star_clusters)):
        locate_stars(star_clusters[i], time)
    for i in range(len(alien_armada.platoon)):
        for j in range(len(alien_armada.platoon[i].unit)):
            draw_sprite(WINDOW, alien_armada.platoon[i].unit[j], True)
    for i in range(len(player_missile_list.missile)):
        draw_sprite(WINDOW, player_missile_list.missile[i], True)
    for i in range(len(alien_missile_list.missile)):
        draw_sprite(WINDOW, alien_missile_list.missile[i], True)
    for i in range(player.lives - 1):
       draw_image(WINDOW, fighter_image[0], (WIDTH * i / 16), 15 / 16 * HEIGHT, 64, 64, 0, False) 
    draw_sprite(WINDOW, player, True)
    if player.shots_fired > 0:
        hit_rate = int((player.hits/player.shots_fired) * 100)
        hit_rate = str(hit_rate)+ "%"
        draw_text(WINDOW,hit_rate, text_font,WHITE, WIDTH - WIDTH/8, HEIGHT/16, True)
    if alien_armada.is_defeated:
        draw_text(WINDOW,"YOU WIN",text_font,WHITE, WIDTH/2, HEIGHT/2,True)


def main():
    a = 0


# play sounds
if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Services"
    )
