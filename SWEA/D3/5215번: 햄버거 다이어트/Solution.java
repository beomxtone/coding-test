import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

class Solution {
    static boolean[][] powersets;
    static int powersetIdx;

    static void powerset(boolean[] visited, int n, int idx) {
        if(idx == n) {
            for (int i = 0; i < n; i++) {
                powersets[powersetIdx][i] = visited[i];
            }
            powersetIdx += 1;
            return;
        }

        visited[idx] = false;
        powerset(visited, n, idx+1);

        visited[idx] = true;
        powerset(visited, n, idx+1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int TC = 1; TC <= T; TC++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int L = Integer.parseInt(st.nextToken());

            powersets = new boolean[(int) Math.pow(2, N)][N];
            powersetIdx = 0;

            int[][] foodInfo = new int[N][2];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                foodInfo[i][0] = Integer.parseInt(st.nextToken());
                foodInfo[i][1] = Integer.parseInt(st.nextToken());
            }

            powerset(new boolean[N], N, 0);

            int ans = 0;
            for (boolean[] foods : powersets) {
                int score = 0, cals = 0;

                for (int i = 0; i < foods.length; i++) {
                    if (foods[i]) {
                        score += foodInfo[i][0];
                        cals += foodInfo[i][1];
                    }
                    if (cals > L) break;
                }

                if (cals <= L && score > ans) ans = score;
            }

            System.out.println("#" + TC + " " + ans);
        }
    }
}
