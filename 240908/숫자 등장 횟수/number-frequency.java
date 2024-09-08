import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        Map<Integer, Integer> map = new HashMap();
        for (int i = 0; i < N; i++) {
            int k = sc.nextInt();
            int currCnt = map.getOrDefault(k, 0);
            map.put(k, currCnt+1);
        }

        for (int i = 0; i < M; i++) {
            System.out.print(map.getOrDefault(sc.nextInt(), 0) + " ");
        }
    }
}