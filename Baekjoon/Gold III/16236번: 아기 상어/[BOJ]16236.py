import sys
input = sys.stdin.readline
from collections import deque

#
# 16236번: 아기 상어
# https://www.acmicpc.net/problem/16236
#
# 1. 상어가 먹을 수 있는 물고기가 없으면 Break
# 2. 먹을 수 있는 물고기가 있으면 BFS로 물고기들의 정보를 구하고, 가장 가까운 물고기를 먹는다.
# 3. 가장 가까운, 여럿이면 상단의, 왼쪽의 물고기를 먹는다.
# 4. 아기 상어의 크기는 2, 먹은 물고기 수와 크기가 같으면 +1
#
# @author  Asher Seo
#
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 아기 상어가 먹을 수 있는 물고기들의 배열을 리턴
def bfs(u, v):
  q = deque()
  q.append((u, v))
  visited = [[0]*n for _ in range(n)]
  visited[u][v] = 1
  res = []

  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      # 지도를 벗어나지 않고, 방문하지 않은 칸이면
      if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
        # 먹을 수 있는 먹이가 있으면 결과 배열에 추가
        if graph[nx][ny] != 0 and graph[u][v] > graph[nx][ny]:
          visited[nx][ny] = visited[x][y] + 1
          res.append((visited[x][y], nx, ny))
        # 가려는 칸이 빈칸이거나, 같은 크기의 물고기가 있으면 지나간다.
        elif graph[nx][ny] == 0 or graph[nx][ny] == graph[u][v]:
          visited[nx][ny] = visited[x][y] + 1
          q.append((nx, ny))

  # 거리, x, y 좌표 순서대로 정렬
  return sorted(res, key = lambda x:(x[0], x[1], x[2]))


n = int(input())
graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] == 9:
      shark = [i, j]

x, y = shark
size = [2, 0]
ans = 0

while True:
  # 상어가 먹은 물고기의 수가 크기와 같으면 성장
  if size[0] == size[1]:
    size[0] += 1
    size[1] = 0
  
  # 상어의 위치 초기화
  graph[x][y] = size[0]
  feeds = bfs(x, y)
  
  # 먹을 먹이가 없으면 break
  if not feeds:
    break

  # 첫 번째 먹이가 가장 가깝고, 조건에 맞는 먹이
  dis, nx, ny = feeds[0]
  # 상어가 먹은 물고기 수, 먹은 칸, 상어의 위치, 답 변경
  size[1] += 1
  graph[x][y] = 0
  x, y = nx, ny
  ans += dis

print(ans)
