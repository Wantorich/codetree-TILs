import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[][] matrix = new int[N][N];

        for (int [] row : matrix) Arrays.fill(row, Integer.MAX_VALUE / 2);
        for (int i = 0; i < N; i++) matrix[i][i] = 0;

        int from = 0, to = 0, cost = 0;
        for (int i = 0; i < M; i++) {
            from = sc.nextInt() - 1;
            to = sc.nextInt() - 1;
            cost = sc.nextInt();
            matrix[from][to] = Math.min(matrix[from][to], cost);
        }

        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                if (i == k) continue;
                for (int j = 0; j < N; j++) {
                    if (j == i || j == k) continue;
                    matrix[i][j] = Math.min(matrix[i][j], matrix[i][k] + matrix[k][j]);
                }
            }
        }

        for (int [] row : matrix) {
            for (int val : row) {
                if (val == Integer.MAX_VALUE / 2) System.out.print(-1 + " ");
                else System.out.print(val + " ");
            }
            System.out.println();
        }
        sc.close();
    }
}