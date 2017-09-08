/*Objective 
Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

Note:  is considered to be an even index.

Input Format

The first line contains an integer,  (the number of test cases). 
Each line  of the  subsequent lines contain a String, .

Constraints

Output Format

For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed characters.

Sample Input

2
Hacker
Rank
Sample Output

Hce akr
Rn ak
Explanation

Test Case 0:  
 
 
 
 
 
 
The even indices are , , and , and the odd indices are , , and . We then print a single line of  space-separated strings; the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices ().

Test Case 1:  
 
 
 
 
The even indices are  and , and the odd indices are  and . We then print a single line of  space-separated strings; the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices ().
*/
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in); 
        
        int n = scan.nextInt();
        scan.nextLine();
        
        for (int i = 0; i < n; i++) {
            String str = scan.nextLine();
            String[] splitStr = str.split("");
            String even = "";
            String odd = "";
            
            for (int j = 0; j < splitStr.length; j++) {
                if(j % 2 == 0) {
                    even += splitStr[j];
                }
                else {
                    odd += splitStr[j]; 
                }
            }
            System.out.println(even + " " + odd);
        }
    }
}