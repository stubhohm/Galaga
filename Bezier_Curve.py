import math
# imports for texting curves
import pygame
from Bezier_Arrays import bezier_points, bezier_step_speed, get_bezier_points
from COLORS import BLACK, WHITE, RED
from CONSTANTS import HEIGHT, WIDTH, FPS


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
    dy = int((
        3 * (1 - t) ** 2 * (P1[0] - P0[0])
        + 6 * (1 - t) * t * (P2[0] - P1[0])
        + 3 * t**2 * (P3[0] - P2[0])
    ))
    dx = int((
        3 * (1 - t) ** 2 * (P1[1] - P0[1])
        + 6 * (1 - t) * t * (P2[1] - P1[1])
        + 3 * t**2 * (P3[1] - P2[1])
    ))
    if dx !=0:
        angle_radians = math.atan(dy/dx)
        angle_degrees = math.degrees(angle_radians)
    else:
        if dy > 0:
            angle_degrees = 270
        else:
            angle_degrees = 90
    x = int(x)
    y = int(y)
    angle_degrees = int(angle_degrees)
    return x, y, angle_degrees

# Create Display
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaga")


def draw_window(coordinate):
    x = coordinate[0]
    y = coordinate[1]
    
    pygame.draw.circle(WINDOW,WHITE,(x,y),5)

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
        draw_window((current_point[0],current_point[1]))
        pygame.draw.line(WINDOW,WHITE,(bezier_points[1]),(bezier_points[0]),2)
        pygame.draw.line(WINDOW,WHITE,(bezier_points[3]),(bezier_points[2]),2)
        pygame.draw.circle(WINDOW,RED,(bezier_points[1]),8)
        pygame.draw.circle(WINDOW,RED,(bezier_points[2]),8)
        pygame.display.update()
        time = time + 0.005 * bezier_step_speed[i]
        if time > 1:
            time = 0 
            i = i + 1
        if i > 9:
            run = False

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Bezier Curves"
    )