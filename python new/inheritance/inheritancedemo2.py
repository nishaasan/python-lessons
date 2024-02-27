class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Example usage:
shape = Shape("Shape")
print("Name:", shape.name)
print("Area:", shape.area())

rectangle = Rectangle("Rectangle", 5, 3)
print("Name:", rectangle.name)
print("Area:", rectangle.area())

# Call the area method of the Shape class using the rectangle object
print("Area (from parent class):", Shape.area(rectangle))
