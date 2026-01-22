class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Bark")

d = Dog()
d.speak()
d.bark()
