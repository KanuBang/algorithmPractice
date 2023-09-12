package Implement;

import java.util.Scanner;

public class Implement4470 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        String[] ans = new String[n];
        for(int i = 0; i < n; i++) {
            ans[i] = sc.nextLine();
        }
        for(int i = 0; i < n; i++) {
            System.out.printf("%d: %s\n",(i+1), ans[i]);
        }

    }
}