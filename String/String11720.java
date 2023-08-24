package String;

import java.util.Scanner;

public class String11720 {
    public static void main() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();
        char[] sCharArr = s.toCharArray();
        long sum = 0l;

        for(int i=0; i < sCharArr.length; i++) {
            sum += sCharArr[i] - '0';
        }

        System.out.println(sum);
    }
}
