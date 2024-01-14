from classes.Classes import Player, Missile
from imported_assets.Galaga_Sprites import fighter_image, fighter_missile
from constants.CONSTANTS import WIDTH

# Plaery class: name, lives, image, score, x position, double fighter
player = Player("Player", 3, fighter_image[0], 0, WIDTH / 2, False, 1)
missile = Missile(fighter_missile, -10, -800, False)


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Players"
    )