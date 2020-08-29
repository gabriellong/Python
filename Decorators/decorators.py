### Functions
# Functions are first-class objects
# Just like any other object (string, int, float, list, and so on)
# Functinos therefore can be passed around and used as arguments 

# These 2 functions are regular functions that expect a name given as a string

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo name, together we are the awesomest!"

# The greet_bob() function however expects a function as its argument. 

def greet_bob(greeter_func):
    return greeter_func("Bob")

# Therefore it is possible to pass it the say_hello() or the be_awesome() function. 

greet_bob(say_hello)
greet_bob(be_awesome)

### Inner Functions
# It’s possible to define functions inside other functions.

def medivac():
    print("Printing from the medivac() function")

    def first_passenger():
        print("Printing from the first_passenger() function")

    def second_passenger():
        print("Printing from the second_passenger() function")

    second_passenger()
    first_passenger()

# The inner functions are not defined until the medivac function is called. 
# They are locally scoped to medivac(): they only exist inside the medivac() function as local variables. 
# Try calling first_passenger(). You should get an error:

medivac()
first_passenger()

### Returning Functions From Functions
# Using functionss as return values.
# Returns one of the inner functions from the outer medivac() function:
# Returning first_passenger without the parentheses, this means that you are returning a reference to the function first_passenger.
def medivac(num):
    def first_passenger():
        return "Hi, I am Jim Raynor"

    def second_passenger():
        return "Call me Kerrigan"

    if num == 1:
        return first_passenger
    else:
        return second_passenger

# The output simply means that the first variable refers to the local first_passenger() function inside of medivac()
# Note that in the earlier example you executed the inner functions within the medivac function, for instance first_passenger().
# However, in this last example, you did not add parentheses to the inner functions
# That way, you got a reference to each function that you could call in the future.
first = medivac(1)
first
second = medivac(2)
first()
second()

### Simple Decorators

# The so-called decoration happens at the following line:
# In effect, the name Jim_Raynor now points to the wrapper() inner function. 
# Remember that you return wrapper as a function when you call my_decorator(Jim_Raynor):
# However, wrapper() has a reference to the original Jim_Raynor as func, and calls that function between the two calls to print().
# Decorators wrap a function, modifying its behavior.

def my_decorator(func):
     """Booting Adjutant and activating Greetings"""
    def wrapper():
        print("Adjutant online. Good morning, Captain.")
        func()
        print("Adjutant online. Good morning, Captain.")
    return wrapper()

def Jim_Raynor():
    print("This Is Jimmy")

Jim_Raynor = my_decorator(Jim_Raynor)

### LEFT OFF https://realpython.com/primer-on-python-decorators/


#### Notes 
### Documenting Daily Fruit and Veg intake, see which days you eat more fruit or veg and what is most popular#
### focus on little bits of everything and keep updated so you can come back to whatever easily plus you'll learn to learn better

help(my_decorator)