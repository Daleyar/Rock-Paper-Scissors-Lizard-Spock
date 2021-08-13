from human import Human


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.game_type()

    def display_welcome(self):
        print(f"Welcome to RPSLS!")

    def display_rules(self):
        print(f"Rule#1: bla bla bla \nRule#2: bla bla \nRule#3: have fun")

    def game_type(self):
        user = input(f"Press 's' for single player or 'm' for multiplayer" )
        if(user == "s"):
            print("selected single-player")
        elif(user == "m"):
            print("selected multi-player")

        #user validation
        else:
            print("try again")
            self.run_game() 
    

