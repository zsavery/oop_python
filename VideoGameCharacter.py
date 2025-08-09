class VideoGameCharacter:
    def __init__(self, name="Player",level=1 ,health=100,
                 skills=None, items_capacity=1,position=(0, 0, 0)):
        
        self._name = name
        self._level = level
        self._health = health
        self._skills = skills
        self._items_capacity = items_capacity
        self._position = position

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if isinstance(level, int) and 0 < level:

            self._level = level
        else:
            raise ValueError(f"You can't enter a negative number." +
                             f"\nYou entered {level}")

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, hp):
        if isinstance(hp, int):
            if 0 <= hp <= 100:
                self._health = hp
            else:
                print("Health entered: {} is out of scope".format(hp))
    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, lst):
        if isinstance(lst, list):
            self._skills = lst

    @property
    def items_capacity(self):
        return self._items_capacity

    @items_capacity.setter
    def items_capacity(self, cap):
        if isinstance(cap, int):
            self._level = cap

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        if isinstance(pos, tuple) and pos.count == 3:
            self._level = pos

    def attack(self) -> str:
        """Step 3.1
        - Create the attack() method in `VideoGameCharacter`.
        """
        msg:str = f"{self.name} make an attck."
        return msg




class Warrior(VideoGameCharacter):
    """
    Step 1.1
    - Create a subclass of `VideoGameCharacter` named `Warrior`.
        - Implement a method named move(distance:int) in where `Warrior` runs a set distance.
    Step 2.2
    - Implement move method in `TestVideoGameCharacter.py`
    """
    def move(self, distance=6):
        return f"Run {distance} feet."
    
    """Step 3.2
    - Create the attack() method in the `Warrior`.
    """
    def attack(self):
        game_class = "Warrior"
        attack_name = "Axe Strike"
        msg = f"{game_class} {super().attack()} with {attack_name}." 
        return msg

class Wizard(VideoGameCharacter):
    """
    Step 1.2
    - Create a subclass of `VideoGameCharacter` named `Wizard`.
        - Implement a method named move(distance:int) in where `Wizard` teleports a set distance.
    Step 2.2
    - Implement move method in `TestVideoGameCharacter.py`.
    """
    def move(self, distance=10):
        return f"Teleport {distance} feet."
    
    """Step 3.3
    - Create the attack() method in the subclass `Wizard`.
    """
    def attack(self):
        game_class = "Wizard"
        attack_name = "Fireball"
        msg = f"{game_class} {super().attack()} with {attack_name}." 
        return msg


"""Step 4 in TestVideoGameCharacter.py
Create function that takes a list of different characters and calls their attack methods
"""
