from Player_Objects import missile
from Alien_Objects import alien_missile
from CONSTANTS import HEIGHT, MISSILE_HEIGHT
from Classes import Missile, Alien_Missile
from Galaga_Sprites import alien_missile_image, fighter_missile


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
        new_alien_missile = Alien_Missile(alien_missile_image, -10, -10)
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


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: List_Manipulation"
    )
