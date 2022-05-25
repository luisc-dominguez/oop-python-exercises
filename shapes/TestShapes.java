package shapes;

public class TestShapes {

    public static void main (String[] args) {

        Shape r = new Rectangle(2, 3, "red", true);
        System.out.println(r);
        System.out.println(r.getArea());
        System.out.println(r.getPerimeter());
        System.out.println(r.toString());
        System.out.println();
        
        Shape c = new Circle(2, "blue", false);
        System.out.println(c);
        System.out.println(c.getArea());
        System.out.println(c.getPerimeter());
        System.out.println(c.getColor());
        System.out.println(c.isFilled());
        System.out.println();
        
        Rectangle s = new Square(2, "red", true);
        System.out.println(s);
        System.out.println(s.getArea());
        System.out.println(s.getPerimeter());
        System.out.println(s.getColor());
        System.out.println(s.isFilled());
        System.out.println();

        Shape t = new EquilateralTriangle(2, "red", true);
        System.out.println(t);
        System.out.println(t.getArea());
        System.out.println(t.getPerimeter());
        System.out.println(t.getColor());
        System.out.println(t.isFilled());
        System.out.println();
    }
}
