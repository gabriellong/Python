# For Loops (Definite Iteration)
# Iteration is executing code more than one time
# Iterables and Iterators
# Range, Break and Continue 

# 3 Types of Definite Iteration: 
# Numeric Range Loop, 3 Expression Loop, Collection-based Loop

# 
# # Numberic Range Loop
# for i = 1 to 10:
#     pass
# 
# # 3 Expression Loop
# for (i = 1; i <= 10; i+= 1)
#     pass
# # Collection-based Loop
# for i in <collection>:
#     <loop body>
# 
# 
# 
# 
# 
# 
# 
# # Definite: Runs a number of times that is know at the construction of the loop 
# for <sequence>: 
#     <loop body>
# # Indefinite: runs until a condition is met 
# while <condition>:
#     <loop body>
# 
# # example:
# for <var> in <iterable>:
#     <statement(s)> 




# Variable with a list
list_1 = ['dragoon', 'marine', 'stalker']
for i in list_1:
    print(i)
# String
string_1 = 'astartes'
for i in string_1:
    print(i)
# Tuple
tuple_1 = ('marine', 'astartes', 'dragoon')
for i in tuple_1:
    print(i)
# Set
set_2 = {'stalker', 'zealot'}
for i in set_2:
    print(i)
# Dict
dict_1 = {'dragoon': 5, 'stalker': 4, 'marine':2}
for i in dict_1:
    print(i)
    pass

# Iterations
list_1 = ['dragoon', 'marine', 'stalker']
itr_1 = iter(list_1)
itr_1
next(itr_1)
list(itr_1)

# Dict
dict_1 = {'adept': 2.5, 'probe': 0.5, 'sentry':1/.5}
for keys in dict_1:
    print(keys)

# Dict
dict_1 = {'adept': 2.5, 'probe': 0.5, 'sentry':1.5}
print("Health Points")
for values in dict_1.values():
    print(values)

dict_1 = {'adept': 2.5, 'probe': 0.5, 'sentry':1.5}
print("Health Points")
for items in dict_1.items():
    print(items)

dict_1 = {'adept': 2.5, 'probe': 0.5, 'sentry':1.5}
for keys, values in dict_1.items():
    print(f'Unit = {keys}, Health = {values}')


zerg_units =range(5)
for i in zerg_units:
    print(i)

zerg_units_2 =range(0, 15, 1,)
print("detecting zerg life forms")
for i in zerg_units_2:
    if i == 1: 
        print(f'{i} zergling incoming')
        continue
    if i == 12:
        print('Ultralisk detected')
        print('self destruct initiated ')
        break
    
    print(f'{i} zerglings incoming')
    


units_10 = ('marine', 'marauder', 'medivac', 'mine', 'ghost', 'siege tank')
for items in units_10:
    if 'g' in items:
        break
    
    print(items)