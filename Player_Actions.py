import pygame
from CONSTANTS import WIDTH, HEIGHT
from Object_Movement import object_movement

# from Player import missile
# from Lists import player_missile_list
from List_Maniplution import add_missile


def player_movement(key_pressed, player):
    if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
        player.position_x, player.position_y = object_movement(
            player, player.speed_x * -1, 0
        )
        if player.position_x < WIDTH / 10:
            player.position_x = WIDTH / 10
    if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
        player.position_x, player.position_y = object_movement(
            player, player.speed_x, 0
        )
        if player.position_x > WIDTH * 9 / 10:
            player.position_x = WIDTH * 9 / 10


def fire_missile(player, player_missile_list, key_released):
    if key_released == [pygame.K_SPACE][0]:
        if len(player_missile_list.missile) == 0:
            player_missile_list.missile = add_missile(player_missile_list)
        elif player_missile_list.missile[0].position_y < (
            player.position_y - (HEIGHT / 6)
        ):
            player_missile_list.missile = add_missile(player_missile_list)
            player_missile_list.missile[0].position_x = player.position_x
            player_missile_list.missile[0].position_y = player.position_y - (
                HEIGHT / 30
            )
            # if a missile is fired it joins the class active missile at the end of the current active missile list
    return player_missile_list


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Player Actions"
    )
