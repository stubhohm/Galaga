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
    def __init__(self, name, id, sprite, hp, can_abduct, value):
        self.name = name
        self.id = id
        self.sprite = sprite
        self.hp = hp
        self.can_abduct = can_abduct
        self.value = value
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
        "this main only runs if this file is ran, not if another program executes it: Object"
    )
