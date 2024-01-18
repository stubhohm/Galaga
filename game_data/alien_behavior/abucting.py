import copy
from ..imported_assets.galaga_sprites import tractor_beam
from ..constants.CONSTANTS import FPS, FIGHTER_HEIGHT
from ..classes.classes import AlienUnit

def attempt_abduction(unit, time_step):
    # shift timestep for this animation
    time_step = time_step - 5
    # make the unit hold unit the animation cycle is completed
    frames = 8
    current_frame = int(time_step * FPS)
    version = 0
    frame = 0
    # the beam takes 1 second to deploy the tractor beam
    # the beam takes 1 second to retract
    shift = int(current_frame / 5)
    if shift % 2 == 0:
        version = 0
    else:
        version = 1
    if time_step <= 1 or 3 < time_step <= 4:
        if time_step > 3:
            current_frame = (4 * FPS) - current_frame - 1
        abduction_frame = int(current_frame / FPS * frames)
        for i in range(0,frames + 1):
            if abduction_frame == i:
                frame = i
                break
    elif 1 < time_step <= 3:
    # the beam is held out for 2 seconds
        frame = 7
    # once animation is completed set can_abduct to false, and the time_step to 0
    elif time_step > 4:
        # this is a blank image
        unit.beam_image = None
        # shift back timestep
        time_step = time_step + 1 + 1/FPS
        unit.can_abduct = False
        return time_step
    unit.beam_image = tractor_beam[version][frame]
    # shift timestep back
    if unit.id == 7:
        unit.beam_image = tractor_beam[2][0]
    time_step = time_step + 5 + 1/FPS
    return time_step

def abduction_animation(player,abductor, armada, i, j):
    # rotate one degree
    
    d_x = (abductor.position_x - player.position_x - 1) * 5
    d_y = abductor.position_y + 32 - player.position_y
    if abs(d_y) > abs(d_x):
        player.position_y = player.position_y - 3
        if abs(d_y) < 3:
            player.position_y = abductor.position_y + 32
            d_y = 0 
    else:
        if d_x > 0:
            player.position_x = player.position_x + 2
        elif abs(d_x) < 6:
            player.position_x = abductor.position_x - 1
            d_x = 0
        else: 
            player.position_x = player.position_x - 2
        
    if player.rotation == - 360:
        player.rotation = 0
    if d_x == 0 and d_y == 0 and player.rotation == -180:
        captured_fighter = AlienUnit(
            "Captured Fighter",
            7,
            0,
            1,
            True,
            1000,
            None,
            0,
            player.position_x,
            player.position_y,
            None,
            None,
            True,
            True,
            False,
            abductor.path_time - 0.3,
            None,
            (abductor.final_position[0],abductor.final_position[1] - FIGHTER_HEIGHT/2),
            abductor.expanded_final_position
        )
        captured_fighter.beam_image = tractor_beam[2][0]
        armada.platoon[i].unit.append(captured_fighter)
        captured_fighter.path = copy.deepcopy(abductor.path)
        captured_fighter.path[0][5][3][1] = abductor.path[0][5][3][1] - FIGHTER_HEIGHT/2
        captured_fighter.path[0][5][2][1] = abductor.path[0][5][2][1] - FIGHTER_HEIGHT/2
        captured_fighter.is_fighter = True
        captured_fighter.boss_capture_id = j
        player.position_x = None
        player.position_y = None
        return True
    else:
        player.rotation = player.rotation - 20

if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: abducting"
    )