import sys
input = sys.stdin.readline

#
# 11657번: 타임머신
# https://www.acmicpc.net/problem/11657
#
# 1. 벨만 포드 알고리즘 구현
#
# @author  Asher Seo
#

INF = 10**9

def bellmanFord(start):
  # 시작점 초기화
  dist[start] = 0
  for i in range(n):
    for j in range(m):
      curr, next, cost = bus[j]
      if dist[curr] != INF and dist[curr] + cost < dist[next]:
        dist[next] = dist[curr] + cost
        # 음수 가중치가 사이클을 이룰 경우 False
        if i == n-1:
          return False
  
  return True


n, m = map(int, input().split())
bus = [list(map(int, input().split())) for _ in range(m)]
dist = [INF] * (n+1)

if not bellmanFord(1):
  print(-1)
else:
  for i in range(2, n+1):
    if dist[i] == INF:
      print(-1)
    else:
      print(dist[i])
