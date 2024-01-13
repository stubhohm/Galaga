import random
from CONSTANTS import HEIGHT, WIDTH


flight_path_step_speed = [
    [
        6,
        8
    ],
    [
        6,
        8,
        8
    ]
]

bezier_step_speed = [
    2,
    4,
    2,
    4,
    2,
    4,
    4,
    2,
    4,
    4
]



bezier_points = [
    # come in the top off set to the left side
    # sweep out to the right side
    # loop down and back toward the middle
    [
        (WIDTH * 3 /8, HEIGHT * - 1 /8),(WIDTH * 5 / 16, HEIGHT * 1 / 8),
        (WIDTH * 7 / 8, HEIGHT * 3 / 8), (WIDTH * 7 / 8, HEIGHT * 4 / 8) 
    ],
    [
        (WIDTH * 7 / 8, HEIGHT * 4 / 8), (WIDTH * 7 / 8, HEIGHT * 5 / 8),
        (WIDTH * 5 / 8, HEIGHT * 5 / 8), (WIDTH * 5 / 8, HEIGHT * 4 / 8) 
    ],
    
    # come in the top off set to the right side
    # sweep out to the left side
    # loop down and back toward the middle
    [
        (WIDTH * 5 /8, HEIGHT * - 1 /8),(WIDTH * 11 / 16, HEIGHT * 1 / 8),
        (WIDTH * 1 / 8, HEIGHT * 3 / 8), (WIDTH * 1 / 8, HEIGHT * 4 / 8) 
    ],
    [
        (WIDTH * 1 / 8, HEIGHT * 4 / 8), (WIDTH * 1 / 8, HEIGHT * 5 / 8),
        (WIDTH * 3 / 8, HEIGHT * 5 / 8), (WIDTH * 3 / 8, HEIGHT * 4 / 8) 
    ],

    # come in bottom left
    [
        (WIDTH * -1 /8, HEIGHT * 7 / 8),(WIDTH * 1 / 8, HEIGHT * 7 / 8),
        (WIDTH * 7 / 16, HEIGHT * 5 / 8), (WIDTH * 7 / 16, HEIGHT * 4 / 8) 
    ],
    [
        (WIDTH * 7 / 16, HEIGHT * 4 / 8), (WIDTH * 7 / 16, HEIGHT * 3 / 8),
        (WIDTH * 2 / 8, HEIGHT * 3 / 8), (WIDTH * 2 / 8, HEIGHT * 4 / 8) 
    ],
    [
        (WIDTH * 2 / 8, HEIGHT * 4 / 8), (WIDTH * 2 / 8, HEIGHT * 5 / 8),
        (WIDTH * 7 / 16, HEIGHT * 5 / 8), (WIDTH * 7 / 16, HEIGHT * 4 / 8) 
    ],
    
    # come in bottom right
    [
        (WIDTH * 9 /8, HEIGHT * 7 / 8),(WIDTH * 7 / 8, HEIGHT * 7 / 8),
        (WIDTH * 9 / 16, HEIGHT * 5 / 8), (WIDTH * 9 / 16, HEIGHT * 4 / 8) 
    ],
    [
        (WIDTH * 9 / 16, HEIGHT * 4 / 8), (WIDTH * 9 / 16, HEIGHT * 3 / 8),
        (WIDTH * 6 / 8, HEIGHT * 3 / 8), (WIDTH * 6 / 8, HEIGHT * 4 / 8) 
    ],
    [
        (WIDTH * 6 / 8, HEIGHT * 4 / 8), (WIDTH * 6 / 8, HEIGHT * 5 / 8),
        (WIDTH * 9 / 16, HEIGHT * 5 / 8), (WIDTH * 9 / 16, HEIGHT * 4 / 8) 
    ]

]

