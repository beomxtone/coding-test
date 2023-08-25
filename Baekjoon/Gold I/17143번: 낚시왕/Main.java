import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;
/*
 1. 낚시왕은 오른쪽으로 한 칸씩 이동하며, 같은 열 & 작은 행의 상어를 한 마리 잡는다.
 2. 상어는 주어진 속력에 따라 칸을 이동, 벽을 마주치면 반대 방향으로 이동한다.
 3. 이동이 끝난 후, 한 칸에 둘 이상의 상어가 있으면 가장 큰 상어만 남는다.
 4. 낚시왕이 잡는 상어 크기의 합을 출력
 */
class Point {   // 상어의 (x, y) 좌표를 key값으로 하는 dictionary 사용하기 위한 class
    int x, y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Point point = (Point) o;
        return x == point.x && y == point.y;
    }

    @Override
    public int hashCode() {
        return x * 31 + y;
    }
}

public class Main {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] graph = new int[r][c];

        Map<Integer, int[]> sharks = new HashMap<>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());

            graph[x-1][y-1] = z;
            sharks.put(z, new int[]{x-1, y-1, s, d});
        }

        int fisher = -1;
        List<Integer> catched = new ArrayList<>();

        while (fisher+1 < c) {
            // 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
            fisher++;

            // 2. 낚시왕이 있는 열에 있는 상어 중, 땅과 제일 가까운 상어를 잡는다.
            for (int i = 0; i < r; i++) {
                if (graph[i][fisher] != 0) {
                    int shark = graph[i][fisher];
                    catched.add(shark);
                    sharks.remove(shark);
                    graph[i][fisher] = 0;
                    break;
                }
            }

            // 3. 상어가 이동한다.
            Map<Point, List<Integer>> moves = new HashMap<>();
            graph = new int[r][c];

            for (Map.Entry<Integer, int[]> entry : sharks.entrySet()) {
                int shark = entry.getKey();
                int[] value = entry.getValue();
                int x = value[0], y = value[1], s = value[2], d = value[3];

                if (d == 1 || d == 2)
                    if (r > 1) s %= 2 * (r - 1);
                    else s = 0;
                else    // 2(c-1)만큼 앞으로 가면 원래 자리, 원 방향 값으로 돌아온다.
                    if (c > 1) s %= 2 * (c - 1);
                    else s = 0;

                int nx = x, ny = y;

                for (int i = 0; i < s; i++) {
                    nx += dx[d - 1];
                    ny += dy[d - 1];

                    if (nx < 0 || ny < 0 || nx >= r || ny >= c) {
                        if (d == 1 || d == 2) d = d == 1 ? 2 : 1;
                        else d = d == 3 ? 4 : 3;

                        // 벽을 만났을 때, 방향 전환
                        if (nx < 0) nx += 2;
                        else if (nx >= r) nx -= 2;
                        else if (ny < 0) ny += 2;
                        else if (ny >= c) ny -= 2;
                    }
                }

                Point pos = new Point(nx, ny);

                if (!moves.containsKey(pos)) {
                    List<Integer> sharkInfo = new ArrayList<>();
                    sharkInfo.add(shark);
                    moves.put(pos, sharkInfo);
                } else {
                    List<Integer> sharkInfo = moves.get(pos);
                    sharkInfo.add(shark);
                }
                sharks.put(shark, new int[]{nx, ny, s, d});
            }

            // 같은 칸에 상어가 여러 마리라면 큰 상어만 남는다.
            for (Map.Entry<Point, List<Integer>> entry : moves.entrySet()) {
                List<Integer> sharkList = entry.getValue();

                if (sharkList.size() > 1) {
                    int res = 0;
                    for (int size : sharkList) {
                        if (size > res) {
                            if (res != 0) sharks.remove(res);
                            res = size;
                        }
                        else sharks.remove(size);
                    }
                }
            }

            // 상어의 위치 정보 갱신
            for (Map.Entry<Integer, int[]> entry : sharks.entrySet()) {
                int shark = entry.getKey();
                int[] sharkInfo = entry.getValue();
                int x = sharkInfo[0];
                int y = sharkInfo[1];

                graph[x][y] = shark;
            }
        }

        int ans = 0;
        for (int shark : catched) {
            ans += shark;
        }
        System.out.println(ans);
    }
}
