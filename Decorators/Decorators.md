# Decorators
Decorators provide a simple syntax for calling higher-order functions.

A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

To understand decorators, it is enough to think about functions as something that turns given arguments into a value.

## Functions
A function returns a value based on the given arguments.

```Python
>>> def add_one(number):
...     return number + 1

>>> add_one(2)
3
```

Functions are first-class objects. This means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on).


``` Python
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")
```
Here, say_hello() and be_awesome() are regular functions that expect a name given as a string. The greet_bob() function however, expects a function as its argument. We can, for instance, pass it the say_hello() or the be_awesome() function:

``` Python
>>> greet_bob(say_hello)
'Hello Bob'

>>> greet_bob(be_awesome)
'Yo Bob, together we are the awesomest!'
```
Note that greet_bob(say_hello) refers to two functions, but in different ways: greet_bob() and say_hello. The say_hello function is named without parentheses. This means that only a reference to the function is passed. The function is not executed. The greet_bob() function, on the other hand, is written with parentheses, so it will be called as usual.

## Inner Functions
It’s possible to define functions inside other functions. Such functions are called inner functions. Here’s an example of a function with two inner functions:

``` Python
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()
```

What happens when you call the parent() function? Think about this for a minute. The output will be as follows:
```Python
>>> parent()
Printing from the parent() function
Printing from the second_child() function
Printing from the first_child() function
```
Note that the order in which the inner functions are defined does not matter. Like with any other functions, the printing only happens when the inner functions are executed.
Furthermore, the inner functions are not defined until the parent function is called. They are locally scoped to parent(): they only exist inside the parent() function as local variables. Try calling first_child(). You should get an error:

```Py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'first_child' is not defined
```
Whenever you call parent(), the inner functions first_child() and second_child() are also called. But because of their local scope, they aren’t available outside of the parent() function.

## Returning Functions From Functions
Python also allows you to use functions as return values. The following example returns one of the inner functions from the outer parent() function:
```py
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child
```
Note that you are returning first_child without the parentheses. Recall that this means that you are returning a reference to the function first_child. In contrast first_child() with parentheses refers to the result of evaluating the function. This can be seen in the following example:
```Py
>>> first = parent(1)
>>> second = parent(2)

>>> first
<function parent.<locals>.first_child at 0x7f599f1e2e18>

>>> second
<function parent.<locals>.second_child at 0x7f599dad5268>
```
The somewhat cryptic output simply means that the first variable refers to the local first_child() function inside of parent(), while second points to second_child().

You can now use first and second as if they are regular functions, even though the functions they point to can’t be accessed directly:
```py
>>> first()
'Hi, I am Emma'

>>> second()
'Call me Liam'
```
Finally, note that in the earlier example you executed the inner functions within the parent function, for instance first_child(). However, in this last example, you did not add parentheses to the inner functions—first_child—upon returning. That way, you got a reference to each function that you could call in the future. Make sense?
