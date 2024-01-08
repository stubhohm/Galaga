from CONSTANTS import FIGHTER_HEIGHT, FIGHTER_WIDTH, ALIEN_HEIGHT, ALIEN_WIDTH
from Galaga_Sprites import *


def scale_sprite(sprite, is_alien, rotation):
    sprite = pygame.transform.rotate(sprite,rotation)
    if is_alien:
        sprite = pygame.transform.scale(sprite, (ALIEN_WIDTH, ALIEN_HEIGHT))
    else:
        sprite = pygame.transform.scale(sprite, (FIGHTER_WIDTH, FIGHTER_HEIGHT))


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Sprite Manipulation"
    )
