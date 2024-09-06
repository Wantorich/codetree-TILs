import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        TreeSet<Integer> ts = IntStream.rangeClosed(1, M).boxed().collect(Collectors.toCollection(TreeSet::new));
        // System.out.println(ts);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            ts.remove(sc.nextInt());
            sb.append(ts.last()).append("\n");
        }
        System.out.println(sb.toString());
    }
}