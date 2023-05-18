package dataStructure;

import java.util.Scanner;

class Node1 {
    public int data;
    public Node1 right;
    public Node1 left;

    Node1(int data, Node1 right, Node1 left) {
        this.data = data;
        this.right = right;
        this.left = left;
    }
}

public class rtrt {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        if (n == 2) {
            System.out.println(1);
            return;
        }
        Node1 head = null;
        Node1 cur = null;
        Node1 tail = null;
        Node1 nextTail = null;
        int tmp = 0;

        for (int i = 0; i < n; i++) {
            if (i == 0) {
                head = new Node1(n - i, null, head);
                cur = head;
            }

            else {
                Node1 newNode = new Node1(n - i, null, null);
                cur.right = newNode;
                newNode.left = cur;
                cur = newNode;
            }

        }

        // 6 5 4 3 2 1
        // 6 5 4 3 2
        // 6 5 4 3
        // 2 6 5 4 3
        // =>=> 1 2

        // 2 6 5 4 3
        // 2 6 5 4
        // 2 6 5
        // 4 2 6 5
        // => => 3 4

        // 4 2 6 5
        // 4 2 6
        //
        // 6 5 4 3 2 1
        // 2 6 5 4 3
        // 4 2 6 5
        // 6 4 2
        // 4 6
        tail = cur;
        while (n > 1) {
            nextTail = tail.left;
            nextTail.right = null; // head 6 5 4 3 2
            // System.out.printf("wad tail %d\n", tail.data);

            tail = nextTail;
            nextTail = tail.left;
            nextTail.right = null; // head 6 5 4 3
            // System.out.printf("fake tail %d\n", tail.data);
            Node1 insertNode = new Node1(tail.data, null, null);
            insertNode.right = head;
            head = insertNode;
            insertNode.left = head;
            insertNode.right.left = insertNode; // head 2 6 5 4 3

            /*
             * Node1 pr = head;
             * while (pr.right != null) {
             * System.out.printf("%d ", pr.data);
             * pr = pr.right;
             * }
             */
            tail = nextTail;
            n--;
        }

        System.out.println(head.data);

    }
}
