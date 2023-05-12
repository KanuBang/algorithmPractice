package dataStructure;

import java.util.Scanner;

public class Bracket9012 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        String[] str = new String[n];
        char[] chars = new char[50];
        boolean judge = false;
        int j = 0;
        for (int i = 0; i < n; i++) {
            str[i] = scanner.next();
        }

        for (int i = 0; i < n; i++) {
            j = 0;
            for (int cnt = 0; cnt < str[i].length(); cnt++) {
                chars[j] = str[i].charAt(cnt);

                if (chars[j] == ')') {

                    if (j == 0) {

                        judge = false;
                        break;
                    }

                    if (chars[j - 1] == '(') {
                        chars[j] = ' ';
                        chars[j - 1] = ' ';
                        j--;
                        judge = true;

                    }

                    else {
                        judge = false;
                        break;
                    }
                }

                else {
                    j++;
                }

            }
            System.out.println(judge == false || chars[0] == '(' ? "NO" : "YES");

        }

    }
}
