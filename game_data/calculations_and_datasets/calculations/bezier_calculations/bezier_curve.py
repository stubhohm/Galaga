import math
import random
import pygame
from ....services.visual_output.drawing_sprites import draw_text
from ....imported_assets.text.FONTS import menu_font
from ....imported_assets.galaga_sprites import tractor_beam
from ...data_sets.bezier_arrays import (
    bezier_step_speed, 
    get_bezier_points, 
    get_bezier_flight_path,
    attack_pattern_bezier_points,
    attack_pattern_speed_steps    
)
from ....constants.COLORS import BLACK, WHITE, RED, YELLOW
from ....constants.CONSTANTS import HEIGHT, WIDTH, FPS

# Create Display for visulaizatoin purposes
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def bezier_curve(bezier_pair, time_step):
    P0 = starting_point = bezier_pair[0]
    P1 = starting_control_point = bezier_pair[1]
    P2 = finishing_control_point = bezier_pair[2]
    P3 = finishing_point = bezier_pair[3]
    t = time_step
    """
    Calculate the position and slope of a cubic Bézier curve at time t.

    Parameters:
    - defined above, wordy, entry varaibles, but makes it easier to understand when using function
    - P0, P1, P2, P3: Control points as (x, y) tuples.
    - t: Time step (0 <= t <= 1).

    Returns:
    - (x, y): Position on the curve at time t.
    - (dx, dy): Slope (derivative) of the curve at time t.
    """
    x = int((
        (1 - t) ** 3 * P0[0]
        + 3 * (1 - t) ** 2 * t * P1[0]
        + 3 * (1 - t) * t**2 * P2[0]
        + t**3 * P3[0]
    ))
    y = int((
        (1 - t) ** 3 * P0[1]
        + 3 * (1 - t) ** 2 * t * P1[1]
        + 3 * (1 - t) * t**2 * P2[1]
        + t**3 * P3[1]
    ))

    # Calculate the derivatives for the slope
    dx = int((
        3 * (1 - t) ** 2 * (P1[0] - P0[0])
        + 6 * (1 - t) * t * (P2[0] - P1[0])
        + 3 * t**2 * (P3[0] - P2[0])
    ))
    dy = int((
        3 * (1 - t) ** 2 * (P1[1] - P0[1])
        + 6 * (1 - t) * t * (P2[1] - P1[1])
        + 3 * t**2 * (P3[1] - P2[1])
    ))
    if dy == 0:
        a = 0
    if dx == 0:
        a = 0
    if dy !=0:
        angle_radians = math.atan(dx/dy)
        angle_degrees = math.degrees(angle_radians)
        angle_degrees = angle_degrees
    else:
        if dy > 0:
            angle_degrees = 90
        else:
            angle_degrees = 270
    if dy < 0:
        angle_degrees = angle_degrees + 180
    
    x = int(x)
    y = int(y)
    angle_degrees = int(angle_degrees)
    # for showing control points and such for bezier home seeking curves
    # draw_window((x,y),bezier_pair)
    return x, y, angle_degrees

def construct_bezier_points(platoon, unit):
    end_bezier_coordinate = [0,0]
    end_bezier_control = [0,0]
    start_bezier_coordinate = [0,0]
    start_bezier_control = [0,0]
    new_bezier_points = [[0,0,0,0]]
    if unit.station_flight_is_completed != True:
        bezier_points = get_bezier_flight_path(platoon.flight_path.path)
    last_curve = len(bezier_points) - 1 
    start_bezier_coordinate[0] = bezier_points[last_curve][3][0]
    start_bezier_coordinate[1] = bezier_points[last_curve][3][1]
    if 90 < unit.rotation < 270:
        a = -1
    else:
        a = -1
    start_bezier_control[1] = start_bezier_coordinate[1] - HEIGHT / 8
    start_bezier_control[0] = start_bezier_coordinate[0]
    end_bezier_coordinate[0] = platoon.expanded_final_position + unit.final_position[0]
    end_bezier_coordinate[1] = platoon.final_position[1] + unit.final_position[1]
    end_bezier_control[0] = end_bezier_coordinate[0]
    end_bezier_control[1] = end_bezier_coordinate[1] + HEIGHT / 8
    new_bezier_points[0][0] = start_bezier_coordinate
    new_bezier_points[0][1] = start_bezier_control
    new_bezier_points[0][2] = end_bezier_control
    new_bezier_points[0][3] = end_bezier_coordinate
    # for showing control points and such for bezier home seeking curves
    # draw_window((0,0),new_bezier_points[0]) 
    return new_bezier_points

