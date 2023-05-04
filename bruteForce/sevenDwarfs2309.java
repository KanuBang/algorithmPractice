package bruteForce;

import java.util.*;

public class sevenDwarfs2309 {
    public static void main(String[] args) {
        Scanner scanf = new Scanner(System.in);
        int[] nineDwarfs = new int[9];
        int tmp = 0;
        int sum = 0;
        int findingIndex1 = 0;
        int findingIndex2 = 0;

        // 9개의 숫자를 입력 받는다.
        // 총 합을 구한다.
        for (int i = 0; i < nineDwarfs.length; i++) {
            nineDwarfs[i] = scanf.nextInt();
            sum += nineDwarfs[i];
        }

        // 버블 정렬로 정렬한다.
        // 정렬은 됬음
        for (int i = 0; i < nineDwarfs.length - 1; i++) {
            for (int j = 0; j < nineDwarfs.length - i - 1; j++) {
                if (nineDwarfs[j] > nineDwarfs[j + 1]) {
                    tmp = nineDwarfs[j];
                    nineDwarfs[j] = nineDwarfs[j + 1];
                    nineDwarfs[j + 1] = tmp;
                }
            }
        }

        for (int i = 0; i < nineDwarfs.length; i++) {
            for (int j = i + 1; j < nineDwarfs.length; j++) {
                if (nineDwarfs[i] + nineDwarfs[j] == sum - 100) {
                    findingIndex1 = i;
                    findingIndex2 = j;
                    break;
                }
            }

            if (findingIndex1 != findingIndex2) {
                break;
            }
        }

        for (int i = 0; i < nineDwarfs.length; i++) {
            if (i == findingIndex1 || i == findingIndex2) {
                continue;
            }
            System.out.println(nineDwarfs[i]);
        }
    }
}

/*
 * 9개의 숫자를 입력받는다.
 * 숫자를 정렬한다.
 * 더해가며 100이 되면 탈출한다.
 * 그때의 인덱스 값으로 출력한다.
 */