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
        while True:
            self.game_round_timer()
            self.round_start()
            self.round_outcome()
            play_again = input("Play again? 'y' or 'n': ")
            if play_again.lower() != "y":
                break

    
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

    def round_outcome(self):
        if self.player_one.choice == self.player_two.choice:
            print(f"Both players selected {self.player_one.choice}. It's a tie!")       
        elif self.player_one.choice == "rock":
            if self.player_two.choice == "scissors":
                print("Rock crushes scissors! You win!")
            elif self.player_two.choice == "lizard":
                print("Rock crushes lizard! You win!")
            elif self.player_two.choice == "spock":
                print("Spock vaporizes rock! You lose.")
            else:
                print("Paper covers rock! You lose.")       
        elif self.player_one.choice == "paper":
            if self.player_two.choice == "rock":
                print("Paper covers rock! You win!")
            elif self.player_two.choice == "spock":
                print("Paper disproves spock! You win!")
            elif self.player_two.choice == "lizard":
                print("Lizard eats paper! You lose.")
            else:
                print("Scissors cuts paper! You lose.")        
        elif self.player_one.choice == "scissors":
            if self.player_two.choice == "paper":
                print("Scissors cuts paper! You win!")
            elif self.player_two.choice == "lizard":
                print("Scissors decapitates lizard! You win!")
            elif self.player_two.choice == "spock":
                print("Spock smashes scissors! You lose.")
            else:
                print("Rock crushes scissors! You lose.")
        elif self.player_one.choice == "lizard":
            if self.player_two.choice == "spock":
                print("Lizard poisons spock! You win!")
            elif self.player_two.choice == "paper":
                print("Lizard eats paper! You win!")
            elif self.player_two.choice == "rock":
                print("Rock crushes lizard! You lose.")
            else:
                print("Scissors decapitates lizard! You lose.")
        elif self.player_one.choice == "spock":
            if self.player_two.choice == "scissors":
                print("Spock smashes scissors! You win!")
            elif self.player_two.choice == "rock":
                print("Spock vaporizes rock! You win!")
            elif self.player_two.choice == "paper":
                print("Paper disaproves spock! You lose.")
            else:
                print("Lizard poisons spock! You lose.")