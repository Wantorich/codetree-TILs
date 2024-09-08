import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        Map<String, Integer> strToIntMap = new HashMap();
        Map<Integer, String> intToStrMap = new HashMap();
        for (int i = 0; i < N; i++) {
            String str = sc.next();
            strToIntMap.put(str, i+1);
            intToStrMap.put(i+1, str);
        }
        for (int i = 0; i < M ; i++) {
            String input = sc.next();
            if (Character.isDigit(input.charAt(0))) 
                System.out.println(intToStrMap.get(Integer.parseInt(input)));
            else 
                System.out.println(strToIntMap.get(input));
        }
    }
}