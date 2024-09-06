import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        TreeSet<Integer> ts = new TreeSet();
        for (int i = 0; i < N; i++) {
            ts.add(sc.nextInt());
        }

        int standard = ts.first();
        int it = standard;
        int minDiff = Integer.MAX_VALUE;
        while (it < ts.last()) {
            int higher = ts.higher(it);
            if (higher - standard >= M) {
                minDiff = higher - standard;
                standard = ts.higher(standard);
                it = standard;
                continue;
            }
            it = higher;
        }
        System.out.println(minDiff);
    }
}