from abc import ABC, abstractmethod
from tokenize import Double
class Shape():

    def __init__(self, color: str = "red", filled: bool = True):
        self.color = color
        self.filled = filled

    def getColor(self) -> str: 
        return self.color

    def setColor(self, color: str):
        self.color = color
    
    def isFilled(self) -> bool:
        return self.filled
    
    def setFilled(self, filled: bool):
        self.filled = filled
    
    @abstractmethod
    def getArea(self) -> Double:
        pass

    @abstractmethod
    def getPerimeter(self) -> Double:
        pass

    def __str__(self) -> str:
        _string = f"Shape[color= {self.color},filled= {self.filled}]\n"
        return _string

