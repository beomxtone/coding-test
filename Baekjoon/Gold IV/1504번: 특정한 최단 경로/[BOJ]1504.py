import sys
input = sys.stdin.readline
import heapq
INF = 10**9

#
# 1504번: 특정한 최단 경로
# https://www.acmicpc.net/problem/1504
#
# 1. 다익스트라 알고리즘 활용
# 2. 1, v1, v2, n을 지나야 하므로, 1 -> v1 -> v2 -> n 까지 다익스트라 알고리즘 적용
# 3. v1, v2의 순서를 바꾼 경로도 저장 후 2번과 비교한 최소값 출력
#
# @author  Asher Seo
#

def dijkstra(start, end):
  distance = [INF]*(n+1)
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
  return distance[end]

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

v1, v2 = map(int, input().split())

answer = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n),
             dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n))
print(answer if answer < INF else -1)
