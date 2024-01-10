from Classes import Alien_Unit, Alien_Missile, Flight_Path
from Galaga_Sprites import alien_missile_image

# varaible = Alien_Unity(name, alien id/sprite set, cycle_position, hp, can abduction, points, completed curve)
alien_explosion = Alien_Unit(
    "Alien Explosion", 8, 0, 0, False, 0, 0, None, None, None, None, False, 0
)
alien_missile = Alien_Missile(alien_missile_image, -10, -10)

# path = name, path_id, start_time, current_time, involved platoons
flight_path_1 = Flight_Path("top_left_start", 0, [0, 6, 7], False)
flight_path_2 = Flight_Path("top_right_start", 1, [1, 8, 9], False)
flight_path_3 = Flight_Path("bottom_left", 2, [2, 3], False)
flight_path_4 = Flight_Path("bottom_right", 3, [4, 5], False)


flight_paths = [flight_path_1, flight_path_2, flight_path_3, flight_path_4]


def build_new_unit(unit):
    if unit == 1:
        unit = Alien_Unit(
            "Bumble Bee", 1, 0, 1, False, 100, 0, None, None, None, None, False, 0
        )
    if unit == 2:
        unit = Alien_Unit(
            "Butter Fly", 2, 0, 1, False, 100, 0, None, None, None, None, False, 0
        )
    if unit == 3:
        unit = Alien_Unit(
            "Galaga", 3, 0, 2, True, 400, 0, None, None, None, None, False, 0
        )
    if unit == 4:
        unit = Alien_Unit(
            "Scorpion", 4, 0, 1, False, 100, 0, None, None, None, None, False, 0
        )
    if unit == 5:
        unit = Alien_Unit(
            "Galaxian", 5, 0, 1, False, 100, 0, None, None, None, None, False, 0
        )
    if unit == 6:
        unit = Alien_Unit(
            "Bosconian", 6, 0, 1, False, 100, 0, None, None, None, None, False, 0
        )
    if unit == 7:
        unit = Alien_Unit(
            "Captured Fighter", 7, 0, 1, False, 100, 0, None, None, None, None, False, 0
        )
    if unit == 8:
        unit = Alien_Unit(
            "Alien Explosion", 8, 0, 0, False, 0, 0, None, None, None, None, False, 0
        )
    return unit


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Aliens"
    )
