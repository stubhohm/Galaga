# game attributes
    # Screen Sizing 
    # all other scaling will be derived from height and width

HEIGHT = 800
WIDTH = 600
    # Frame Rate
FPS = 60

# sprite sizing
ALIEN_HEIGHT = HEIGHT / 8 
ALIEN_WIDTH = WIDTH / 6
FIGHTER_HEIGHT = HEIGHT / 8
FIGHTER_WIDTH = WIDTH / 6
MISSILE_HEIGHT = 100
MISSILE_WIDTH = 200

# fighter y position
FIGHTER_Y = HEIGHT * 7 / 8

# scaled movement
FIGHTER_SPEED = WIDTH / 200
MISSILE_SPEED = HEIGHT / 100


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Constants"
    )
