import pygame
import math
import random
from COLORS import BLACK
from Classes import Stars
from CONSTANTS import HEIGHT, WIDTH, FPS

pygame.init()

close_stars = Stars("close stars", None, 1)
medium_stars = Stars("medium stars", None, .5)
far_stars = Stars("far stars", None, .25)


# Create Display for visulaizatoin purposes
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stars")


def determine_star_brightness(star, time, frequency):
    amplitude = 65
    frequency = 1 / frequency
    brightness = amplitude + amplitude * math.sin(2 * math.pi * frequency * time)
    star_brightness = star + brightness
    return star_brightness

def draw_star(star, brightness, x, y):
    b = int(brightness)
    if b < 0:
        b = 0
    if b > 255:
        b = 255
    pygame.draw.circle(WINDOW,(b,b,b),(x,y),1)
    
def locate_stars(stars, time):
    for i in range(len(stars.array)):
        for j in range(len(stars.array[i])):
            if not isinstance(stars.array[i][j], int):
                star = stars.array[i][j]
                star_time = time + star[1]          
                brightness = determine_star_brightness(star[0], star_time, star[4])
                x = WIDTH * i / 22 + WIDTH/44 + star[2]
                y = HEIGHT * j / 37 + star[3]
                y = translate_stars(star, y, time, stars.speed)
                draw_star(star, brightness, x, y) 
   
def translate_stars(stars, y, time, speed):
    y =  y + (speed * time)
    scroll_start = HEIGHT * 36 / 32
    while y > scroll_start:
        y = y - scroll_start
    return y

def fill_in_array(x, y, array, brightness_low, brightness_high, hit_rate):
    brightness = random.randrange(brightness_low, brightness_high)
    hit = random.randrange(0,100)
    if hit > hit_rate:
        brightness = 0
    if brightness !=0:
        cycle_offset = random.randrange(0,180)
        y_offset= random.randrange(-10,10)
        x_offset= random.randrange(-10,10)
        frequency= random.randrange(180,360)
        brightness = [brightness, cycle_offset, x_offset, y_offset, frequency]
    return brightness
  
def generate_stars():
    y = int(HEIGHT / 36)
    x = int(WIDTH / 16)
    close_stars_array = [[0] * x for _ in range(y)]
    medium_stars_array = [[0] * x for _ in range(y)]
    far_stars_array = [[0] * x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            close_stars_array[i][j] = fill_in_array(j, i, close_stars_array, 0, 125, 10)
            medium_stars_array[i][j] = fill_in_array(j, i, medium_stars_array, 0, 65,5)
            far_stars_array[i][j] = fill_in_array(j, i, medium_stars_array, 0, 10,2)
    close_stars.array = close_stars_array
    medium_stars.array = medium_stars_array
    far_stars.array = far_stars_array
    star_cluster = [far_stars, medium_stars, close_stars]
    return star_cluster
            
def main():
    clock = pygame.time.Clock()
    generate_stars()
    run = True
    time = 1
    i = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WINDOW.fill((BLACK))
        pygame.display.update()
        locate_stars(close_stars, time)
        locate_stars(medium_stars, time)
        locate_stars(far_stars, time)
        time = time + 1
        pygame.display.update()

    
# play sounds
if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Star_Drawing"
    )
