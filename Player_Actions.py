import pygame
from CONSTANTS import WIDTH, HEIGHT
from Object_Movement import object_movement

def player_movement(key_pressed, player):
    if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
        player.position_x, player.position_y = object_movement(player,  player.speed_x * -1, 0) 
        if player.position_x < WIDTH / 10:
            player.position_x = WIDTH /10
    if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
        player.position_x, player.position_y = object_movement(player, player.speed_x, 0)
        if player.position_x > WIDTH * 9 / 10:
            player.position_x = WIDTH * 9 / 10

def fire_missile(player, missile, key_released):
    if key_released == [pygame.K_SPACE][0]:
        missile.position_x = player.position_x
        missile.position_y = player.position_y


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Player Actions"
    )