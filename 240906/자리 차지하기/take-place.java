import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        TreeSet<Integer> ts = IntStream.rangeClosed(1, M).boxed().collect(Collectors.toCollection(TreeSet::new));
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            if (ts.floor(num) == null) break;
            int floor = ts.floor(num);
            ts.remove(floor);
            cnt++;
        }
        System.out.println(cnt);
    }
}