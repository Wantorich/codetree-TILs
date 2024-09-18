import java.util.*;
import java.util.Map.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int [][] arr = new int[4][N];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        Map<Integer, Integer> map1 = new HashMap();
        Map<Integer, Integer> map2 = new HashMap();

        for (int i = 0; i < N; i++) {
            int val1 = arr[0][i];
            int val2 = arr[2][i];
            for (int j = 0; j < N; j++) {
                int key1 = val1 + arr[1][j];
                int key2 = val2 + arr[3][j];

                if (map1.get(key1) == null) map1.put(key1, 1);
                else map1.compute(key1, (k, v) -> v+1);

                if (map2.get(key2) == null) map2.put(key2, 1);
                else map2.compute(key2, (k, v) -> v+1);
            }
        }

        int ans = 0;
        for (Entry<Integer, Integer> entry : map1.entrySet()) {
            int a = entry.getKey();
            if (map2.get(-a) != null) {
                ans += entry.getValue() * map2.get(-a);
            }
        }

        System.out.println(ans);
    }
}