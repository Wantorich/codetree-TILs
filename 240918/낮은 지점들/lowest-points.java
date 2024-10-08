import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Map<Integer, Integer> hmap = new HashMap();
        while (N-- > 0) {
            int key = sc.nextInt();
            int value = sc.nextInt();
            // if (!hmap.containsKey(key)) hmap.put(key, value);
            // else hmap.compute(key, (k, v) -> value < v ? value : v);
            hmap.computeIfPresent(key, (k, v) -> value < v ? value : v);
            hmap.computeIfAbsent(key,  (v) -> value);
        }
        System.out.println(hmap.values().stream().mapToLong(v -> v).sum());
    }
}