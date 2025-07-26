# Notes

## Objects

Contain the properties and behaviors defined in their class. Objects are stored red in memory and their properties can contain their unique from their class.

## Classes

### Class Definition

When creating a class you need a **constructor** which define the properties of a class.

### Dog Class

Imagine you have a class named **Dog**, what feature of a dog will you need to add to your class.

#### Dog Class Setup

Dog

- Name: `str`
- Breed: `str`
- Size: `int`
- Fur Type: `str`
- Fur Color: `str`
- Bark Sound: `str`
- Mood: `str`
- Has Owner: `bool`

#### Python Implementation

In Python, a constructed is defined with the `def` keyword like all python functions and with the method name of `__init__`. Inside the arguments section is the keyword `self` which is needed to access class properties.

```python
class Dog:
    def __init__(self):
        self.name = None
        self.breed = None
        self.size = -1
        self.fur_type = None
        self.fur_color = None
        self.bark_sound = None # file path
        self.mood = None
        self.has_owner = None
```

```python
class Dog:
    def __init__(self, n, b, s, ft, fc, bs, m:, ho):
        self.name = n
        self.breed = b
        self.size = s
        self.fur_type = ft
        self.fur_color = fc
        self.bark_sound = bs # file path
        self.mood = m
        self.has_owner = ho
```

```python
class Dog:
    def __init__(self, n:str = 'NA', b:str = 'NA', s:int = 0, ft:str = 'NA', 
                fc:str = 'NA', bs:str = 'NA', m:str = 'NA', ho:bool = False):
        self.name = n
        self.breed = b
        self.size = s
        self.fur_type = ft
        self.fur_color = fc
        self.bark_sound = bs # file path
        self.mood = m
        self.has_owner = ho
```

#### Table

|Name|Breed|Size|Fur Type|Fur Color|Bark Sound|Mood|Has Owner|
|:--:|:---:|:--:|:------:|:-------:|:--------:|:--:|:-------:|
|Fido|Whippet|3|Soft/Short|Tan|Fido_bark.mpp3|Hyper|T|
|Husker|NaN|NaN|NaN|NaN|NaN|NaN|NaN|
|Philip|NaN|NaN|NaN|NaN|NaN|NaN|NaN|


