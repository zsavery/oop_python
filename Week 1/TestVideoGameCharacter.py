from VideoGameCharacter import *

def attack_initative(players:list):
    for player in players:
        if isinstance(players, VideoGameCharacter):
            print(players.attack())
        else:
            print(f"{type(player)} is not a valid player classs.")

# create player object
my_player = VideoGameCharacter("Zyon", 1, 100,[], 5)
my_warrior = Warrior()
my_wizard = Wizard()
try:
    print(f"Warrior: {my_warrior.move(10)}")
    print(f"Wizard: {my_wizard.move(10)}")
except ValueError as er:
    print(f"Error caught - {er}")