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
