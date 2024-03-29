from game_data.constants.CONSTANTS import HEIGHT, MISSILE_HEIGHT, FIGHTER_HEIGHT, FIGHTER_WIDTH
from game_data.classes.classes import Missile, AlienMissile
from . .imported_assets.galaga_sprites import alien_missile_image, fighter_missile

def add_missile(active_missile_list, shooter):
    # move all missiles up one spot in the array
    if shooter.is_fighter:
        if shooter.double_fighter:
            gap = 2
        else: 
            gap = 1
    else:
        gap = 1
    new_active_missile_list = [None] * (len(active_missile_list.missile) + gap)
    for i in range(len(active_missile_list.missile)):
        new_active_missile_list[i + gap] = active_missile_list.missile[i]
    if active_missile_list.is_player_list:
        missile_y = shooter.position_y - FIGHTER_HEIGHT / 6
        if not shooter.double_fighter:
            new_missile = Missile(fighter_missile, shooter.position_x, missile_y, False)
            new_active_missile_list[0] = new_missile
        else:
            flip = 1
            for i in range(2):
                missile_x = shooter.position_x + flip * FIGHTER_WIDTH / 4
                new_missile = Missile(fighter_missile, missile_x, missile_y, False)
                new_active_missile_list[i] = new_missile
                flip = -1
    else:
        d_x  = 1
        if shooter.rotation > 0:
            d_x = d_x * -1
        new_missile = AlienMissile(alien_missile_image, shooter.position_x, shooter.position_y, d_x)
        new_active_missile_list[0] = new_missile
        
    return new_active_missile_list

def clean_missile_list(active_missile_list):
    for i in range(len(active_missile_list.missile)):
        if not active_missile_list.missile[i]:
            active_missile_list.missile = active_missile_list.missile[:i]
            break
        if active_missile_list.missile[i].position_y < -(2 * MISSILE_HEIGHT) or (
            active_missile_list.missile[i].position_y > HEIGHT + (MISSILE_HEIGHT)
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
    missile_list.missile.pop()
    a = 0


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: List_Manipulation"
    )
