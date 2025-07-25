class Dog:
    def __init__(self, n:str = 'NA', b:str = 'NA', s:int = 0, ft:str = 'NA', fc:str = 'NA',
                bs:str = 'NA', m:str = 'NA', ho:bool = False):
        self.name = n
        self.breed = b
        self.size = s
        self.fur_type = ft
        self.fur_color = fc
        self.bark_sound = bs
        self.mood = m
        self.has_owner = ho