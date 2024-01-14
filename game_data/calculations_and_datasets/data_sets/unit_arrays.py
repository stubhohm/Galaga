from ...constants.CONSTANTS import HEIGHT, WIDTH, UNIT_OFFSET_X, UNIT_OFFSET_Y

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
    [1, 1, 1, 1],
]

# these will get tweaked after positioning function is completed
start_time = [0, 0, 200, 232, 400, 432, 600, 632, 800, 832]

platoon_paths = [1, 2, 3, 3, 4, 4, 1, 1, 2, 2]

platoon_expansion_multiple = [
    0,
    0,
    -1,
    1,
    -2,
    2,
    -1.5,
    1.5,
    -2.5,
    2.5
]

platoon_final_position = [
    [WIDTH * 4 / 8, HEIGHT * 4 / 16],
    [WIDTH * 4 / 8, HEIGHT * 3 / 16],
    [WIDTH * 7 / 16, HEIGHT * 5 / 32],
    [WIDTH * 9 / 16, HEIGHT * 5 / 32],
    [WIDTH * 5 / 16, HEIGHT * 3 / 16],
    [WIDTH * 11 / 16, HEIGHT * 3 / 16],
    [WIDTH * 3 / 8, HEIGHT * 4 / 16],
    [WIDTH * 5 / 8, HEIGHT * 4 / 16],
    [WIDTH * 2 / 8, HEIGHT * 4 / 16],
    [WIDTH * 6 / 8, HEIGHT * 4 / 16],
]

x = UNIT_OFFSET_X
y = UNIT_OFFSET_Y
unit_offset = [
    # offsets are either a grid shape
    # unit 1(-x,-y), unit 3 (+x, -y)
    # unit 2(-x, +y), unit 4 (+x, +y)

    # or an L shape
    # unit 1 butterfly  unit 3 boss   # #
    # unit 2 butterly       shape:      #
    # unit 4 boss or                    #
    # unit 1 butterfly  unit 3 boss         # #
    # unit 2 butterfly      shape:          #
    # unit 4 boss                           #
    # nearly all units are grid shapes except for those with a boss galaga in them
    [
        (-x, -y), (x, -y), (-x, y), (x, y)
    ],
    [
        (-x, y), (- 3 * x, - 3 *y), (-x, + 3 * y), (0.5 * 3, - 3 * y)
    ],
    [
        (x, y), (-0.5 * x , - 3 * y), (x, + 3 * y), (3 * x, - 3 * y)
    ]
]

if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Unit Arrays"
    )