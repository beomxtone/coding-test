import sys
input = sys.stdin.readline

#
# 2217번: 로프
# https://www.acmicpc.net/problem/2217
#
# @author  Asher Seo
#

n = int(input())
ropes = [int(input()) for _ in range(n)]
res = []

ropes.sort(reverse=True)
for i in range(n):
  res.append(ropes[i] * (i+1))

print(max(res))
