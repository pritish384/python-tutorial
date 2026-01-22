class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):   # +
        return Point(self.x + other.x)

    def __sub__(self, other):   # -
        return Point(self.x - other.x)

    def __mul__(self, other):   # *
        return Point(self.x * other.x)

    def __str__(self):
        return str(self.x)

p1 = Point(10)
p2 = Point(5)

print(p1 + p2)   # 15
print(p1 - p2)   # 5
print(p1 * p2)   # 50
