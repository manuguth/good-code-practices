# Prerequisites

Please have a look at the examples below. If something looks unfamiliar, please,
read up on it before the start of the workshop.

# variables

<!-- write pre.py -->
```python
# variable assignment
favorite_number = 42
hello = "World"
```

<!-- append pre.py
```
assert favorite_number == 42
assert hello == "World"
```
-->

## integer
<!-- append pre.py -->
```python
num = 3
other = (num * 2)**2 + 3  # arithmetics
num += 1  # in-place arithmetics
```

<!-- append pre.py
```
assert num == 4
assert other == 39
```
-->

## float
<!-- append pre.py -->
```python
circle = 3.14
cake = (circle * 2)**2 + 3  # arithmetics
circle *= 2  # in-place arithmetics
```
<!-- append pre.py
```
assert abs(circle - 6.28) < 1e-6
assert abs(cake - 42.4384) < 1e-6
```
-->

## complex
<!-- append pre.py -->
```python
point = 1.2+3.4j
other = point * 2  # arithmetics
point += 3.2  # in-place arithmetics
x = other.real  # real part
y = other.imag  # imaginary part
```
<!-- append pre.py
```
assert abs(point.real - 4.4) < 1e-6
assert abs(point.imag - 3.4) < 1e-6
assert abs(other.real - 2.4) < 1e-6
assert abs(other.imag - 6.8) < 1e-6
assert abs(x - 2.4) < 1e-6
assert abs(y - 6.8) < 1e-6
```
-->

## string
<!-- append pre.py -->
```python
greeting = "Hello, World!"
upper = greeting.upper()  # HELLO, WORLD!
lower = greeting.lower()  # hello, world!
start = greeting.startswith("Hello")  # True
end = greeting.endswith("Earth!")  # False
sub = greeting[1:5]  # substring: ello

name = "Uni" + "Freiburg"  # concatenation
scream =  "a" * 10  # aaaaaaaaaa


# String formatting
to_dave = "Hello %s" % "David"
to_gina = "Hello {:s}".format("Gina")

cake = "There are %06.2f pieces of cake." % 3.1415
```

<!-- append pre.py
```python
assert greeting == "Hello, World!"
assert upper == "HELLO, WORLD!"
assert lower == "hello, world!"
assert start
assert not end 
assert sub == "ello"

assert name == "UniFreiburg"
assert scream == "aaaaaaaaaa"

assert to_dave == "Hello David"
assert to_gina == "Hello Gina"
assert cake == "There are 003.14 pieces of cake."
```
-->

## tuple
<!-- append pre.py -->
```python
point = (3.42, 4)  # 2-tuple
first = point[0]  # 3.42
```

<!-- append pre.py
```
assert point == (3.42, 4)
assert first == 3.42
```
-->

## list
<!-- append pre.py -->
```python
numbers = [1, 2, 3, 5]
numbers.append(7)  # append number
numbers[0] = 3   # set item
5 in numbers  # True

listed = "--".join(["A", "B", "C", "D"])  # A--B--C--D
```
<!-- append pre.py
```
assert numbers == [3, 2, 3, 5, 7]
assert listed == "A--B--C--D"
```
-->

## set
<!-- append pre.py -->
```python
numbers = {1, 2, 3, 5}
numbers.add(7)  # add number
9 in numbers  # False
```
<!-- append pre.py
```
assert numbers == {1, 2, 3, 5, 7}
```
-->

## dict
<!-- append pre.py -->
```python
phonebook = {
    "Alice": 1234567,
    "Bob": 2345678,
}

phonebook["Bob"] = 3456789  # update item
phonebook["David"] = 1357924  # add item
"Eva" in phonebook  # False
phonebook.keys()  # Alice, Bob, David
phonebook.values()  # 1234567, 3456789, 1357924
phonebook.items()  # (Alice, 1234567), ...
```
<!-- append pre.py
```
assert phonebook == {
    "Alice": 1234567,
    "Bob": 3456789,
    "David": 1357924,
}
```
-->

