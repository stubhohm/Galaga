import pygame
from CONSTANTS import WIDTH, HEIGHT, FIGHTER_Y, MISSILE_SPEED, FIGHTER_SPEED


class Alien_Armada:  # defines the entire alien fleet for a level
    def __init__(self, platoon):
        self.platoon = platoon


class Alien_Platoon:  # defines a specific group of eight aliens
    def __init__(self, platoon_id, unit, start_time, path_time):
        # position within the Armada
        self.platoon_id = platoon_id
        # each ship and its rank in the platoon
        self.unit = unit
        self.start_time = start_time
        self.path_time = path_time


class Alien_Unit:  # the uique atributes of each ship unit
    def __init__(
        self,
        name,
        id,
        image_in_cylce,
        hp,
        can_abduct,
        point_value,
        rotation,
        position_x,
        position_y,
        d_x,
        d_y,
        completed,
        path_time
    ):
        self.name = name
        self.id = id
        self.sprite = id
        self.position_x = position_x
        self.position_y = position_y
        self.d_x = d_x
        self.d_y = d_y
        self.sprite_cycle = image_in_cylce
        self.hp = hp
        self.can_abduct = can_abduct
        self.point_value = point_value
        self.is_alien = True
        self.rotation = rotation
        self.is_missile = False
        self.is_fighter = False
        self.flight_is_completed = completed
        self.path_time = path_time


class Alien_Missile:
    def __init__(self, sprite, position_x, position_y):
        self.sprite = sprite
        self.position_x = position_x
        self.position_y = position_y
        self.rotation = 0
        self.is_alien = True
        self.is_missile = True
        self.speed_y = MISSILE_SPEED * -1


class Missile:
    def __init__(self, sprite, position_x, position_y, double_fighter):
        self.sprite = sprite
        self.position_x = position_x
        self.position_y = position_y
        self.double_fighter = double_fighter
        self.rotation = 0
        self.is_alien = False
        self.is_missile = True
        self.is_fighter = False
        self.speed_y = MISSILE_SPEED


class Active_Missiles:
    def __init__(self, missile, is_player_list):
        self.missile = missile
        self.is_player_list = is_player_list


# define the player class
class Player:
    # attributes for the player
    def __init__(self, name, lives, sprite, score, position_x, double_fighter, active):
        self.name = name
        self.lives = lives
        self.sprite = sprite
        self.score = score
        # y position is a constant
        self.position_x = position_x
        self.position_y = FIGHTER_Y
        self.double_fighter = double_fighter
        self.active = active
        self.rotation = 0
        self.is_alien = False
        self.is_fighter = True
        self.is_missile = False
        self.speed_x = FIGHTER_SPEED

class Flight_Path:
    def __init__(self, name, path_id, platoon, completed):
        self.name = name
        self.path = path_id
        self.platoon = platoon
        self.is_completed = completed
if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Objects"
    )
