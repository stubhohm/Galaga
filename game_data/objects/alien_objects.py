from game_data.classes.classes import AlienUnit, AlienMissile, FlightPath
from game_data.imported_assets.galaga_sprites import alien_missile_image

# varaible = AlienUnity(name, alien id/sprite set, cycle_position, hp, can abduction, points, completed curve)

alien_explosion = AlienUnit("Alien Explosion", 9, 0, 0, False, 0)
alien_missile = AlienMissile(alien_missile_image, -100, -100, 0)

# path = name, path_id, start_time, current_time, involved platoons
flight_path_1 = FlightPath("top_left_start", 0, [0, 6, 7], False)
flight_path_2 = FlightPath("top_right_start", 1, [1, 8, 9], False)
flight_path_3 = FlightPath("bottom_left", 2, [2, 3], False)
flight_path_4 = FlightPath("bottom_right", 3, [4, 5], False)

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
