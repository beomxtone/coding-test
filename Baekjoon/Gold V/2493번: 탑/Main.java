import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;
import java.util.StringTokenizer;
/*
 * 1. summary: 문제 해석
 * 탑은 왼쪽에 있는 자신보다 큰 탑 중에서 가장 가까운 탑을 송신탑으로 설정한다.
 * 송신탑을 출력, 자신보다 큰 탑이 없을 경우 0을 출력한다.
 *
 * 2. strategy: 해결 전략
 * 스택과 Pair를 사용, 스택에 역순으로 집어넣는다.
 * 현재 넣는 탑이 스택의 마지막 탑과 같거나 크다면, 현재 탑보다 큰 탑이 있을 때까지 pop
 * 스택에 현재 탑을 push, 반복한다.
 *
 * 3. note:
 */
class Pair {
    private int index;
    private int height;

    Pair(int index, int height) {
        this.index = index;
        this.height = height;
    }

    public int getIndex(){
        return index;
    }

    public int getHeight(){
        return height;
    }
}

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        int[] tops = new int[n];
        for (int i = 0; i < n; i++) {
            tops[i] = Integer.parseInt(st.nextToken());
        }

        Stack<Pair> stk = new Stack<>();
        int[] ans = new int[n];
        // 거꾸로 스택에 넣음
        for (int i = n-1; i > -1; i--) {
            if (stk.empty()) stk.push(new Pair(i, tops[i]));
            else {
                // 현재 탑이 스택의 마지막 탑과 같거나 크다면, 스택의 탑이 현재 탑보다 클 때까지 pop
                if (stk.peek().getHeight() <= tops[i]) {
                    while (true) {
                        if (stk.empty()) break;
                        if (stk.peek().getHeight() > tops[i]) break;
                        Pair temp = stk.pop();
                        ans[temp.getIndex()] = i + 1;
                    }
                }
                stk.push(new Pair(i, tops[i]));
            }
        }

        for (int i = 0; i < n; i++) {
            System.out.print(ans[i] + " ");
        }
    }
}
