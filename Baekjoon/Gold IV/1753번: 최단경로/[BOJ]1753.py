import sys
input = sys.stdin.readline
import heapq
INF = 10**9

#
# 1753번: 최단경로
# https://www.acmicpc.net/problem/1753
#
# 1. 다익스트라 알고리즘 구현
#
# @author  Asher Seo
#

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
  a, b, m = map(int, input().split())
  graph[a].append((b, m))

dijkstra(k)

for i in range(1, v+1):
  print(distance[i] if distance[i] != INF else 'INF')
