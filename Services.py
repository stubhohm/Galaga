import pygame
from CONSTANTS import WIDTH, HEIGHT, FIGHTER_Y
from COLORS import BLACK, WHITE
from drawing_sprites_playing_sounds import draw_sprite, draw_text, play_sound
from Classes import *
from Object_Movement import object_movement
from Player_Objects import player

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create Display
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaga")


def draw_window(player_missile_list, player, alien_missile_list, alien_armada):
    WINDOW.fill((BLACK))
    draw_sprite(WINDOW, player, True)
    for i in range(len(alien_armada)):
        for j in range(len(alien_armada[i])):
            alien_armada[i][j].position_y = -i * HEIGHT / 25 + 200
            alien_armada[i][j].position_x = j * WIDTH / 11 + 100
            draw_sprite(WINDOW, alien_armada[i][j], True)
    for i in range(len(player_missile_list.missile)):
        draw_sprite(WINDOW, player_missile_list.missile[i], True)
    for i in range(len(alien_missile_list.missile)):
        draw_sprite(WINDOW, alien_missile_list.missile[i], True)


def main():
    a = 0


# play sounds
if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Services"
    )
