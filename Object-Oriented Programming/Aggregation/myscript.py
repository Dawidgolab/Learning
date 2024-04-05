'''
Aggregation and Composition vs Inheritance
'''
class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def count_surface_area(self):
        return self.a * self.b
  
# ===========================================
 
class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a,a)
 
    def area(self):
        return self.count_surface_area() ** 2
 
# ===========================================
 
class Cube(Square):
    def __init__(self, a):
        super().__init__(a)
 
    def count_surface_area(self):
        return 6 * (self.a ** 2)
 
    def count_surface_volume(self):
        return self.a ** 3


rectangle = Rectangle(2,3)
square = Square(3)
cube = Cube(3)

print(rectangle.count_surface_area())
print(square.count_surface_area())
print(cube.count_surface_area())
print(cube.count_surface_volume())