# Class: Irirdium
# Author: Ali Daley & Samuel LP McKnight
# Project:RPSLS
# Created: August 13th 2021
class Player:
    def __init__(self):
        self.name = ""
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
        print(f"{self.name} selects {self.choice}!")

    def define_name(self, player):
        while True:
            defined_name = input("What is your name? ")
            if defined_name.isalpha():
                print(f"Your name is now {defined_name.capitalize()}")
                player.name = defined_name.capitalize()
                break
            else:
                print("Please refrain from using numbers")