from constants.CONSTANTS import HEIGHT, MISSILE_HEIGHT
from classes.classes import Missile, AlienMissile
from imported_assets.Galaga_Sprites import alien_missile_image, fighter_missile


def add_missile(active_missile_list, shooter):
    # move all missiles up one spot in the array
    new_active_missile_list = [None] * (len(active_missile_list.missile) + 1)
    for i in range(len(active_missile_list.missile)):
        new_active_missile_list[i + 1] = active_missile_list.missile[i]

    if active_missile_list.is_player_list:
        new_missile = Missile(fighter_missile, -10, -10, False)
        new_active_missile_list[0] = new_missile
        new_missile.position_x = shooter.position_x
        new_missile.position_y = shooter.position_y - HEIGHT / 8
    else:
        new_alien_missile = AlienMissile(alien_missile_image, -10, -10)
        active_missile_list[0] = new_alien_missile
    new_missile.position_x = shooter.position_x
    new_missile.position_y = shooter.position_y
    return new_active_missile_list

def clean_missile_list(active_missile_list):
    for i in range(len(active_missile_list.missile)):
        if active_missile_list.missile[i].position_y < -(2 * MISSILE_HEIGHT) or (
            active_missile_list.missile[i].position_y > HEIGHT + (2 * MISSILE_HEIGHT)
        ):
            # truncate off values that are off screen
            active_missile_list.missile = active_missile_list.missile[:i]
            break
    return active_missile_list

def remove_missile(missile_list, missile_rank):
    # if alien, set y to Height * 2
    # if fighter, set y to Height * - 2
    if missile_list.missile[missile_rank].is_alien:
        missile_list.missile[missile_rank].position_y = HEIGHT * 2
    else:
        missile_list.missile[missile_rank].position_y = HEIGHT * -2
    # bubble it to the end of the list
    for i in range(missile_rank, len(missile_list.missile) - 1 ):
        holding_missile = missile_list.missile[i + 1]
        missile_list.missile[i + 1] = missile_list.missile[i]
        missile_list.missile[i] = holding_missile


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: List_Manipulation"
    )
