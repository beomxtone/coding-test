import sys
input = sys.stdin.readline

#
# 11066번: 파일 합치기
# https://www.acmicpc.net/problem/11066
#
# 1. 합쳐진 파일들과 남은 파일 중 가장 작은 값을 고르면 -> 연속성을 보장받지 못하는 그리디
# 2. d[i][j] = i부터 j까지 파일 합의 최소값
# 3.         = min(d[i][i+k] + d[j-k][j]) + sum(files[i:j+1])
#
# @author  Asher Seo
#

t = int(input())
for _ in range(t):
  k = int(input())
  f = list(map(int, input().split()))
  dp = [[0]*k for _ in range(k)]
  
  for i in range(k-1):
    dp[i][i+1] = f[i] + f[i+1]
    for j in range(i+2, k):
      dp[i][j] = dp[i][j-1] + f[j]

  for d in range(2, k):
    for i in range(k-d):
      j = i+d
      res = [dp[i][k] + dp[k+1][j] for k in range(i, j)]
      dp[i][j] += min(res)

  print(dp[0][k-1])
