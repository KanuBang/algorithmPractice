package dataStructure;

import java.util.*;

class Node {
    int data;
    Node nextNode;

    Node(int data, Node nextNode) {
        this.data = data;
        this.nextNode = nextNode;
    }
}

public class stack10828 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int orders = Integer.parseInt(scanner.next());
        String myOrder = "";
        int top = 0;
        int size = 0;
        Node head = new Node(null, null);

        for (int i = 0; i < orders; i++) {
            myOrder = scanner.next();

            // push
            if (myOrder.charAt(0) == 'u') {

            }

            // top
            else if (myOrder.charAt(0) == 't') {

            }

            else if (myOrder.charAt(0) == 's') {

            }
        }

    }

}
