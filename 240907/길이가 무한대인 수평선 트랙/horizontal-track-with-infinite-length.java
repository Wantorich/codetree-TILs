import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        long [] curr = new long[N];
        long [] accel = new long[N];
        for (int i = 0; i < N; i++) {
            curr[i] = sc.nextLong();
            accel[i] = sc.nextLong();
        }        

        TreeSet<Long> ts = new TreeSet();
        for (int i = N-1; i >= 0; i--) {
            long nextPos = curr[i] + accel[i] * M;
            if (ts.floor(nextPos) == null) {
                // 내가 누굴 추월하지 않았음
                ts.add(nextPos);
                curr[i] = nextPos;
            } 
        }

        System.out.println(ts.size());
    }
}