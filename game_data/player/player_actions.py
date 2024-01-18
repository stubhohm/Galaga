import pygame
from game_data.constants.CONSTANTS import WIDTH, HEIGHT
from game_data.objects.object_movement import object_movement
from game_data.missile_tracking.missile_management import add_missile

def player_movement(key_pressed, player):
    if player.abducted == True:
        a = 0
    else:
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

def player_fire_missile(player, player_missile_list, key_released):
    if player.abducted == True:
        return
    if key_released == [pygame.K_SPACE][0]:
        if 0 <= len(player_missile_list.missile) <= 1:
            player_missile_list.missile = add_missile(player_missile_list, player)
            player.shots_fired = player.shots_fired + 1
            # if a missile is fired it joins the class active missile at the end of the current active missile list

def increase_player_score(unit,player):
    player.score = int(player.score + unit.point_value)

if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Player Actions"
    )
