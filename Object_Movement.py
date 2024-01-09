

def object_movement(object, d_x, d_y):
    object.position_x = object.position_x + d_x
    object.position_y = object.position_y + d_y
    return object.position_x, object.position_y


def missile_movement(missiles):
    pos_x, pos_y = object_movement(missiles, 0, missiles.speed_y * -1)
    
def alien_movement():
    a = 0
