import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        TreeSet<Integer> ts = new TreeSet();
        int minDis = Integer.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            ts.add(num);
            if (ts.higher(num) != null && ts.higher(num) - num >= M) minDis = Math.min(minDis, ts.higher(num) - num);
            if (ts.lower(num) != null && num - ts.lower(num) >= M) minDis = Math.min(minDis, num - ts.lower(num));
        }
        if (minDis == Integer.MAX_VALUE) minDis = -1;
        System.out.println(minDis);
    }
}