flight_paths = [
    [
      bezier_points[0],
      bezier_points[1],
    ],
    [
      bezier_points[2],
      bezier_points[3], 
    ],
    [
      bezier_points[4],
      bezier_points[5],
      bezier_points[6], 
    ],
    [
      bezier_points[7],
      bezier_points[8],
      bezier_points[9], 
    ],
]

attack_pattern_bezier_points = [
    #[start, start control, finish control, finish]
    # red attack pattern 1 can only do this attack or its mirror 
    # since the attack is based on x,y == 0 just take the numbers and either add or subtract the x values to get the mirror
    # 0
    [
    [[WIDTH * 0 / 8, HEIGHT * 0 / 8],[WIDTH * 0 / 8, HEIGHT * -1 / 16],[WIDTH * -1 / 8,  HEIGHT * -1 / 16],[ WIDTH * -1 / 8, HEIGHT * 0 /8]],
    [[WIDTH * -1 / 8, HEIGHT * 0 / 8],[WIDTH * -1 / 8, HEIGHT * 1/ 8],[WIDTH * 2 / 8, HEIGHT * 2/ 8],[WIDTH * 2 / 8, HEIGHT * 3 / 8]],
    [[WIDTH * 2 / 8, HEIGHT * 3 / 8],[WIDTH * 2 / 8, HEIGHT * 4/ 8],[WIDTH * 6 / 8, HEIGHT * 10/ 8],[WIDTH * 6 / 8, HEIGHT * 9 / 8]],
    ],
    # blue attack pattern 1 base, includes the swoop down and the bottom of the loop
    # last two lines are the blue attack pattern second loop into off screen
    # 1
    [
    [[WIDTH * 0 / 8, HEIGHT * 0 / 8],[WIDTH * 0 / 8, HEIGHT * -1/ 16],[WIDTH * -1 / 8, HEIGHT * -1/ 16],[WIDTH * -1 / 8, HEIGHT * 0 / 8]],
    [[WIDTH * -1 / 8, HEIGHT * 0 / 8],[WIDTH * -1 / 8, HEIGHT * 1/ 8],[WIDTH * 3 / 8, HEIGHT * 2/ 8],[WIDTH * 3 / 8, HEIGHT * 3 / 8]],
    [[WIDTH * 3 / 8, HEIGHT * 3 / 8],[WIDTH * 3 / 8, HEIGHT * 4/ 8],[WIDTH * 4 / 8, HEIGHT * 5/ 8],[WIDTH * 4 / 8, HEIGHT * 6 / 8]],
    [[WIDTH * 4 / 8, HEIGHT * 6 / 8],[WIDTH * 4 / 8, HEIGHT * 7/ 8],[WIDTH * 2 / 8, HEIGHT * 7/ 8],[WIDTH * 2 / 8, HEIGHT * 6 / 8]],
    [[WIDTH * 3 / 8, HEIGHT * 6 / 8],[WIDTH * 3 / 8, HEIGHT * 5/ 8],[WIDTH * 5 / 8, HEIGHT * 5/ 8],[WIDTH * 5 / 8, HEIGHT * 6 / 8]],
    [[WIDTH * 5 / 8, HEIGHT * 6 / 8],[WIDTH * 5 / 8, HEIGHT * 7/ 8],[WIDTH * 6 / 8, HEIGHT * 10/ 8],[WIDTH * 6 / 8, HEIGHT * 9 / 8]],
    ],
    # blue attack pattern 1 base, includes the swoop down and the bottom of the loop
    # 2
    [
    [[WIDTH * 0 / 8, HEIGHT * 0 / 8],[WIDTH * 0 / 8, HEIGHT * -1/ 16],[WIDTH * -1 / 8, HEIGHT * -1/ 16],[WIDTH * -1 / 8, HEIGHT * 0 / 8]],
    [[WIDTH * -1 / 8, HEIGHT * 0 / 8],[WIDTH * -1 / 8, HEIGHT * 1/ 8],[WIDTH * 3 / 8, HEIGHT * 2/ 8],[WIDTH * 3 / 8, HEIGHT * 3 / 8]],
    [[WIDTH * 3 / 8, HEIGHT * 3 / 8],[WIDTH * 3 / 8, HEIGHT * 4/ 8],[WIDTH * 4 / 8, HEIGHT * 5/ 8],[WIDTH * 4 / 8, HEIGHT * 6 / 8]],
    [[WIDTH * 4 / 8, HEIGHT * 6 / 8],[WIDTH * 4 / 8, HEIGHT * 7/ 8],[WIDTH * 2 / 8, HEIGHT * 7/ 8],[WIDTH * 2 / 8, HEIGHT * 6 / 8]],
    ],
    # blue attack patter 2 finish, returns to starting spot
    # 3
    [
    [[WIDTH * 2 / 8, HEIGHT * 6 / 8],[WIDTH * 2 / 8, HEIGHT * 5/ 8],[WIDTH * 0 / 8, HEIGHT * 1/ 8],[WIDTH * 0 / 8, HEIGHT * 0 / 8]],
    ],
    # Boss Galaga attack and abduct
    # 4
    [
    [[WIDTH * 0 / 8, HEIGHT * 0 / 8],[WIDTH * 0 / 8, HEIGHT * -1/ 8],[WIDTH * -2 / 8, HEIGHT * -1/ 8],[WIDTH * -2 / 8, HEIGHT * 0 / 8]],
    [[WIDTH * -2 / 8, HEIGHT * 0 / 8],[WIDTH * -2 / 8, HEIGHT * 1/ 8],[WIDTH * -2 / 8, HEIGHT * 1 / 8],[WIDTH * -2 / 8, HEIGHT * 2 / 8]],
        # these two lines are are a telegraph for when he is doing to abduction
    [[WIDTH * -2 / 8, HEIGHT * 2 / 8],[WIDTH * -2 / 8, HEIGHT * 3/ 8],[WIDTH * 0 / 8, HEIGHT * 3/ 8],[WIDTH * 0 / 8, HEIGHT * 2 / 8]],
    [[WIDTH * 0 / 8, HEIGHT * 2 / 8],[WIDTH * 0 / 8, HEIGHT * 1/ 8],[WIDTH * -2 / 8, HEIGHT * 1/ 8],[WIDTH * -2 / 8, HEIGHT * 2 / 8]],
        # swoop down
    [[WIDTH * -2 / 8, HEIGHT * 2 / 8],[WIDTH * -2 / 8, HEIGHT * 3/ 8],[WIDTH * 4 / 8, HEIGHT * 3/ 8],[WIDTH * 4 / 8, HEIGHT * 4 / 8]],
    ],
    # Boss Galaga attack and no abduct
    # 5
    [
    [[WIDTH * 0 / 8, HEIGHT * 0 / 8],[WIDTH * 0 / 8, HEIGHT * -1/ 8],[WIDTH * -2 / 8, HEIGHT * -1/ 8],[WIDTH * -2 / 8, HEIGHT * 0 / 8]],
    [[WIDTH * -2 / 8, HEIGHT * 0 / 8],[WIDTH * -2 / 8, HEIGHT * 1/ 8],[WIDTH * -2 / 8, HEIGHT * 1 / 8],[WIDTH * -2 / 8, HEIGHT * 2 / 8]],
    # swoop down
    [[WIDTH * -2 / 8, HEIGHT * 2 / 8],[WIDTH * -2 / 8, HEIGHT * 3/ 8],[WIDTH * 4 / 8, HEIGHT * 3/ 8],[WIDTH * 4 / 8, HEIGHT * 4 / 8]],
        #if attack, fly off bottom
    [[WIDTH * 4 / 8, HEIGHT * 4 / 8],[WIDTH * 4 / 8, HEIGHT * 5/ 8],[WIDTH * 3 / 8, HEIGHT * 9/ 8],[WIDTH * 3 / 8, HEIGHT * 8 / 8]],
    ],
    # return to position from the top of the screen
    # 6
    [
    [[WIDTH * 4 / 8, HEIGHT * 4 / 8],[WIDTH * 4 / 8, HEIGHT * 5/ 8],[WIDTH * 0 / 8, HEIGHT * 1/ 8],[WIDTH * 0 / 8, HEIGHT * 0 / 8]],
    ],
    # 7
    # if abducting, return to start
    [
    [[WIDTH * 1 / 8, HEIGHT * -2 / 8],[WIDTH * 1 / 8, HEIGHT * -1/ 8],[WIDTH * 0 / 8, HEIGHT * -1/ 8],[WIDTH * 0 / 8, HEIGHT * 0 / 8]]
    ]
]

