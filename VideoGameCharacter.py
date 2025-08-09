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

    def set_name(self, n):
        if isinstance(n, str):
            self._name = n
        else:
            print("Wrong type: Expected str")

    @property
    def name(self):
        return self._name

    def set_level(self, level):
        self._level = level

    @property
    def level(self):
        return self._level

    def set_skills(self, lst):
        self._skills = lst

    @property
    def skills(self):
        return self._skills

    def set_items_capacity(self, cap):
        self._level = cap

    @property
    def items_capacity(self):
        return self._items_capacity

    def set_position(self, pos):
        self._level = pos

    @property
    def position(self):
        return self._position
