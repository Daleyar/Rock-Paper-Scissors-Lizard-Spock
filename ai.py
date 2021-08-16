# Class: Irirdium
# Author: Ali Daley & Samuel LP McKnight
# Project:RPSLS
# Created: August 13th 2021
from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.choice = random.choice(self.gesture_list)
        if(self.choice == "rock"):
            print(f"Player 2 selects {self.choice}!")
        elif(self.choice == "paper"):
            print(f"Player 2 selects {self.choice}!")
        elif(self.choice == "scissors"):
            print(f"Player 2 selects {self.choice}!")
        elif(self.choice == "lizard"):
            print(f"Player 2 selects {self.choice}!")
        elif(self.choice == "spock"):
            print(f"Player 2 selects {self.choice}!")

    def define_name(self, player):
        pass  


        