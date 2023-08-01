import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
 
class Solution {
    public static int recur(int[] arr, int cnt) {
        if (cnt == 0) {
            Arrays.sort(arr);
            return arr[arr.length-1] - arr[0];
        }
 
        Arrays.sort(arr);
        arr[arr.length-1] -= 1;
        arr[0] += 1;
 
        return recur(arr, cnt-1);
    }
 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
        for (int t = 1; t < 11; t++) {
 
            int dmpCnt = Integer.parseInt(br.readLine());
            int[] dumps = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
 
            System.out.println("#" + t + " " + recur(dumps, dmpCnt));
        }
    }
}
