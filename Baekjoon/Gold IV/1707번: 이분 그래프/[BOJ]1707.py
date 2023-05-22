import sys
input = sys.stdin.readline
from collections import deque

#
# 1707번: 이분 그래프
# https://www.acmicpc.net/problem/1707
#
# 1. 정점 v1이 있고, 정점과 인접한 정점 v2, v3 가 있다고 가정 (간선 v1-v2, v1-v3)
# 2. v1과 (v2, v3)는 각각 다른 집합에 있어야 한다. = 이분 그래프 규칙
# 3. BFS로 v1을 탐색하고, v2와 v3가 다른 집합에 존재하는지 확인하면 이분 그래프라 할 수 있다.
#
# @author  Asher Seo
#

def bfs(start):
  q = deque([start])
  visited[start] = 1
  
  while q:
    value = q.popleft()
    for i in graph[value]:
      # 방문하지 않은 정점이면
      if not visited[i]:
        # 이전 정점과 다른 집합에 넣는다. (1, -1)
        visited[i] = -1 * visited[value]
        q.append(i)
      # 방문한 정점인데 이전 정점과 같은 집합에 있으면 이분 그래프 False
      elif visited[i] == visited[value]:
        return False
  # 두 집합으로 분리할 수 있으면 이분 그래프 True
  return True

# T: 테스트 케이스의 수
T = int(input())
for _ in range(T):
  # v: 정점의 수, e: 간선의 수
  v, e = map(int, input().split())
  # 그래프의 0번 인덱스는 비워둔다
  graph = [[] for _ in range(v+1)]
  # 그래프 초기화
  for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

  # visited: 방문 여부
  visited = [0]*(v+1)

  for i in range(1, v+1):
    if not visited[i]:
      answer = bfs(i)
      if not answer:
        print('NO')
        break
  if answer: print('YES')
