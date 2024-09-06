import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TreeSet<Integer> ts = new TreeSet();
        int N = sc.nextInt();
        int M = sc.nextInt();
        for (int i = 0; i < N; i++) ts.add(sc.nextInt());
        for (int i = 0; i < M; i++) {
            int num = sc.nextInt();
            if (ts.floor(num) != null) {
                int delVal = ts.floor(num);
                System.out.println(delVal);
                ts.remove(delVal);
            } else System.out.println(-1);
        }
    }
}