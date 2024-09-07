import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        TreeSet<Integer> delts = new TreeSet();
        TreeSet<Integer> dists = new TreeSet();

        for (int i = 0; i < M; i++) {
            int del = sc.nextInt();
            delts.add(del);
            int left = -1, right = N+1;
            int leftDis = 0, rightDis = 0;

            if (delts.lower(del) != null) {
                left = delts.lower(del);
            }
            if (delts.higher(del) != null) {
                right = delts.higher(del);
            }

            leftDis = del - left - 1;
            rightDis = right - del - 1;

            if (dists.size() >= 2) dists.remove(leftDis + rightDis + 1);
            dists.add(leftDis);
            dists.add(rightDis);
            System.out.println(dists.last());
        }
    }
}