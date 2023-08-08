import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for (int TC = 1; TC <= T; TC++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int[] snack = new int[N];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                snack[i] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(snack);

            // 가장 작은 과자 두 봉지가 M 초과일 경우 -1
            if (snack[0] + snack[1] > M) {
                System.out.println("#" + TC + " -1");
                continue;
            }

            int ans = 0;
            for (int i = 1; i < N; i++) {
                for (int j = 0; j < i; j++) {
                    if (snack[j] + snack[i] <= M) {
                        ans = Math.max(ans, snack[j] + snack[i]);
                    } else {
                        break;
                    }
                }
            }

            System.out.println("#" + TC + " " + ans);
        }

        br.close();
    }
}
