import java.io.*;
import java.util.*;

public class FizzBuzz {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        
        for (int i = 1; i <= t; i++) {
            
            if(i % 3 == 0 && i % 5 == 0) {
                System.out.println("FizzBuzz");
            }
            else if(i % 3 == 0) {
                System.out.println("Fizz");
            }
            
            else if(i % 5 == 0) {
                System.out.println("Buzz");
            }
            
            else {
                System.out.println(i);
            }
        }  
    }
}