import pygame


# collect Key pressed and key released
def get_key_pressed(event):
    key_pressed = event
    return key_pressed


def get_key_released(event):
    if event == pygame.KEYUP:
        # gives me the key number
        key_released = event.Key
        return key_released


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Player_Input"
    )
