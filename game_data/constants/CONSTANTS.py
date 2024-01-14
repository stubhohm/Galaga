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

# fighter y position
FIGHTER_Y = HEIGHT * 7 / 8

# scaled movement
FIGHTER_SPEED = WIDTH / 200
MISSILE_SPEED = HEIGHT / 64

# alien x and y offsets
UNIT_OFFSET_X = WIDTH / 32
UNIT_OFFSET_Y = HEIGHT / 64

def main():
    print("seems pretty constant to me")

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Constants"
    )
