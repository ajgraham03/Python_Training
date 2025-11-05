from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        print(f"The area of the Circle is {self.radius*math.pi}")
        

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        print(f"The area of the Rectangle is {self.length * self.width}")
        

class Triangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height
    
    def Area(self):
        print(f"The area of the triangle is {self.length*self.height/2}")

inRadius = float(input("Enter the radius: "))

circle1 = Circle(inRadius)
circle1.Area()

rectLength = float(input("Enter the length of the rectangle: "))
rectWidth = float(input("Enter the width of the rectangle: "))

rectangle1 = Rectangle(rectLength, rectWidth)
rectangle1.Area()

triLength = float(input("Enter the length of the triangle: "))
triHeight = float(input("Enter the height of the rectangle: "))

triangle1 = Triangle(triHeight, triLength)
triangle1.Area()
