# dictionary
# are dynamic (mutable)
# can be nested (contain other dicts or lists)
# objects can be changed
# contains keys and values
from pprint import pprint
# key value pairs
barracks_dict_1 = {
    'marine_1': 'marine',
    'marine_2': 'marine',
    'kerrigan': 'ghost',
    'raynor': 'marine',
    'ghost_1': 'ghost',
    'chansey': 'medic'
}
print(barracks_dict_1)
pprint(barracks_dict_1)

print(barracks_dict_1['raynor'])
print(barracks_dict_1['chansey'])

# Adding new key and value
barracks_dict_1['tiberius'] = 'marauder'
pprint(barracks_dict_1)
# Changing a key's value
barracks_dict_1['chansey'] = 'pokemon'
pprint(barracks_dict_1)
# Deleting a key
del barracks_dict_1['chansey']
pprint(barracks_dict_1)

# You can't access Dictionaries like a list with index numbers[0]
barracks_dict_1[0]
#  KeyError: 0

# However you could use index numbers as the keys
hatchery_dict_1 = {
    0: "queen",
    1: "larvae",
    2: "zergling"
}
hatchery_dict_1[0]

# Incrementally Building a Dictionary
hatchery_dict_2 = {}
hatchery_dict_2['larvae_1'] = 3
hatchery_dict_2['larvae_2'] = 3
hatchery_dict_2['larvae_3'] = 3
hatchery_dict_2['queen_1'] = 1
hatchery_dict_2['zergling_1'] = 2
# Value is a list
hatchery_dict_2['larvae_4_list'] = ['hydralisk', 'roach', 'viper']
# Nesting a dictionary
hatchery_dict_2['drone_1'] = {'hatchery_3': 'larvae_1', 'larvae_2': 'roach'}

pprint(hatchery_dict_2)
# Nested dictionary
pprint(hatchery_dict_2['drone_1'])

# Using the list and it's index
hatchery_dict_2['larvae_4_list'][0]
hatchery_dict_2['larvae_4_list'][1]
hatchery_dict_2['larvae_4_list'][2]

# Nested dictionary keys
pprint(hatchery_dict_2['drone_1']['larvae_2'])


# Restrictions on keys & values
# keys can be only used once
# keys must be immutable
# values can be ANYTHING

nexus_1 = {
    0.5: 'Probe',
    True: 1,
    (1,3): 'a tuple probe'
}
pprint(nexus_1)
pprint(nexus_1[True])

# can't do this because lists are mutable 
nexus_1[[0,2,3,4]]='test'
# TypeError: unhashable type: 'list'

# Operators and Methods for Dictionaries

barracks_dict_1 = {
    'marine_1': 'marine',
    'marine_2': 'marine',
    'kerrigan': 'ghost',
    'raynor': 'marine',
    'ghost_1': 'ghost',
    'chansey': 'medic'
}

'chansey' in barracks_dict_1
'chansey' not in barracks_dict_1
'mengsk' in barracks_dict_1


barracks_dict_1.get('chansey')
pprint(barracks_dict_1.get('mengsk'))

barracks_dict_1.items()
list(barracks_dict_1.items())
list(barracks_dict_1.items())[1]

for items in list(barracks_dict_1.items()):
    print(items[1])

# ?WHAT
# 
# for items in list(barracks_dict_1.items()):
#     if items == ['marine']:
#         print('ok')
# 

barracks_dict_1.keys()
barracks_dict_1.values()

# pop removes a key and returns it's value
barracks_dict_1.pop('chansey')
barracks_dict_1.get('chansey') is True
pprint(barracks_dict_1)

# popitem pulls a random key pair and return it as a tuple
barracks_dict_1.popitem()
pprint(barracks_dict_1)


barracks_dict_1 = {
    'marine_1': 'marine',
    'marine_2': 'marine',
    'kerrigan': 'ghost',
    'raynor': 'marine',
    'ghost_1': 'ghost',
    'chansey': 'medic'
}

barracks_dict_2 = {
    'marine_3': 'marine',
    'marine_4': 'marine',
    'gabriel': 'ghost',
    'tychus': 'marine',
    'ghost_2': 'ghost',
    'chansey': 'pokemon'
}

barracks_dict_2.update(chansey='medic', gabriel='spectre')
pprint(barracks_dict_2)

barracks_dict_2 = {
    'marine_3': 'marine',
    'marine_4': 'marine',
    'gabriel': 'ghost',
    'tychus': 'marine',
    'ghost_2': 'ghost',
    'chansey': 'pokemon'
}
barracks_dict_2.update(barracks_dict_1)
pprint(barracks_dict_2)

# Emptys dictionary 
barracks_dict_1.clear()
pprint(barracks_dict_1)
