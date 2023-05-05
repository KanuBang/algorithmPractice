package bruteForce;

import java.util.*;

public class candyGame3085 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = 0;
        char tmp = 'a';
        n = Integer.parseInt(scanner.nextLine());
        // 그 전 까지는 nextInt를 썻는데 이러면 일일이 개행 문자를 처리해야한다.
        // 차리리 nextLine으로 바교 parsing을하자

        String[] inputs = new String[n];
        char[][] array2D = new char[n][n];

        // 입력 받기
        for (int i = 0; i < n; i++) {
            inputs[i] = scanner.nextLine();

        }

        // 2D Array로변환

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                array2D[i][j] = inputs[i].charAt(j);
            }
        }


        // 2D array 출력 테스트
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.printf("%c ", array2D[i][j]);
            }

            System.out.println();
        }

        // 2D array -> 방향으로 인접이 다르면 위치를 바꾼다
        int sameCnt = 0;
        int max = 0;
        for (int i = 0; i < n; i++) {
            // 2D array -> 방향으로 인접이 다르면 위치를 바꾼다
            for (int j = 0; j < n-1; j++) {
                if(array2D[i][j] != array2D[i][j+1]) {
                    tmp = array2D[i][j];
                    array2D[i][j] = array2D[i][j+1];
                    array2D[i][j+1] = tmp;
                }

            }
            if(sameCnt > max) {
                max = sameCnt;
            }
        }
    }

    public int searchRow(char[][])
}
