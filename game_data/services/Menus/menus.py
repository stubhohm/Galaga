import pygame
from ...constants.CONSTANTS import HEIGHT, WIDTH, ALHAPHABET
from ...constants.COLORS import WHITE
from ...imported_assets.text import FONTS
from ...imported_assets.galaga_sprites import galaga_logo
from ...calculations_and_datasets.data_sets import high_scores
from ...classes.classes import Menu
from ..visual_output.drawing_sprites import draw_text, draw_image


game_menu = Menu("Game Menu","Title Menu")
title_menu = Menu("Title Menu")
high_score_list = Menu("High Score List")
high_score_menu = Menu("High Score Menu")

def update_high_scores(score, name):
    high_scores_list = high_scores.load_high_scores()

    if len(high_scores_list) < 20 or score > high_scores_list[-1]["score"]:
        new_entry = {"name": name, "score": score}
        high_scores_list.append(new_entry)
        high_scores_list.sort(key=lambda x: x["score"], reverse=True)
        high_scores_list = high_scores_list[:20]
        high_scores.save_high_scores(high_scores_list)

def reset_menu(menu):
    menu.choice_1 = 0
    menu.choice_2 = 0
    menu.choice_3 = 0
    menu.choice_4 = 0
    menu.select = False

def name_input(menu, key_released):
    if key_released == [pygame.K_LEFT][0]:
            menu.choice_1 = menu.choice_1 - 1
    elif key_released == [pygame.K_RIGHT][0]:
            menu.choice_1 = menu.choice_1 + 1 
    if menu.choice_1 == 0:
        if key_released == [pygame.K_DOWN][0]:
            menu.choice_2 = menu.choice_2 - 1
        if key_released == [pygame.K_UP][0]:
            menu.choice_2 = menu.choice_2 + 1
    elif menu.choice_1 == 1:
        if key_released == [pygame.K_DOWN][0]:
            menu.choice_3 = menu.choice_3 - 1
        if key_released == [pygame.K_UP][0]:
            menu.choice_3 = menu.choice_3 + 1
    elif menu.choice_1 == 2:
        if key_released == [pygame.K_DOWN][0]:
            menu.choice_4 = menu.choice_4 - 1
        if key_released == [pygame.K_UP][0]:
            menu.choice_4 = menu.choice_4 + 1

def menu_navigating(menu, key_released):
    if menu.name == "High Score Menu":
        scrub_choice(menu.choice_1, 3)
        name_input(menu, key_released)
    else:
        if key_released == [pygame.K_UP][0]:
            menu.choice_1 = menu.choice_1 - 1
        if key_released == [pygame.K_DOWN][0]:
            menu.choice_1 = menu.choice_1 + 1  
    if key_released == [pygame.K_RETURN][0]:
        menu.select = True 

def scrub_choice(c, options):
    c_mod = 1
    if c < 0:
        c_mod = -1
    c = abs(c)
    while c > options:
        c = c - options
    if c_mod == -1:
        c = options - c
    return c

def draw_title_menu(menu, time, key_released, WINDOW):
    draw_image(WINDOW, galaga_logo, WIDTH / 2, HEIGHT * 2 / 8, WIDTH * 7 /8, HEIGHT * 3 / 8, 0, True)
    choice = scrub_choice(menu.choice_1,2)
    if choice == 0:
        draw_text(WINDOW, "View High Scores", FONTS.text_font, WHITE, WIDTH/2, HEIGHT * 9 / 16, True)
        if time % 40 > 15:
            draw_text(WINDOW, "Play Galaga", FONTS.text_font, WHITE, WIDTH/2, HEIGHT * 4 / 8, True)
        if key_released == [pygame.K_RETURN][0]:
            return "Play" 
    if choice == 1:
        draw_text(WINDOW, "Play Galaga", FONTS.text_font, WHITE, WIDTH/2, HEIGHT * 4 / 8, True)
        if time % 40 > 15:
            draw_text(WINDOW, "View High Scores", FONTS.text_font, WHITE, WIDTH/2, HEIGHT * 9 / 16, True)
        if key_released == [pygame.K_RETURN][0]:
            return "High Score List"
    text = "use arrow keys and press enter to select"
    draw_text(WINDOW, text,FONTS.menu_font, WHITE, WIDTH/2, HEIGHT * 5 / 8, True)
    text = "Control the fighter with arrow keys"
    draw_text(WINDOW, text, FONTS.menu_font, WHITE, WIDTH/2, HEIGHT * 28 / 32, True)
    text = "press space to shoot missiles"
    draw_text(WINDOW, text, FONTS.menu_font, WHITE, WIDTH/2, HEIGHT * 29 / 32, True)
    text = "press 'q' at any time to quit"
    draw_text(WINDOW, text, FONTS.menu_font, WHITE, WIDTH/2, HEIGHT * 30 / 32, True)
    return "Title Menu"

def draw_high_scores(y_shift, WINDOW):
    high_scores_list = high_scores.load_high_scores()
    rank = 0
    for scorers in list(high_scores_list):
        text = f"{rank + 1}. {scorers['name']}: {scorers['score']}"
        draw_text(WINDOW, text, FONTS.text_font, WHITE, WIDTH / 2, y_shift + HEIGHT/32 * rank, True)
        rank = rank + 1

