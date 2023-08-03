import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {
    static boolean[][] powerSets;
    static int idx = 0;

    static void powerSet(boolean[] visited, int n, int cnt) {
        if(cnt == n) {
            for (int i = 0; i < n; i++) {
                powerSets[idx][i] = visited[i];
            }
            idx += 1;
            return;
        }

        visited[cnt] = false;
        powerSet(visited, n, cnt + 1);

        visited[cnt] = true;
        powerSet(visited, n, cnt + 1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        powerSets = new boolean[(int) Math.pow(2, n)][n];
        powerSet(new boolean[n], n, 0);

        int[][] subs = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            subs[i][0] = Integer.parseInt(st.nextToken());
            subs[i][1] = Integer.parseInt(st.nextToken());
        }

        int ans = Integer.MAX_VALUE;
        for (int i = 1; i < powerSets.length; i++) {
            int a = 1, b = 0;
            for (int j = 0; j < powerSets[i].length; j++) {
                if (powerSets[i][j]) {
                    a *= subs[j][0];
                    b += subs[j][1];
                }
            }
            if (Math.abs(a-b) < ans) ans = Math.abs(a-b);
        }

        System.out.println(ans);
    }
}