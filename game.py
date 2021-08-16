# Class: Irirdium
# Author: Ali Daley & Samuel LP McKnight
# Project:RPSLS
# Created: August 13th 2021
from random import choice
from ai import AI
from human import Human

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def run_game(self):
        #setup
        self.welcome()
        self.display_rules()
        self.game_type()
        #game rounds
        self.game_round_timer()
        self.round_start()
    
    def welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock!")
    
    def display_rules(self):
        print('\tRULES:')
        print("Rule#1: Game is set to best of three\nRule#2: There are no points for ties")    
        print("\tHOW TO WIN:")
        print("Scissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock crushes Scissors")

    def game_type(self):
        game_selection = input("Would you like to play to SinglePlayer or MultiPlayer?\nPress 's' for SinglePlayer or 'm' for MultiPlayer")
        if(game_selection.lower() == 's'):
            print('You have selected SinglePlayer')
        elif(game_selection.lower() == 'm'):
            print('you have selected Mulitplayer')
        else:
            print("try again")
            self.game_type()

    def game_round_timer(self):
        round_count = 0
        round_count += 1
        print(f"Round {round_count} Start!")

    def round_start(self):
        print("Player 1 turn")
        self.player_one.choose_gesture()
        chosen_gesture = int(input())
        self.player_one.gesture_list[chosen_gesture] = self.player_one.choice
        print(f"Player 1 selects {self.player_one.choice}!")

    def ai_round(self):
        self.player_two = AI()
        self.player_two.name = 'Player'
        self.player_two.choose_gesture()