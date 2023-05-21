import sys
input = sys.stdin.readline
from collections import deque

#
# 2206번: 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206
#
# 1. BFS 3차원 배열
# 2. 벽을 뚫지 않고 가는 상태는 [x][y][0], 벽을 한번 뚫고 가는 상태는 [x][y][1]에 저장한다.
#
# @author  Asher Seo
#

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
  q = deque()
  q.append((0, 0, 0))
  visited[0][0][0] = 1
  while q:
    x, y, z = q.popleft()
    # 목표 지점(n, m)에 도달하면 정답을 출력한다.
    if x == n-1 and y == m-1:
      return visited[x][y][z]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 이동한 방향이 행렬을 벗어나지 않는지 체크
      if 0 <= nx < n and 0 <= ny < m:
        # 방문할 칸이 벽이 아니면서, 아직 방문하지 않은 칸일 때
        if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
          visited[nx][ny][z] = visited[x][y][z] + 1
          q.append((nx, ny, z))
        # 방문할 칸이 벽이면서, 벽을 아직 뚫지 않은 상태일 때
        elif graph[nx][ny] == 1 and z == 0:
          visited[nx][ny][1] = visited[x][y][0] + 1
          q.append((nx, ny, 1))
  # 목표 지점(n, m)에 도달하지 못하면 -1을 출력한다.
  return -1

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

print(bfs())
