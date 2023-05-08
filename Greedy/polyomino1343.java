package Greedy;

import java.util.*;

public class polyomino1343 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();
        int xCnt = 0;
        String answer = "";

        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == 'X') {
                xCnt++;
            }
        }

        // XX의 개수가 홀수나 0개면 -1
        if (xCnt % 2 == 1 || input.length() == 0) {
            System.out.println(-1);
            return;
        }

        xCnt = 0;
        for (int i = 0; i < input.length(); i++) {
            // 문자열에 .이 아예 없는 경우 처리
            // XX.XXXX에서 마지막 XXXX를 처리함
            if (i == input.length() - 1) {
                xCnt++;

                if (xCnt >= 4) {
                    answer += "AAAA".repeat(xCnt / 4);
                    xCnt = xCnt % 4;
                }

                xCnt = xCnt / 2;
                answer += "BB".repeat(xCnt);

                // ..XXXX..... 처럼 마지막이 .으로 끝날 경우 뒤에 '.'만 붙인다.
                if (input.charAt(i) == '.') {
                    answer += '.';
                }

                System.out.println(answer);
                return;
            }

            // XX.XXXX에서 .앞의 XX를 처리함
            else if (input.charAt(i) == '.') {

                // XX의 개수가 홀수나 0개면 -1
                if (xCnt % 2 == 1 || input.length() == 0) {
                    System.out.println(-1);
                    return;
                }

                if (xCnt >= 4) {
                    answer += "AAAA".repeat(xCnt / 4);
                    xCnt = xCnt % 4;
                }

                xCnt = xCnt / 2;
                answer += "BB".repeat(xCnt);
                answer += ".";
                xCnt = 0;
            }

            // XX.XXXX에서 . 이전에 몇개의 XX가 왔는지 처리함
            else {
                xCnt++;
            }
        }

    }

}