import java.util.*;
import java.util.Map.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        Map<Integer, Integer> map = new HashMap();
        while (N-- > 0) {
            int key = sc.nextInt();
            if (map.get(key) == null) map.put(key, 1);
            else map.compute(key, (k, v) -> v+1);
        }

        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((arr1, arr2) -> {
            int frequentCmp = Integer.compare(arr2[1], arr1[1]);
            if (frequentCmp != 0) return frequentCmp;
            else return Integer.compare(arr2[0], arr1[0]);
            });

        for (Entry<Integer, Integer> entry : map.entrySet()) {
            pq.offer(new int[]{entry.getKey(), entry.getValue()});
        }

        while (K-- > 0) System.out.print(pq.poll()[0] + " ");
    }
}