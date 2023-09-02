import sys
input = sys.stdin.readline

#
# 9095번: 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095
#
# 1. 5를 만드는 방법 = 4방법+1, 3방법+2, 2방법+3
# 2. DP[n] = DP[n-1] + DP[n-2] + DP[n-3]
# 3. n은 최대 10
#
# @author  Asher Seo
#

# n = 1, 2, 3 초기화
dp = [1, 2, 4] + [0]*7
for i in range(3, 10):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

t = int(input())
for _ in range(t):
  n = int(input())
  print(dp[n-1])
