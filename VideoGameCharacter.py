class VideoGameCharacter:
    def __init__(self, name="Player", level=0, health=100, skills=[], 
                 item_capacity=1, position= (0,0,0)):
            self.name = name
            self.level = level
            self.health = health
            self.skills = skills
            self.item_capacity = item_capacity
            self.position = position
    
    