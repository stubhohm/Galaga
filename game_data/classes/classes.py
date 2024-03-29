from ..constants.CONSTANTS import WIDTH, HEIGHT, FIGHTER_Y, MISSILE_SPEED, FIGHTER_SPEED


class AlienArmada:  # defines the entire alien fleet for a level
    def __init__(self, platoon, is_defeated = False, active_attackers = 0, hatched_fighters = False, game_level = 0):
        self.platoon = platoon
        self.is_defeated = is_defeated
        self.active_attackers = active_attackers
        self.hatched_fighters = hatched_fighters
        self.game_level = game_level

class AlienPlatoon:  # defines a specific group of eight aliens
    def __init__(
            self, 
            platoon_id, 
            unit, 
            start_time, 
            path_time, 
            final_position, 
            flight_path = 0, 
            expanded_final_position = 0, 
            expansion_scaler = 0, 
            is_defeated = False):
        # position within the Armada
        self.platoon_id = platoon_id
        # each ship and its rank in the platoon
        self.unit = unit
        self.start_time = start_time
        self.path_time = path_time
        self.final_position = final_position
        self.flight_path = flight_path
        self.expanded_final_position = expanded_final_position
        self.expansion_scaler = expansion_scaler
        self.is_defeated = is_defeated

class AlienUnit:  # the uique atributes of each ship unit
    def __init__(
        self,
        name,
        id,
        image_in_cylce,
        hp,
        can_abduct,
        point_value,
        beam_image = None,
        rotation = 0,
        position_x = None,
        position_y = None,
        d_x = None,
        d_y = None,
        entry_flight_is_completed = False,
        station_flight_is_completed = False,
        attack_flight_is_completed = True,
        path_time = 0,
        path = None,
        final_position = None,
        expanded_final_position = None,
        boss_capture_id = None

    ):
        self.name = name
        self.id = id
        self.sprite = id
        self.position_x = position_x
        self.position_y = position_y
        self.d_x = d_x
        self.d_y = d_y
        self.image_in_cycle = image_in_cylce
        self.hp = hp
        self.point_value = point_value
        self.can_abduct = can_abduct
        self.beam_image = beam_image
        self.is_alien = True
        self.rotation = rotation
        self.is_missile = False
        self.is_fighter = False
        self.entry_flight_is_completed = entry_flight_is_completed
        self.station_flight_is_completed = station_flight_is_completed
        self.attack_flight_is_completed = attack_flight_is_completed
        self.path_time = path_time
        self.path = path
        self.final_position = final_position
        self.expanded_final_position = expanded_final_position
        self.boss_capture_id = boss_capture_id

class AlienMissile:
    def __init__(self, sprite, position_x, position_y, d_x):
        self.sprite = sprite
        self.position_x = position_x
        self.position_y = position_y
        self.rotation = 0
        self.is_alien = True
        self.is_missile = True
        self.d_y = MISSILE_SPEED * -0.25
        self.d_x = d_x

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
        self.d_y = MISSILE_SPEED
        self.d_x = 0

class ActiveMissiles:
    def __init__(self, missile, is_player_list):
        self.missile = missile
        self.is_player_list = is_player_list

class Menu:
    def __init__(
        self,
        name,
        text = "",
        choice_1 = 0,
        choice_2 = 0,
        choice_3 = 0,
        choice_4 = 0,
        select = False
    ):
        self.name = name
        self.text = text
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        self.choice_3 = choice_3
        self.choice_4 = choice_4
        self.select = select

class Event:
    def __init__(self, name, id, start_time, duration, end_time = 0):
        self.name = name
        self.id = id
        self.start_time = start_time
        self.duration = duration
        self.end_time = end_time

    def set_event_timer(self, duration):
        self.end_time = duration + self.start_time

class Player:
    # attributes for the player
    def __init__(
        self,
        name, 
        lives, 
        sprite, 
        score = 0, 
        position_x = WIDTH / 2,
        hp = 1,
        double_fighter = False,  
        kills = 0, 
        hits = 0, 
        shots_fired = 0,
        pause = False,
        rotation = 0,
        abducted = False,
        boss_capture_id = None,
        image_in_cycle = 0,
        extra_life = False

        ):
        self.name = name
        self.lives = lives
        self.sprite = sprite
        self.score = score
        # y position is a constant
        self.position_x = position_x
        self.position_y = FIGHTER_Y
        self.hp = hp
        self.double_fighter = double_fighter
        self.pause = pause
        self.rotation = 0
        self.is_alien = False
        self.is_fighter = True
        self.is_missile = False
        self.speed_x = FIGHTER_SPEED
        self.kills = kills
        self.hits = hits
        self.shots_fired = shots_fired
        self.rotation = rotation
        self.abducted = abducted
        self.boss_capture_id = boss_capture_id
        self.image_in_cycle = image_in_cycle
        self.extra_life = extra_life

    def reset_player(self):
        self.hp = 1
        self.position_x = WIDTH /2
        self.position_y = FIGHTER_Y
        self.rotation = 0
        self.abducted = False
        self.pause = True
        self.double_fighter = False
        self.boss_capture_id = None
        self.image_in_cycle = 0
            

class FlightPath:
    def __init__(self, name, path_id, platoon, completed):
        self.name = name
        self.path = path_id
        self.platoon = platoon
        self.is_completed = completed

class Stars:
    def __init__(self, name, array, speed):
        self.name = name
        self.array = array
        self.speed = speed

if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Objects"
    )
