from CONSTANTS import HEIGHT, WIDTH

# bumble bee == 1
# butterfly == 2
# galaga == 3
# scorpion == 4
# galaxian == 5
# bosonian == 6

unit_arrays = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [2, 3, 2, 3],
    [2, 3, 2, 3],
    [2, 2, 2, 2],
    [2, 2, 2, 2],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]  
]

# these will get tweaked after positioning function is completed
start_time = [
    0,
    0,
    200,
    232,
    400,
    432,
    600,
    632,
    800,
    832
]

platoon_paths = [
    1,
    2,
    3,
    3,
    4,
    4,
    1,
    1,
    2,
    2
]

platoon_final_positions = [
    [WIDTH * 8/ 16, HEIGHT * 7 / 16],
    [WIDTH * 8/ 16, HEIGHT * 5 / 16],
    [WIDTH * 7/ 16, HEIGHT * 4 / 16],
    [WIDTH * 9/ 16, HEIGHT * 4 / 16],
    [WIDTH * 11/ 16, HEIGHT * 5 / 16],
    [WIDTH * 5/ 16, HEIGHT * 5 / 16],
    [WIDTH * 7/ 16, HEIGHT * 7 / 16],
    [WIDTH * 9/ 16, HEIGHT * 7 / 16],
    [WIDTH * 6/ 16, HEIGHT * 7 / 16],
    [WIDTH * 10/ 16, HEIGHT * 7 / 16],
]

unit_offset = [
    [(1,2),(1,2),(1,2),(1,2)],[(1,2),(1,2),(1,2),(1,2)]
]