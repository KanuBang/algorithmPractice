package Math;
import java.util.Scanner;
/*
 * 시간 제한 2초 => 2억번
 * 메모리 128MB
 * 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다. 둘째 줄에 세준이의 현재 성적이 주어진다. 
 * 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
 * 첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.
 */

 /*
  * 문제 분석
  모든 점수를 입력받고
  A / M * 100 + B / M * 100 + C / M * 100을 하면 된다.
  분배 법칙을 사용하면
  (A + B + C) / M * 100 이다.
  그리고 평균을 구해야 하므로 
  (A+ B + C) / M / 3 * 100이다.
  */

  /*
   * 슈도 코드
   ! 단순 접근 이므로 배열을 사용할 것.
   
   1. 과목 수 입력 (int)
   2. 점수를 입력 받고 배열에 저장 (int)
   3. 합 구하기 (long), 최댓갑 구하기(int)
   4. 평균 구하기 (double)
   5. 출력
   */
public class Math1564 {
    public static void main (String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] subs = new int[n];
        for(int i = 0; i < subs.length; i++) {
            subs[i] = sc.nextInt();
        }

        long sum = 0l;
        int max = 0;
        double fakeAvg = 0;
        for(int i = 0; i < subs.length; i++) {
            if(subs[i] > max) {
                subs[i] = max;
            }
            sum += subs[i];
        }

        fakeAvg = (double)sum / max / n * 100;
        System.out.println(fakeAvg);
    }
}