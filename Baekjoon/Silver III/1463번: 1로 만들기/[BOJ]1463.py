import sys
input = sys.stdin.readline

#
# 1463번: 1로 만들기
# https://www.acmicpc.net/problem/1463
#
# 1. DP - bottom up 방식
# 2. d[i] = min(d[i//3], d[i//2], d[i-1]) + 1
#
# @author  Asher Seo
#

n = int(input())
d = [0] * (n+1)

for i in range(2, n+1):
  d[i] = min(
    d[i//3] if i%3 == 0 else 1000001,
    d[i//2] if i%2 == 0 else 1000001,
    d[i-1]
  ) + 1

print(d[n])
