from Shape import Shape

class Rectangle(Shape):
        
    def __init__(self, color, filled, width = 1.0, length = 1.0):
        super().__init__(color, filled)
        self.width = width
        self.length = length
        
    def getWidth(self):
        return self.width
    
    def setWidth(self, width: int):
        self.width = width
    
    def getLength(self):
        return self.length

    def setLength(self, length: int):
        self.length = length
    
    def getArea(self):
        super().getArea()
        return self.width * self.length
    
    def getPerimeter(self):
        super().getPerimeter()
        return self.width * 2 + self.length * 2
    
    def __str__(self):
        _string = f"Rectangle[ Shape[ color: {self.color}, filled = {self.filled}], width = {self.width}, lenght = {self.length}]"
        return _string
