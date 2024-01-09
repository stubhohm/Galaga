import pygame
from CONSTANTS import WIDTH, HEIGHT, FIGHTER_Y
from COLORS import BLACK, WHITE
from drawing_sprites_playing_sounds import draw_sprite, draw_text, play_sound
from Objects import *
from Object_Movement import object_movement
from Player import Player

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# Create Display
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaga")

def draw_window(missile, player):
    WINDOW.fill((BLACK))
    draw_sprite(WINDOW,missile,True)
    draw_sprite(WINDOW,player,True)



# play sounds
if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Services"
    )