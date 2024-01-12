import math
import pygame
from Bezier_Arrays import bezier_step_speed, get_bezier_points, get_bezier_flight_path
from COLORS import BLACK, WHITE, RED, YELLOW
from CONSTANTS import HEIGHT, WIDTH, FPS

# Create Display for visulaizatoin purposes
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bezier Curves")

def bezier_curve(bezier_pair, time_step):
    P0 = starting_point = bezier_pair[0]
    P1 = starting_control_point = bezier_pair[1]
    P2 = finishing_point = bezier_pair[2]
    P3 = finishing_control_point = bezier_pair[3]
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
    return x, y, angle_degrees

def construct_bezier_points(platoon, unit):
    end_bezier_coordinate = [0,0]
    end_bezier_control = [0,0]
    start_bezier_coordinate = [0,0]
    start_bezier_control = [0,0]
    new_bezier_points = [[0,0,0,0]]
    bezier_points = get_bezier_flight_path(platoon.flight_path.path)
    start_bezier_coordinate[0] = bezier_points[len(bezier_points) - 1][3][0]
    start_bezier_coordinate[1] = bezier_points[len(bezier_points) - 1][3][1]
    start_bezier_control[1] = start_bezier_coordinate[1] - HEIGHT / 8
    start_bezier_control[0] = start_bezier_coordinate[0]
    end_bezier_coordinate[0] = platoon.expanded_final_position + unit.final_position[0]
    end_bezier_coordinate[1] = platoon.final_position[1] + unit.final_position[1]
    end_bezier_control[0] = end_bezier_coordinate[0]
    end_bezier_control[1] = end_bezier_coordinate[1] - HEIGHT / 8
    new_bezier_points[0][0] = start_bezier_coordinate
    new_bezier_points[0][1] = start_bezier_control
    new_bezier_points[0][3] = end_bezier_control
    new_bezier_points[0][2] = end_bezier_coordinate
    # for showing control points and such for bezier home seeking curves
    # draw_window((0,0),new_bezier_points[0]) 
    return new_bezier_points

def draw_window(coordinate, bezier_points):
    x = coordinate[0]
    y = coordinate[1]
    pygame.draw.circle(WINDOW,WHITE,(x,y),5)
    pygame.draw.line(WINDOW,WHITE,(bezier_points[1]),(bezier_points[0]),2)
    pygame.draw.line(WINDOW,WHITE,(bezier_points[3]),(bezier_points[2]),2)
    pygame.draw.circle(WINDOW,RED,(bezier_points[1]),8)
    pygame.draw.circle(WINDOW,YELLOW,(bezier_points[2]),8)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    time = 0
    i = 0
    WINDOW.fill((BLACK))
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        current_point = [0,0,0]
        bezier_points = get_bezier_points(i)
        current_point = bezier_curve(bezier_points, time)
        draw_window((current_point[0],current_point[1]), bezier_points)
        time = time + 0.005 * bezier_step_speed[i]
        if time > 1:
            time = 0 
            i = i + 1
        if i > 9:
           i = 0

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Bezier Curves"
    )
