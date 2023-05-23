package Math;
import java.util.Scanner;


public class FindPrimeNumber1978 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        int[] nums = new int[n];
        int cnt = 0;
        int pCnt = 0;

        for(int i =0; i < n ;i++) {
            nums[i] = Integer.parseInt(scanner.next());
        }


        for(int i=0; i<n; i++) {
            for(int j=1; j <= nums[i]; j++){
                if(nums[i] % j == 0) {
                    cnt++;
                    
                }
            }
            
            if(cnt == 2) {
                pCnt++;
            }
            cnt = 0;
        }

        System.out.println(pCnt);
        
    }
}
