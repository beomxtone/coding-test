import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
/*
 * 1. summary: 문제 해석
 * 입력받은 문자열의 부분 문자열을 subString이라 할 때,
 * [A, C, G, T] 입력 조건의 개수에 맞는 subString의 수를 출력한다.
 *
 * 2. strategy: 해결 전략
 * 문자열을 주어진 P까지 자른 후 문자를 카운트한다. (1번째 subString)
 * 문자열을 하나씩 옆으로 옮기면서 문자를 카운트한다. (i+1번째 subString)
 *
 * 3. note:
 * StringBuilder로 문자열을 직접 만들면서 세면 TLE
 */
class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // S: 임의의 DNA 문자열의 길이, P: 비밀번호로 사용할 부분 문자열의 길이
        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        String dnaString = st.nextToken();

        st = new StringTokenizer(br.readLine());
        // cnts: {A, C, G, T} 의 개수
        int[] cnts = new int[4];
        for (int i = 0; i < 4; i++) {
            cnts[i] = Integer.parseInt(st.nextToken());
        }

        // 문자열을 P까지 자름
        StringBuilder sb = new StringBuilder();
        sb.append(dnaString).setLength(P);
        int ans = 0;

        // A, C, G, T의 개수
        int Acnt = 0, Ccnt = 0, Gcnt = 0, Tcnt = 0;
        String res = sb.toString();

        // 문자 카운트
        for (int i = 0; i < P; i++) {
            char chr = res.charAt(i);
            if (chr == 'A') Acnt++;
            else if (chr == 'C') Ccnt++;
            else if (chr == 'G') Gcnt++;
            else if (chr == 'T') Tcnt++;
        }

        // 조건에 맞으면 정답 추가
        if (Acnt >= cnts[0] && Ccnt >= cnts[1] && Gcnt >= cnts[2] && Tcnt >= cnts[3]) ans ++;

        // 문자열을 하나씩 뒤로 민다.
        for (int i = P; i < S; i++) {
            char chr = dnaString.charAt(i-P);
            // 뺀 문자를 -1씩
            if (chr == 'A') Acnt--;
            else if (chr == 'C') Ccnt--;
            else if (chr == 'G') Gcnt--;
            else if (chr == 'T') Tcnt--;

            chr = dnaString.charAt(i);
            // 더한 문자를 +1씩
            if (chr == 'A') Acnt++;
            else if (chr == 'C') Ccnt++;
            else if (chr == 'G') Gcnt++;
            else if (chr == 'T') Tcnt++;

            if (Acnt >= cnts[0] && Ccnt >= cnts[1] && Gcnt >= cnts[2] && Tcnt >= cnts[3]) ans ++;
        }

        System.out.println(ans);
    }
}