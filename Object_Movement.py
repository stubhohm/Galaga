from constants.CONSTANTS import MISSILE_SPEED
from missile_tracking.missile_management import clean_missile_list


def object_movement(object, d_x, d_y):
    object.position_x = object.position_x + d_x
    object.position_y = object.position_y + d_y
    return object.position_x, object.position_y


def missile_movement(missile_list):
    # iterate through all missiles in active player missiles
    for i in range(len(missile_list.missile)):
        pos_x, pos_y = object_movement(missile_list.missile[i], missile_list.missile[i].d_x, MISSILE_SPEED * -1)
    missile_list = clean_missile_list(missile_list)


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Object_Movement"
    )
