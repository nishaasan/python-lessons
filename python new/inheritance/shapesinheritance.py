class Shape:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def description():
        return "This is a shape."

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Creating a Circle object
circle = Circle("Circle", 5)

# Calling the static method using the Circle object
print(circle.description())  # Outputs: "This is a shape."
