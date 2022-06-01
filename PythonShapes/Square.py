from Rectangle import Rectangle

class Square(Rectangle):
        
    def __init__(self, color, filled, side = 1.0):
        super().__init__(color, filled)
        self.side = side
        
    def getSide(self):
        return self.side
    
    def setSide(self, side):
        self.side = side
    
    def getArea(self):
        super().getArea()
        return self.side * self.side
    
    def getPerimeter(self):
        super().getPerimeter()
        return self.side * 4

    def setWidth():
        super().setWidth()
        self.side = self.width
    
    def setLength():
        super().setLength()
        self.side = self.length
    
    def __str__(self):
        _string = f"Square[ Rectangle[ Shape[ color: {self.color}, filled = {self.filled}], width = {self.width}, lenght = {self.length}]"
        return _string