def draw_high_score_list(key_released, WINDOW):
    high_scores_list = high_scores.load_high_scores()
    scorer_count = len(high_scores_list)
    if scorer_count > 1:
        text = f"The current top {scorer_count} Scorer's in Galaga"
    elif scorer_count == 0:
        text = f"There are currently no High Scores in Galaga"
    elif scorer_count == 1:
        text = f"The current and only Scorer in Galaga"
    draw_text(WINDOW, text, FONTS.menu_font, WHITE, WIDTH/2, HEIGHT* 1 / 32, True)
    pygame.draw.rect(WINDOW,WHITE,(WIDTH * 1 /16, HEIGHT * 2 /32, WIDTH * 7 /8, HEIGHT * 1 / 128),3)
    text = f"Press enter to return to the title Screen"
    draw_text(WINDOW, text, FONTS.menu_font, WHITE, WIDTH/2, HEIGHT * 3 / 32, True)
    draw_high_scores(HEIGHT * 2 / 16, WINDOW)
    if key_released == [pygame.K_RETURN][0]: 
        return "Title Menu"
    return "High Score List"

def draw_high_score_menu(menu, time, key_released, score, WINDOW):
    text = f"Your Final Score: {score}"
    draw_text(WINDOW,text, FONTS.text_font, WHITE, WIDTH / 2, HEIGHT * 1 / 32, True)    
    pygame.draw.rect(WINDOW,WHITE,(WIDTH * 1 / 16, HEIGHT * 2 / 32, WIDTH * 7 / 8, HEIGHT * 1 / 128),3)
    high_scores_list = high_scores.load_high_scores()
    your_rank = 0
    if len(high_scores_list) == 20:
        for scorers in list(high_score_list):
            if scorers.score < score:
                continue
            rank = rank + 1    
    if your_rank < 20:
        draw_text(WINDOW, "use arrow keys and press enter", FONTS.menu_font, WHITE, WIDTH / 2, HEIGHT * 3 / 16, True)
        draw_text(WINDOW, "to submit your score", FONTS.menu_font, WHITE, WIDTH / 2, HEIGHT * 7 / 32, True)
        c_1 = scrub_choice(menu.choice_1, 3)
        c_2 = scrub_choice(menu.choice_2,26)
        c_3 = scrub_choice(menu.choice_3,26)
        c_4 = scrub_choice(menu.choice_4,26)
        letters = [
        ALHAPHABET[c_2],
        ALHAPHABET[c_3],
        ALHAPHABET[c_4],
        ]
        name = ''.join([letter for letter in letters])
        center_w = WIDTH / 2
        for i in range(3):
            draw_text(WINDOW,letters[i], FONTS.text_font, WHITE, center_w + (WIDTH/32 * (i - 1)), HEIGHT /8, True)
        # making triangles
        y_top_base = int(HEIGHT * 7/64)
        gap = HEIGHT * 1 / 32
        y_bottom_base = int(y_top_base + gap)
        height = HEIGHT/64
        y_bottom_height = int(y_bottom_base + height)
        y_top_height = int(y_top_base - height)
        for i in range(3):
            if time % 40 > 15 and c_1 == i:
                continue
            x_top_point = int(center_w + (WIDTH/32 * (i - 1))) - 1
            width = WIDTH * 2 / 128
            x_left_point = x_top_point - width
            x_right_point = x_top_point + width
            pygame.draw.polygon(WINDOW, WHITE,( (x_top_point,y_top_height), (x_left_point,y_top_base), (x_right_point, y_top_base),), 0)
            pygame.draw.polygon(WINDOW, WHITE,((x_left_point,y_bottom_base), (x_right_point, y_bottom_base),(x_top_point,y_bottom_height),), 0)
        draw_high_scores(HEIGHT * 4 / 16, WINDOW)
        if key_released == [pygame.K_RETURN][0]:
            update_high_scores(score, name) 
            return "High Score List"
        return "High Score Menu"
    else:
        return "High Score List"

def menu_selecting(key_released, time, WINDOW, text, score):
    game_menu.text = text
    if game_menu.text == "Title Menu":
        chosen_menu = title_menu
    elif game_menu.text == "High Score List":
        chosen_menu = high_score_list
    elif game_menu.text == "High Score Menu":
        chosen_menu = high_score_menu
    menu_navigating(chosen_menu, key_released)
    game_menu.text = select_menu_window_to_draw(chosen_menu, time, key_released, score, WINDOW)
    if key_released == [pygame.K_RETURN][0]:
        reset_menu(chosen_menu)
    return game_menu.text 

def select_menu_window_to_draw(menu, time, key_released, score, WINDOW):
    if menu.name == "Title Menu":
        selection = draw_title_menu(menu, time, key_released, WINDOW)
    elif menu.name == "High Score List":
        selection = draw_high_score_list(key_released, WINDOW)
    elif menu.name =="High Score Menu":   
        selection = draw_high_score_menu(menu, time, key_released, score, WINDOW)
    return selection



