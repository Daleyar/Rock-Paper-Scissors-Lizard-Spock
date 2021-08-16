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
        self.player_one.define_name(self.player_one)
        self.player_two.define_name(self.player_two)
        while True:
            #self.game_round_timer()
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            self.round_outcome()
            self.display_score()
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
        game_selection = input("Would you like to play to SinglePlayer or MultiPlayer?\nPress 's' for SinglePlayer or 'm' for MultiPlayer ")
        if(game_selection.lower() == 's'):
            print('You have selected SinglePlayer')
            self.player_two = AI()
        elif(game_selection.lower() == 'm'):
            print('you have selected Mulitplayer')
            self.player_two = Human()
        else:
            print("try again")
            self.game_type()

    #def game_round_timer(self): #needs fixing doesnt acutally count
     #   round_count = 0
      #  round_count = 1
    #    print(f"Round {round_count} Start!")

    def round_outcome(self):
        if self.player_one.choice == self.player_two.choice:
            print(f"Both players selected {self.player_one.choice}. It's a tie!")       
        elif self.player_one.choice == "rock":
            if self.player_two.choice == "scissors":
                print(f"Rock crushes scissors! {self.player_one.name} wins this round!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "lizard":
                print(f"Rock crushes lizard! {self.player_one.name} wins this round!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "spock":
                print(f"Spock vaporizes rock! {self.player_one.name} loses this round.")
                self.player_two.score = self.score_counter
            elif self.player_two.choice == "paper":
                print(f"Paper covers rock! {self.player_one.name} loses this round.") 
                self.player_two.score = self.score_counter      
        elif self.player_one.choice == "paper":
            if self.player_two.choice == "rock":
                print(f"Paper covers rock! {self.player_one.name} wins this round!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "spock":
                print(f"Paper disproves spock! {self.player_one.name} wins this round!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "lizard":
                print(f"Lizard eats paper! {self.player_one.name} loses this round.")
                self.player_two.score = self.score_counter
            elif self.player_two.choice == "scissors":
                print(f"Scissors cuts paper! {self.player_one.name} loses this round.")
                self.player_two.score = self.score_counter      
        elif self.player_one.choice == "scissors":
            if self.player_two.choice == "paper":
                print(f"Scissors cuts paper! {self.player_one.name} wins this round!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "lizard":
                print(f"Scissors decapitates lizard! {self.player_one.name} wins this round!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "spock":
                print(f"Spock smashes scissors! {self.player_one.name} loses this round.")
                self.player_two.score = self.score_counter
            elif self.player_two.choice == "rock":
                print(f"Rock crushes scissors! {self.player_one.name} lose this round.")
                self.player_two.score = self.score_counter
        elif self.player_one.choice == "lizard":
            if self.player_two.choice == "spock":
                print(f"Lizard poisons spock! {self.player_one.name} wins this round!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "paper":
                print(f"Lizard eats paper! {self.player_one.name} wins this round!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "rock":
                print(f"Rock crushes lizard! {self.player_one.name} loses this round.")
                self.player_two.score = self.score_counter
            elif self.player_two.choice == "scissors":
                print(f"Scissors decapitates lizard! {self.player_one.name} loses this round.")
                self.player_two.score = self.score_counter
        elif self.player_one.choice == "spock":
            if self.player_two.choice == "scissors":
                print(f"Spock smashes scissors! {self.player_one.name} wins this round!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "rock":
                print(f"Spock vaporizes rock! {self.player_one.name} wins this round!")
                self.player_one.score = self.score_counter
            elif self.player_two.choice == "paper":
                print(f"Paper disaproves spock! {self.player_one.name} loses this round.")
                self.player_two.score = self.score_counter
            elif self.player_two.choice == "lizard":
                print(f"Lizard poisons spock! {self.player_one.name} loses this round.")
                self.player_two.score = self.score_counter

    def score_counter(self): #needs fixing doesnt acutally count
        counter = 0
        counter += 1

    def display_score(self):
        print(f"The score is {self.player_one.score}-{self.player_two.score}")

    def display_winners(self):
        if (self.player_one.score == 2):
             print("Player 1 wins!")
        elif (self.player_two.score == 2):
            print("Player 1 loses!") 