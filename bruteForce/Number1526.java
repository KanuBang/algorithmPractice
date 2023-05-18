package bruteForce;

import java.util.*;

public class Number1526 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        int max = 4;
        int cnt = 0;
        int i = 0;
        String str = "";
        while (i <= n) {
            str = i + "";
            for (int k = 0; k < str.length(); k++) {
                if (!(str.charAt(k) == '4' || str.charAt(k) == '7'))
                    cnt++;
            }
            max = cnt == 0 ? i : max;
            i++;
            cnt = 0;
        }

        System.out.println(max);
    }
}
