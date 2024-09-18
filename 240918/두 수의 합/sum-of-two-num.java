import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        Map<Integer, Integer> map = new HashMap();
        for (int i = 0; i < N; i++) {
            int val = sc.nextInt();
            if (map.get(val) == null) map.put(val, 1);
            else map.compute(val, (k, v) -> v+1);
        }

        int cnt = 0;
        for (Integer key : map.keySet()) {
            if (map.get(K - key) == null) continue;
            int val = map.get(key);
            if (K == key * 2) cnt += val * (val - 1);
            else cnt += val * map.get(K - key); 
        }

        System.out.println(cnt / 2);
    }
}