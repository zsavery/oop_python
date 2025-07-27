class Car:
    # def __init__(self) -> None
    #     self.color = None
    #     self.brand = None
    #     self.model = None
    #     self.year = None

    def __init__(self, color=None, brand=None, model=None, year=0) -> None:
        self.color = color
        self.brand = brand
        self.model = model
        self.year = year


class Truck:
    def __init__(self, color=None, brand=None, model=None, year=0) -> None:
        self.color = color
        self.brand = brand
        self.model = model
        self.year = year
