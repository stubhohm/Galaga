from . .constants.CONSTANTS import WIDTH
from ..classes.classes import AlienArmada, AlienPlatoon, AlienUnit
from ..calculations_and_datasets.data_sets.unit_arrays import unit_arrays, platoon_final_position, platoon_expansion_multiple, start_time, flight_paths, unit_offset

# remaining class atributes left as default and modified later
def build_new_unit(unit_type, unit_rank, platoon_rank):
    if unit_type == 1:
        unit = AlienUnit(
            "Bumble Bee", 1, 0, 1, False, 100)
    if unit_type == 2:
        unit = AlienUnit(
            "Butter Fly", 2, 0, 1, False, 160)
    if unit_type == 3:
        unit = AlienUnit(
            "Galaga", 3, 0, 2, False, 400, 0)
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

def build_alien_platoon(i, time):
    platoon = [0, 1, 2, 3]#
    for j in range(len(platoon)):
        unit = unit_selection(i, j)
        platoon[j] = build_new_unit(unit, j, i)
        for k in range(len(flight_paths)):
            for l in range(len(flight_paths[k].platoon)):
                if flight_paths[k].platoon[l] == i:
                    flight_path = flight_paths[k]
    platoon = AlienPlatoon(
        i, 
        platoon, start_time[i] + time,
        0, # path_time set to zero
        platoon_final_position[i], 
        flight_path, 
        None, #expanded_final_position, this is calculated later
        platoon_expansion_multiple[i] ,
        False
        )
    return platoon

def build_alien_armada(level, time):
    armada = AlienArmada([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], False)#
    for i in range(len(armada.platoon)):
        armada.platoon[i] = build_alien_platoon(i, time)
    armada.level = level
    return armada

def unit_selection(i, j):
    return unit_arrays[i][j]

if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: building"
    )