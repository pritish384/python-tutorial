class Engine:
    def start(self):
        print("Engine started")

class Wheel:
    def run(self):
        print("brrr brbrr")

class Car:
    def __init__(self):
        self.engine = Engine()   # composition
        self.wheel = Wheel()

    def drive(self):
        self.engine.start()
        self.wheel.run()
        print("Car moving")

c = Car()
c.drive()
