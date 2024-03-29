import random
from ..constants.CONSTANTS import WIDTH, FIGHTER_Y
from .movement import armada_expand_contract, plot_unit, unit_entry_movement, unit_final_station_movement
from .building import build_alien_armada
from .attacking import select_attackers, unit_attack_movement
from .abucting import abduction_animation
from . .services.visual_output.sprite_manipulation import toggle_alien_sprite_images

def alien_explodes(unit, armada):
    unit.entry_flight_is_completed = True
    unit.station_flight_is_completed = True
    unit.attack_flight_is_completed = True
    y = unit.position_y
    x = unit.position_x
    plot_unit(unit, x, y, 0)

def alien_armada_update(armada, alien_missile_list, time, player):
    for i in range(len(armada.platoon)):
        toggle_alien_sprite_images(armada.platoon[i], time)
        if armada.is_defeated == True or armada.platoon[i].is_defeated == True:
            continue
        if not player.pause:
            select_attackers(armada, time)          
        platoon_behavior(armada.platoon[i], i, time, armada, alien_missile_list, player)
        armada_expand_contract(armada.platoon[i], time)
            
def platoon_behavior(platoon, i, time, armada, alien_missile_list, player):
    # iterate through the flightpaths and platoons in that path
    for j in range(len(platoon.unit)):
        if platoon.unit[j].hp == 0:
            alien_explodes(platoon.unit[j], armada)
            continue
        if platoon.unit[j].id ==7 and platoon.unit[j].boss_capture_id == None:
            # fx can handle both alien capture, and player reclaim
            abduction_animation(platoon.unit[j],player, armada, i, j)
            continue
        entry_flight = platoon.unit[j].entry_flight_is_completed
        station_flight = platoon.unit[j].station_flight_is_completed
        attack_flight = platoon.unit[j].attack_flight_is_completed
        if attack_flight != True and platoon.unit[j].id !=7:
            unit_attack_movement(platoon, platoon.unit[j], j, armada, alien_missile_list)
        elif entry_flight != True:
            unit_entry_movement(platoon, j, time)
        elif station_flight != True:
            unit_final_station_movement(platoon, j, platoon.unit[j])
        if attack_flight == entry_flight == station_flight == True:
            rotation = 180
            x = platoon.expanded_final_position + platoon.unit[j].expanded_final_position
            y = platoon.final_position[1] + platoon.unit[j].final_position[1]
            plot_unit(platoon.unit[j], x, y, rotation)
            if platoon.unit[j].id == 7 and player.abducted:
                # considering making an event to handle player deaths and stuff             
                player.position_x = WIDTH / 2
                player.position_y = FIGHTER_Y
                player.rotation = 0
                player.boss_capture_id = None

def main():
    run = True
    time = 0
    armada = build_alien_armada()
    while run:
        alien_mvmt = alien_armada_behavior(armada, time)
        time = time + 10
        # if armada.platoon[7].unit[3].entry_flight_is_completed:
        run = False

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: alien_actions"
    )
