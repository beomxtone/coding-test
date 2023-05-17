import sys
input = sys.stdin.readline

#
# 1932번: 정수 삼각형
# https://www.acmicpc.net/problem/1932
#
# 1. DP - bottom up 방식
#
# @author  Asher Seo
#

n = int(input())
tri = []
for _ in range(n):
  tri.append(list(map(int, input().split())))
# bottom up 방식을 위해 역순 정렬
tri = tri[::-1]

if n == 1:
  print(tri[0][0])
  exit()

dp = [[] for _ in range(n-1)]
for i in range(n):
  for j in range(1, len(tri[i])):
    if i == 0:
      dp[i].append(max(tri[i][j-1], tri[i][j]) + tri[i+1][j-1])
    else:
      dp[i].append(max(dp[i-1][j-1], dp[i-1][j]) + tri[i+1][j-1])

print(dp[n-2][0])
