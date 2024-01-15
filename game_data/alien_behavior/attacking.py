import random
from ..calculations_and_datasets.data_sets.bezier_arrays import get_bezier_attack_pattern
from ..calculations_and_datasets.calculations.bezier_calculations.bezier_curve import shift_bezier_array
from .movement import find_position_on_curve

def make_unit_attacker(unit, armada):
    if unit.hp == 0:
        return
    if unit.attack_flight_is_completed != True:
        return
    if unit.entry_flight_is_completed and unit.station_flight_is_completed:
        unit.path = get_bezier_attack_pattern(unit)
        shift_bezier_array(unit)
        unit.attack_flight_is_completed = False
        armada.active_attackers = armada.active_attackers + 1

def select_attackers(armada, time):
    # sets attack frequency
    if time % 90 == 0:
        if armada.active_attackers < armada.game_level + 3:
            if armada.active_attackers > 6:
                return
            # recursively gets units until one works
            a, b = get_random_unit(armada)
            make_unit_attacker(armada.platoon[a].unit[b], armada)

def unit_attack_movement(platoon, unit, i, armada):
    bezier_points = unit.path[0]
    unit.attack_flight_is_completed = find_position_on_curve(platoon, i, bezier_points)
    if unit.attack_flight_is_completed == True:
        armada.active_attackers = armada.active_attackers - 1
        platoon.unit[i].path_time = 0

def get_random_unit(armada):
    a = random.randrange(0,(len(armada.platoon)))- 1
    b = random.randrange(0,(len(armada.platoon[a].unit)))- 1
    if armada.platoon[a].unit[b].hp == 0:
        a, b = get_random_unit(armada)
    return a, b


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: attacking"
    )