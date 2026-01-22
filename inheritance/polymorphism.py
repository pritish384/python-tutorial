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
    b.sound()
