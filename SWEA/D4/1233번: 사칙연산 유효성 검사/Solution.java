import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
/*
 * 1. summary: 문제 해석
 * 트리로 만든 식이 올바른지 검증한다.
 *
 * 2. strategy: 해결 전략
 * 트리의 최하위 노드에 연산자가 있을 경우 올바른 식이 아니다.
 *
 * 3. note:
 */

class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int TC = 1; TC < 11; TC++) {
            int N = Integer.parseInt(br.readLine());

            boolean flag = true;
            for (int i = 0; i < N; i++) {
                String[] input = br.readLine().split(" ");

                // 최하위 노드는 2칸으로 주어짐
                if (flag && input.length == 2) {
                    // 최하위 노드 중 연산자가 있는지 검사
                    if (input[1].equals("+") || input[1].equals("-") || input[1].equals("*") || input[1].equals("\\")) {
                        flag = false;
                    }
                }
            }

            System.out.println(flag ? "#" + TC + " " + 1 : "#" + TC + " " + 0);
        }

    }
}
