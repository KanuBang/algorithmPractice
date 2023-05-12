package dataStructure;

import java.util.Scanner;

class myNode {
    public int data;
    public myNode next;

    myNode(int data, myNode next) {
        this.data = data;
        this.next = next;
    }
}

public class My11866 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        int k = Integer.parseInt(scanner.next());
        int cnt = 0;
        int size = n;
        String answer = "";
        myNode cur = null;
        myNode head = null;
        myNode before = null;
        // 1 2 3 4 5 6 7 원형 연결 리스트 생성
        for (int i = 0; i < n; i++) {

            if (i == 0) {
                head = new myNode(i + 1, null);
                cur = head;
            }

            else {
                myNode newNode = new myNode(i + 1, null);
                cur.next = newNode;
                cur = newNode;
            }

            if (i == n - 1) {
                cur.next = head;
            }
        }

        answer = "<";
        if (k == 1) {
            cur = head;
            while (cnt != n) {
                if (cnt != n - 1) {
                    answer += cur.data + ", ";
                }

                else {
                    answer += cur.data + ">";
                }
                cur = cur.next;
                cnt++;
            }
            System.out.println(answer);
            return;
        }

        while (true) {
            before = cur;
            cur = cur.next;
            cnt++;

            if (cnt == k) {
                // System.out.println(cur.data);
                if (size == 1) {
                    answer += cur.data + ">";
                } else {
                    answer += cur.data + ", ";
                }
                before.next = cur.next;
                cur = cur.next;
                cnt = 1;
                size--;
            }

            if (size == 0) {
                break;
            }
        }

        System.out.println(answer);

    }
}
