import random
import math
import copy
from ..constants.CONSTANTS import HEIGHT, FIGHTER_HEIGHT
from ..calculations_and_datasets.data_sets.bezier_arrays import get_bezier_attack_pattern
from ..calculations_and_datasets.calculations.bezier_calculations.bezier_curve import shift_bezier_array
from .movement import find_position_on_curve, set_unit_score, check_and_tow_captured_fighter
from ..missile_tracking.missile_management import add_missile

def fire_alien_missiles(unit,alien_missile_list):
    if abs(int(unit.rotation)) == 356 or abs(int(unit.rotation == 4)):
        if HEIGHT * 3 / 8 < unit.position_y < HEIGHT * 7 / 8:
            alien_missile_list.missile = add_missile(alien_missile_list, unit)

def get_random_unit(armada, depth):
    depth = depth + 1
    if depth > 50:
        a = None
        b = None
        return a, b
    a = random.randrange(0,(len(armada.platoon)))- 1
    b = random.randrange(0,(len(armada.platoon[a].unit)))- 1
    if armada.platoon[a].unit[b].hp == 0 or armada.platoon[a].unit[b].id == 7:
        a, b = get_random_unit(armada,depth)
    return a, b

def make_unit_attacker(unit, armada):
    if unit.hp == 0 or unit.attack_flight_is_completed != True:
        return
    if unit.entry_flight_is_completed and unit.station_flight_is_completed:
        unit.path = get_bezier_attack_pattern(unit)
        shift_bezier_array(unit)
        unit.attack_flight_is_completed = False
        set_unit_score(unit,unit.attack_flight_is_completed)

def select_attackers(armada, time):
    # sets attack frequency
    if time % 90 == 0:
        armada.active_attackers = 0
        for platoon in list(armada.platoon):
            if platoon.is_defeated:
                continue
            for unit in list(platoon.unit):
                if unit.attack_flight_is_completed == False:
                    armada.active_attackers = armada.active_attackers  + 1
        if armada.active_attackers < armada.level + 3:
            if armada.active_attackers > 15:
                return
            depth = 0
            # recursively gets units until one works
            a, b = get_random_unit(armada, depth)
            if not a:
                return
            make_unit_attacker(armada.platoon[a].unit[b], armada)
            if len(armada.platoon[a].unit) > 4 and armada.platoon[a].unit[b].id == 3:
                check_and_tow_captured_fighter(armada.platoon[a].unit[b], armada.platoon[a].unit[4], b)

def unit_attack_movement(platoon, unit, i, armada, alien_missile_list):
    bezier_points = unit.path[0]
    unit.attack_flight_is_completed = find_position_on_curve(platoon, i, bezier_points)
    fire_alien_missiles(unit, alien_missile_list)
    if len(platoon.unit) > 4 and unit.id == 3:
                check_and_tow_captured_fighter(unit, platoon.unit[4], i)
    if unit.attack_flight_is_completed == True:
        set_unit_score(unit, unit.attack_flight_is_completed)
        platoon.unit[i].path_time = 0
    else:
        fire_alien_missiles(unit, alien_missile_list)

if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: attacking"
    )