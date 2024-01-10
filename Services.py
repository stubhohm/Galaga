import pygame
from CONSTANTS import WIDTH, HEIGHT
from COLORS import BLACK, WHITE
from drawing_sprites_playing_sounds import draw_sprite, draw_image, draw_text, play_sound
from Galaga_Sprites import fighter_image

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create Display
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaga")

def fill_window():
    WINDOW.fill((BLACK))

def draw_window(player_missile_list, player, alien_missile_list, alien_armada):
    WINDOW.fill((BLACK))
    
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


def main():
    a = 0


# play sounds
if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Services"
    )
