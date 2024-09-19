import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        TreeMap<Integer, Integer> tmap = new TreeMap();
        while (N-- > 0) {
            switch (sc.next()) {
                case "add" :
                    tmap.put(sc.nextInt(), sc.nextInt());
                    break;
                case "find" :
                    int key = sc.nextInt();
                    if (tmap.get(key) == null) System.out.println("None");
                    else System.out.println(tmap.get(key));
                    break;
                case "remove" :
                    tmap.remove(sc.nextInt());
                    break;
                case "print_list" :
                    if (tmap.isEmpty()) {
                        System.out.println("None");
                        break;
                    }
                    for (Integer value : tmap.values())
                        System.out.print(value + " ");
                    System.out.println();
            }
        }
    }
}