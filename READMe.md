# Python Concepts: A Quick Reference Guide
 ## 1. Python Basics
### Variables and Types:
- Variables store data values.

- Types can be checked using type().

```bash
x = 4
y = "Hello"
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
```
### Lists:
- Ordered, mutable collections.

- Common methods: append(), insert(), remove(), pop(), count(), reverse(), sort().

```bash
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits.remove('banana')
fruits.reverse()
```
### Tuples:
- Ordered, immutable collections.

- Used when you want to store data that shouldn’t change.

```bash
t1 = (1, 2, 3)
print(t1[0])  # Access by index
```
### Sets:
- Unordered collections of unique items.

- Common methods: add(), remove(), union(), intersection(), difference(), issubset(), issuperset(), isdisjoint().

```bash
my_set = {1, 2, 3}
my_set.add(4)
```
### Dictionaries:
- Collection of key-value pairs.

- Methods: keys(), values(), items().

```bash
my_dict = {'name': 'John', 'age': 25}
print(my_dict['name'])
```
## 2. Loops and Functions
### Loops:
For loop: Iterates over a sequence (e.g., list, tuple, string).

- While loop: Continues while a condition is true.

```bash
for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1
```
### Functions:
- Defining a function with parameters and return values.

- Arguments and return statements allow for flexibility.

```bash
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```
## 3. Object-Oriented Programming (OOP)
### Encapsulation:
- Hiding the internal details of a class and controlling access to them through public methods.

```bash
class Car:
    def __init__(self, brand):
        self.__brand = brand  # private attribute
    
    def get_brand(self):
        return self.__brand
```
### Abstraction:
- Hiding complex implementation details and only exposing necessary functionalities (using abstract classes).

```bash
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    
    def start(self):
        print(f"{self.__brand} {self.model} is starting.")
```
### Inheritance:
- Inheriting attributes and methods from a parent class into a child class.

```bash
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Inheriting the parent constructor
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving...")
```
### Polymorphism:
- The ability of an object to take on different forms, especially by overriding methods.

```bash
class Bike(Vehicle):
    def start(self):
        print(f"{self.brand} bike is starting...")

car = Car("Toyota", "Camry")
bike = Bike("Yamaha")

car.start()  # Toyota is starting...
bike.start()  # Yamaha bike is starting...
```
## 4. Summary
By mastering these concepts, you have gained a solid foundation in Python:

- **Data types**: Lists, tuples, dictionaries, sets.

- **Control flow**: Loops and conditions.

- **Functions**: Definition, arguments, and returns.

- **OOP**: Encapsulation, Abstraction, Inheritance, Polymorphism.