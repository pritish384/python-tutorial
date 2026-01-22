class Vehicle:
    def move(self):
        print("Vehicle moving")

class Car(Vehicle):
    def move(self):   # override
        print("Car moving")

c = Car()
c.move()
