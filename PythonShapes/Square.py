from Rectangle import Rectangle
from tokenize import Double
class Square(Rectangle):
        
    def __init__(self, color: str, filled: bool, side: Double = 1.0):
        super().__init__(color, filled)
        self.side = side
        
    def getSide(self) -> Double:
        return self.getWidth()
    
    def setSide(self, side: Double):
        self.setWidth(side)
        self.setLength(side)

    def setWidth(self, side: Double):
        self.width = side
    
    def setLength(self, side: Double):
        self.lenght = side
    
    def __str__(self) -> str:
        _string = f"Square[Rectangle[Shape[color= {self.color},filled= {self.filled}],width= {self.width},lenght= {self.length}]\n"
        return _string
