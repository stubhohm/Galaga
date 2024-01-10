import pygame
from CONSTANTS import ALIEN_HEIGHT, ALIEN_WIDTH, FIGHTER_HEIGHT, FIGHTER_WIDTH

## alien ship images
# aliens also have a unique sprite for when they are hit
# is the same shape, just yellow and orange color scheme
# one will need to be made for each ship as they are not present yet
# galaxian and bosconians only have one sprite
# captured fighter is the same as the ship image and needs a recoloring

bumble_bee_image = [
    pygame.image.load("Sprites//Aliens//bumble_bee_1.png"),
    pygame.image.load("Sprites//Aliens//bumble_bee_2.png"),
]
butterfly_image = [
    pygame.image.load("Sprites//Aliens//butterfly_1.png"),
    pygame.image.load("Sprites//Aliens//butterfly_2.png"),
]
galaga_image = [
    pygame.transform.rotate(pygame.image.load("Sprites//Aliens//galaga_1.png"),180),
    pygame.transform.rotate(pygame.image.load("Sprites//Aliens//galaga_2.png"),180),
    pygame.transform.rotate(pygame.image.load("Sprites//Aliens//galaga_damaged_1.png"),180),
    pygame.transform.rotate(pygame.image.load("Sprites//Aliens//galaga_damaged_2.png"),180),
]
scorpion_image = [
    pygame.image.load("Sprites//Aliens//scorpion_1.png"),
    pygame.image.load("Sprites//Aliens//scorpion_2.png"),
]
galaxian_image = [
    pygame.image.load("Sprites//Aliens//galaxian_1.png"),
    pygame.image.load("Sprites//Aliens//galaxian_2.png"),
]
bosconian_image = [
    pygame.image.load("Sprites//Aliens//bosconian_1.png"),
    pygame.image.load("Sprites//Aliens//bosconian_2.png"),
]
captured_fighter_image = [
    pygame.image.load("Sprites//Aliens//captured_fighter_1.png"),
    pygame.image.load("Sprites//Aliens//captured_fighter_2.png"),
]

alien_missile_image = pygame.image.load("Sprites//Aliens//alien_missile.png")

alien_explosion = [
    pygame.image.load("Sprites//Aliens//alien_explosion_1.png"),
    pygame.image.load("Sprites//Aliens//alien_explosion_2.png"),
    pygame.image.load("Sprites//Aliens//alien_explosion_3.png"),
    pygame.image.load("Sprites//Aliens//alien_explosion_4.png"),
    pygame.image.load("Sprites//Aliens//alien_explosion_5.png"),
]

Alien_Image = [
    bumble_bee_image,
    butterfly_image,
    galaga_image,
    scorpion_image,
    galaxian_image,
    bosconian_image,
    captured_fighter_image,
    alien_missile_image,
    alien_explosion,
]

# fighter images
fighter_image = [
    pygame.image.load("Sprites//Fighter//fighter.png"),
    pygame.image.load("Sprites//Fighter//double_fighter.png"),
]

fighter_missile = pygame.image.load("Sprites//Fighter//fighter_missile.png")
# same exlposion as aliens, might change later
fighter_explosion = [
    pygame.image.load("Sprites//Fighter//fighter_explosion_1.png"),
    pygame.image.load("Sprites//Fighter//fighter_explosion_2.png"),
    pygame.image.load("Sprites//Fighter//fighter_explosion_3.png"),
    pygame.image.load("Sprites//Fighter//fighter_explosion_4.png"),
    pygame.image.load("Sprites//Fighter//fighter_explosion_5.png"),
]

if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Galaga_Sprites"
    )
