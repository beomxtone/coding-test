import sys
input = sys.stdin.readline
import heapq

#
# 18352번: 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352
#
# 1. 다익스트라 알고리즘 활용
# 2. 최단 거리가 k인 도시의 배열을 출력, 그런 도시가 없으면 -1을 출력
#
# @author  Asher Seo
#

INF = 10**9

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue

    for node in graph[now]:
      cost = dist + node[1]
      if cost < distance[node[0]]:
        distance[node[0]] = cost
        heapq.heappush(q, (cost, node[0]))


n, m, k, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1))

dijkstra(start)

ans = []
for i in range(1, n+1):
  if distance[i] == k:
    ans.append(i)

if ans:
  for num in ans:
    print(num)
else:
  print(-1)
