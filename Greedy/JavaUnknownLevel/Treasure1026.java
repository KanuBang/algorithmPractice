package Greedy;

import java.util.Scanner;

public class Treasure1026 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        int[] a = new int[n];
        int[] b = new int[n];
        int tmp = 0;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(scanner.next());
        }

        for (int i = 0; i < n; i++) {
            b[i] = Integer.parseInt(scanner.next());
        }

        for (int i = 0; i < n - 1; i++) {

            for (int j = 0; j < n - 1 - i; j++) {
                if (a[j] > a[j + 1]) {
                    tmp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = tmp;
                }

                if (b[j] < b[j + 1]) {
                    tmp = b[j];
                    b[j] = b[j + 1];
                    b[j + 1] = tmp;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            sum += a[i] * b[i];
        }

        System.out.println(sum);
    }

}
