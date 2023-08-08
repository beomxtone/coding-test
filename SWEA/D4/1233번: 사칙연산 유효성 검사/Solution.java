import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
/*
 * 1. summary: 문제 해석
 * 트리로 만든 식이 올바른지 검증한다.
 *
 * 2. strategy: 해결 전략
 * 트리의 최하위 노드에 연산자가 있을 경우 올바른 식이 아니다.
 * 자식 노드가 있는 경우 연산자여야 한다.
 *
 * 3. note:
 */

class Solution {
    public static boolean isNumeric(String input) {
        try {
            Double.parseDouble(input);
            return true;
        }
        catch (NumberFormatException e) {
            return false;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int TC = 1; TC < 11; TC++) {
            int N = Integer.parseInt(br.readLine());

            boolean flag = true;
            for (int i = 0; i < N; i++) {
                String[] input = br.readLine().split(" ");

                // 최하위 노드는 2칸으로 주어짐
                if (input.length == 2) {
                    // 최하위 노드 중 연산자가 있는지 검사
                    if (flag && input[1].equals("+") || input[1].equals("-") || input[1].equals("*") || input[1].equals("\\")) {
                        flag = false;
                    }
                }
                // 자식 노드가 있는 경우
                else {
                    // 연산자인지 확인
                    if (flag && isNumeric(input[1])) {
                        flag = false;
                    }
                }
            }

            System.out.println(flag ? "#" + TC + " " + 1 : "#" + TC + " " + 0);
        }

    }
}
