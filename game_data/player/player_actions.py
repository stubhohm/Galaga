import pygame
from game_data.constants.CONSTANTS import WIDTH, HEIGHT
from game_data.objects.object_movement import object_movement
from game_data.missile_tracking.missile_management import add_missile
from ..services.visual_output.sprite_manipulation import cycle_explosion

def player_update(player, player_missile_list, time, key_released, key_pressed):
    if player.abducted == True:
        return
    if not player.pause:
        player_movement(key_pressed, player, time)
        player_fire_missile(player, player_missile_list, key_released)
    if player.hp == 0:
        cycle_explosion(player, time)

def player_movement(key_pressed, player, time):
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
    if key_released == [pygame.K_SPACE][0]:
        if player.double_fighter:
             max = 4
        else:
            max = 2
        if 0 <= len(player_missile_list.missile) < max:
            if len(player_missile_list.missile) == 2:
                a = 0
            player_missile_list.missile = add_missile(player_missile_list, player)
            player.shots_fired = player.shots_fired + 1
            # if a missile is fired it joins the class active missile at the end of the current active missile list

def increase_player_score(unit,player):
    before = int(player.score / 12000)
    player.score = int(player.score + unit.point_value)
    after = int(player.score / 12000)
    if before != after:
        player.extra_life = True

def check_to_reclaim_captured_fighter(platoon, unit, unit_rank):
    if len(platoon.unit) > 4:
        if unit.id == 9 and platoon.unit[4].boss_capture_id == unit_rank and unit.hp == 0:
            if unit.position_y > 0:
                platoon.unit[-1].boss_capture_id = None
            else:
                platoon.unit[4].hp = 0

if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Player Actions"
    )
