import pygame
from ...services.visual_output.sprite_manipulation import scale_sprite

def draw_beam_image(WINDOW, unit):
    scale_sprite(unit)
    sprite = unit.sprite
    sprite_size = sprite.get_size()
    a = int(sprite_size[0] * 21 / 32) 
    b = int(sprite_size[1] / 4)
    # picks a point at the units bottom middle
    x = unit.position_x  - a
    y = unit.position_y + b
    scale_sprite(unit, True)
    WINDOW.blit(unit.beam_image, (x, y))

# draw sprite
def draw_sprite(WINDOW, object, centered):
    scale_sprite(object)
    sprite = object.sprite
    x = object.position_x
    y = object.position_y
    sprite_size = sprite.get_size()
    if centered:
        a = sprite_size[0] / 2
        b = sprite_size[1] / 2
    else:
        a = b = 0
    # if we have a none value, just don't draw this one
    if not isinstance(x, (int, float)):
        return
    WINDOW.blit(sprite, (x - a, y - b))

def draw_image(WINDOW, image, pos_x , pos_y, scale_x, scale_y, rotation, centered):
    image = pygame.transform.rotate(image,0)
    image = pygame.transform.scale(image,(scale_x, scale_y))
    image = pygame.transform.rotate(image,rotation)
    image_size = image.get_size()
    if centered:
        a = image_size[0] / 2
        b = image_size[1] / 2
    else:
        a = 0
        b = 0

    WINDOW.blit(image, (pos_x - a, pos_y - b))

# draw text
def draw_text(WINDOW, text, font, text_color, x_positon, y_position, centered):
    img = font.render(text, True, text_color)
    text_size = img.get_size()
    if centered:
        a = text_size[0] / 2
        b = text_size[1] / 2
    else:
        a = 0
        b = 0
    WINDOW.blit(img, (x_positon - a, y_position - b))
