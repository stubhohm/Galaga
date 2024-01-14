import math
import random
from constants.CONSTANTS import WIDTH
from classes.Classes import AlienArmada, AlienPlatoon
from Unit_Arrays import unit_arrays, start_time, platoon_final_position, platoon_expansion_multiple
from objects.Alien_Objects import build_new_unit, flight_paths
from calculations_and_datasets.calculations.bezier_calculations.Bezier_Curve import bezier_curve, construct_bezier_points, shift_bezier_array
from calculations_and_datasets.data_sets.Bezier_Arrays import get_bezier_flight_path, entry_path_step_speed, get_bezier_attack_pattern
from Sprite_Manipulation import toggle_alien_sprite_images

def alien_explodes(unit, armada):
    unit.entry_flight_is_completed = True
    unit.station_flight_is_completed = True
    if unit.attack_flight_is_completed != True and armada.active_attackers > 0:
        armada.active_attackers = armada.active_attackers - 1
    unit.attack_flight_is_completed = True
    y = unit.position_y
    x = unit.position_x
    plot_unit(unit, x, y, 0)

def alien_armada_behavior(armada,time):
    for i in range(len(armada.platoon)):
        toggle_alien_sprite_images(armada.platoon[i], time)
        if armada.is_defeated == True:
            continue
        select_attackers(armada, time)
        if armada.platoon[i].is_defeated == True:
            continue          
        platoon_behavior(armada.platoon[i], time, armada)
        armada_expand_contract(armada.platoon[i], time)
            
def armada_expand_contract(platoon, time):
    amplitude = WIDTH / 600
    frequency = 1 / 360
    expansion_factor = 9
    x_expansion = amplitude + amplitude * math.sin(2 * math.pi * frequency * time)
    platoon.expanded_final_position = (
        platoon.final_position[0] +
        x_expansion * expansion_factor * platoon.expansion_scaler 
    )
    for i in range(len(platoon.unit)):
        if platoon.unit[i].hp != 0:
            x = platoon.unit[i].final_position[0]
            if x > 0:
                unit_scaler = expansion_factor / 3
            elif x < 0:
                unit_scaler = -expansion_factor / 3
            else:
                unit_scaler = 0
            platoon.unit[i].expanded_final_position = (
            platoon.unit[i].final_position[0] 
            + x_expansion * unit_scaler
        )

def build_alien_platoon(i):
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
        platoon, start_time[i],
        0, # path_time set to zero
        platoon_final_position[i], 
        flight_path, 
        None, #expanded_final_position, this is calculated later
        platoon_expansion_multiple[i] ,
        False
        )
    return platoon

def build_alien_armada():
    armada = AlienArmada([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], False)#
    for i in range(len(armada.platoon)):
        armada.platoon[i] = build_alien_platoon(i)
    return armada

def find_position_on_curve (platoon, i, bezier_points):
    # get its curve position and rotation and move to the next unit minus some time step
    step_speed = 0.003
    flight_is_completed = False
    time_step = platoon.unit[i].path_time
    if platoon.unit[i].attack_flight_is_completed == True:
        time_step = time_step - (i * 0.15)
    curve_segment = 0
    while time_step >= 1:
        curve_segment = curve_segment + 1
        if curve_segment > len(bezier_points) -1 :
            platoon.unit[i].path_time = 0 + (i * 0.15)
            curve_segment = len(bezier_points) - 1
            flight_is_completed = True
            return flight_is_completed
        else: time_step = time_step - 1
    x, y, rotation = bezier_curve(bezier_points[curve_segment], time_step) 
    plot_unit(platoon.unit[i], x, y, rotation)
    flight_path_mod = get_flight_path_step_speed(platoon, i, curve_segment)
    platoon.unit[i].path_time = (
        platoon.unit[i].path_time 
        + step_speed 
        * flight_path_mod
    )
    return flight_is_completed

def get_flight_path_step_speed(platoon, i, curve_segment):
    speed = 6
    if platoon.unit[i].station_flight_is_completed != True:
            speed = entry_path_step_speed[1][curve_segment]
    if platoon.unit[i].entry_flight_is_completed != True:
        if platoon.flight_path.path < 2:
            speed = entry_path_step_speed[1][curve_segment]
        if platoon.flight_path.path > 1:
            speed = entry_path_step_speed[1][curve_segment]
    if platoon.unit[i].attack_flight_is_completed !=True:
            speed = platoon.unit[i].path[1][curve_segment][0] * 2
    return speed

def get_random_unit(armada):
    a = random.randrange(0,(len(armada.platoon)))- 1
    b = random.randrange(0,(len(armada.platoon[a].unit)))- 1
    if armada.platoon[a].unit[b].hp == 0:
        a, b = get_random_unit(armada)
    return a, b

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

def platoon_behavior(platoon, time, armada):
    # iterate through the flightpaths and platoons in that path
    for j in range(len(platoon.unit)):
        if platoon.unit[j].hp == 0:
            alien_explodes(platoon.unit[j], armada)
            continue
        entry_flight = platoon.unit[j].entry_flight_is_completed
        station_flight = platoon.unit[j].station_flight_is_completed
        attack_flight = platoon.unit[j].attack_flight_is_completed
        if attack_flight != True:
            unit_attack_movement(platoon, platoon.unit[j], j, armada)
        elif entry_flight != True:
            unit_entry_movement(platoon, j, time)
        elif station_flight != True:
            unit_final_station_movement(platoon, j, platoon.unit[j])
        if attack_flight == entry_flight == station_flight == True:
            rotation = 180
            x = platoon.expanded_final_position + platoon.unit[j].expanded_final_position
            y = platoon.final_position[1] + platoon.unit[j].final_position[1]
            plot_unit(platoon.unit[j], x, y, rotation)

def plot_unit(unit, x, y, rotation):
    unit.position_x = x
    unit.position_y = y 
    unit.rotation = rotation

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

def unit_entry_movement(platoon, i, time):
    #drawing curves to see whats going on
    if time > platoon.start_time:
        bezier_points = get_bezier_flight_path(platoon.flight_path.path)
        #time step needs to be adjusted
        platoon.unit[i].entry_flight_is_completed = find_position_on_curve(platoon, i, bezier_points)

def unit_final_station_movement(platoon, i, unit):
    bezier_points = construct_bezier_points(platoon,unit)
    platoon.unit[i].station_flight_is_completed = find_position_on_curve(platoon, i, bezier_points)
    if platoon.unit[i].station_flight_is_completed:
        platoon.unit[i].path_time = 0

def unit_selection(i, j):
    return unit_arrays[i][j]

def main():
    run = True
    time = 0
    armada = build_alien_armada()
    while run:
        alien_mvmt = alien_armada_behavior(armada, time)
        time = time + 10
        # if armada.platoon[7].unit[3].entry_flight_is_completed:
        run = False

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Alien_Actions"
    )
