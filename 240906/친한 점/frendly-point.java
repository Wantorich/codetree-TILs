import java.util.*;

class Point implements Comparable<Point>{
    int r, c;

    Point (int r, int c) {
        this.r = r;
        this.c = c;
    }

    @Override
    public int compareTo(Point p) {
        int compareX = Integer.compare(this.r, p.r);
        if (compareX != 0) return compareX;
        return Integer.compare(this.c, p.c);
    }

    @Override
    public String toString() {
        return String.format("[r : %d, c: %d]", r, c);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        TreeSet<Point> ts = new TreeSet();
        for (int i = 0; i < N; i++) ts.add(new Point(sc.nextInt(), sc.nextInt()));

        for (int i = 0; i < M; i++) {
            Point p = new Point(sc.nextInt(), sc.nextInt());
            Point fp = ts.ceiling(p);
            if (fp == null) System.out.println("-1 -1");
            else System.out.println(fp.r + " " + fp.c);
        }
    }
}