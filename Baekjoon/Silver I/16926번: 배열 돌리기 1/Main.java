import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/*
1. summary: 배열을 한 칸씩 왼쪽으로 회전
2. strategy: 정직하고 건실하게 구현
3. note: swap 꼼수는 편하다
*/
public class Main {
    static int[][] arr;

    static int swap(int a, int b) {
        return a;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        arr = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < r; i++) {
            int repeat = Math.min(n, m) / 2;

            // repeat 만큼 사각형 안으로 들어가면서 회전
            for (int j = 0; j < repeat; j++) {
                int x = j, y = j;
                int val = arr[x][y];

                // 왼쪽
                for (int k = x+1; k < n-j; k++) {
                    arr[k][j] = swap(val, val = arr[k][j]);
                }

                // 아래쪽
                for (int k = y+1; k < m-j; k++) {
                    arr[n-j-1][k] = swap(val, val = arr[n-j-1][k]);
                }

                // 오른쪽
                for (int k = n-j-2; k >= j; k--) {
                    arr[k][m-j-1] = swap(val, val = arr[k][m-j-1]);
                }

                // 위쪽
                for (int k = m-j-2; k >= j; k--) {
                    arr[j][k] = swap(val, val = arr[j][k]);
                }
            }
        }

        for (int[] ar : arr) {
            for (int val : ar) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }
}
