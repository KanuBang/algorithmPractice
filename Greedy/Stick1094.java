package Greedy;

import java.util.*;

public class Stick1094 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sum = 64;
        int half = 64;
        int n = Integer.parseInt(scanner.next());
        int stickCnt = 1; // 막대기가 적어도 1개는 필요하다

        while (sum > n) {
            // 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
            half /= 2;

            // sum - half는 위에서 자른 막대의 절반 중 하나를 버리고 남아있는 막대의 길이의 합이다.
            // 이 합이 n보다 작을때는 쪼개진 막대기 두개가 모두 살아남기에 결과적으로 막대기 1개가 추가된다.
            if (sum - half < n) {
                stickCnt++;
                continue;
            }

            else if (sum - half == n) {
                break;
            }

            // sum-half = n인 순간 답은 구해졌다.
            else {
                sum = sum - half;
            }
        }

        System.out.println(stickCnt);
    }
}