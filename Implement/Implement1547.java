package Implement;
/*
 * 1. m을 입력받는다
2. m에 따른 입력을 9번 받는다
3. 입력에 현재 공 컵이 있다면 컵을 바꾼다
4. 입력에 현재 공 컵이 없다면 그냥 진행한다.
 */

import java.util.Scanner;

public class Implement1547 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = Integer.parseInt(scanner.next());
        //int[][] arr = new int[m][2];
        int x = 0;
        int y = 0;
        int ans = 1;
        
        for(int i =0; i < m; i++) {
            x = Integer.parseInt(scanner.next());
            y = Integer.parseInt(scanner.next());

            if(x == ans) {
                ans = y;
            }
            
            else if(y == ans) {
                ans = x;
            }

            else {
                continue;
            }
        }

        System.out.println(ans);
    }
}

/*
 * 의사코드
 * 컵1, 컵2, 컵3
 * 컵1에 공을 하나 넣는다
 * 두 컵을 고른다
 * 위치를 바꾼다
 * 
 * 컵의 위치를 M번 바꿀 것, 컵의 위치는 바꾼 방법이 입력으로 주어진다
 * M번 바꾼 이후에 공이 들어있는 컵의 번호를 구하자
 * 
 * 출력: 공이 들어있는 컵의 번호를 출력한다
 * 공이 사라져서 컵 밑에 없는 경우에는 -1을 출력한다
 * 
 * 
 * 
 * 4
 * 
 * 
 * 예시
 * 9
1 2 => 2
3 2 => 3
1 2 => 3
2 1 => 3
2 1 => 3
3 2 => 2
1 3 => 2
3 1 => 2
1 2 => 1


1. m을 입력받는다
2. m에 따른 입력을 9번 받는다
3. 입력에 현재 공 컵이 있다면 컵을 바꾼다
4. 입력에 현재 공 컵이 없다면 그냥 진행한다.
 * 
 */
