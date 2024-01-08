class Menu:
    def __init__(
        self,
        name,
        selected_option,
    ):
        self.name = name
        self.selcected_option = selected_option


title_menu = Menu("Title Menu", 0)
play_screen = Menu("Play Screen", 0)
pause_menu = Menu("Pause Menu", 0)
game_over_screen = Menu("Game Over Screen", 0)
game_over_menu = Menu("Game Over Menu", 0)
