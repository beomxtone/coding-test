import sys
input = sys.stdin.readline

#
# 25682번: 체스판 다시 칠하기 2
# https://www.acmicpc.net/problem/25682
#
# 1. B와 W로 시작하는 이상적인 체스판을 선언
# 2. 입력값과 1을 비교해 각 칸이 같으면 0, 다르면 1인 2차원 배열을 만든다.
# 3. B와 W로 비교한 2개의 2차원 배열에서 K*K의 구간합을 구해 가장 작은 칸의 정보를 가져온다.
# 4. 가장 작은 칸의 누적합 결과를 출력한다.
#
# @author  Asher Seo
#

n, m, k = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

# w로 시작하는 완성된 체스판
wBoard = ['WB'*(m//2) + 'W'*(m%2), 'BW'*(m//2) + 'B'*(m%2)] * (n//2) + ['WB'*(m//2) + 'W'*(m%2)] * (n%2)

wArr, bArr = [[0]*m for _ in range(n)], [[0]*m for _ in range(n)]
for i in range(n):
  for j in range(m):
    # 입력값이 w로 시작하는 체스판과 같으면 b로 시작하는 체스판에서는 다르다
    if board[i][j] == wBoard[i][j]:
      bArr[i][j] = 1
    # 입력값이 w로 시작하는 체스판과 다르면 w 체스판에 1
    else:
      wArr[i][j] = 1

# 누적합
wDP, bDP = [[0]*(m+1) for _ in range(n+1)], [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
  for j in range(1, m+1):
    wDP[i][j] = wArr[i-1][j-1] + wDP[i-1][j] + wDP[i][j-1] - wDP[i-1][j-1]
    bDP[i][j] = bArr[i-1][j-1] + bDP[i-1][j] + bDP[i][j-1] - bDP[i-1][j-1]

ans = 10**9
for i in range(k, n+1):
  for j in range(k, m+1):
    # 구간합
    wRes = wDP[i][j] - (wDP[i-k][j] + wDP[i][j-k]) + wDP[i-k][j-k]
    bRes = bDP[i][j] - (bDP[i-k][j] + bDP[i][j-k]) + bDP[i-k][j-k]
    ans = min(ans, min(wRes, bRes))

print(ans)
