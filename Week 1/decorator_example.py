def Backflip(func):
    def wrapper():
        print("Do a backflip")
        func()
        print("You did a backflip")
    return wrapper


@Backflip
def DrinkWater():
    print("Drink water")

DrinkWater()

def simple_decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")

greet()