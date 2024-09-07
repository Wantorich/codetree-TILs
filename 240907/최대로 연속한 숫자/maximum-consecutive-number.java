import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        TreeSet<Integer> delts = new TreeSet();
        TreeSet<Integer> dists = new TreeSet();

        delts.add(-1); delts.add(N+1);
        for (int i = 0; i < M; i++) {
            int del = sc.nextInt();
            delts.add(del);
            int left = 0, right = 0;
            int leftDis = 0, rightDis = 0;

            left = delts.lower(del);
            right = delts.higher(del);

            leftDis = del - left - 1;
            rightDis = right - del - 1;

            if (dists.size() >= 2) dists.remove(leftDis + rightDis + 1);
            dists.add(leftDis);
            dists.add(rightDis);
            System.out.println(dists.last());
        }
    }
}