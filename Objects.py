import pygame
from CONSTANTS import WIDTH, HEIGHT


class Armada:  # defines the entire alien fleet for a level
    def __init__(self, platoons):
        self.platoons = platoons


class Platoon:  # defines a specific group of eight aliens
    def __init__(self, platoon_id, units):
        # position within the Armada
        self.platoon_id = platoon_id
        # each ship and its rank in the platoon
        self.units = units


class AlienUnit:  # the uique atributes of each ship unit
    def __init__(self, name, alien_image_group, image_in_cylce, hp, can_abduct, point_value):
        self.name = name
        self.sprite = alien_image_group
        self.sprite_cycle = image_in_cylce
        self.hp = hp
        self.can_abduct = can_abduct
        self.point_value = point_value
        self.is_alien = True


# define the player class
class Player:
    # attributes for the player
    def __init__(self, name, lives, sprite, score, position_y, double_fighter):
        self.name = name
        self.lives = lives
        self.sprite = sprite
        self.score = score
        self.position_y = position_y
        self.double_fighter = double_fighter


class Missile:
    def __init__(self, sprite, position_x, position_y, double_fighter):
        self.sprite = sprite
        self.position_x = position_x
        self.position_y = position_y
        self.double_fighter = double_fighter


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Objects"
    )
