
from Classes import Alien_Armada, Alien_Platoon
from Unit_Arrays import unit_arrays, start_time
from Alien_Objects import build_new_unit, flight_paths
from Bezier_Curve import bezier_curve
from Bezier_Arrays import get_bezier_flight_path, flight_path_step_speed 

def unit_selection(i, j):
    return unit_arrays[i][j]

def build_alien_platoon(i):
    platoon = [0, 1, 2, 3]
    for j in range(len(platoon)):
        unit = unit_selection(i, j)
        platoon[j] = build_new_unit(unit) 
    platoon = Alien_Platoon(i, platoon, start_time[i], 0)
    return platoon


def build_alien_armada():
    armada = Alien_Armada([0, 1, 2, 3, 4, 5, 6 ,7 ,8 ,9])
    for i in range(len(armada.platoon)):
        armada.platoon[i] = build_alien_platoon(i)
    return armada

def plot_units(platoon, flight_path, time):
    #drawing curves to see whats going on
    if time > platoon.start_time:
        bezier_points = get_bezier_flight_path(flight_path.path)
        if flight_path.path == 0 or flight_path.path == 1:
            k = 0
            j = 0
        else:
            k = 1
            j = 0
        step_speed = 0.003
        for i in range(len(platoon.unit)):
            if platoon.unit[i].flight_is_completed != True:
                # get its curve position and rotation and move to the next unit minus some time step
                time_step = platoon.unit[i].path_time - (i * 0.15) 
                j = 0
                while time_step > 1:
                    j = j + 1
                    if j > len(bezier_points) -1 :
                        time_step = time_step - len(bezier_points)
                        j = len(bezier_points) - 1
                        platoon.unit[i].flight_is_completed = True
                        break
                    else: time_step = time_step - 1
                x, y, rotation = bezier_curve(bezier_points[j], time_step) 
                platoon.unit[i].position_x = x
                platoon.unit[i].position_y = y 
                platoon.unit[i].rotation = rotation
                platoon.unit[i].path_time = platoon.unit[i].path_time + step_speed * flight_path_step_speed[k][j]
        platoon.path_time = platoon.path_time + step_speed * flight_path_step_speed[k][j]


def platoon_movement(platoon, i, time):
    # iterate through the flightpaths and platoons in that path
    for j in range(len(flight_paths)):
        for k in range(len(flight_paths[j].platoon)):
            if flight_paths[j].platoon[k] == i:
                plot_units(platoon, flight_paths[j], time)
                 
def alien_movement(armada,time):
    for i in range(len(armada.platoon)):
        platoon_movement(armada.platoon[i], i, time)


def main():
    build_alien_armada()


if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Alien_Actions"
    )
