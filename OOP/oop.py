
# list: name, age, type, sight
unit1 = ["Zealot", 34, "Melee", 9]
unit2 = ["Sentry", 21, "Ranged", 10]
unit3 = ["Stalker", "Ranged", 10]

# age index
unit1[1]
# error unit3 does not have the same number of elements in the list
unit3[1]
# Make the code more manageable and more maintainable by using classes. 
# A class is a blueprint for how something should be defined. 
# It doesn’t actually contain any data. 
# An instance is an object that is built from a class and contains real data.
# Many instances can be created from a single class.

# Python class names are written in CapitalizedWords notation by convention.
# pass is often used as a placeholder
class StarcraftUnit:
    pass
# the first parameter will always be a variable called self.
# When a new class instance is created, the instance is automatically passed
# to the self parameter in .__init__() so that new attributes can be defined on the object.
# creates an attribute and assigns it the value of the selected parameter  
# Attributes created in .__init__() are called instance attributes
class StarcraftUnit:
    def __init__(self, name, sight):
        self.name = name
        self.sight = sight

# Class attributes are attributes that have the same value for all class instances. 
# You can define a class attribute by assigning a value to a variable name outside of .__init__().
# Use class attributes to define properties that should have the same value for every class instance
class StarcraftUnit:
    race = "Protoss"
    def __init__(self, name, sight):
        self.name = name
        self.sight = sight


# Instantiate an Object in Python
# Creating a new object from a class is called instantiating an object. 
# To pass arguments to the name and age parameters 
# put values into the parentheses after the class name:

Sentry = StarcraftUnit("Sentry", 10)
Zealot = StarcraftUnit("Zealot", 9)
Stalker = StarcraftUnit("Stalker", 10)
Zergling = StarcraftUnit("Zergling", 8)
ChangelingZealot = StarcraftUnit("Zealot", 9)
# After creating the StarcraftUnit instances 
# You can access their instance attributes using dot notation
Sentry.name
Sentry.sight
Sentry.race
Zergling.race = "Zerg"
Zergling.race
# Insatance methods 
class StarcraftUnit:
    race = "Protoss"
    
    def __init__(self, name, sight):
        self.name = name
        self.sight = sight
    
    def description(self):''
         return f"{self.name} has {self.sight} sight"
        
    def speak(self, sound):
        return f"{self.name}: {sound} "
    
Sentry.description()
Sentry.speak('...')
Zealot.speak('My life for Aiur!')
ChangelingZealot.description()
ChangelingZealot.race = "Zerg"
ChangelingZealot.race
ChangelingZealot.speak('Metamorphosis complete.')

# <__main__.StarcraftUnit object at 0x7f7127b2f550>
print(Sentry)  

class StarcraftUnit:
    race = "Protoss"
    
    def __init__(self, name, sight):
        self.name = name
        self.sight = sight
    
    def __str__(self):
        return f"{self.name} has {self.sight} sight"

# Adept has 9 sight
Adept = StarcraftUnit("Adept", 9)
print(Adept)