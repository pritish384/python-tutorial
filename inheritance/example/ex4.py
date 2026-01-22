class Father:
    def __init__(self):
        self.eye_colour = "Brown"

class Mother:
    def __init__(self):
        self.skin_colour = "Black"

class Child(Father,Mother):
    def __init__(self, name):
        Father.__init__(self)
        Mother.__init__(self)
        self.name = name
        print(f"{self.name} has {self.eye_colour} eyes and {self.skin_colour} skin colour")

Child("Pritish")