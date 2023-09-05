import sys
input = sys.stdin.readline

#
# 11049번: 행렬 곱셈 순서
# https://www.acmicpc.net/problem/11049
#
# 1. 행렬의 곱셈 연산을 최소로 하는 방법 = DP
# 2. 행렬 n개: 행렬 n-1개를 곱했을 때 최소 연산 횟수를 구한다.
#
# @author  Asher Seo
#

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for j in range(1, n):
  for i in range(n):
    # 범위를 넘어갔을 때
    if i+j == n: break

    dp[i][i+j] = 2**31
    for k in range(i, i+j):
      dp[i][i+j] = min(dp[i][i+j], dp[i][k] + dp[k+1][i+j] + mat[i][0] * mat[k][1] * mat[i+j][1])

print(dp[0][n-1])
