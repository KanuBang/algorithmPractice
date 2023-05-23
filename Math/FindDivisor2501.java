package Math;
import java.util.Scanner;

public class FindDivisor2501 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        int k = Integer.parseInt(scanner.next());        
        int cnt = 0;
        for(int i=1; i <= n; i++) {
            if(n % i == 0) {
                cnt++;
            }

            if(cnt == k) {
                System.out.println(i);
                return;
            }
        }

        System.out.println(0);
    }
}

/*
 * 
 * 1. n과 k를 입력받는다
 * 2. for문으로 n을 1부터 n까지 나눈다.
 * 3. n이 0으로 나누어 떨어지면 약수다
 * 4. 그 변경한 횟수가 3이 되면 out하고 출력한다
 * 5. 변경한 횟수가 k에 도달하지 못하면 0을 출력한다.
 */
