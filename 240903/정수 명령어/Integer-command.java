import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();

        for (int t = 1; t <= tc; t++) {
            int N = sc.nextInt();
            sc.nextLine();
            TreeSet<Integer> ts = new TreeSet();

            for (int i = 0; i < N; i++) {
                String [] command = sc.nextLine().split(" ");
                int val = Integer.parseInt(command[1]);
                switch (command[0]) {
                    case "I" :
                        ts.add(val); break;
                    case "D" :
                        if (ts.isEmpty()) break;
                        if (val > 0) ts.remove(ts.last());
                        else  ts.remove(ts.first());
                        break;
                }
            }

            if (ts.isEmpty()) System.out.println("EMPTY");
            else System.out.printf("%d %d\n", ts.last(), ts.first());
        }
    } 
}