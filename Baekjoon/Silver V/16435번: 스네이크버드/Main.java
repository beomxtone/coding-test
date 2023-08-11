import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;
/*
    1. Array sort
    2. 앞부터 과일을 먹으며 먹을 수 없으면 종료
 */
class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] fruits = new int[n];
        for (int i = 0; i < n; i++) {
            fruits[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(fruits);

        // 뱀의 위치
        int idx = 0;
        while (true && idx < n) {
            if (l < fruits[idx]) break;
            l += 1;
            idx++;
        }
        System.out.println(l);
    }
}
