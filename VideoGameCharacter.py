class VideoGameCharacter:
    def __init__(self, name="Player", level=0, health=100, skills=[], 
                 item_capacity=1, position= (0,0,0)):
            self._name = name
            self._level = level
            self._health = health
            self._skills = skills
            self._item_capacity = item_capacity
            self._position = position
    
    def set_name(self, n):
          self._name = n

    @property
    def name(self):
          return self._name