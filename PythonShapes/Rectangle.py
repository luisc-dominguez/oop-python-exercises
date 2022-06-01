from Shape import Shape
from tokenize import Double

class Rectangle(Shape):
        
    def __init__(self, color, filled, width: Double = 1.0, length: Double = 1.0):
        super().__init__(color, filled)
        self.width = width
        self.length = length
        
    def getWidth(self) -> Double:
        return self.width
    
    def setWidth(self, width: Double):
        self.width = width
    
    def getLength(self) -> Double:
        return self.length

    def setLength(self, length: Double):
        self.length = length
    
    def getArea(self) -> Double:
        return self.width * self.length
    
    def getPerimeter(self) -> Double:
        return self.width * 2 + self.length * 2
    
    def __str__(self) -> str:
        _string = f"Rectangle[Shape[color= {self.color},filled= {self.filled}],width= {self.width},lenght= {self.length}]\n"
        return _string
