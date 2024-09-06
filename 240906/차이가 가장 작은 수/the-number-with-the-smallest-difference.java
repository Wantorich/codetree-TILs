import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int [] nums = new int[N];
        TreeSet<Integer> ts = new TreeSet();
        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            nums[i] = num;
            ts.add(num);
        }

        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            int curr = nums[i];
            if (ts.ceiling(curr + M) != null) minDiff = Math.min(minDiff, ts.ceiling(curr + M) - curr);
            if (ts.floor(curr - M) != null) minDiff = Math.min(minDiff, curr - ts.floor(curr - M));
        }
        if (minDiff == Integer.MAX_VALUE) minDiff = -1;
        System.out.println(minDiff);
    }
}