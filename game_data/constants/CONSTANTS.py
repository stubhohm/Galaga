# game attributes
# Screen Sizing
# all other scaling will be derived from height and width

HEIGHT = 800
WIDTH = 600
# Frame Rate
FPS = 60

PIXEL_ART_SCALE = 32
# sprite sizing
ALIEN_HEIGHT = PIXEL_ART_SCALE * 2
ALIEN_WIDTH = PIXEL_ART_SCALE * 2
FIGHTER_HEIGHT = PIXEL_ART_SCALE * 3
FIGHTER_WIDTH = PIXEL_ART_SCALE * 3
MISSILE_HEIGHT = PIXEL_ART_SCALE * 3
MISSILE_WIDTH = PIXEL_ART_SCALE * 2
BEAM_HEIGHT = PIXEL_ART_SCALE * 5.5
BEAM_WIDTH = PIXEL_ART_SCALE * 2.5


# fighter y position
FIGHTER_Y = HEIGHT * 7 / 8

# scaled movement
FIGHTER_SPEED = WIDTH / 200
MISSILE_SPEED = HEIGHT / 64

# alien x and y offsets
UNIT_OFFSET_X = WIDTH / 32
UNIT_OFFSET_Y = HEIGHT / 64

# alien platoon attack wave start times
WAVE_STARTS = [
    0,
    200,
    400,
    600,
    800
]
SECOND_PLATOON_DELAY = 32
START_DELAY = 200

ALHAPHABET = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

def main():
    print("seems pretty constant to me")

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Constants"
    )
