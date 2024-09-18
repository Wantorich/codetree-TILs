import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int [] arr = new int[N];
        for (int i = 0; i < N; i++) arr[i] = sc.nextInt();

        Map<Integer, Integer> map = new HashMap();
        for (int i = 0; i < arr.length; i++) {
            for (int j = i+1; j < arr.length; j++) {
                int key = arr[i] + arr[j];
                if (key != K) continue;
                map.computeIfPresent(key, (k, v) -> v+1);
                map.computeIfAbsent(key, v -> 1);
            }
        }
        System.out.println(map.get(K));
    }
}