class Point:
    def __init__(self, x , y):
        self.x = x 
        self.y = y
        
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else: 
            return False
p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(5, 1)

print(p1 == p2)   # True
print(p1 == p3)   # False
         
        

        
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2

print(v3.x, v3.y)

p = Point(4, 6)

print(v3 == p)

