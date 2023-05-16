import sys
input = sys.stdin.readline

#
# 9461번: 파도반 수열
# https://www.acmicpc.net/problem/9461
#
# 1. d[i] = d[i-3] + d[i-2]
# 2. d[1], d[2], d[3] = 1
#
# @author  Asher Seo
#

T = int(input())
for _ in range(T):
  dp = [1, 1, 1]
  n = int(input())
  for i in range(3, n):
    dp.append(dp[i-3] + dp[i-2])
  print(dp[n-1])
