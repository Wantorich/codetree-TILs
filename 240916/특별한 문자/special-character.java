import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        HashMap<Character, Integer> map = new HashMap();
        for (int i = 0; i < str.length(); i++) {
            char key = str.charAt(i);
            if (map.containsKey(key)) map.put(key, -1);
            else map.put(key, i);
        }
        int minIdx = str.length();
        String result = "None";
        for (char key : map.keySet()) {
            if (map.get(key) == -1) continue;
            if (map.get(key) < minIdx) {
                minIdx = map.get(key);
                result = "" + key;
            }
        }
        System.out.println(result);
    }
}