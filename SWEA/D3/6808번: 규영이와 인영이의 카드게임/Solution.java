import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Solution {
    static void permutations(int[] arr, int index, List<int[]> perm) {
        if (index == arr.length) {
            int[] copy = arr.clone();
            perm.add(copy);
            return;
        }

        for (int i = index; i < arr.length; i++) {
            swap(arr, index, i);
            permutations(arr, index+1, perm);
            swap(arr, index, i);
        }
    }

    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int TC = 1; TC <= T; TC++) {
            // 1부터 18까지의 카드
            int[] deck = new int[18];
            for (int i = 0; i < 18; i++) {
                deck[i] = i+1;
            }

            // 규영이의 카드 입력 받음
            int[] kCards = new int[9];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 9; i++) {
                kCards[i] = Integer.parseInt(st.nextToken());
            }

            // 인영이의 카드 찾기
            List<Integer> iCards = new ArrayList<>();
            for (int card : deck) {
                boolean found = false;
                for (int kCard : kCards) {
                    if (card == kCard) {
                        found = true;
                        break;
                    }
                }
                if (!found) iCards.add(card);
            }

            int win = 0, lose = 0;
            List<int[]> permCards = new ArrayList<>();
            // 규영이가 낼 수 있는 카드의 순열 구하기
            permutations(kCards, 0, permCards);

            // 구해진 카드 순열에 따라 승패 판정
            for (int[] permCard : permCards) {
                int kScore = 0, iScore = 0;
                for (int i = 0; i < 9; i++) {
                    int score = iCards.get(i) + permCard[i];
                    if (iCards.get(i) > permCard[i]) iScore += score;
                    else kScore += score;
                }

                if (iScore > kScore) lose++;
                else if (iScore < kScore) win++;
            }

            System.out.println("#" + TC + " " + win + " " + lose);
        }
    }
}
