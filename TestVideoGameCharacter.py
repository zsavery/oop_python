from VideoGameCharacter import *

def attack_initative(players:list):
    for player in players:
        if isinstance(player, VideoGameCharacter):
            print(player.attack())
        else:
            print(f"{type(player)} is not a valid player classs.")

# create player object
my_player = VideoGameCharacter("Zyon", 1, 100,[], 5)
my_warrior = Warrior(name="Brick")
my_wizard = Wizard(name="The Wiz")

try:
    print(f"Warrior: {my_warrior.move(10)}")
    print(f"Wizard: {my_wizard.move(10)}")
except ValueError as er:
    print(f"Error caught - {er}")

# test attack_initative
try:
    player_lst = [my_player, my_warrior, my_wizard]
    attack_initative(player_lst)
except ValueError as er:
    print(f"Error caught - {er}")