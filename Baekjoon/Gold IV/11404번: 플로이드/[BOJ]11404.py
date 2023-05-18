import sys
input = sys.stdin.readline
INF = 10**9

#
# 11404번: 플로이드
# https://www.acmicpc.net/problem/11404
#
# @author  Asher Seo
#

n = int(input())
m = int(input())
city = [[INF]*n for _ in range(n)]

for _ in range(m):
  a, b, c = map(int, input().split())
  if city[a-1][b-1] > c:
    city[a-1][b-1] = c

for i in range(n):
  for j in range(n):
    if i == j: city[i][j] = 0

for k in range(n):
  for i in range(n):
    for j in range(n):
      city[i][j] = min(city[i][j], city[i][k] + city[k][j])

for i in range(n):
  for j in range(n):
    print(city[i][j] if city[i][j] < INF else 0, end=' ')
  print()
