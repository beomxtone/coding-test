import sys
input = sys.stdin.readline

#
# 11053번: 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
#
# 1. LIS 문제
#
# @author  Asher Seo
#

n = int(input())
L = list(map(int, input().split()))
d = [1] * n

for i in range(1, n):
  for j in range(0, i):
    if L[i] > L[j]:
      d[i] = max(d[i], d[j] + 1)

print(max(d))
