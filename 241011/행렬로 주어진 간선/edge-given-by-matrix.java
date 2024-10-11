import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int [][] matrix = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                matrix[i][j] = sc.nextInt();
                if (i == j) matrix[i][j] = 1;
            }
        }

        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                if (i == k) continue;
                for (int j = 0; j < N; j++) {
                    if (i == j || j == k) continue;
                    if (matrix[i][k] == 1 && matrix[k][j] == 1)
                        matrix[i][j] = 1;
                }
            }
        }

        for (int [] row : matrix) {
            for (int val : row) System.out.print(val + " ");
            System.out.println();
        }
        sc.close();
    }
}