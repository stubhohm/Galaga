import pygame
from CONSTANTS import ALIEN_HEIGHT, ALIEN_WIDTH, FIGHTER_HEIGHT, FIGHTER_WIDTH

## alien ship images
# aliens also have a unique sprite for when they are hit
# is the same shape, just yellow and orange color scheme
# one will need to be made for each ship as they are not present yet
# galaxian and bosconians only have one sprite
# captured fighter is the same as the ship image and needs a recoloring
bumble_bee_image  = [
    pygame.image.load("Sprites//Aliens//bumble_bee_1.png"),
    pygame.image.load("Sprites//Aliens//bumble_bee_2.png")
]
butterfly_image = [
    pygame.image.load("Sprites//Aliens//butterfly_1.png"),
    pygame.image.load("Sprites//Aliens//butterfly_2.png")
]
galaga_image = [
    pygame.image.load("Sprites//Aliens//galaga_1.png"),
    pygame.image.load("Sprites//Aliens//galaga_2.png")
]
galaga_damaged_image = [
    pygame.image.load("Sprites//Aliens//galaga_damaged_1.png"),
    pygame.image.load("Sprites//Aliens//galaga_damaged_2.png")
]
scorpion_image = [
    pygame.image.load("Sprites//Aliens//scorpion_1.png"),
    pygame.image.load("Sprites//Aliens//scorpion_2.png")
]
galaxian_image = [
    pygame.image.load("Sprites//Aliens//galaxian_1.png"),
    pygame.image.load("Sprites//Aliens//galaxian_2.png")
]
bosconian_image = [
    pygame.image.load("Sprites//Aliens//bosconian_1.png"),
    pygame.image.load("Sprites//Aliens//bosconian_2.png")
]
captured_fighter_image = [
    pygame.image.load("Sprites//Aliens//captured_fighter_1.png"),
    pygame.image.load("Sprites//Aliens//captured_fighter_2.png")
]

alien_missile_image = pygame.image.load("Sprites//Aliens//alien_missile.png")


alien_explosion = [
    pygame.image.load("Sprites//Aliens//alien_explosion_1.png"),
    pygame.image.load("Sprites//Aliens//alien_explosion_2.png"),
    pygame.image.load("Sprites//Aliens//alien_explosion_3.png"),
    pygame.image.load("Sprites//Aliens//alien_explosion_4.png"),
    pygame.image.load("Sprites//Aliens//alien_explosion_5.png")
]

# fighter images
fighter_image = pygame.image.load("Sprites//Fighter//fighter_1.png")
double_fighter_image = pygame.image.load("Sprites//Fighter//fighter_2.png")
fighter_missile = pygame.image.load("Sprites//Fighter//fighter_missile.png")
# same exlposion as aliens, might change later
fighter_explosion = [
    pygame.image.load("Sprites//Fighter//fighter_explosion_1.png"),
    pygame.image.load("Sprites//Fighter//fighter_explosion_2.png"),
    pygame.image.load("Sprites//Fighter//fighter_explosion_3.png"),
    pygame.image.load("Sprites//Fighter//fighter_explosion_4.png"),
    pygame.image.load("Sprites//Fighter//fighter_explosion_5.png")
]

if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Galaga_Sprites"
    )