attack_pattern_speed_steps = [
    [
        [3],[1],[1]
    ],
    [
        [3],[1],[2],[2],[2],[1]
    ],
    [
        [3],[1],[2],[2]
    ],
    [
        [1]
    ],
    [
        [2],[2],[2],[1],[1]
    ],
    [
        [2],[2],[1],[1]
    ],
    [
        [2]
    ],
    [
        [1]
    ],
]

def get_bezier_points(i):
    return bezier_points[i]

def get_bezier_attack_pattern(unit):
    """
    a is the start path
    b is the finishing path
    Butterflys only one attack path: id = 1
        They attack on path (0) and fly off screen (7) is its only return path
    Bumblebees have two moves: id = 2
        They can attack and loop off the bottom of the screen (1),
        or they can loops back across the screen (2).
        The respective return paths are (7) for off screen, or (3) for on screen
    Boss Galages also have two moves: id = 3
        They will do an extra flip and try to abduct the player (4)
        They will fly at the player and just shoot missiles and fly off screen (5)
        The respective return paths are (6) for abducting, or (7) for off screen
    """
    a = 0
    b = 6
    if unit.id != 3 or unit.id != 1:
        a = 2
        b = 3
        if random.randrange(0,10) > 7:
            a = 1
            b = 7
    if unit.id == 3:
        a = 4
        b = 6
        if random.randrange(0,10) > 6:
            a = 5
            b = 7
    start_pattern_path = attack_pattern_bezier_points[a]
    start_pattern_speed = attack_pattern_speed_steps[a]
    finish_pattern_path = attack_pattern_bezier_points[b]
    finish_pattern_speed = attack_pattern_speed_steps[b]
    pathing = [start_pattern_path, start_pattern_speed, finish_pattern_path, finish_pattern_speed]
    return pathing

