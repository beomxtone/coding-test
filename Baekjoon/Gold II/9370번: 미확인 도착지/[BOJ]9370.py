import sys
input = sys.stdin.readline
import heapq
INF = 10**9

#
# 9370번: 미확인 도착지
# https://www.acmicpc.net/problem/9370
#
# 1. 최단 경로는 s-g-h-t, s-h-g-t 의 두 가지 경우가 있다.
# 2. h-t와 g-t의 경로 중 최소경로를 가지게 되는 t들을 저장한다.
# 3. g-h 도로를 지났음이 확실하며 최단거리로 갔으므로, s-g-h-t와 s-t의 다익스트라 결과는 같다.
#
# @author  Asher Seo
#

def dijkstra(start):
  distance = [INF] * (n+1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
    
  return distance

TC = int(input())
for _ in range(TC):
  # n: 교차로, m: 도로, t: 목적지 후보
  n, m, t = map(int, input().split())
  # s: 출발지, g h: 지나간 도로
  s, g, h = map(int, input().split())
  # 각 교차로 끼리의 거리
  graph = [[] for _ in range(n+1)]
  # 목적지 후보의 집합
  dest = []
  answer = []

  for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

  for _ in range(t):
    dest.append(int(input()))

  start = dijkstra(s)  # 시작 정점 S에서의 다익스트라 최단경로
  dijkG = dijkstra(g)  # 시작 정점 G에서의 다익스트라 최단경로
  dijkH = dijkstra(h)  # 시작 정점 H에서의 다익스트라 최단경로

  for d in dest:
    # S->G->H->D 의 최소거리가 S->D 의 최소 거리와 같으면 정답 배열에 추가
    if start[g] + dijkG[h] + dijkH[d] == start[d]:
      answer.append(d)
    # S->H->G->D 의 최소거리가 S->D 의 최소 거리와 같으면 정답 배열에 추가
    if start[h] + dijkH[g] + dijkG[d] == start[d]:
      answer.append(d)

  print(*sorted(answer))
