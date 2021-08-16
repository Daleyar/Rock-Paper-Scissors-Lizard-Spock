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
        #print("AI is selecting a gesture")
        self.choice = random.choice(self.gesture_list)
        if(self.choice == "rock"):
            print(f"AI selects {self.choice}!")
        elif(self.choice == "paper"):
            print(f"AI selects {self.choice}!")
        elif(self.choice == "scissors"):
            print(f"AI selects {self.choice}!")
        elif(self.choice == "lizard"):
            print(f"AI selects {self.choice}!")
        elif(self.choice == "Spock"):
            print(f"AI selects {self.choice}!")      


        