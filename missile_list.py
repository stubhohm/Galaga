from classes.Classes import ActiveMissiles
from objects.Player_Objects import missile

player_missile_list = ActiveMissiles([missile], True)
alien_missile_list = ActiveMissiles([missile], False)


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Lists"
    )