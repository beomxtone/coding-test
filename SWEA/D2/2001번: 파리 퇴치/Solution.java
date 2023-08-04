import java.util.Scanner;

public class Solution {
    public static int solve(int x, int y, int[][] board, int M) {
        int res = 0;
        for (int i = x; i < x + M; i++) {
            for (int j = y; j < y + M; j++) {
                res += board[i][j];
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        for (int TC = 1; TC <= T; TC++) {
            int N = scanner.nextInt();
            int M = scanner.nextInt();
            int[][] board = new int[N][N];
            int ans = 0;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    board[i][j] = scanner.nextInt();
                }
            }

            for (int i = 0; i < N - M + 1; i++) {
                for (int j = 0; j < N - M + 1; j++) {
                    ans = Math.max(ans, solve(i, j, board, M));
                }
            }

            System.out.println("#" + TC + " " + ans);
        }
    }
}
