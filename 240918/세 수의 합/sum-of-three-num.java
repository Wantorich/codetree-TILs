import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        Map<Integer, Integer> map = new HashMap();
        int [] arr = new int[N];

        for (int i = 0; i < N; i++) arr[i] = sc.nextInt();

        int ans = 0;
        for (int i = 0; i < arr.length; i++) {
            if (map.get(K - arr[i]) != null) {
                ans += map.get(K - arr[i]);
            }

            for (int j = 0; j < i; j++) {
                int key = arr[i] + arr[j];
                if (map.get(key) == null) map.put(key, 1);
                else map.compute(key, (k, v) -> v+1);
            }
        }

        System.out.println(ans);
    }
}