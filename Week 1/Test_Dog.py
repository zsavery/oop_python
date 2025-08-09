from Dog import *

Jack = Bulldog(name="Jack")
Jack.set_size(2)
print(type(Jack), Jack.get_name(), 
      Jack.get_size(), Jack.bark())

Louise = Poodle(name="Louise", size=4)
print(type(Louise), Louise.get_name(),
      Louise.get_size(), Louise.bark())

Linda = Beagle(name="Linda", size=2)
print(type(Linda), Linda.get_name(),
      Linda.get_size(), Linda.bark())