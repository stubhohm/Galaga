import math
from ..constants.CONSTANTS import WIDTH, FIGHTER_HEIGHT
from . .calculations_and_datasets.calculations.bezier_calculations.bezier_curve import (
    bezier_curve, 
    construct_bezier_points, 
    get_curve_segment_and_time_step,
    )
from . .calculations_and_datasets.data_sets.bezier_arrays import (
    get_bezier_flight_path,
    entry_path_step_speed,
    )
from .abucting import attempt_abduction

def check_and_tow_captured_fighter(boss_galaga, captured_fighter, i):
    if captured_fighter.boss_capture_id == i:
        captured_fighter.path = None
        captured_fighter.attack_flight_is_completed = boss_galaga.attack_flight_is_completed
        trailing_distance = FIGHTER_HEIGHT / 2
        target_theta = boss_galaga.rotation + 180
        if 520 < boss_galaga.position_y < 525 and boss_galaga.can_abduct:
            target_theta = boss_galaga.rotation
        target_theta = math.radians(target_theta)
        x = int(trailing_distance * math.sin(target_theta)) + boss_galaga.position_x
        if captured_fighter.position_y == 474 and captured_fighter.position_y < boss_galaga.position_y:
            y = captured_fighter.position_y
            x = captured_fighter.position_x
        else:
            y = int(trailing_distance * math.cos(target_theta)) + boss_galaga.position_y
        target_theta = math.degrees(target_theta)
        captured_fighter.rotation = (captured_fighter.rotation  + target_theta) / 2
        captured_fighter.position_x = x
        captured_fighter.position_y = y
        plot_unit(
            captured_fighter,
            captured_fighter.position_x, 
            captured_fighter.position_y,
            captured_fighter.rotation)
        a = 0

def find_position_on_curve (platoon, i, bezier_points):
    # get its curve position and rotation and move to the next unit minus some time step
    step_speed = 0.003
    flight_is_completed = False
    time_step = platoon.unit[i].path_time
    # if the beam is active, stop and do the beaming
    if platoon.unit[i].beam_image:
        time_step = attempt_abduction(platoon.unit[i], time_step)
        x = platoon.unit[i].position_x
        y = platoon.unit[i].position_y
        plot_unit(platoon.unit[i], x, y, 180)
        platoon.unit[i].path_time = time_step
        if len(platoon.unit) > 4:
            check_and_tow_captured_fighter(platoon.unit[i], platoon.unit[4], i)
        if platoon.unit[i].beam_image:
            return flight_is_completed
    if platoon.unit[i].attack_flight_is_completed == True:
        time_step = time_step - (i * 0.15)
    curve_segment, time_step, flight_is_completed = get_curve_segment_and_time_step(0, time_step, platoon.unit[i], i, bezier_points)
    if flight_is_completed == True:
        return flight_is_completed
    x, y, rotation = bezier_curve(bezier_points[curve_segment], time_step) 
    if platoon.unit[i].id == 7:
        rotation = rotation - 180
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
        set_unit_score(platoon.unit[i], platoon.unit[i].station_flight_is_completed)

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

def set_unit_score(unit, is_done_flying):
    if is_done_flying != True:
        if unit.id == 3:
            unit.point_value = 400
        else:
            unit.point_value = int(unit.point_value * 2)
    else:
        if unit.id == 3:
            unit.point_value = 160
        else:
            unit.point_value = int(unit.point_value / 2)
        unit.can_abduct = False

if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: movement"
    )