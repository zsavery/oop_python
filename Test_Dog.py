from Dog import Dog

Fido = Dog("Fido", "Greyhound", 4, "short/soft",
           "grey", "hyper", True)

Billy = Dog()

print(Fido.name, Fido.breed, Fido.size, Fido.fur_color, Fido.fur_type, Fido.mood, Fido.has_owner)

print(Billy.name, Billy.breed, Billy.size, Billy.fur_color, Billy.fur_type, Billy.mood, Billy.has_owner)