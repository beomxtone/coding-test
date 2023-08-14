import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
/*
 summary
 - z 방향으로 순회할 때, (r, c)는 언제 탐색되는가
 strategy
 - 사각형을 4개의 구역으로 나눈다. (size: 사각형 변의 길이)
 - 1사분면일 경우: 탐색 순서에 변함은 없다.
 - 2사분면일 경우: 탐색 순서를 (size/2)**2만큼 더한다.
 - 3사분면일 경우: 탐색 순서를 ((size/2)**2)*2만큼 더한다.
 - 4사분면일 경우: 탐색 순서를 ((size/2)**2)*3만큼 더한다.
 - len이 1이 될 때까지 반복
 */
class Main {
    static int ans;

    static void solve(int r, int c, int len) {
        // 사각형의 길이가 1이 되면 종료
        if (len == 1) return;

        // 1사분면에 있을 경우
        if (r < len/2 && c < len/2)
            solve(r, c, len/2);

        // 2사분면에 있을 경우
        if (r < len/2 && c >= len/2) {
            ans += (len/2) * (len/2);
            solve(r, c - len/2, len/2);
        }

        // 3사분면에 있을 경우
        if (r >= len/2 && c < len/2) {
            ans += ((len/2) * (len/2)) * 2;
            solve(r - len/2, c, len/2);
        }

        // 4사분면에 있을 경우
        if (r >= len/2 && c >= len/2) {
            ans += ((len/2) * (len/2)) * 3;
            solve(r - len/2, c - len/2, len/2);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        // 사각형 변의 길이
        int len = (int) Math.pow(2, n);

        ans = 0;
        solve(r, c, len);

        System.out.println(ans);
    }
}
