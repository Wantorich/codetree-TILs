import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        TreeSet<Integer> ts = new TreeSet();

        for (int i = 0; i < N; i++) {
            String [] command = sc.nextLine().split(" ");
            if (command.length == 2) {
                int val = Integer.parseInt(command[1]);
                switch (command[0]) {
                    case "add" :
                        ts.add(val); break;
                    case "find" :
                        if (ts.contains(val)) System.out.println("true");
                        else System.out.println("false");
                        break;
                    case "remove" :
                        ts.remove(val);
                        break;
                    case "lower_bound" :
                        if (ts.ceiling(val) == null) System.out.println("None");
                        else System.out.println(ts.ceiling(val));
                        break;
                    case "upper_bound" :
                        if (ts.higher(val) == null) System.out.println("None");
                        else System.out.println(ts.higher(val));
                        break;
                }
            }
            else {
                if (ts.isEmpty()) {
                    System.out.println("None");
                    continue;
                }

                switch (command[0]) {
                    case "largest" :
                        System.out.println(ts.last());
                        break;
                    case "smallest" :
                        System.out.println(ts.first());
                        break;
                }
            }
        }
    } 
}