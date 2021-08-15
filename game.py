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
        print("Welcome to Rock Paper Scissors Lizard Spock!")
    

    def display_rules(self):
        print("Rule#1: Game is set to best of three\nRule#2: There are no points for ties")    
        print("\tHOW TO WIN:")
        print("Scissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock crushes Scissors")

    def game_type(self):
        game_selection = input("Would you like to play to SinglePlayer or MultiPlayer?\nPress 's' for SinglePlayer or 'm' for MultiPlayer")
        if(game_selection == 's'):
            print('You have selected SinglePlayer')
        if(game_selection == 'm'):
            print('you have selected Mulitplayer')
        else:
            print("try again")
            self.game_type()
