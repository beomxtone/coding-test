import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**4)

#
# 2573번: 빙산
# https://www.acmicpc.net/problem/2573
#
# 1. 빙산이 녹는 구현은 BFS로 0인 칸을 큐에 넣고 상하좌우 칸이 1 이상일 때 1을 빼준다.
# 2. 1초마다 DFS로 빙산이 분리되었는지 확인한다.
# 3. 빙산이 분리되면 해당 시간을 출력, 빙산이 다 녹을 때까지 빙산이 분리되지 않으면 0을 출력한다.
#
# @author  Asher Seo
#

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  if x<0 or x>=n or y<0 or y>=m:
    return False

  if not visited[x][y] and maps[x][y]:
    visited[x][y] = 1

    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      dfs(nx, ny)

    return True
  
  return False

def bfs():
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      
      if 0<=nx<n and 0<=ny<m:
        if maps[nx][ny] > 0:
          maps[nx][ny] -= 1


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
ans = 0

while True:
  ans += 1
  q = deque()
  
  for i in range(n):
    for j in range(m):
      if maps[i][j] == 0:
        q.append((i, j))
  
  bfs()
  
  visited = [[0]*m for _ in range(n)]
  cnt, oneMore = 0, 0
  
  for i in range(n):
    for j in range(m):
      if maps[i][j]:
        oneMore += 1
        if not visited[i][j] and dfs(i, j):
          cnt += 1

  if cnt >= 2:
    print(ans)
    break

  if not oneMore:
    print(0)
    break
