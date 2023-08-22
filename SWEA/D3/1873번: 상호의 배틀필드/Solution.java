import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/*
 1. 구현하자
 */
class Solution {
    static int x, y, dir;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= t; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            // board 입력
            char[][] board = new char[h][w];
            for (int i = 0; i < h; i++) {
                String input = br.readLine();
                for (int j = 0; j < w; j++) {
                    board[i][j] = input.charAt(j);
                    // 전차의 위치 정보
                    if (board[i][j] == '^' || board[i][j] == 'v' || board[i][j] == '<' || board[i][j] == '>') {
                        x = i; y = j;
                        if (board[i][j] == '^') dir = 0;
                        if (board[i][j] == 'v') dir = 1;
                        if (board[i][j] == '<') dir = 2;
                        if (board[i][j] == '>') dir = 3;
                        // 전차의 아래는 평지
                        board[i][j] = '.';
                    }
                }
            }

            // command 입력
            int n = Integer.parseInt(br.readLine());
            char[] commands = new char[n];
            String input = br.readLine();
            for (int i = 0; i < n; i++) {
                commands[i] = input.charAt(i);
            }

            for (char cmd: commands) {
                if (cmd == 'U') {
                    dir = 0;
                    if (x-1 >= 0 && board[x-1][y] == '.') {
                        x -= 1;
                    }
                }
                if (cmd == 'D') {
                    dir = 1;
                    if (x+1 < h && board[x+1][y] == '.') {
                        x += 1;
                    }
                }
                if (cmd == 'L') {
                    dir = 2;
                    if (y-1 >= 0 && board[x][y-1] == '.') {
                        y -= 1;
                    }
                }
                if (cmd == 'R') {
                    dir = 3;
                    if (y+1 < w && board[x][y+1] == '.') {
                        y += 1;
                    }
                }
                if (cmd == 'S') {
                    int nx = x, ny = y;
                    while (true) {
                        // 포탄이 맵 밖으로 벗어나면 종료
                        if (nx < 0 || ny < 0 || nx >= h || ny >= w) break;
                        // 포탄이 벽돌에 부딪히면 벽을 부수고 종료
                        if (board[nx][ny] == '*') {
                            board[nx][ny] = '.';
                            break;
                        }
                        // 포탄이 강철에 부딪히면 아무 일도 일어나지 않고 종료
                        if (board[nx][ny] == '#') break;

                        // 포탄의 이동 방향
                        switch (dir) {
                            case 0:
                                nx -= 1;
                                break;
                            case 1:
                                nx += 1;
                                break;
                            case 2:
                                ny -= 1;
                                break;
                            case 3:
                                ny += 1;
                                break;
                            default:
                                break;
                        }
                    }
                }
            }
            // 전차를 배치
            switch (dir) {
                case 0:
                    board[x][y] = '^';
                    break;
                case 1:
                    board[x][y] = 'v';
                    break;
                case 2:
                    board[x][y] = '<';
                    break;
                case 3:
                    board[x][y] = '>';
                    break;
                default:
                    break;
            }

            System.out.print("#" + tc + " ");
            for (int i = 0; i < h; i++) {
                System.out.println(board[i]);
            }
        }
    }
}
