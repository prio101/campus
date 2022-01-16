import java.util.Scanner;
import java.lang.Math.*;

class Main {
  public static void main(String[] args) {
    Scanner input_radius = new Scanner(System.in); 
    System.out.println("Enter the radius:");

    String radius = input_radius.nextLine();
    System.out.println("You entered the radius:"+radius);

    System.out.println("The Area of the Circle is:");
    double area = (Math.PI * Math.pow(Integer.parseInt(radius), 2)) ;
    System.out.println("Radius is: "+area);
  }
}
