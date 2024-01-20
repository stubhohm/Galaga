from game_data.constants.CONSTANTS import (
    FIGHTER_HEIGHT,
    FIGHTER_WIDTH,
    ALIEN_HEIGHT,
    ALIEN_WIDTH,
    MISSILE_WIDTH,
    MISSILE_HEIGHT,
    BEAM_WIDTH,
    BEAM_HEIGHT
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

def cycle_explosion(explosion, time):
    if time % 6 == 0:
        explosion.image_in_cycle = explosion.image_in_cycle + 1
        if explosion.image_in_cycle > 5:
            explosion.image_in_cycle = 5

def toggle_alien_sprite_images(platoon, time):
    time_90 = time % 90 == 0
    time_6 = time % 6 == 0
    for i in range(len(platoon.unit)):
        if platoon.unit[i].id == 3 and time_90:
            toggle_boss_galaga_sprite(platoon.unit[i])
        elif platoon.unit[i].id != 9 and time_90:
            toggle_bug_sprite(platoon.unit[i])
        elif platoon.unit[i].id == 9 and time_6:
            platoon.unit[i].attack_flight_is_completed = True 
            cycle_explosion(platoon.unit[i], time)

def scale_sprite(object, is_beam=False):
    if is_beam:
        object.beam_image = pygame.transform.scale(
            object.beam_image, (BEAM_WIDTH, BEAM_HEIGHT)
        )
    elif object.is_missile:
        object.sprite = pygame.transform.scale(
            object.sprite, (MISSILE_WIDTH, MISSILE_HEIGHT)
        )
    else:
        if object.is_fighter:
            object.sprite = fighter_image[0]
            if object.hp == 0:
                object.sprite = fighter_explosion[object.image_in_cycle]
            elif object.is_alien:
                object.sprite = Alien_Image[6][0]
            elif object.double_fighter:
                object.sprite = fighter_image[1]
            object.sprite = pygame.transform.scale(
                object.sprite, (FIGHTER_WIDTH, FIGHTER_HEIGHT)
                )
        elif object.is_alien:
            sprite = Alien_Image[object.id - 1][object.image_in_cycle]
            object.sprite = pygame.transform.rotate(sprite, 0)
            object.sprite = pygame.transform.scale(
                object.sprite, (ALIEN_WIDTH, ALIEN_HEIGHT)
            )
        
        object.sprite = pygame.transform.rotate(object.sprite, object.rotation)

def main():
    print(MISSILE_HEIGHT)

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Sprite Manipulation"
    )
