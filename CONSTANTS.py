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
FIGHTER_HEIGHT = PIXEL_ART_SCALE * 4
FIGHTER_WIDTH = PIXEL_ART_SCALE * 4
MISSILE_HEIGHT = PIXEL_ART_SCALE * 3
MISSILE_WIDTH = PIXEL_ART_SCALE * 3

# fighter y position
FIGHTER_Y = HEIGHT * 7 / 8

# scaled movement
FIGHTER_SPEED = WIDTH / 200
MISSILE_SPEED = HEIGHT / 200


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Constants"
    )
