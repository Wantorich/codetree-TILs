import java.util.*;

class Problem implements Comparable<Problem>{
    int num, level;

    Problem (int num, int level) {
        this.num = num;
        this.level = level;
    }

    @Override
    public int compareTo(Problem p) {
        int compareLevel = Integer.compare(this.level, p.level);
        if (compareLevel != 0) return compareLevel;
        return Integer.compare(this.num, p.num);
    }

    @Override
    public String toString() {
        return String.format("[num : %d, level: %d]", num, level);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TreeSet<Problem> ts = new TreeSet();
        int N = sc.nextInt();
        for (int i = 0; i < N; i++) ts.add(new Problem(sc.nextInt(), sc.nextInt()));

        int M = sc.nextInt();
        for (int i = 0; i < M; i++) {
            switch (sc.next()) {
                case "ad":
                    ts.add(new Problem(sc.nextInt(), sc.nextInt()));
                    break;
                case "sv":
                    Problem p = new Problem(sc.nextInt(), sc.nextInt());
                    ts.remove(ts.floor(p));
                    break;
                case "rc":
                    int x = sc.nextInt();
                    if (x == 1) System.out.println(ts.last().num);
                    else System.out.println(ts.first().num);
            }
        }
    }
}