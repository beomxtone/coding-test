import sys
input = sys.stdin.readline

#
# 9184번: 신나는 함수 실행
# https://www.acmicpc.net/problem/9184
#
# 1. 재귀 함수를 DP로 개선하는 문제
#
# @author  Asher Seo
#

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(a, b, c):
  if a <= 0 or b <= 0 or c <= 0:
    return 1
  if a > 20 or b > 20 or c > 20:
    return w(20, 20, 20)
  if dp[a][b][c]:
    return dp[a][b][c]
  if a < b < c:
    dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
  else:
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
  return dp[a][b][c]

while True:
  a, b, c = map(int, input().split())
  if a == b == c == -1: break
  print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
