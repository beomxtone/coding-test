import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
/*
 * 1. summary: 문제 해석
 *  맨 앞 숫자에서 1 to 5까지 빼고 해당 숫자를 맨 뒤에 넣는다.
 *  뺀 숫자가 0 이하이면 0으로 변경 후 종료
 *
 * 2. strategy: 해결 전략
 *  Queue를 사용
 *
 * 3. note:
 */
class Solution {
 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
 
        for (int t = 0; t < 10; t++) {
            int testcase = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
 
            // 암호를 저장할 Queue
            Queue<Integer> queue = new LinkedList<>();
            for (int i = 0; i < 8; i++) {
                queue.add(Integer.parseInt(st.nextToken()));
            }
            if (t < 9) st = new StringTokenizer(br.readLine());
 
            // flag가 false이면 루프 종료
            boolean flag = true;
            while (flag) {
                for (int i = 1; i < 6; i++) {
                    int num = queue.poll();
                    num -= i;
                    // 뺀 값이 0 이하가 되면 종료
                    if (num <= 0) {
                        flag = false;
                        num = 0;
                        queue.add(num);
                        break;
                    }
                    queue.add(num);
                }
            }
 
            System.out.println("#" + testcase + " " + queue.toString().replaceAll("[^0-9 ]",""));
        }
    }
}