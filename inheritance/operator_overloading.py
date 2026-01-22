class ComplexNumber:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def display(self):
        print(f"{self.real} + {self.img}i")

    def __add__(self,other):
        return (f"{self.real + other.real} + {self.img + other.img}i")
    
    def __sub__(self,other):
        return (f"{self.real - other.real} + {self.img - other.img}i")
    
    def __mul__(self, other):
        new_real = self.real * other.real - self.img * other.img
        new_imaginary = self.real * other.img + other.real * self.img
        return f"{new_real} + {new_imaginary}i"
            
        


c1 = ComplexNumber(2,3)
c2 = ComplexNumber(5,8)
c1.display()
c2.display()

print(c1+c2)
print(c1-c2)
print(c1*c2)
