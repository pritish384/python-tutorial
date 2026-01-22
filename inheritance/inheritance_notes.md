# Inheritance in Python

This document provides notes on various Object-Oriented Programming (OOP) concepts related to inheritance in Python. Each section explains a concept with code examples from the corresponding Python files in this folder.

## 1. Basic Inheritance

Inheritance allows a class (child or subclass) to inherit attributes and methods from another class (parent or superclass). The child class can use the parent's methods and also add its own.

**Example from `inheritance.py`:**

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Bark")

d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # Own method
```

**Explanation:** The `Dog` class inherits the `speak` method from `Animal`. When we create a `Dog` object, it can call both inherited and its own methods.

## 2. Method Overriding

Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The subclass method replaces the parent method.

**Example from `method_overriding.py`:**

```python
class Vehicle:
    def move(self):
        print("Vehicle moving")

class Car(Vehicle):
    def move(self):   # override
        print("Car moving")

c = Car()
c.move()  # Calls Car's move, not Vehicle's
```

**Explanation:** The `Car` class overrides the `move` method from `Vehicle`. When called on a `Car` object, it uses the overridden version.

## 3. Super Method

The `super()` function allows you to call methods from the parent class. It's commonly used in `__init__` methods to initialize the parent class.

**Example from `supermethod.py`:**

```python
class Parent:
    def __init__(self):
        print("Parent init")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child init")

Child()  # Output: Parent init\nChild init
```

**Explanation:** `super().__init__()` calls the parent's `__init__` method before executing the child's initialization code.

## 4. Multiple Inheritance

A class can inherit from multiple parent classes. Python uses Method Resolution Order (MRO) to determine which method to call when there are conflicts.

**Example from `multiple_inheritance.py`:**

```python
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

c = C()
c.show()  # Output: A (from A, since A comes first in MRO)
```

**Explanation:** Class `C` inherits from both `A` and `B`. Since both have `show`, it uses `A`'s version due to MRO.

## 5. Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It's often achieved through method overriding.

**Example from `polymorphism.py`:**

```python
class Bird:
    def sound(self):
        print("Bird sound")

class Crow(Bird):
    def sound(self):
        print("Caw")

class Sparrow(Bird):
    def sound(self):
        print("Chirp")

birds = [Crow(), Sparrow()]

for b in birds:
    b.sound()  # Each calls its own sound method
```

**Explanation:** Different bird objects respond to the same `sound()` method call with their specific implementations.

## 6. Abstraction

Abstraction involves hiding complex implementation details and showing only the necessary features. In Python, it's achieved using abstract base classes (ABC).

**Example from `abstractions.py`:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        return 4 * 4

s = Square()
print(s.area())  # Output: 16
```

**Explanation:** `Shape` is an abstract class with an abstract method `area`. `Square` must implement this method. You can't instantiate `Shape` directly.

## 7. Encapsulation

Encapsulation is about bundling data and methods that operate on that data within a class, often using private attributes. While not directly inheritance-related, it's a key OOP concept.

**Example from `encapsulation.py`:**

```python
class Account:
    def __init__(self):
        self.__balance = 0   # private

    def deposit(self, amt):
        self.__balance += amt

    def get_balance(self):
        return self.__balance

a = Account()
a.deposit(1000)
print(a.get_balance())  # Output: 1000
```

**Explanation:** `__balance` is private (name mangling). It can only be accessed through public methods.

## 8. Composition

Composition is an alternative to inheritance where a class contains objects of other classes. It's often preferred over inheritance for "has-a" relationships.

**Example from `composition.py`:**

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()   # composition

    def drive(self):
        self.engine.start()
        print("Car moving")

c = Car()
c.drive()
```

**Explanation:** `Car` has an `Engine` object. This is composition, not inheritance. `Car` "has-a" `Engine`.

## 9. Operator Overloading

Operator overloading allows you to define how operators work with your custom objects. This can be used in inherited classes as well.

**Example from `operator_overloading.py`:**

```python
class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):   # +
        return Point(self.x + other.x)

    def __sub__(self, other):   # -
        return Point(self.x - other.x)

    def __mul__(self, other):   # *
        return Point(self.x * other.x)

    def __str__(self):
        return str(self.x)

p1 = Point(10)
p2 = Point(5)

print(p1 + p2)   # 15
print(p1 - p2)   # 5
print(p1 * p2)   # 50
```

**Explanation:** Special methods like `__add__` define behavior for operators. Here, `+` adds the x values of two Point objects.