from Shape import Shape
import math

class EquilateralTriangle(Shape):
        
    def __init__(self, color, filled, sideLength = 1.0):
        super().__init__(color, filled)
        self.sideLength = sideLength
        
    def getSideLength(self):
        return self.sideLength
    
    def setSideLength(self, sideLength: int):
        self.sideLength = sideLength
    
    def getArea(self):
        super().getArea()
        return (math.sqrt(3)/ 4) * (self.sideLength * self.sideLength)
    
    def getPerimeter(self):
        super().getPerimeter()
        return self.sideLength * 3
    
    def __str__(self):
        _string = f"Equilateral Triangle[ Shape[ color: {self.color}, filled = {self.filled}], sideLength = {self.sideLength}]"
        return _string
