# Class: Irirdium
# Author: Ali Daley & Samuel LP McKnight
# Project:RPSLS
# Created: August 13th 2021
from typing import Counter
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
            self.player_one_turn()
            self.player_two_turn()
            self.ai_turn()
            self.round_outcome()
            self.display_winners()
            if (self.display_winners == True):
                break
            play_again = input("Ready for the next round? 'y' or 'n': ")
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
            self.player_two = AI()
        elif(game_selection.lower() == 'm'):
            print('you have selected Mulitplayer')
            self.player_two = Human()
        else:
            print("try again")
            self.game_type()

    def game_round_timer(self):
        round_count = 0
        round_count += 1
        print(f"Round {round_count} Start!")

    def player_one_turn(self):
        print("Player 1 turn")
        self.player_one.choose_gesture()
        chosen_gesture = int(input())
        self.player_one.choice = self.player_one.gesture_list[chosen_gesture]
        print(f"Player 1 selects {self.player_one.choice}!")

    def player_two_turn(self):
        if(self.player_two == Human()):
            print("Player 2 turn")
            self.player_two.choose_gesture()
            chosen_gesture = int(input())
            self.player_two.choice = self.player_two.gesture_list[chosen_gesture] 
            print(f"Player 2 selects {self.player_two.choice}!")

    def ai_turn(self):
        if(self.player_two == AI()):
            self.player_two.choose_gesture()
            print(f"Player AI selects {self.player_two.choice}")

    def round_outcome(self):
        if self.player_one.choice == self.player_two.choice:
            print(f"Both players selected {self.player_one.choice}. It's a tie!")       
        elif self.player_one.choice == "rock":
            if self.player_two.choice == "scissors":
                print("Rock crushes scissors! You win!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "lizard":
                print("Rock crushes lizard! You win!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "spock":
                print("Spock vaporizes rock! You lose.")
                self.player_two.score = self.score_counter
            elif self.player_two.choice == "paper":
                print("Paper covers rock! You lose.") 
                self.player_two.score = self.score_counter      
        elif self.player_one.choice == "paper":
            if self.player_two.choice == "rock":
                print("Paper covers rock! You win!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "spock":
                print("Paper disproves spock! You win!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "lizard":
                print("Lizard eats paper! You lose.")
                self.player_two.score = self.score_counter
            elif self.player_two.choice == "scissors":
                print("Scissors cuts paper! You lose.")
                self.player_two.score = self.score_counter      
        elif self.player_one.choice == "scissors":
            if self.player_two.choice == "paper":
                print("Scissors cuts paper! You win!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "lizard":
                print("Scissors decapitates lizard! You win!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "spock":
                print("Spock smashes scissors! You lose.")
                self.player_two.score = self.score_counter
            elif self.player_two.choice == "rock":
                print("Rock crushes scissors! You lose.")
                self.player_two.score = self.score_counter
        elif self.player_one.choice == "lizard":
            if self.player_two.choice == "spock":
                print("Lizard poisons spock! You win!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "paper":
                print("Lizard eats paper! You win!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "rock":
                print("Rock crushes lizard! You lose.")
                self.player_two.score = self.score_counter
            elif self.player_two.choice == "scissors":
                print("Scissors decapitates lizard! You lose.")
                self.player_two.score = self.score_counter
        elif self.player_one.choice == "spock":
            if self.player_two.choice == "scissors":
                print("Spock smashes scissors! You win!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "rock":
                print("Spock vaporizes rock! You win!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "paper":
                print("Paper disaproves spock! You lose.")
                self.player_two.score = self.score_counter
            elif self.player_two.choice == "lizard":
                print("Lizard poisons spock! You lose.")
                self.player_two.score = self.score_counter

    def score_counter(self):
        counter = 0
        counter += 1

    def display_winners(self):
        if (self.player_one.score == 2):
             print("Player 1 wins!")
        elif (self.player_two.score == 2):
            print("Player 2 wins!")