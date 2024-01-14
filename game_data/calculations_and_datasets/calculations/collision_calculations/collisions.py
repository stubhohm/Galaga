from constants.CONSTANTS import FIGHTER_HEIGHT, FIGHTER_WIDTH, ALIEN_HEIGHT, ALIEN_WIDTH, FIGHTER_Y
from missile_tracking.missile_management import remove_missile
from objects.Alien_Objects import AlienUnit
from Sprite_Manipulation import toggle_boss_galaga_sprite


def armada_defeated(armada):
    for i in range(len(armada.platoon)):
        if armada.platoon[i].is_defeated != True:
           return
    armada.is_defeated = True

def platoon_defeated(armada, i):
    if armada.platoon[i].is_defeated != True:
        for j in range(len(armada.platoon[i].unit)):
            if armada.platoon[i].unit[j].hp != 0:
                return
        armada.platoon[i].is_defeated = True
        armada_defeated(armada)

def alien_takes_damage(unit, player):
    unit.hp = unit.hp - 1
    if unit.hp == 0:
        unit = AlienUnit(
            "Alien Explosion",
            9,
            0,
            0,
            False,
            0,
            0,
            unit.position_x,
            unit.position_y,
            0,
            0,
            True,
            True,
            unit.attack_flight_is_completed,
            0,
            None,
            None,
            )
        
        player.kills = player.kills + 1
        player.hits = player.hits + 1
    else:
        unit.name = "Damaged Galaga"
        player.hits = player.hits + 1
        toggle_boss_galaga_sprite(unit)
    return unit

def alien_to_player_fighter_collision(alien_armada, player):
    contact = False
    for i in range(len(alien_armada.platoon)):
        for j in range(len(alien_armada.platoon[i].unit)):
            unit = alien_armada.platoon[i].unit[j]
            if unit.position_y:
                if unit.position_y > FIGHTER_Y - FIGHTER_HEIGHT / 2:
                    return convert_to_coordinates(unit, player)

def alien_missile_to_player_fighter_collision(alien_missile_list, player):
    for i in range(len(alien_missile_list.missile)):
        missile = alien_missile_list.missile[i]
        if missile.position_y > FIGHTER_Y - FIGHTER_HEIGHT / 2:
            hit = convert_to_coordinates(missile, player)
            if hit:
                remove_missile(alien_missile_list, i)
            return hit

def collision_check(player_missile_list,player, alien_missile_list, alien_armada):
    if len(player_missile_list.missile) > 0:
        player_missile_to_alien_collision(player_missile_list, alien_armada, player)    
    if len(alien_missile_list.missile) > 0:
        contact = alien_missile_to_player_fighter_collision(alien_missile_list, player)
        if contact:
            a = 0 # return player death
    contact = alien_to_player_fighter_collision(alien_armada, player)
    if contact:
            a = 0 # return player death

def convert_to_coordinates(unit, player):
    # the 4 is to shrink it since there is a good amount of white space on the sprite drawings
    # this number will need to be tweaked to get the collision just right so its not bs
    x = unit.position_x 
    y = unit.position_y
    nose_tip_x = player.position_x
    nose_tip_y = player.position_y - FIGHTER_HEIGHT / 4
    left_wing_tip_x = player.position_x - FIGHTER_WIDTH / 4
    left_wing_tip_y = right_wing_tip_y = player.position_y + FIGHTER_WIDTH / 4
    right_wing_tip_x = player.position_x + FIGHTER_WIDTH / 4
    a = (nose_tip_x, nose_tip_y)
    b = (left_wing_tip_x, left_wing_tip_y)
    c = (right_wing_tip_x, right_wing_tip_y)
    return player_collision_calculation(a, b, c, x, y)

def player_collision_calculation(a, b, c, x, y):
    
    #calculate barycentric coordinates
    det_T = (b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])
    alpha = ((b[1] - c[1]) * (x - c[0]) + (c[0] - b[0]) * (y - c[1])) / det_T
    beta = ((c[1] - a[1]) * (x - c[0]) + (a[0] - c[0]) * (y - c[1])) / det_T
    gamma = 1 - alpha - beta

    # Check if the point is inside the triangle
    return 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1

def player_missile_to_alien_collision(player_missile_list, alien_armada, player):
    y = ALIEN_HEIGHT / 3
    x = ALIEN_WIDTH / 4
    for i in range(len(player_missile_list.missile)):
        missile = player_missile_list.missile[i]
        for j in range(len(alien_armada.platoon)):
            if alien_armada.platoon[j].is_defeated:
                continue
            for k in range(len(alien_armada.platoon[j].unit)):
                unit = alien_armada.platoon[j].unit[k]
                if unit.hp != 0 and unit.position_y:
                    if unit.position_y + y > missile.position_y > unit.position_y - y:
                        if unit.position_x + x > missile.position_x > unit.position_x - x:
                            remove_missile(player_missile_list, i)
                            alien_armada.platoon[j].unit[k] = alien_takes_damage(unit, player)
                            platoon_defeated(alien_armada, j)

                        
def main():
    collision = player_collision_calculation((64,0), (0,32), (0,-32), 18, 18)
    print(collision)

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Colissions"
    )