from ..constants.CONSTANTS import FPS, WIDTH, FIGHTER_Y
from ..classes.classes  import Event, Player, AlienArmada
from ..alien_behavior.building import build_alien_armada

def clean_event_list(events, time):
    for event in list(events):
        if event.end_time < time or event.start_time > time:
            events.remove(event)

def create_event(name, id, time, duration):
    new_event = Event(name, id, time, duration)
    new_event.set_event_timer(duration)
    return new_event

def trigger_pause_event(time, duration):
    name = "pause"
    id = 5
    return create_event(name, id, time, duration)

def resolve_pause_event(player):
    player.pause = False

def check_for_unique_event(events,event_id):
    uniqueness = True
    for i in range(len(events)):
        event = events[i]
        if event.id == event_id:
            uniqueness = False
            return uniqueness
    return uniqueness

def trigger_player_death_event(events, time, player):
    event_id = 0
    unique = check_for_unique_event(events,event_id)
    if not unique:
        return
    player.lives = player.lives - 1
    player.pause = True
    event_name = "Player Death"
    event_start = time 
    seconds = 3
    event_duration = seconds * FPS
    new_event = create_event(event_name, event_id, event_start, event_duration)
    events.append(new_event)

def resolve_player_death_event(player, time, events):
    player.reset_player()
    seconds = 2
    duration = seconds * FPS
    pause = trigger_pause_event(time, duration)
    events.append(pause)

def trigger_player_abduction_event(events, time, player):
    event_id = 1
    player.pause = True
    unique = check_for_unique_event(events,event_id)
    if not unique:
        return
    player.lives = player.lives - 1
    event_name = "Player Abduction"
    event_start = time 
    seconds = 6
    event_duration = seconds * FPS
    new_event = create_event(event_name, event_id, event_start, event_duration)
    events.append(new_event)

def trigger_level_up_event(events, time):
    event_id = 2
    unique = check_for_unique_event(events,event_id)
    if not unique:
        return
    event_name = "Level Up"
    event_start = time 
    seconds = 2
    event_duration = seconds * FPS
    new_event = create_event(event_name, event_id, event_start, event_duration)
    events.append(new_event)

def resolve_level_up_event(events, armada, time):
    armada.level = armada.level + 1
    level = armada.level
    new_armada = build_alien_armada(level, time)
    seconds = 2
    duration = seconds * FPS 
    pause = trigger_pause_event(time, duration)
    events.append(pause)
    return new_armada
  
def trigger_game_over_event(events, time, player):
    event_id = 3
    unique = check_for_unique_event(events,event_id)
    if not unique:
        return
    event_name = "Game Over"
    player.pause = True
    event_start = time 
    seconds = 3
    event_duration = seconds * FPS
    new_event = create_event(event_name, event_id, event_start, event_duration)
    events.append(new_event)

def resolve_game_over_event(player, armada):
    player.pause = True 
    # puts you into the game over menu

def trigger_extra_life_event(events, time):
    event_id = 4
    unique = check_for_unique_event(events,event_id)
    if not unique:
        return
    event_name = "Extra Life"
    event_start = time 
    # takes 5 frames, buffered just cuz
    event_duration = 5
    new_event = create_event(event_name, event_id, event_start, event_duration)
    events.append(new_event)

def resolve_extra_lives_event(player):
    player.lives = player.lives + 1
    player.extra_life = False

def check_game_events(player, armada, time, events):
    """
    checks for specific in game events that I either want to pause the clock,
    or do a big level reset or something else.
    """
    clean_event_list(events,time)
    if player.hp == 0:
        # event id = 0
        trigger_player_death_event(events,time, player)
    if player.abducted:
        # event id = 1
        trigger_player_abduction_event(events,time, player)
    if armada.is_defeated:
        # event id = 2
        trigger_level_up_event(events,time)
    if player.lives == 0:
        # event id = 3
        trigger_game_over_event(events,time, player)
    if player.extra_life:
        # event id = 4
        trigger_extra_life_event(events, time)

def resolve_game_events(player, armada, time, events):
    for event in list(events):
        if event.end_time == time:
            if event.name == "Player Death" or event.name == "Player Abduction":
                resolve_player_death_event(player, time, events)
            elif event.name == "Level Up":
                armada = resolve_level_up_event(events, armada, time)
            elif event.name == "Game Over":
                resolve_game_over_event(player, armada)
            elif event.name == "Extra Life":
                resolve_extra_lives_event(player)
            elif event.name == "pause":
                resolve_pause_event(player)
            else:
                continue
    return armada

def main():
    events = []
    player = Player("player", 3, 0, 12000, None, None)
    armada = AlienArmada(None, True)
    for i in range(20):
        player.abducted = True
        player.hp = 0
        check_game_events(player, armada, i * 100, events)
        print(f"{i * 100}")
        for event in list(events):
            print(f"{event.name} started at {event.start_time}, and ends at {event.end_time}\n")
        i = i + 1
        
if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Galaga"
    )
