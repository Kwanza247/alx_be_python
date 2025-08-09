# File: oop/polymorphism_demo.py

import math

# Base Class
class Shape:
    def area(self):
        # Force subclasses to override this method
        raise NotImplementedError("Subclasses must implement the area method.")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Rectangle area formula

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)  # Circle area formula
