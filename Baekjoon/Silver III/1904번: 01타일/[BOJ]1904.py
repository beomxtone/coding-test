import sys
input = sys.stdin.readline

#
# 1904번: 01타일
# https://www.acmicpc.net/problem/1904
#
# 1. 피보나치 수열
#    i. 만들 수 있는 2진 수열의 수는 1, 2, 3, 5, 8, ... 로 늘어난다.
#   ii. n-2번째 숫자들 뒤에 00을 붙이는 경우 + n-1번째 숫자들 뒤에 1을 붙이는 경우 = dp[n-2] + dp[n-1]
# 2. 15746의 나머지만 dp 배열에 저장한다.
#
# @author  Asher Seo
#

n = int(input())
dp = [1, 2]

for i in range(2, n):
  dp.append((dp[i-2] + dp[i-1]) % 15746)

print(dp[n-1])
