import pygame
from CONSTANTS import WIDTH, HEIGHT, FIGHTER_Y, MISSILE_SPEED, FIGHTER_SPEED


class Armada:  # defines the entire alien fleet for a level
    def __init__(self, platoons):
        self.platoons = platoons


class Platoon:  # defines a specific group of eight aliens
    def __init__(self, platoon_id, units, path):
        # position within the Armada
        self.platoon_id = platoon_id
        # each ship and its rank in the platoon
        self.units = units
        self.path = path


class AlienUnit:  # the uique atributes of each ship unit
    def __init__(
        self, name, alien_image_group, image_in_cylce, hp, can_abduct, point_value, rotation
    ):
        self.name = name
        self.sprite = alien_image_group
        self.sprite_cycle = image_in_cylce
        self.hp = hp
        self.can_abduct = can_abduct
        self.point_value = point_value
        self.is_alien = True
        self.rotation = rotation
        self.is_missile = False
        self.is_fighter = False

class Alien_Missile:
    def __init__(self, sprite, position_x, position_y):
        self.sprite = sprite
        self.position_x = position_x
        self.position_y = position_y
        self.rotation = 0
        self.is_alien = True
        self.is_missile = True

# define the player class
class Player:
    # attributes for the player
    def __init__(self, name, lives, sprite, score, position_x, double_fighter, active):
        self.name = name
        self.lives = lives
        self.sprite = sprite
        self.score = score
        #y position is a constant
        self.position_x = position_x
        self.position_y = FIGHTER_Y
        self.double_fighter = double_fighter
        self.active = active
        self.rotation = 0
        self.is_alien = False
        self.is_fighter = True
        self.is_missile = False
        self.speed_x = FIGHTER_SPEED


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


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Objects"
    )
