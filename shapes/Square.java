package shapes;
public class Square extends Rectangle {

    private double side; 

    public Square() { 
        super(); 
        side = 1.0;
    }

    public Square(double side) {  
        super();
        this.side = side;
    }
   
    public Square(double side, String color, boolean filled) {  
        super();
        this.side = side;
    }
   
    public double getSide() {
        return side; 
    }
   
    public void setSide(double side) {
        this.side = side;
    }

    public void setWidth(double side) {
        this.side = side;
    }

    public void setLength(double side) {
        this.side = side;
    }

    @Override
    public String toString() {
        return "Square " + super.toString() + ", side = "+ side + "]";
    }
}