def get_bezier_flight_path(i):
    return flight_paths[i]

def make_bezier_points(x,y, d_x, d_y, heading):
    x_str = "WIDTH * " + str(x) + " / 8"
    y_str = "HEIGHT * " + str(y) + " / 8"
    bezier_points = [0,1,2,3]
    bezier_points[0] = [x_str,y_str]
    x_fin = x + d_x
    y_fin = y + d_y
    bezier_points[3] = ["WIDTH * " + str(x_fin) + " / 8","HEIGHT * " + str(y_fin) + " / 8"] 

    y_con_s = "HEIGHT * " + str(y + heading) + "/ 8"
    y_con_f = "HEIGHT * " + str(y_fin + heading) + "/ 8"
    x_fin
    bezier_points[1] = [x_str,y_con_s ]
    bezier_points[2] = ["WIDTH * " + str(x_fin) + " / 8",y_con_f]
    print("[")
    for i in range(len(bezier_points)):
        print(str(bezier_points[i]) + ",")
    print("],")


if __name__ == "__main__":
    x_start = 1
    y_start = -2
    x_distance = -1
    y_distance = 2
    starting_y_direction = 1
    make_bezier_points(x_start, y_start, x_distance,y_distance, starting_y_direction)
    
    print(
        "this main only runs if this file is ran, not if another program executes it: Bezier_Arrays"
    )