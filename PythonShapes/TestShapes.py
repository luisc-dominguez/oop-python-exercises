from Shape import Shape
from Circle import Circle
from Rectangle import Rectangle
from EquilateralTriangle import EquilateralTriangle
from Square import Square

def testShape(Shape):
    s1 = Shape("red", True)
    s1.getArea()
    s1.getPerimeter()
    print(s1)

def testCircle(Circle):
    c1 = Circle("yellow", False, 5.0)
    c1.getArea()
    c1.getPerimeter()
    print(c1)

def testRectangle(Rectangle):
    r1 = Rectangle("red", True, 1.0, 1.0)
    r1.getArea()
    r1.getPerimeter()
    print(r1)

def testEquilateralTriangle(EquilateralTriangle):
    et1 = EquilateralTriangle("red", True, 1.0)
    et1.getArea()
    et1.getPerimeter()
    print(et1)

def testSquare(Square):
    s1 = Square("red", True, 1.0)
    s1.getArea()
    s1.getPerimeter()
    print(s1)

if __name__ == "__main__":
    testShape(Shape)
    testCircle(Circle)
    testEquilateralTriangle(EquilateralTriangle)
    testRectangle(Rectangle)
    testSquare(Square)
