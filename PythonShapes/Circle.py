from Shape import Shape
import math

class Circle(Shape):
        
    def __init__(self, color, filled, radius = 1.0):
        super().__init__(color, filled)
        self.radius = radius
        
    def getRadius(self):
        return self.radius
    
    def setRadius(self, radius: int):
        self.radius = radius
    
    def getArea(self):
        super().getArea()
        return self.radius * self.radius * math.pi
    
    def getPerimeter(self):
        super().getPerimeter()
        return self.radius * 2 * math.pi
    
    def __str__(self):
        _string = f"Circle[ Shape[ color: {self.color}, filled = {self.filled}], radius = {self.radius}]"
        return _string
