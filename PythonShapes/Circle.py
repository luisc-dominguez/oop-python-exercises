from Shape import Shape
import math
from tokenize import Double

class Circle(Shape):
        
    def __init__(self, color: str, filled: bool, radius: Double = 1.0):
        super().__init__(color, filled)
        self.radius = radius
        
    def getRadius(self) -> Double:
        return self.radius
    
    def setRadius(self, radius: str):
        self.radius = radius
    
    def getArea(self) -> Double:
        return math.pi * self.radius ** 2

    def getPerimeter(self) -> Double:
        return self.radius * 2 * math.pi
    
    def __str__(self) -> str:
        _string = f"Circle[Shape[color= {self.color},filled= {self.filled}],radius= {self.radius}]\n"
        return _string
