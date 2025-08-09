class Dog:
    def __init__(self,name="NA",breed="NA",size=1,fur_type="NA",
        fur_color="NA",mood="NA",has_owner=False):
        self.name = name
        self._breed = breed
        self.__size = size
        self.fur_type = fur_type
        self.fur_color = fur_color
        self.mood = mood
        self.has_owner = has_owner

    def set_size(self, size: int):
        if 1 <= size <= 5:
            self.__size = size
        else:
            print(f"Invalid size: You enterd {size}. The size should be from [1-5].")
    
    def get_size(self):
        return self.__size
        
    def setter_name(self, n: str):
        self.name = n

    def get_name(self):
        return self.name
        
    def setter_breed(self, b: str):
        self._breed = b

    def get_breed(self):
        return self._breed
        
    def setter_fur_type(self, t: str):
        self.fur_type = t

    def get_fur_type(self):
        return self.fur_type

    def setter_fur_color(self, c: str):
        self.fur_color = c

    def get_fur_color(self):
        return self.fur_color

    def setter_mood(self, m: str):
        self.mood = m

    def getter_mood(self):
        return self.mood

    def setter_has_owner(self, o: bool):
        self.has_owner = o

    def getter_has_owner(self, o):
        return self.has_owner


class Bulldog(Dog):
    def bark(self):
        return "Loud bark"
        
    def set_size(self, size):
        if size >= 3:
            self.__size = size
        else:
            print(f"Bulldogs are usally larger than {size}.")
            super().set_size(size)

class Poodle(Dog):
    def bark(self):
        return "Yappy bark"

    def set_size(self, size):
        if size >= 4:
            self.__size = size
        else:
            print(f"Poodles are usally larger than {size}.")
            super().set_size(size)

class Beagle(Dog):
    def bark(self):
        return "Howl"

    def set_size(self, size):
        if size >= 2:
            self.__size = size
        else:
            print(f"Beagles are usally larger than {size}.")
            super().set_size(size)