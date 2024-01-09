from Classes import Alien_Armada, Alien_Platoon
from Unit_Arrays import unit_arrays
from Alien_Objects import build_new_unit


def unit_selection(i, j):
    return unit_arrays[i][j]


def build_alien_platoon(i):
    platoon = [0, 1, 2, 3, 4, 5, 6, 7]
    for j in range(len(platoon)):
        unit = unit_selection(i, j)
        platoon[j] = build_new_unit(unit)
    return platoon


def build_alien_armada():
    armada = [0, 1, 2, 3, 4, 5]
    for i in range(len(armada)):
        armada[i] = build_alien_platoon(i)
    return armada


def alien_movement():
    a = 0


def main():
    build_alien_armada()


if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Alien_Actions"
    )
