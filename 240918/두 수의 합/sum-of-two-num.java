import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        Set<Integer> set = new HashSet();
        while (N-- > 0) set.add(sc.nextInt());
        Integer [] arr = set.toArray(new Integer[0]);

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