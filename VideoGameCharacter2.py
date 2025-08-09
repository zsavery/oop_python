class VideoGameCharacter:
    def __init__(
        self,
        name="Player",
        level=0,
        health=100,
        skills=None,
        items_capacity=1,
        position=(0, 0, 0),
    ):
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
        if isinstance(level, int):
            if 0 <= level:
                self._level = level
            else:
                print("You can't enter a negative number.")

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
