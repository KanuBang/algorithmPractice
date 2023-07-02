package Greedy;

import java.util.*;

public class ATM11399 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        int[] nums = new int[n];
        int sum = 0;
        int tmp = 0;

        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(scanner.next());
        }

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (nums[j] > nums[j + 1]) {
                    tmp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = tmp;
                }
            }
        }

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i] * n;
            n--;
        }

        System.out.println(sum);
    }
}
