import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.List;

class Solution {
    static void combinations(List<List<Integer>> combs, List<Integer> currCombs, int n, int r, int start) {
        if (r == 0) {
            combs.add(new ArrayList<>(currCombs));
            return;
        }

        for (int i = start; i < n; i++) {
            currCombs.add(i);
            combinations(combs, currCombs, n, r-1, i+1);
            currCombs.remove(currCombs.size()-1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int TC = 1; TC <= T; TC++) {
            int N = Integer.parseInt(br.readLine());
            int[][] synergy = new int[N][N];

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    synergy[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int ans = Integer.MAX_VALUE;
            // A 음식의 식재료 조합 구하기
            List<List<Integer>> selectAcombs = new ArrayList<>();
            combinations(selectAcombs, new ArrayList<>(), N, N/2, 0);

            for (List<Integer> selectAcomb : selectAcombs) {
                List<Integer> selectA = selectAcomb;
                List<Integer> selectB = new ArrayList<>();

                // B 음식의 식재료 조합 구하기
                for (int food = 0; food < N; food++) {
                    if (!selectA.contains(food))
                        selectB.add(food);
                }

                int tasteA = 0, tasteB = 0;

                // A 음식의 시너지 합
                for (int i = 0; i < selectA.size(); i++) {
                    for (int j = i + 1; j < selectA.size(); j++) {
                        int x = selectA.get(i);
                        int y = selectA.get(j);
                        tasteA += synergy[x][y] + synergy[y][x];
                    }
                }

                // B 음식의 시너지 합
                for (int i = 0; i < selectB.size(); i++) {
                    for (int j = i + 1; j < selectB.size(); j++) {
                        int x = selectB.get(i);
                        int y = selectB.get(j);
                        tasteB += synergy[x][y] + synergy[y][x];
                    }
                }

                int res = Math.abs(tasteA - tasteB);
                if (res < ans) {
                    ans = res;
                }
            }
            System.out.println("#" + TC + " " + ans);
        }
    }
}
