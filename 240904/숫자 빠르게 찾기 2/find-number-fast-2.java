import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        TreeSet<Integer> ts = new TreeSet();
        int [] nums = new int[N];
        for (int i = 0; i < N; i++) ts.add(sc.nextInt());

        for (int i = 0; i < M; i++) {
            int val = sc.nextInt();
            if (ts.ceiling(val) == null) System.out.println(-1);
            else System.out.println(ts.ceiling(val));
        }
            
    } 
}