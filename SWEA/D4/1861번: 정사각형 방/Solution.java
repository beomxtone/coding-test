import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Solution {
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int N;

    static int bfs(int row, int col, int[][] arr, boolean[][] visited) {
        int cnt = 1;
        visited[row][col] = true;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{row, col});

        while (!queue.isEmpty()) {
            int[] element = queue.poll();
            int x = element[0], y = element[1];
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
                    if (arr[nx][ny] == arr[x][y] + 1) {
                        cnt += 1;
                        visited[nx][ny] = true;
                        queue.add(new int[]{nx, ny});
                    }
                }
            }
        }

        return cnt;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int TC = 1; TC < T+1; TC++) {
            N = Integer.parseInt(br.readLine());
            int[][] rooms = new int[N][N];

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    rooms[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int roomNum = Integer.MAX_VALUE, count = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    // visited 초기화
                    boolean[][] visited = new boolean[N][N];
                    int res = bfs(i, j, rooms, visited);

                    if (res >= count) {
                        // count가 같을 때, 방에 적힌 수가 크면 넘기고, 작으면 정답 갱신
                        if (res == count && rooms[i][j] > roomNum) continue;
                        roomNum = rooms[i][j];
                        count = res;
                    }
                }
            }

            System.out.println("#" + TC + " " + roomNum + " " + count);
        }

        br.close();
    }
}