## Other values
<!-- append pre.py -->
```python
# boolean
a = True
b = False

# special value
c = None
```

## Mutable and immutable objects

<!-- append pre.py -->
```python
# Immutable
original = "hello"
reference = original
reference = "hi"
# original is still "hello"

# Mutable
greetings = ["hello"]
reference = greetings
reference.append("hi")
# both are now ["hello", "hi"]
```
<!-- append pre.py
```
assert original == "hello"
assert reference == ["hello", "hi"]
```
-->

# import
<!-- append pre.py -->
```python
# standard import
import math

# import parts
from time import sleep

# import as alias
import numpy as np
```
<!-- append pre.py
```
assert math
assert sleep
assert np
```
-->

# functions
<!-- append pre.py -->
```python
# Function definition
def greet(people):
    for person in people:
        print("Hello", person)

# Call function
greet(["Lea", "Mark"])
```

## default arguments
<!-- append pre.py -->
```python
def root(number, base=2):
    return math.pow(number, 1/base)

a = root(4)  # use default
b = root(27, 3)  # use different base
c = root(3, base=1)  # named arguments
```
<!-- append pre.py
```
assert a == 2
assert b == 3
assert c == 3
```
-->

## Lambda, usually passed to other functions
<!-- append pre.py -->
```python
first = lambda x: x[0]

# equal to
def first(x):
    return x[0]
```

## Positional arguments and keyword arguments
<!-- append pre.py -->
```python
def func(pos_1, pos_2, *args, kwd_1="a", kwd_2="b", **kwds):
    pass

func(6, 7, 8, 9, 10, kwd_2="c", hello="world")
    # -> pos_1 = 6
    # -> pos_2 = 7
    # -> args = [8, 9, 10]
    # -> kwd_1 = "a"
    # -> kwd_2 = "c"
    # -> kwds = {"hello": "world"}
```

## builtins

<!-- append pre.py
```
some_file = open("measurement.txt", "w")
```
-->

<!-- append pre.py -->
```python
len(["a", "b", "c"])  # 3
len("hello")  # 5
len({"Hello": "world"}) # 1

sorted([3, 5, 1])  # 1, 3, 5
sorted("hello")  # e, h, l, l, o

print("Hello", "World")  # Hello World
print("Hello", "World", sep="")  # HelloWorld
print("Hello", "World", file=some_file)  # prints to file
print("Hello", "World", end="!")  # Hello World! (no new line)

round(3.1415)  # 3
round(3.1415, 2)  # 3.14

reversed([1, 2, 5])  # 5, 2, 1

sum([1, 2, 3, 5, 8])  # 19
max([1, 2, 3, 5, 8])  # 8
min([1, 2, 3, 5, 8])  # 1

abs(7)  # 7
abs(-4)  # 4

any([True, False, False])  # True
all([True, False, False])  # False
```

```python
help(int)  # print help about object
dir(int)  # lists all attributes of object
vars(int)  # lists all attributes and its values

name = input("Please enter name: ")  # prompt user to enter name
```

# slicing
<!-- append pre.py -->
```python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

primes[3]  # access item: 7
primes[5]  # access item: 13
primes[3:5]  # range: 7, 11
primes[3:]  # range: 7, 11, 13, 17, 19, 23, 29
primes[:5]  # range: 2, 3, 5, 7, 11
primes[:-3]  # range: 2, 3, 5, 7, 11, 13, 17

primes[::2]  # steps: 2, 5, 11, 17, 23
primes[1::2]  # steps: 3, 7, 13, 19, 29
```

# if
<!-- append pre.py -->
```python
if 3 < 5:
    print("Three is less than five")
```

# and, or, not
<!-- append pre.py -->
```python
if "eva" in phonebook and phonebook["eva"] == 12345:
    print("Her number is 12345")

number = 2
if not number > 10:
    print("Number is too small")

if "eva" not in phonebook:
    print("We don't have Eva's number.")
```

