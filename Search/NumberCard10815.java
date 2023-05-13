package Search;

import java.util.*;

public class NumberCard10815 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n, m = 0;
        int tmp = 0;

        // input
        n = Integer.parseInt(scanner.next());
        int[] cards = new int[n];
        for (int i = 0; i < n; i++) {
            cards[i] = Integer.parseInt(scanner.next());
        }

        m = Integer.parseInt(scanner.next());
        int[] myCards = new int[m];
        for (int i = 0; i < m; i++) {
            myCards[i] = Integer.parseInt(scanner.next());
        }

        // sort for binary search
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (cards[j] > cards[j + 1]) {
                    tmp = cards[j];
                    cards[j] = cards[j + 1];
                    cards[j + 1] = tmp;
                }
            }
        }

        // binary search
        int d, start, mid, end = 0;

        for (int i = 0; i < m; i++) {
            boolean result = false;
            int msg = 0;
            d = myCards[i];
            start = 0;
            end = cards.length - 1;

            while (start <= end) {
                mid = (start + end) / 2 / 1;

                if (cards[mid] == d) {
                    result = true;
                    break;
                }

                else if (d > cards[mid]) {
                    start = mid + 1;
                }

                else {
                    end = mid - 1;
                }
            }
            msg = result == true ? 1 : 0;
            System.out.println(msg);
        }

    }
}
