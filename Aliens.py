from Objects import AlienUnit, Alien_Missile
from Galaga_Sprites import alien_missile_image
x = 0
#varaible = AlienUnity(name, alien image group, cycle_position, hp, can abduction, points)
bumble_bee = AlienUnit("Bumble Bee", 1, 0, 1, False, 100)
butter_fly = AlienUnit("Butter Fly", 2, 0, 1, False, 100)
galaga = AlienUnit("Galaga", 3, 0, 2, True, 400)
scorpion = AlienUnit("Scorpion", 4, 0, 1, False, 100)
galaxian = AlienUnit("Galaxian", 5, 0, 1, False, 100)
bosconian = AlienUnit("Bosconian", 6, 0, 1, False, 100)
captured_fighter = AlienUnit("Captured Fighter", 7, 0, 1, False, 100)
alien_explosion = AlienUnit("Alien Explosion", 8, 0, 0, False, 0)
alien_missile = Alien_Missile(alien_missile_image, -10, -10)

if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Aliens"
    )