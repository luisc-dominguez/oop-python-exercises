from Shape import Shape
import math
from tokenize import Double

class EquilateralTriangle(Shape):
        
    def __init__(self, color: str, filled: bool, sideLength: Double = 1.0):
        super().__init__(color, filled)
        self.sideLength = sideLength
        
    def getSideLength(self) -> Double:
        return self.sideLength
    
    def setSideLength(self, sideLength: Double):
        self.sideLength = sideLength
    
    def getArea(self) -> Double:
        return (math.sqrt(3)/ 4) * (self.sideLength * self.sideLength)
    
    def getPerimeter(self) -> Double:
        return self.sideLength * 3
    
    def __str__(self) -> str:
        _string = f"Equilateral Triangle[Shape[color= {self.color},filled= {self.filled}],sideLength= {self.sideLength}]\n"
        return _string
