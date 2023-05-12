package Sort;

import java.util.*;

class Size {
    public int weight;
    public int height;
    public int rank;

    public Size(int w, int h) {
        this.weight = w;
        this.height = h;
        this.rank = 1;
    }

    public void setRank() {
        this.rank += 1;
    }

    public int getRank() {
        return this.rank;
    }

}

public class Size7568 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.next());
        Size[] mySize = new Size[n];
        int w, h = 0;

        for (int i = 0; i < n; i++) {
            w = Integer.parseInt(scanner.next());
            h = Integer.parseInt(scanner.next());
            mySize[i] = new Size(w, h);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {

                if (i == j) {
                    continue;
                }
                // 자신이 큰 경우
                else if (mySize[i].height > mySize[j].height && mySize[i].weight > mySize[j].weight) {
                    continue;
                }

                // 자신보다 큰 경우
                else if (mySize[i].height < mySize[j].height && mySize[i].weight < mySize[j].weight) {
                    mySize[i].setRank();
                    continue;
                }

            }

            System.out.println(mySize[i].getRank());
        }

    }
}