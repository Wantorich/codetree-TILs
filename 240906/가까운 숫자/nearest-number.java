import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        TreeSet<Integer> ts = new TreeSet();
        ts.add(0);
        int minDis = Integer.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            ts.add(num);
            if (ts.lower(num) != null) minDis = Math.min(minDis, num - ts.lower(num));
            if (ts.higher(num) != null) minDis = Math.min(minDis, ts.higher(num) - num);
            System.out.println(minDis);
        }
    }
}