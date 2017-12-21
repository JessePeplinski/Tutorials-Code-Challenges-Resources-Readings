import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class MakingAnagrams {
    public static int numberNeeded(String first, String second) {
      HashSet<String> hset1 = new HashSet<String>();
      HashSet<String> hset2 = new HashSet<String>();

      String[] firstString = first.split("\\s");
      String[] secondString = second.split("\\s");

      for (String letter : firstString) {
        letter.add(hset1);
      }

      for (String letter : secondString) {
        letter.add(hset2);
      }

      if (hset1.equals(hset2)) {
          return 0;
      }

      return 1;
    }
  
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String a = in.next();
        String b = in.next();
        numberNeeded(a, b);
        // System.out.println(numberNeeded(a, b));
    }
}
