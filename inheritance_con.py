class Animal:
    def __init__(self):
        self.species = "Animal"
        self.sound = "Boooo"

    def display(self):
        print(self.sound)


class Dog(Animal):
    def __init__(self):
       
        self.sound = "Bhow bhow"


an1 = Dog()
an2 = Animal()
an1.display()
an2.display()