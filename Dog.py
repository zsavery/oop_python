class Dog:
    def __init__(
        self,
        name="NA",
        breed="NA",
        size=1,
        fur_type="NA",
        fur_color="NA",
        mood="NA",
        has_owner=False,
    ):
        self.name = name
        self.breed = breed
        self.size = size
        self.fur_type = fur_type
        self.fur_color = fur_color
        self.mood = mood
        self.has_owner = has_owner

    def set_size(self, s: int):
        if 1 <= s <= 5:
            self.size = s
        else:
            print(f"Invalid size: You enterd {s}. The size should be from [1-5].")
        """
        if 1 <= s and s <= 5:
            self.size = s
        """

    def setter_name(self, n: str):
        self.name = n

    def setter_breed(self, b: str):
        self.breed = b

    def setter_fur_type(self, t: str):
        self.fur_type = t

    def setter_fur_color(self, c: str):
        self.fur_color = c

    def setter_mood(self, m: str):
        self.mood = m

    def setter_has_owner(self, o: bool):
        self.has_owner = o
