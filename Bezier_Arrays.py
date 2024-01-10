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
        (WIDTH * 11 / 16, HEIGHT * 5 / 8), (WIDTH * 5 / 8, HEIGHT * 4 / 8) 
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
        (WIDTH * 5 / 16, HEIGHT * 5 / 8), (WIDTH * 3 / 8, HEIGHT * 4 / 8) 
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

def get_bezier_points(i):
    return bezier_points[i]

def get_bezier_flight_path(i):
    return flight_paths[i]


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Bezier_Arrays"
    )