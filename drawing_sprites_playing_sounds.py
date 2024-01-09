from Sprite_Manipulation import scale_sprite


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

    WINDOW.blit(sprite, (x - a, y - b))


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


def play_sound(mute_toggle, audio_channel, aduio_volume):
    # if there is a device and mute is not active play called sound at called volume
    # unsure how to check for an audio channel right now
    if audio_channel:
        if not mute_toggle:
            a = 0
