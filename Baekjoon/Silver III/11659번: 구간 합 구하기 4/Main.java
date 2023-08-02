import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");

        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);
        int[] arr = new int[N];
        int[] sumArr = new int[N+1];

        inputs = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(inputs[i]);
            sumArr[i+1] += sumArr[i] + arr[i];
        }

        for (int t = 0; t < M; t++) {
            inputs = br.readLine().split(" ");
            int i = Integer.parseInt(inputs[0]);
            int j = Integer.parseInt(inputs[1]);
            
            System.out.println(sumArr[j] - sumArr[i-1]);
        }

    }
}