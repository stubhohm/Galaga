from . . .constants.CONSTANTS import (
    FIGHTER_HEIGHT,
    FIGHTER_WIDTH,
    ALIEN_HEIGHT,
    ALIEN_WIDTH,
    MISSILE_WIDTH,
    MISSILE_HEIGHT,
)
from game_data.imported_assets.galaga_sprites import *

def toggle_boss_galaga_sprite(boss_galaga):
    if boss_galaga.hp == 2:
        if boss_galaga.image_in_cycle != 1:
            boss_galaga.image_in_cycle = 1
        else:
            boss_galaga.image_in_cycle = 0
    else:
        if boss_galaga.image_in_cycle == 2 or boss_galaga.image_in_cycle == 1:
            boss_galaga.image_in_cycle = 3
        else:
            boss_galaga.image_in_cycle = 2

def toggle_bug_sprite(unit):
    if unit.image_in_cycle == 0:
        unit.image_in_cycle = 1
    else:
        unit.image_in_cycle = 0

def toggle_alien_explosion(explosion):
    explosion.image_in_cycle = explosion.image_in_cycle + 1
    if explosion.image_in_cycle > 5:
        explosion.image_in_cycle = 5

def toggle_alien_sprite_images(platoon, time):
    if time % 90 == 0:
        for i in range(len(platoon.unit)):
            if platoon.unit[i].id == 3:
                toggle_boss_galaga_sprite(platoon.unit[i])
            elif platoon.unit[i].id != 9:
                toggle_bug_sprite(platoon.unit[i])
    if time % 6 == 0:
        for i in range(len(platoon.unit)):
            if platoon.unit[i].id == 9: 
                toggle_alien_explosion(platoon.unit[i])

def scale_sprite(object):
    if object.is_missile:
        object.sprite = pygame.transform.scale(
            object.sprite, (MISSILE_WIDTH, MISSILE_HEIGHT)
        )
    else:
        if object.is_alien:
            sprite = Alien_Image[object.id - 1][object.image_in_cycle]
            object.sprite = pygame.transform.rotate(sprite, 0)
            object.sprite = pygame.transform.scale(
                object.sprite, (ALIEN_WIDTH, ALIEN_HEIGHT)
            )
            object.sprite = pygame.transform.rotate(object.sprite, object.rotation)

        if object.is_fighter:
            object.sprite = pygame.transform.scale(
                object.sprite, (FIGHTER_WIDTH, FIGHTER_HEIGHT)
            )

def main():
    print(MISSILE_HEIGHT)

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Sprite Manipulation"
    )
