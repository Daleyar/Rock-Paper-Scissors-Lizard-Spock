# Class: Irirdium
# Author: Ali Daley & Samuel LP McKnight
# Project:RPSLS
# Created: August 13th 2021


from ai import AI
from human import Human


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def run_game(self):
        self.welcome()
        self.display_rules()
        self.game_type()
    
    def welcome(self):
        print("Rock paper sissors time!!")
    

    def display_rules(self):
        print("Game is set to best of three ")    
        print("There are no points for ties")
        print("Rock crushes Scissors,", end = "Scissors cuts Paper")
        print("Paper covers Rock", end = "Rock crushes Lizard")
        print("Lizard poisons Spock", end = "Spock smashes Scissors")
        print("Spock smashes Scissors",end ="Scissors decapitates Lizard")
    def game_type(self):
        pass
