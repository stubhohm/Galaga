from CONSTANTS import FIGHTER_HEIGHT, FIGHTER_WIDTH, ALIEN_HEIGHT, ALIEN_WIDTH, MISSILE_WIDTH, MISSILE_HEIGHT
from Galaga_Sprites import *


def scale_sprite(object):
    object.sprite = pygame.transform.rotate(object.sprite, object.rotation)
    if object.is_missile:
            object.sprite = pygame.transform.scale(object.sprite, (MISSILE_WIDTH, MISSILE_HEIGHT))
    else:
        if object.is_alien:
            object.sprite = pygame.transform.scale(object.sprite, (ALIEN_WIDTH, ALIEN_HEIGHT))
    
        if object.is_fighter:
            object.sprite = pygame.transform.scale(object.sprite, (FIGHTER_WIDTH, FIGHTER_HEIGHT))
        


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Sprite Manipulation"
    )
