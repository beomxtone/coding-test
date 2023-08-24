import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
/*
 Kruskal을 쓰자
 거리 대신 환경 부담 세율(cost = e * length**2)로 비교하자
 */
class Solution {
    static int find(int[] parent, int x) {
        if (parent[x] != x)
            parent[x] = find(parent, parent[x]);
        return parent[x];
    }

    static void union(int[] parent, int a, int b) {
        a = find(parent, a);
        b = find(parent, b);
        if (a < b) parent[b] = a;
        else parent[a] = b;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= t; tc++) {
            // 섬의 개수 n
            int n = Integer.parseInt(br.readLine());
            int[][] inputs = new int[2][n];
            for (int i = 0; i < 2; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    inputs[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            // 환경 부담 세율 e
            double e = Double.parseDouble(br.readLine());

            int[][] islands = new int[n][2];
            for (int i = 0; i < n; i++) {
                islands[i][0] = inputs[0][i];
                islands[i][1] = inputs[1][i];
            }

            // (cost, x좌표, y좌표)로 이루어진 edge의 배열
            double[][] edges = new double[n * (n - 1) / 2][3];
            int edgeIndex = 0;

            // parent 초기화
            int[] parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }

            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    double x = Math.pow(islands[j][0] - islands[i][0], 2);
                    double y = Math.pow(islands[j][1] - islands[i][1], 2);
                    // 환경부담세율: ((x+y)**0.5) = l, l**2 * e
                    double cost = (x + y) * e;
                    edges[edgeIndex][0] = cost;
                    edges[edgeIndex][1] = i;
                    edges[edgeIndex][2] = j;
                    edgeIndex++;
                }
            }

            // 환경부담세율을 기준으로 정렬
            Arrays.sort(edges, (a, b) -> Double.compare(a[0], b[0]));

            double ans = 0;

            for (double[] edge : edges) {
                double cost = edge[0];
                int a = (int) edge[1];
                int b = (int) edge[2];

                // kruskal algorithm
                if (find(parent, a) != find(parent, b)) {
                    union(parent, a, b);
                    ans += cost;
                }
            }

            System.out.println("#" + tc + " " + Math.round(ans));
        }
    }
}
