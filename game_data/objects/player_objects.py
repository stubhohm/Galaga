from game_data.classes.classes import Player, Missile
from game_data.imported_assets.galaga_sprites import fighter_image, fighter_missile
from game_data.constants.CONSTANTS import WIDTH

# Plaery class: name, lives, image, score, x position, double fighter
player = Player("Player", 3, fighter_image[0], 0, WIDTH / 2, False, 1)
missile = Missile(fighter_missile, -10, -800, False)


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Players"
    )
