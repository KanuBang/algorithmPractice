package String;

import java.util.*;

public class WordStudy1157 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[26]; // 영문자의 개수는 26개
        String str = scanner.next();

        for (int i = 0; i < str.length(); i++) {
            if ('A' <= str.charAt(i) && str.charAt(i) <= 'Z') {
                arr[str.charAt(i) - 'A']++;
            }

            else {
                arr[str.charAt(i) - 'a']++;
            }
        }

        int max = -1;
        char ch = '?';

        for (int i = 0; i < 26; i++) {
            if (arr[i] > max) {
                max = arr[i];
                ch = (char) (i + 65);
            }

            else if (arr[i] == max) {
                ch = '?';
            }
        }

        System.out.println(ch);
    }
}
