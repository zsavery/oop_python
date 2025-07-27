class VideoGameCharacter:
    def __init__(self, name="Player", level=0, health=100, skills=[], 
                 items_capacity=1, position= (0,0,0)):
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
    def name(self, n):
          self._name = n

    @property
    def level(self):
          return self._level
    
    @level.setter
    def level(self, l):
          self._level = l

    @property
    def skills(self):
          return self._skills
    
    @skills.setter
    def skills(self, lst):
          self._skills = lst

    @property
    def items_capacity(self):
          return self._items_capacity
    
    @items_capacity.setter
    def items_capacity(self, cap):
          self._level = cap

    @property
    def position(self):
          return self._position
    
    @position.setter
    def position(self, pos):
          self._level = pos