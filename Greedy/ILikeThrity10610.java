package Greedy;

import java.util.Scanner;

public class ILikeThrity10610 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        int[] parts = new int[6];
        int size = 0;
        boolean isExist30 = false;
        int tmp = 0;
        while (n != 0) {
            parts[size] = n % 10;
            n /= 10;
            size++;
        }

        for (int i = 0; i < size; i++) {
            if (parts[i] == 0) {
                isExist30 = true;
                break;
            }
        }

        if (isExist30 == false) {
            System.out.println(-1);
            return;
        }

        else {
            int num = 0;
            for (int i = 0; i < size - 1; i++) {
                for (int j = 0; j < size - 1 - i; j++) {
                    if (parts[j + 1] > parts[j]) {
                        tmp = parts[j + 1];
                        parts[j + 1] = parts[j];
                        parts[j] = tmp;
                    }
                }
            }

            num = Integer.parseInt(parts.toString());

            System.out.println(num);
        }

    }

}
