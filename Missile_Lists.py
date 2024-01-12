from Classes import Active_Missiles
from Player_Objects import missile

player_missile_list = Active_Missiles([missile], True)
alien_missile_list = Active_Missiles([missile], False)


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Lists"
    )
