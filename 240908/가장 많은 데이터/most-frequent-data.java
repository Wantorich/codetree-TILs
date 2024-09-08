import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int result = 0;
        Map<String, Integer> map = new HashMap();
        for (int i = 0; i < N; i++) {
            String str = sc.next();
            int currCnt = map.getOrDefault(str, 0);
            map.put(str, currCnt+1);
            result = Math.max(result, currCnt+1);
        }
        System.out.println(result);
    }
}