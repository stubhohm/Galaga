from Classes import Alien_Armada, Alien_Platoon, Alien_Unit, Alien_Missile
from Galaga_Sprites import alien_missile_image

# varaible = Alien_Unity(name, alien id/sprite set, cycle_position, hp, can abduction, points)
alien_explosion = Alien_Unit(
    "Alien Explosion", 8, 0, 0, False, 0, 0, None, None, None, None
)
alien_missile = Alien_Missile(alien_missile_image, -10, -10)


def build_new_unit(unit):
    if unit == 1:
        unit = Alien_Unit(
            "Bumble Bee", 1, 0, 1, False, 100, 0, None, None, None, None
            )
    if unit == 2:
        unit = Alien_Unit(
            "Butter Fly", 2, 0, 1, False, 100, 0, None, None, None, None
            )
    if unit == 3:
        unit = Alien_Unit(
            "Galaga", 3, 0, 2, True, 400, 0, None, None, None, None
            )
    if unit == 4:
        unit = Alien_Unit(
            "Scorpion", 4, 0, 1, False, 100, 0, None, None, None, None
            )
    if unit == 5:
        unit = Alien_Unit(
            "Galaxian", 5, 0, 1, False, 100, 0, None, None, None, None
            )
    if unit == 6:
        unit = Alien_Unit(
            "Bosconian", 6, 0, 1, False, 100, 0, None, None, None, None
            )
    if unit == 7:
        unit = Alien_Unit(
            "Captured Fighter", 7, 0, 1, False, 100, 0, None, None, None, None
        )
    if unit == 8:
        unit = Alien_Unit(
            "Alien Explosion", 8, 0, 0, False, 0, 0, None, None, None, None
        )
    return unit


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Aliens"
    )
