# Functional Programming 

# "Style" (A Programming Paradigm)
# Avoids side effects by performing computation mainly through the evaluation of functions  
# Relies heavily on immutable data structures 
# Reduces the liklihood of bugs 
# Filter. Map. Reduce. Functions are the Core building blocks of Functional Programming

# Mutable data structures: lists and dictionaries 
# Immutable Data structures: namedtuple

# Immutable means that the data can't be changed or updated - so no fear of any bugs or errors because of mistakes

# Defining a class - with the namedtuple function imported from collections
# Creating a "factory function"
import collections 
Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel', 
    ])
print(Scientist)

# Creating new class instances - new "scientist instances"
# These are not just Dictionary keys but Keyword arguements that you are passing to the Scientist function
jen = Scientist(name= 'Jenson Archimedes', field = 'math', born=1815, nobel=False)
print(jen.name)
# So now you can't change the attribute becasue namedtuple is immutable

# Creating a list - "scientists list"
# Failing to define an Immutable Data Structure because a list is Mutable
# Storing Immutable items in a list which is Mutable
scientists = [
    Scientist(name= 'Jenson Archimedes', field = 'math', born=1815, nobel=False),
    Scientist(name= 'Talen Ayers', field = 'math', born=1882, nobel=False),
]
from pprint import pprint
pprint(scientists)
del scientists[0]
pprint(scientists)

# Immutable Data Structure 
# Creating a tuple - an Immutable data structure 
# Unlike a list - it is Immutable 
scientists = (
    Scientist(name= 'Jenson Archimedes', field = 'math', born=1815, nobel=False),
    Scientist(name= 'Talen Ayers', field = 'geneticist', born=1882, nobel=False),
    Scientist(name= 'Talise Cogan', field = 'xenobiologist', born=1882, nobel=False),
    Scientist(name= 'Helek Branamoor', field = 'geology', born=1867, nobel=True),
    Scientist(name= 'Stanley Burgess ', field = 'biology', born=1930, nobel=False),
    Scientist(name= 'Ariel Hanson', field = 'biology', born=1939, nobel=True),
    Scientist(name= 'Warren Held', field = 'xenobiologist', born=1928, nobel=False),
    Scientist(name= 'Daniel Rothfuss', field = 'astrophysicist', born=1951, nobel=False),    
)
# Prints an immutable array of the Scientists objects 
pprint(scientists)
 
# TypeError: 'tuple' object doesn't support item deletion
del scientists[0] 
# But you still can access everything by index
print(scientists[0].name)


# filter() Function 
# The built-in lambda expression

# A Shorcut for Defining a function in Python, 
# So you can put arguments and then you have one expression that gets evaluated
# It will evaluate this expression and return it back out of the lamda function 

# <filter object at 0x7fa9a6203d50> 
print(filter(lambda x: x.nobel is True, scientists))

fs = filter(lambda x: x.nobel is True, scientists)
pprint(list(fs))
fs = filter(lambda x: x.nobel is True, scientists)
pprint(next(fs))

# The filter() function 
# Allows you to apply a function over a whole list of things, or an iterable of things 
# And then every item in this list, or in this iterable, gets passed to the function 
fs = tuple(filter(lambda x: x.nobel is True, scientists))
pprint(fs)
pprint(tuple(filter(lambda x: True, scientists)))
pprint(tuple(filter(lambda x: x.field == 'biology', scientists)))
pprint(tuple(filter(lambda x: x.field == 'biology' and x.nobel, scientists)))

# But why the filter() Function when you can use a forloop with an if statement 
for nobel in scientists:
    if nobel.nobel is True:
        print(nobel)

def nobel_filter(x):
    return x.nobel is True

pprint(tuple(filter(nobel_filter, scientists)))

# List Comprehensions 
pprint(tuple([x for x in scientists if x.nobel is True]))
pprint(tuple(x for x in scientists if x.nobel is True))
tuple([1, 2, 3])




# The map() Function
pprint(scientists)
# Beautiful 
names_and_ages = (tuple(map(
    lambda x: {'name': x.name, 'age': 2020 - x.born},
    scientists
)))
pprint(names_and_ages)

# Pythonic 
names_and_ages = tuple([{'name': x.name.upper(), 'age': 2020 - x.born}
    for x in scientists])



# The reduce() Function 
from functools import reduce

pprint(names_and_ages)

total_age = reduce(
    lambda acc, val: acc + val['age'],
    names_and_ages,
    0)

pprint(total_age)

pprint(sum(x['age'] for x in names_and_ages))

def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc

scientists_by_field = reduce(
    reducer,
    scientists,
    {'math': [], 'geneticist': [], 'xenobiologist': [], 'geology': [], 'biology': [], 'astrophysicist': []}
)


pprint(scientists_by_field)

import collections 
scientists_scientists_by_field = reduce(
    reducer,
    scientists,
    collections.defaultdict(list)

)
pprint(scientists_by_field)

https://realpython.com/lessons/why-use-reduce-function/