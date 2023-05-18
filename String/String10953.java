package String;

import java.util.*;

public class String10953 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        String[] strs = new String[n];

        for (int i = 0; i < n; i++) {
            strs[i] = scanner.next();
        }

        for (int i = 0; i < n; i++) {
            System.err.println(Integer.parseInt(Character.toString(strs[i].charAt(0)))
                    + Integer.parseInt(Character.toString(strs[i].charAt(2))));
        }
    }
}
