package Greedy;

import java.util.*;

public class CupHolder2810 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.next());
        String row = scanner.next();
        int cupHolders = 2;
        int cntL = 0;

        for (int i = 0; i < row.length(); i++) {
            if (i == row.length() - 1) {
                break;
            }

            else if (row.charAt(i) == 'S') {
                cupHolders += 1;
            }

            else if (row.charAt(i) == 'L') {
                cntL++;

                if (cntL == 2) {
                    cupHolders += 1;
                    cntL = 0;
                }

                else {
                    continue;
                }
            }
        }

        System.out.println(cupHolders >= n ? n : cupHolders);
    }
}
