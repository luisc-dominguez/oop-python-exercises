package shapes;
public class EquilateralTriangle extends Shape {  

    private double sideLength; 
   
    public EquilateralTriangle() { 
        super(); 
        sideLength = 1.0;
    }

    public EquilateralTriangle(double sideLength) {  
        super();
        this.sideLength = sideLength;
    }
   
    public EquilateralTriangle(double sideLength, String color, boolean filled){  
        super(color, filled);
        this.sideLength = sideLength;
    }
   
    public double getSideLength() {
        return sideLength; 
    }
   
    public void setSideLength(double sideLength) {
        this.sideLength = sideLength;
    }

    public double getArea() {
        return sideLength * sideLength * Math.PI;
    }

    public double getPerimeter() {
        return 2 * sideLength * Math.PI;
    }

    @Override
    public String toString() {
        return "Equilateral Triangle " + super.toString() + ", sideLength = "+ sideLength + "]";
    }
}