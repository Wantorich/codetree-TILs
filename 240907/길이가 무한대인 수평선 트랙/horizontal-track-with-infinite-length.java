import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int [] group = new int[N];
        for (int i = 0; i < N; i++) group[i] = 1;
        int [] curr = new int[N];
        int [] accel = new int[N];
        for (int i = 0; i < N; i++) {
            curr[i] = sc.nextInt();
            accel[i] = sc.nextInt();
        }        

        TreeSet<Integer> ts = new TreeSet();
        for (int t = 1; t <= M; t++) {
            for (int i = N-1; i >= 0; i--) {
                if (group[i] == 0) continue; // 다른 누군가의 그룹에 속해있음

                int nextPos = curr[i] + accel[i];
                if (ts.floor(nextPos) == null) {
                    // 내가 누굴 추월하지 않았음
                    ts.add(nextPos);
                    curr[i] = nextPos;
                } else {
                    // 내가 i+1번째를 추월해버림
                    for (int k = i+1; k < N; k++) {
                        if (group[k] == 0) continue;
                        group[k] += group[i];
                        group[i] = 0;
                        break;
                    }
                }
            }
            ts.clear();
        }

        int result = 0;
        for (int i = 0; i < N; i++) {
            if (group[i] > 0) result++;
        }

        System.out.println(result);
    }
}