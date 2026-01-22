class Person:
    def call(self):
        return "Paise nahi h"

class Disha(Person):
    def call(self):
        return "Chal"
    
class Sam(Person):
    def call(self):
        return "Nahi aaauga"

benzo = Person()
print(Sam().call())
print(Disha().call())
print(benzo.call())