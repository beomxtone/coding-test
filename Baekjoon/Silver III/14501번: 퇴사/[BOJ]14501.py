import sys
input = sys.stdin.readline

#
# 14501번: 퇴사
# https://www.acmicpc.net/problem/14501
#
# 1. DP, 각 날짜마다 얻을 수 있는 최대 금액을 저장
#
# @author  Asher Seo
#

n = int(input())
consults = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n):
  for j in range(i+consults[i][0], n+1):
    if dp[j] < dp[i] + consults[i][1]:
      dp[j] = dp[i] + consults[i][1]

print(dp[-1])
