import java.util.Scanner;
import java.lang.Math.*;

class Main {
  public static void main(String[] args){
    Scanner input = new Scanner(System.in); 
    System.out.println("Enter the Height:");

    String height = input.nextLine();
    System.out.println("You entered the height:"+height);
    input.close();

    Scanner input2 = new Scanner(System.in);

    String base = input2.nextLine();
    input2.close();
    System.out.println("You entered the base:"+base);


    System.out.println("The Area of the Triangle is:");
    double area = (Integer.parseInt(height) * ( Integer.parseInt(base)/2));
    System.out.println("Area is: "+area);
  }
}
