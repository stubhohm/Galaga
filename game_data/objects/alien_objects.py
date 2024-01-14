from classes.Classes import AlienUnit, AlienMissile, FlightPath
from imported_assets.Galaga_Sprites import alien_missile_image
from game_data.calculations_and_datasets.data_sets.Unit_Arrays import unit_offset

# varaible = AlienUnity(name, alien id/sprite set, cycle_position, hp, can abduction, points, completed curve)

alien_explosion = AlienUnit("Alien Explosion", 9, 0, 0, False, 0)
alien_missile = AlienMissile(alien_missile_image, -100, -100, 0)

# path = name, path_id, start_time, current_time, involved platoons
flight_path_1 = FlightPath("top_left_start", 0, [0, 6, 7], False)
flight_path_2 = FlightPath("top_right_start", 1, [1, 8, 9], False)
flight_path_3 = FlightPath("bottom_left", 2, [2, 3], False)
flight_path_4 = FlightPath("bottom_right", 3, [4, 5], False)

flight_paths = [flight_path_1, flight_path_2, flight_path_3, flight_path_4]

# remaining class atributes left as default and modified later
def build_new_unit(unit_type, unit_rank, platoon_rank):
    if unit_type == 1:
        unit = AlienUnit(
            "Bumble Bee", 1, 0, 1, False, 100)
    if unit_type == 2:
        unit = AlienUnit(
            "Butter Fly", 2, 0, 1, False, 100)
    if unit_type == 3:
        unit = AlienUnit(
            "Galaga", 3, 0, 2, True, 400, 0)
    if unit_type == 4:
        unit = AlienUnit(
            "Scorpion", 4, 0, 1, False, 100, 0)
    if unit_type == 5:
        unit = AlienUnit(
            "Galaxian", 5, 0, 1, False, 100, 0)
    if unit_type == 6:
        unit = AlienUnit(
            "Bosconian", 6, 0, 1, False, 100, 0)
    if unit_type == 7:
        unit = AlienUnit(
            "Captured Fighter", 7, 0, 1, False, 100, 0)
    if unit_type == 8:
        unit = AlienUnit(
            "Alien Explosion", 8, 0, 0, False, 0, 0)
    
    if platoon_rank == 2 or platoon_rank == 3:
        if platoon_rank == 2:
            unit.final_position = unit_offset[1][unit_rank]
        else:
            unit.final_position = unit_offset[2][unit_rank]
    else:
        unit.final_position = unit_offset[0][unit_rank]
    return unit

def main():
    unit = None
    for platoon_rank in range(8):
        for unit_rank in range(4):
            for unit_type in range(4):
                unit = build_new_unit(unit_type + 1, unit_rank, platoon_rank)
                print("platoon:",platoon_rank + 1,"unit:",unit.name)

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Aliens"
    )
