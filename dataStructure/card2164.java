package dataStructure;

import java.util.Scanner;

class Node {
    public int data;
    public Node next;

    Node(int data, Node next) {
        this.data = data;
        this.next = next;
    }
}

public class card2164 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        Node head = null;
        Node cur = null;

        for (int i = 0; i < n; i++) {

            if (i == 0) {
                head = new Node(n - i, null);
                cur = head;
            }

            else {
                Node newNode = new Node(n - i, null);
                cur.next = newNode;
                cur = newNode;
            }
        }

        System.out.println(head.data);
        System.out.println(head.next.data);

    }
}
