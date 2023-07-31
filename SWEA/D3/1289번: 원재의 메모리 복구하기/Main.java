import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        for (int t = 1; t < tc + 1; t++) {
            String input = br.readLine();
            String[] temp;
            temp = input.split("");
            int[] arr = new int[input.length()];
            int[] init = new int[input.length()];

            for (int i = 0; i < input.length(); i++) {
                arr[i] = Integer.parseInt(temp[i]);
            }

            int ans = 0;

            for (int i = 0; i < input.length(); i++) {
                if (arr[i] != init[i]) {
                    ans += 1;
                    int idx = i;
                    while (idx < input.length()) {
                        init[idx] = arr[i];
                        idx += 1;
                    }
                }
            }

            System.out.println("#" + t + " " + ans);

        }
    }
}