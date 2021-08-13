from human import Human


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def run_game(self):
        self.welcome
        self.display_rules
        self.game_type
    
