import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] switches = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int stuCnt = Integer.parseInt(br.readLine());

        for (int i = 0; i < stuCnt; i++) {
            int[] stuInfo = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int gen = stuInfo[0];
            int num = stuInfo[1];

            // 남성일 경우
            if (gen == 1) {
                for (int j = num-1; j < n; j += num) {
                    int change = switches[j] == 1 ? 0 : 1;
                    switches[j] = change;
                }
            }
            // 여성일 경우
            else {
                int x = num-2;
                int y = num;

                // 받은 index 변경
                if (switches[num-1] == 0) switches[num-1] = 1;
                else switches[num-1] = 0;

                while (true) {
                    if (x < 0 || y >= n) break;

                    if (switches[x] != switches[y]) break;

                    if (switches[x] == 0) {
                        switches[x] = 1;
                        switches[y] = 1;
                    }
                    else {
                        switches[x] = 0;
                        switches[y] = 0;
                    }

                    x -= 1;
                    y += 1;
                }
            }
        }

        int cnt = 0;
        for (int i = 0; i < switches.length-1; i++) {
            System.out.print(switches[i] + " ");
            cnt += 1;
            if (cnt % 20 == 0) System.out.println();
        }
        System.out.println(switches[switches.length-1]);
    }
}