import math
from ..constants.CONSTANTS import WIDTH
from . .calculations_and_datasets.calculations.bezier_calculations.bezier_curve import bezier_curve, construct_bezier_points
from . .calculations_and_datasets.data_sets.bezier_arrays import get_bezier_flight_path, entry_path_step_speed


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

def plot_unit(unit, x, y, rotation):
    unit.position_x = x
    unit.position_y = y 
    unit.rotation = rotation

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

if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: movement"
    )