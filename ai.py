# Class: Irirdium
# Author: Ali Daley & Samuel LP McKnight
# Project:RPSLS
# Created: August 13th 2021



from player import Player
import random

class AI:
    def __init__(self):
        super.__int__()
        self.permant_name()

    def permant_name(self):
        self.name = "AI"

    def choose_gesture(self):
        self.choice = random.randint(0,4)
        if(self.choice == 0):
            return 'Rock'
        elif(self.choice == 1):
            return 'Paper'




    def setting_score(self):
        self.wins += 1       


        