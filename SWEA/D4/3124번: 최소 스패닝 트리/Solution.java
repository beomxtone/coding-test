import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Solution {
    static int[] parents, size;
    private static int find(int x) {
        if (parents[x] == x) return x;
        return parents[x] = find(parents[x]);
    }

    private static boolean union(int a, int b) {
        int aRoot = find(a);
        int bRoot = find(b);

        if (aRoot == bRoot) return false;

        if (size[aRoot] > size[bRoot]) parents[bRoot] = aRoot;
        else if (size[aRoot] == size[bRoot]) size[bRoot]++;
        if (size[bRoot] > size[aRoot]) parents[aRoot] = bRoot;

        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= t; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            parents = new int[v+1];
            size = new int[v+1];

            for (int i = 1; i <= v; i++) {
                parents[i] = i;
            }

            PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[2] - o2[2]);
            for (int i = 0; i < e; i++) {
                st = new StringTokenizer(br.readLine());
                pq.offer(new int[]{
                   Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()),
                });
            }

            int cnt = 0;
            long ans = 0;

            while (cnt != v-1) {
                int[] edge = pq.poll();
                if (!union(edge[0], edge[1])) continue;
                ans += edge[2];
                cnt++;
            }
            System.out.println("#" + tc + " " + ans);
        }
    }
}
