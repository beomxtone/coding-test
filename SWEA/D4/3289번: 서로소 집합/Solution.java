import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

class Solution {
    static int[] parents;
    static StringBuilder sb;
    static int find(int a) {
        if (a == parents[a]) return a;
        return parents[a] = find(parents[a]);
    }

    static boolean union(int a, int b) {
        int aRoot = find(a);
        int bRoot = find(b);

        if (aRoot == bRoot) return false;
        parents[bRoot] = aRoot;
        return true;
    }

    static boolean check(int a, int b) {
        int aRoot = find(a);
        int bRoot = find(b);

        if (aRoot == bRoot) return true;
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= t; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            parents = new int[n];
            for (int i = 0; i < n; i++) {
                parents[i] = i;
            }

            sb = new StringBuilder();
            sb.append("#" + tc + " ");

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int isFind = Integer.parseInt(st.nextToken());
                int a = Integer.parseInt(st.nextToken()) - 1;
                int b = Integer.parseInt(st.nextToken()) - 1;

                if (isFind == 0) union(a, b);
                if (isFind == 1) {
                    if (check(a, b)) sb.append(1);
                    else sb.append(0);
                }
            }

            System.out.println(sb.toString());
        }
    }
}
