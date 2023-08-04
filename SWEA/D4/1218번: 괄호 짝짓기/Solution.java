import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;
import java.util.StringTokenizer;
/*
 * 1. summary: 문제 해석
 * 괄호의 쌍이 맞으면 1
 * 쌍이 맞지 않으면 0
 *
 * 2. strategy: 해결 전략
 * 괄호마다 스택을 생성
 * 조건에 맞게 스택에 추가, 삭제
 * 스택의 길이가 모두 0이면 정답
 *
 * 3. note:
 */
class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int testcase = 1; testcase < 11; testcase++) {
            // 입력받은 테스트 케이스의 길이
            int len = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            // 입력받은 문자열
            String input = st.nextToken();
            if (testcase < 10) st = new StringTokenizer(br.readLine());
            // 괄호를 검사할 스택
            Stack<String> stk1 = new Stack<>(); // ()
            Stack<String> stk2 = new Stack<>(); // []
            Stack<String> stk3 = new Stack<>(); // {}
            Stack<String> stk4 = new Stack<>(); // <>

            for (int i = 0; i < len; i++) {
                char chr = input.charAt(i);
                // check ()
                if (chr == '(') {
                    if (stk1.contains(")")) stk1.pop();
                    else stk1.push("(");
                } else if (chr == ')') {
                    if (stk1.contains("(")) stk1.pop();
                    else stk1.push(")");
                }
                // check []
                else if (chr == '[') {
                    if (stk2.contains("]")) stk2.pop();
                    else stk2.push("[");
                } else if (chr == ']') {
                    if (stk2.contains("[")) stk2.pop();
                    else stk2.push("]");
                }
                // check {}
                else if (chr == '{') {
                    if (stk3.contains("}")) stk3.pop();
                    else stk3.push("{");
                } else if (chr == '}') {
                    if (stk3.contains("{")) stk3.pop();
                    else stk3.push("{");
                }
                // check <>
                else if (chr == '<') {
                    if (stk4.contains(">")) stk4.pop();
                    else stk4.push("<");
                }else if (chr == '>') {
                    if (stk4.contains("<")) stk4.pop();
                    else stk4.push(">");
                }
            }

            int ans = 0;
            if (stk1.empty() && stk2.empty() && stk3.empty() && stk4.empty()) ans = 1;

            System.out.println("#" + testcase + " " + ans);
        }
    }
}