## else, elif
<!-- append pre.py -->
```python
command = "quit"
if command == "help":
    print_help()
elif command == "exit":
    sys.exit(0)
else:
    print("Unknown command")
```
# loops
<!-- append pre.py -->
```python
for fruit in ["banana", "apple", "peach"]:
    print("I like", fruit)
```

```python
while True:
    command = input("Please type 'exit': ")
    if command == "exit":
        break
```

## continue, break

<!-- append pre.py
```
def is_prime(x):
  return (x % 2 != 0)
```
-->


<!-- append pre.py -->
```python
for i in range(10):
    if is_prime(i):
        # skip prime numbers
        continue

for i in range(10):
    if is_prime(i):
        # found prime number, exit loop
        break
```

## range
<!-- append pre.py -->
```python
for number in range(10):
    print("The square of %d is %d." % (number, number**2))
```
## zip
<!-- append pre.py -->
```python
positions = [1, 2, 4, 8]
times = [0.3, 0.6, 0.8, 1.0]

for position, time in zip(positions, times):
    print("It travelled %g m in %g s." % (position, time))
```
## enumerate
<!-- append pre.py -->
```python
for i, movie in enumerate(["Avengers", "Avatar", "Titanic"]):
    print("The %d-th movie is %s" % (i, movie))
```

## for-else
<!-- append pre.py
```
events = [False, False, False, True, False, True]
def is_higgs(event):
  return event
```
-->

<!-- append pre.py -->
```python
for event in events:
    if is_higgs(event):
        print("We've found the higgs.")
        break  # No need to find a second
else:
    print("There was no higgs in the list.")
```

# with, open
<!-- append pre.py -->
```python
with open("measurement.txt") as data:
    for line in data:
        pass
```
# comprehension
<!-- append pre.py -->
```python
# list comprehension
squares_list = [i**2 for i in range(10)]
# -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# set comprehension
squares_set = {i**2 for i in range(10)}
# -> {0, 1, 4, 9, 16, 25, 36, 49, 64, 81} 

# dict comprehension
squares_dict = {i: i**2 for i in range(3)}
# -> {0: 0, 1: 1, 2: 4}
```
<!-- append pre.py
```
assert squares_list == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
assert squares_set == {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
assert squares_dict == {0: 0, 1: 1, 2: 4}
```
-->

# numpy
<!-- append pre.py -->
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])

b = a * 2 + 3  # piecewise arithmetics
c = a + b  # piecewise arithmetics of two arrays
```
<!-- append pre.py
```
assert (a == [1, 2, 3, 4, 5]).all()
assert (b == [5, 7, 9, 11, 13]).all()
assert (c == [6, 9, 12, 15, 18]).all()
```
-->

## linspace, logspace and arange
<!-- append pre.py -->
```python
a = np.arange(4)  # 0, 1, 2, 3
b = np.linspace(0, 1, 5)  # 0, 0.25, 0.5, 0.75, 1
c = np.logspace(0, 6, 4)  # 1e0, 1e2, 1e4, 1e6
```
<!-- append pre.py
```
assert (a == [0, 1, 2, 3]).all()
assert (b == [0, 0.25, 0.5, 0.75, 1]).all()
assert (c == [1, 100, 1e4, 1e6]).all()
```
-->

<!-- console_output
```
$ python3 pre.py
Hello Lea
Hello Mark
Hello World
HelloWorld
Hello World!Three is less than five
Number is too small
We don't have Eva's number.
Unknown command
I like banana
I like apple
I like peach
The square of 0 is 0.
The square of 1 is 1.
The square of 2 is 4.
The square of 3 is 9.
The square of 4 is 16.
The square of 5 is 25.
The square of 6 is 36.
The square of 7 is 49.
The square of 8 is 64.
The square of 9 is 81.
It travelled 1 m in 0.3 s.
It travelled 2 m in 0.6 s.
It travelled 4 m in 0.8 s.
It travelled 8 m in 1 s.
The 0-th movie is Avengers
The 1-th movie is Avatar
The 2-th movie is Titanic
We've found the higgs.
```
-->