def draw_window(coordinate, bezier_points):
    W = WIDTH /3
    H = HEIGHT / 8
    H = 0
    W = 0
    x = coordinate[0]
    y = coordinate[1]
    pygame.draw.circle(WINDOW,WHITE,(x + W,y + H),5)
    pygame.draw.line(WINDOW,WHITE,(bezier_points[1][0] + W, bezier_points[1][1] + H),(bezier_points[0][0] + W ,bezier_points[0][1] + H),2)
    pygame.draw.line(WINDOW,WHITE,(bezier_points[3][0] + W, bezier_points[3][1] + H),(bezier_points[2][0] + W ,bezier_points[2][1] + H),2)
    pygame.draw.circle(WINDOW,RED,(bezier_points[1][0] + W,bezier_points[1][1] + H),8)
    pygame.draw.circle(WINDOW,YELLOW,(bezier_points[2][0] + W,bezier_points[2][1] + H),8)
    pygame.display.update()

def shift_bezier_array(unit):
    x_scale_rand = random.randrange(70,100)
    for i in range(len(unit.path[0])):
        for j in range(len(unit.path[0][i])):
            x_mod = x_scale_rand / 100
            if unit.position_x > WIDTH/2:
                x_mod = x_mod * -1
            unit.path[0][i][j][0] = int(x_mod * unit.path[0][i][j][0]) + int(unit.position_x)
            unit.path[0][i][j][1] = int((unit.path[0][i][j][1] * 7 / 8)) + int(unit.position_y)
    a = 0

def get_curve_segment_and_time_step(curve_segment, time_step, unit, i, bezier_points):
    flight_is_completed = False
    while time_step >= 1:
        curve_segment = curve_segment + 1
        if unit.can_abduct and curve_segment == len(bezier_points) - 1:
            unit.beam_image = tractor_beam[2][0]
            time_step = time_step - 1
            break
        elif curve_segment > len(bezier_points) -1 :
            unit.path_time = 0 + (i * 0.15)
            curve_segment = len(bezier_points) - 1
            flight_is_completed = True
            break
        else: 
            time_step = time_step - 1
    return curve_segment, time_step, flight_is_completed

def main():
    clock = pygame.time.Clock()
    run = True
    time = 0
    i = 0
    while run:
        clock.tick(FPS)
        current_point = [0,0,0]
        for j in range(len(attack_pattern_bezier_points)):
            WINDOW.fill((BLACK))
            if run == False:
                    break
            for k in range(len(attack_pattern_bezier_points[j])):
                if run == False:
                    break   
                time = 0 
                while time < 1:
                    #bezier_points = get_bezier_points(i)
                    bezier_points = attack_pattern_bezier_points[j][k]
                    current_point = bezier_curve(bezier_points, time)
                    draw_window((current_point[0],current_point[1]), bezier_points)
                    viewing = "Currently Viewing Pattern: "+ str( + j + 1) +" Step:"+ str(k + 1)
                    draw_text(WINDOW, viewing, menu_font, WHITE, WIDTH/2, HEIGHT - HEIGHT/8, True)
                    step_speed = attack_pattern_speed_steps[j][k][0]
                    time = time + step_speed * 0.0001
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            break
                    if time > .90:
                        a = 0
                
if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Bezier Curves"
    )
