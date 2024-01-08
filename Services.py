import pygame
from CONSTANTS import WIDTH, HEIGHT
from COLORS import BLACK, WHITE
from drawing_sprites_playing_sounds import draw_sprite, draw_text, play_sound

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# Create Display
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaga")

def draw_window():
    WINDOW.fill(WHITE)
# play sounds
