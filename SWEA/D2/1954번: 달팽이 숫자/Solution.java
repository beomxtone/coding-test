import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(st.nextToken());
        // 오른쪽, 아래쪽, 왼쪽, 위쪽
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};

        for (int tc = 1; tc < t+1; tc++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int[][] ans = new int[n][n];

            int num = 1; // 채울 숫자
            int dir = 0; // 방향
            int x = 0, y = -1;

            while (num <= n * n) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (nx >= 0 && nx < n && ny >= 0 && ny < n && ans[nx][ny] == 0) {
                    ans[nx][ny] = num;
                    num += 1;
                    x = nx;
                    y = ny;
                } else {
                    dir = (dir + 1) % 4;
                }
            }

            System.out.println("#" + tc);
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.print(ans[i][j] + " ");
                }
                System.out.println();
            }
        }

    }
}