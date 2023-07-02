package Greedy;

import java.util.*;

public class change5585 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int change = 1000 - Integer.parseInt(scanner.nextLine());
        int[] myCoins = { 500, 100, 50, 10, 5, 1 };
        int cnt = 0;
        // 620 = 500 + 100 + 10 + 10

        for (int i = 0; i < myCoins.length; i++) {
            while (change / myCoins[i] != 0) {
                cnt++;
                change = change - myCoins[i];
            }
        }

        System.out.println(cnt);
    }
}