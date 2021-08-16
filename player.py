# Class: Irirdium
# Author: Ali Daley & Samuel LP McKnight
# Project:RPSLS
# Created: August 13th 2021
class Player:
    def __init__(self):
        self.score = 0
        self.choice = ""
        self.gesture_list = ["rock","paper","scissors","lizard","spock"]
         
    def choose_gesture(self):
        print("Choose your gesture:")
        index = 0
        for gesture in self.gesture_list:
            print(f"Press {index} for {gesture}")
            index += 1
        self.choice = self.gesture_list[int(input())]
        print(f"Player 1 selects {self.choice}!")