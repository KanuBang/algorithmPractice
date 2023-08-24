package Math;
/*
 * 시간제한: 1초 => 1억번	
 * 메모리: 256 MB
 * 입력: 
 * N(데이터 개수) M(케이스 개수)
 * arr(데이터 배열)
 * i j (i<= x <= j) 구간 1은 인덱스 0
 * 
 * 1 ≤ N ≤ 100,000
    1 ≤ M ≤ 100,000
    1 ≤ i ≤ j ≤ N
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

/*
  * 문제 분석
  1. 입력 받고
  2. 타입은 long이 좋을 듯
  3. 1억번 넘어갈 위험이 높은. O(n)이 안정적일 듯
  4. type도 왠만해서는 int 가능하나?
  */
public class Math11659 {
    public static void main(String args[]) throws IOException{
       BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
       StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
       int suNo = Integer.parseInt(stringTokenizer.nextToken());
       int quizNo = Integer.parseInt(stringTokenizer.nextToken());
       long[] s = new long[suNo +1];
    }
}
