import math
from CONSTANTS import WIDTH
from Classes import Alien_Armada, Alien_Platoon
from Unit_Arrays import unit_arrays, start_time, platoon_final_position, platoon_expansion_multiple
from Alien_Objects import build_new_unit, flight_paths
from Bezier_Curve import bezier_curve, construct_bezier_points
from Bezier_Arrays import get_bezier_flight_path, flight_path_step_speed
from Sprite_Manipulation import toggle_alien_sprite_images


def alien_explodes(unit):
    unit.entry_flight_is_completed = True
    unit.station_flight_is_completed = True
    y = unit.position_y
    x = unit.position_x
    plot_unit(unit, x, y, 0)

def alien_movement(armada,time):
    armada_defeated(armada)
    if armada.is_defeated != True:
        for i in range(len(armada.platoon)):
            if armada.platoon[i].is_defeated != True:
                platoon_movement(armada.platoon[i], time)
                toggle_alien_sprite_images(armada.platoon[i], time)
                armada_expand_contract(armada.platoon[i], time)

def armada_defeated(armada):
    for i in range(len(armada.platoon)):
        if armada.platoon[i].is_defeated != True:
            return
    armada.is_defeated == True

def armada_expand_contract(platoon, time):
    amplitude = WIDTH / 600
    frequency = 1 / 360
    expansion_factor = 8
    x_expansion = amplitude + amplitude * math.sin(2 * math.pi * frequency * time)
    platoon.expanded_final_position = (
        platoon.final_position[0] +
        x_expansion * expansion_factor * platoon.expansion_scaler 
    )
    for i in range(len(platoon.unit)):
        if platoon.unit[i].id != 9:
            x = platoon.unit[i].final_position[0]
            if x > 0:
                unit_scaler = expansion_factor / 3
            elif x < 0:
                unit_scaler = -expansion_factor / 3
            else:
                unit_scaler = 0
            platoon.unit[i].expanded_final_position = (
            platoon.unit[i].final_position[0] +
            x_expansion * unit_scaler
        )

def build_alien_platoon(i):
    platoon = [0, 1, 2,3]
    for j in range(len(platoon)):
        unit = unit_selection(i, j)
        platoon[j] = build_new_unit(unit, j, i)
        for k in range(len(flight_paths)):
            for l in range(len(flight_paths[k].platoon)):
                if flight_paths[k].platoon[l] == i:
                    flight_path = flight_paths[k]
    platoon = Alien_Platoon(
        i, 
        platoon, start_time[i],
        0, # path_time set to zero
        platoon_final_position[i], 
        flight_path, 
        None, #expanded_final_position, this is calculated later
        platoon_expansion_multiple[i] 
        )
    return platoon

def build_alien_armada():
    armada = Alien_Armada([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in range(len(armada.platoon)):
        armada.platoon[i] = build_alien_platoon(i)
    return armada

def find_position_on_curve (platoon, i, bezier_points):
    # get its curve position and rotation and move to the next unit minus some time step
    step_speed = 0.003
    flight_is_completed = False
    time_step = platoon.unit[i].path_time - (i * 0.15)
    curve_segment = 0
    if platoon.flight_path.path < 2:
        curve_speed_array = 0
    if platoon.flight_path.path > 1:
        curve_speed_array = 1
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
    if platoon.unit[i].entry_flight_is_completed:
        curve_speed_array = 0
        curve_segment = 1
    platoon.unit[i].path_time = (
        platoon.unit[i].path_time + 
        step_speed * 
        flight_path_step_speed[curve_speed_array][curve_segment]
    )
    return flight_is_completed

def platoon_defeated(platoon):
    if platoon.is_defeated != True:
        for i in range(len(platoon.unit)):
            if platoon.unit[i].id != 9:
                return
        platoon.is_defeated == True

def platoon_movement(platoon, time):
    # iterate through the flightpaths and platoons in that path
    platoon_defeated(platoon)
    for j in range(len(platoon.unit)):
        entry_flight = platoon.unit[j].entry_flight_is_completed
        station_flight = platoon.unit[j].station_flight_is_completed
        if platoon.unit[j].id == 9:
            alien_explodes(platoon.unit[j])
        if entry_flight != True:
            unit_entry_movement(platoon, j, time)
        elif station_flight != True:
            unit_final_station_movement(platoon, j, platoon.unit[j])
        elif station_flight and entry_flight == True and platoon.unit[j].id != 9:
            rotation = 180
            x = platoon.expanded_final_position + platoon.unit[j].expanded_final_position
            y = platoon.unit[j].position_y
            plot_unit(platoon.unit[j], x, y, rotation)
            #write function for static shifting based on platoon final location

def plot_unit(unit, x, y, rotation):
    unit.position_x = x
    unit.position_y = y 
    unit.rotation = rotation

def unit_entry_movement(platoon, j, time):
    #drawing curves to see whats going on
    if time > platoon.start_time:
        bezier_points = get_bezier_flight_path(platoon.flight_path.path)
        #time step needs to be adjusted
        platoon.unit[j].entry_flight_is_completed = find_position_on_curve(platoon, j, bezier_points)

def unit_final_station_movement(platoon, j, unit):
    bezier_points = construct_bezier_points(platoon,unit)
    # platoon.unit[j].path_time = platoon.unit[j].path_time + (j * 0.15)
    platoon.unit[j].station_flight_is_completed = find_position_on_curve(platoon, j, bezier_points)

def unit_selection(i, j):
    return unit_arrays[i][j]

def main():
    run = True
    time = 0
    while run:
        armada = build_alien_armada()
        alien_mvmt = alien_movement(armada, time)
        time = time + 10
        # if armada.platoon[7].unit[3].entry_flight_is_completed:
        run = False

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Alien_Actions"
    )
