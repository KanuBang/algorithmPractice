package Greedy;

import java.util.*;

public class UNSOLVEDNumberSort2751 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[1000000];
        int size = Integer.parseInt(scanner.next());

        int tmp = 0;

        for (int i = 0; i < size; i++) {
            arr[i] = Integer.parseInt(scanner.next());
        }

        for (int i = 0; i < size - 1; i++) {
            for (int j = 0; j < size - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    tmp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = tmp;
                }
            }
        }

        for (int i = 0; i < size; i++) {
            System.out.println(arr[i]);
        }
    }
}