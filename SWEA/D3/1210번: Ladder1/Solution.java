import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static boolean go(int[][] arr, int x, int y, boolean isBeforeLeft, boolean isBeforeRight) {
        if (x == 99) {
            if (arr[x][y] == 2) return true;
            else return false;
        }

        int dx = x, dy = y;
        if (y-1 > -1 && arr[x][y-1] == 1 && !isBeforeRight) {
            isBeforeLeft = true;
            dy -= 1;
        } else if (y+1 < 100 && arr[x][y+1] == 1 && !isBeforeLeft) {
            isBeforeRight = true;
            dy += 1;
        } else {
            isBeforeLeft = false;
            isBeforeRight = false;
            dx += 1;
        }

        return go(arr, dx, dy, isBeforeLeft, isBeforeRight);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int t = 0; t < 10; t++) {

            int tc = Integer.parseInt(br.readLine());
            int[][] board = new int[100][];

            for (int i = 0; i < 100; i++) {
                board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            }

            for (int i = 0; i < 100; i++) {
                if (board[0][i] == 1) {
                    if (go(board, 0, i, false, false)) {
                        System.out.println("#" + tc + " " + i);
                        break;
                    }
                }
            }

        }
    }
}
