import sys
input = sys.stdin.readline

#
# 17070번: 파이프 옮기기 1
# https://www.acmicpc.net/problem/17070
#
# 1. 완전 탐색의 경우 시간 초과 예상 (n은 최대 16) 따라서 DP로 풀이
# 2. 첫 가로 줄은 가로인 파이프만 올 수 있다.
# 3. 가로 파이프는 이전 파이프가 가로거나 대각선인 경우, 세로 파이프는 이전 파이프가 세로거나 대각선인 경우
# 4. 대각선 파이프는 이전 파이프가 어떤 상태이던 올 수 있다.
# 5. 가로, 세로는 해당 칸만 벽이 없다면 가능하지만, 대각선은 이전 가로, 이전 세로칸도 빈칸이어야 한다.
#
# @author  Asher Seo
#

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# 가로, 세로, 대각선
dp = [[[0]*n for _ in range(n)] for _ in range(3)]
# 시작 위치 (0, 1)
dp[0][0][1] = 1

# 첫 가로 줄은 가로인 파이프만 올 수 있다.
for i in range(2, n):
  if board[0][i] == 0:
    dp[0][0][i] = dp[0][0][i-1]

for i in range(1, n):
  for j in range(1, n):
    if board[i][j] == 0:
      # 가로, 세로 파이프
      dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
      dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

      if board[i-1][j] == 0 and board[i][j-1] == 0:
        # 대각선 파이프
        dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

ans = 0
for i in range(3):
  ans += dp[i][n-1][n-1]
print(ans)
