class Parent:
    def __init__(self):
        self.eye_colour = "RED"
        print("Abhijeet")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print(f"Pritish has {self.eye_colour} eyes")

Child()