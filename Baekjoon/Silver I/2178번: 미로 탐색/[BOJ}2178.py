import sys
input = sys.stdin.readline
from collections import deque

#
# 2178번: 미로 탐색
# https://www.acmicpc.net/problem/2178
#
# 1. BFS
# 2. 각 노드마다 최단 거리를 구할 수 있음
#
# @author  Asher Seo
#

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 그래프를 벗어나면 무시
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      # 해당 위치가 0, 벽일 경우 무시
      if graph[nx][ny] == 0:
        continue
      # 해당 위치가 처음 방문하는 노드일 경우
      if graph[nx][ny] == 1:
        # 해당 위치에 이전 위치 + 1 값을 저장 후 queue에 삽입
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

bfs(0, 0)
print(graph[n-1][m-1])
