import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Map<String, Integer> strToIntMap = new HashMap();
        int result = 0;
        for (int i = 0; i < N; i++) {
            String str = sc.next();
            char[] charArr = str.toCharArray();
            Arrays.sort(charArr);
            String key = new String(charArr);
            int currCnt = strToIntMap.getOrDefault(key, 0);
            strToIntMap.put(key, currCnt+1);
            result = Math.max(result, currCnt+1);
        }
        System.out.println(result);
    }
}