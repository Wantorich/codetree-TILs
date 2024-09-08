import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Map<Integer, Integer> map = new HashMap();
        for (int i = 0; i < N; i++) {
            switch (sc.next()) {
                case "add" :
                    map.put(sc.nextInt(), sc.nextInt());
                    break;
                case "find" :
                    int key = sc.nextInt();
                    if (map.containsKey(key)) System.out.println(map.get(key));
                    else System.out.println("None");
                    break;
                case "remove":
                    map.remove(sc.nextInt());
            }
        }
    }
}