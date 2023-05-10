package dataStructure;

import java.util.Scanner;

// 1 3 5 4 0 0 7 0 0 6 
// 1 3 5 4 (0 i = 4 
// 1 3 5 0 
public class zero10773 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        int number = 0;
        int sum = 0;
        int[] stack = new int[n];
        int cnt = 0;
        int i = 0;
        while (cnt < n) {
            number = Integer.parseInt(scanner.next());
            if (number == 0) {
                i--;
                stack[i] = 0;
            }

            else {
                stack[i] = number;
                i++;
            }

            cnt++;
        }

        for (int j = 0; j < i; j++) {
            sum += stack[j];
        }

        System.out.println(sum);

    }
}
