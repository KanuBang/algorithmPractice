package dataStructure;

import java.util.*;

public class Clothes26558 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[3];
        int tmp = 0;

        for (int i = 0; i < 3; i++) {
            arr[i] = Integer.parseInt(scanner.next());
        }

        for (int i = 0; i < 3 - 1; i++) {
            for (int j = 0; j < 3 - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    tmp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = tmp;
                }
            }
        }

        System.out.println(arr[1]);
    }
}
